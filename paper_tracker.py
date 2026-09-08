#!/usr/bin/env python3
"""
paper-tracker: 自动检索 + 自动开 PR（无需手动粘贴）
====================================================
每天（GitHub Actions 定时）检索新论文，按 config.yaml 的「既有分类」归类，
把新行直接插入 README 对应的 <details> 表格（列数由每个分类的 row_template
决定），然后推到一个新分支并开 Pull Request。你只需审阅 diff、点一下 Merge。

数据源（均免费、无需密钥即可跑）：
  1. OpenAlex  —— 主源，覆盖 arXiv 预印本 + 会议/期刊，限额宽松（polite pool）。
  2. arXiv    —— 兜底源，best-effort；对 429 与「200 空 feed」静默限流做重试退避。
  3. Semantic Scholar —— 可选，免费额度很低，建议配 S2_API_KEY 再用。

依赖: requests, pyyaml
环境变量: GITHUB_TOKEN, GITHUB_REPOSITORY, S2_API_KEY(可选)
未设置 GITHUB_TOKEN 时进入「调试模式」，只改本地 README 草稿、不提交。
"""
import os
import re
import time
import datetime
import subprocess
import yaml
import requests

CONFIG_PATH = os.environ.get("CONFIG_PATH", "config.yaml")
README_PATH = os.environ.get("README_PATH", "README.md")
API_BASE = "https://api.github.com"

# arXiv / OpenAlex 都建议在请求里带上可联系到的 User-Agent
UA = "paper-tracker-bot/1.0 (mailto:paper-tracker@example.com)"


def log(m):
    print(f"[paper-tracker] {m}", flush=True)


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


# ----------------------------------------------------------- HTTP helper
def http_get(url, params=None, headers=None, timeout=45, max_retries=4):
    """带 User-Agent、指数退避重试的 GET。

    对 429 / 5xx / 超时重试（退避 3→6→12→24→60s），其余 4xx 直接抛错。
    """
    h = {"User-Agent": UA}
    if headers:
        h.update(headers)
    delay = 3
    for attempt in range(max_retries + 1):
        try:
            r = requests.get(url, params=params, headers=h, timeout=timeout)
        except requests.exceptions.RequestException as e:
            if attempt >= max_retries:
                raise
            log(f"请求异常（{e}），{delay}s 后重试")
            time.sleep(delay)
            delay = min(delay * 2, 60)
            continue
        if r.status_code == 200:
            return r
        if attempt >= max_retries:
            r.raise_for_status()
        if r.status_code in (429, 500, 502, 503, 504):
            log(f"服务端限流/错误 {r.status_code}，{delay}s 后重试")
            time.sleep(delay)
            delay = min(delay * 2, 60)
            continue
        r.raise_for_status()  # 其它 4xx 直接失败，不重试
    raise RuntimeError("重试耗尽")


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


# ---------------------------------------------------------- OpenAlex (主源)
def _oa_abstract(inv):
    if not inv:
        return ""
    words = {}
    for w, positions in inv.items():
        for p in positions:
            words[p] = w
    return " ".join(words[i] for i in sorted(words))


def fetch_openalex(queries, since_str, mailto, per_page=50):
    base = "https://api.openalex.org/works"
    out = []
    for q in queries:
        params = {
            "search": q,
            "filter": f"from_publication_date:{since_str}",
            "per-page": per_page,
            "mailto": mailto,
        }
        try:
            r = http_get(base, params=params, timeout=45)
            data = r.json()
        except Exception as e:
            log(f"OpenAlex 失败 ({q[:40]}): {e}")
            continue
        for w in data.get("results", []):
            title = w.get("title") or ""
            url, arxiv_id = None, None
            for loc in (w.get("locations") or []):
                for key in ("landing_page_url", "pdf"):
                    u = loc.get(key) or ""
                    m = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)", u)
                    if m:
                        arxiv_id = m.group(1)
                        url = f"https://arxiv.org/abs/{arxiv_id}"
                        break
                if url:
                    break
            if not url:
                doi = (w.get("ids") or {}).get("doi")
                url = doi or ""
                if not url:
                    continue  # 没有链接的论文跳过
            pub = w.get("publication_date") or ""
            out.append({
                "id": f"arxiv:{arxiv_id}" if arxiv_id else f"oa:{(w.get('id') or '').split('/')[-1]}",
                "title": title,
                "authors": [a.get("author", {}).get("display_name")
                            for a in (w.get("authorships") or [])][:5],
                "url": url,
                "abstract": _oa_abstract(w.get("abstract_inverted_index")),
                "published": pub,
                "source": "OpenAlex",
            })
        time.sleep(1)  # OpenAlex 礼貌池也建议稍作间隔
    return out


# ---------------------------------------------------------------- arXiv
def _arxiv_id(raw):
    m = re.search(r"abs/([0-9]+\.[0-9]+)", raw)
    return m.group(1) if m else raw


def fetch_arxiv(search_queries, cats, max_results):
    """search_queries: 已拼好的完整查询片段列表（每个对应一个分类）。"""
    base = "https://export.arxiv.org/api/query"
    out = []
    catf = "+OR+".join(f"cat:{c}" for c in cats)
    for frag in search_queries:
        params = {"search_query": f"({catf}) AND ({frag})",
                  "start": 0, "max_results": max_results,
                  "sortBy": "submittedDate", "sortOrder": "descending"}
        entries = []
        # arXiv 有时返回 200 空 feed（静默限流），对 0 结果额外重试
        for _ in range(3):
            try:
                r = http_get(base, params=params)
            except Exception as e:
                log(f"arXiv 失败 ({frag[:40]}): {e}")
                entries = None
                break
            entries = re.findall(r"<entry>(.*?)</entry>", r.text, re.S)
            if entries:
                break
            log(f"arXiv 空 feed（疑似限流），重试 {frag[:30]}")
            time.sleep(5)
        if entries is None:
            continue
        for e in entries:
            if "<title>Error</title>" in e:
                continue
            pid = _arxiv_id(re.search(r"<id>(.*?)</id>", e).group(1))
            title = re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", e, re.S).group(1)).strip()
            abstract = re.sub(r"\s+", " ", re.search(r"<summary>(.*?)</summary>", e, re.S).group(1)).strip()
            authors = [a.strip() for a in re.findall(r"<name>(.*?)</name>", e)]
            pub = re.search(r"<published>(.*?)</published>", e).group(1)[:10]
            out.append({"id": f"arxiv:{pid}", "title": title, "authors": authors[:5],
                        "url": f"https://arxiv.org/abs/{pid}", "abstract": abstract,
                        "published": pub, "source": "arXiv"})
        time.sleep(3)  # arXiv 建议 < 1 请求/3 秒
    return out


# ---------------------------------------------------------- Semantic Scholar
def fetch_s2(queries, limit, api_key=None):
    base = "https://api.semanticscholar.org/graph/v1/paper/search"
    fields = "title,abstract,authors,year,publicationDate,externalIds,url"
    headers = {"x-api-key": api_key} if api_key else {}
    out = []
    for q in queries:
        try:
            r = http_get(base, params={"query": q, "limit": limit, "fields": fields},
                         headers=headers, timeout=45)
            data = r.json()
        except Exception as e:
            log(f"S2 失败 ({q[:40]}): {e}")
            continue
        for d in data.get("data", []):
            doi = (d.get("externalIds") or {}).get("DOI")
            pid = f"doi:{doi}" if doi else f"s2:{d.get('paperId')}"
            pub = d.get("publicationDate") or ""
            out.append({"id": pid, "title": d.get("title") or "",
                        "authors": [a.get("name") for a in (d.get("authors") or [])][:5],
                        "url": d.get("url") or (f"https://doi.org/{doi}" if doi else ""),
                        "abstract": d.get("abstract") or "", "published": pub,
                        "source": "SemanticScholar"})
        time.sleep(3)  # S2 免费额度很低，放慢节奏
    return out


# ----------------------------------------------------------- classify (首匹配)
def classify(paper, categories):
    text = (paper["title"] + " " + paper["abstract"]).lower()
    for c in categories:
        if any(k.lower() in text for k in c.get("keywords", [])):
            return c
    return None


def already_in_readme(p, text):
    if p["url"] and p["url"] in text:
        return True
    if p["id"].split(":", 1)[1] in text:
        return True
    # 跨源去重：标题也比对（OpenAlex 与 arXiv 可能同源不同链接）
    return norm_title(p["title"]) in text


def year_of(p):
    return p["published"][:4] if p.get("published") else str(datetime.date.today().year)


def row_for(cat, p):
    venue = "arXiv" if "arxiv.org" in (p.get("url") or "") else "Preprint"
    return cat["row_template"].format(title=p["title"], url=p["url"], venue=venue, year=year_of(p))


# --------------------------------------------------- 定位目标表格最后一行
def locate_target(lines, substr):
    for i, line in enumerate(lines):
        if substr.lower() in line.lower() and "<summary>" in line:
            start = None
            for j in range(i, -1, -1):
                if lines[j].strip() == "<details>":
                    start = j
                    break
            end = None
            for j in range(i, len(lines)):
                if lines[j].strip() == "</details>":
                    end = j
                    break
            if start is None or end is None:
                return None
            last = None
            for k in range(start, end):
                s = lines[k].lstrip()
                if s.startswith("|") and "---" not in s:
                    last = k
            return last
    return None


# ----------------------------------------------------------- git / PR
def commit_and_open_pr(n):
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]
    branch = f"paper-tracker/{datetime.datetime.utcnow():%Y%m%d-%H%M%S}"
    run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"])
    run(["git", "config", "user.name", "github-actions[bot]"])
    run(["git", "remote", "set-url", "origin",
         f"https://x-access-token:{token}@github.com/{repo}.git"])
    run(["git", "checkout", "-b", branch])
    run(["git", "add", "README.md"])
    run(["git", "commit", "-m", f"paper-tracker: add {n} new papers"])
    run(["git", "push", "-u", "origin", branch])
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    body = (f"自动检索并新增 {n} 篇论文到 README 对应分类。\n\n"
            "请审阅 diff，确认无误后点击 Merge。脚本不会直接改 main 分支。")
    r = requests.post(f"{API_BASE}/repos/{repo}/pulls",
                      json={"title": f"[paper-tracker] 自动新增 {n} 篇论文",
                            "head": branch, "base": "main", "body": body},
                      headers=headers, timeout=30)
    log(f"PR 创建 -> {r.status_code}")


# ----------------------------------------------------------- main
def main():
    cfg = load_config()
    debug = not (os.environ.get("GITHUB_TOKEN") and os.environ.get("GITHUB_REPOSITORY"))
    if debug:
        log("调试模式（无 token）：仅修改本地 README 草稿，不提交/不开 PR。")
    lookback = int(cfg.get("lookback_days", 30))
    since = datetime.date.today() - datetime.timedelta(days=lookback)
    since_str = since.isoformat()
    categories = cfg.get("categories", [])
    sources = cfg.get("sources", {})

    # 每个分类生成查询：OpenAlex 用关键词拼接；arXiv 用 OR 组合（一个分类一次请求）
    oa_queries = [" ".join(c.get("keywords", [])) for c in categories]
    arxiv_frags = [" OR ".join(f"(abs:{k} OR ti:{k})" for k in c.get("keywords", []))
                   for c in categories]

    allp = []
    if sources.get("openalex", {}).get("enabled", True):
        o = sources["openalex"]
        allp += fetch_openalex(oa_queries, since_str,
                               o.get("mailto", "paper-tracker@example.com"),
                               o.get("per_page", 50))
    if sources.get("arxiv", {}).get("enabled", True):
        a = sources["arxiv"]
        allp += fetch_arxiv(arxiv_frags, a.get("categories", ["cs.CV", "cs.AI", "cs.MM", "cs.RO"]),
                            a.get("max_results", 40))
    if sources.get("semantic_scholar", {}).get("enabled", False):
        s = sources["semantic_scholar"]
        q = [x for c in categories for x in c.get("s2_queries", c.get("keywords", []))]
        s2_key = os.environ.get("S2_API_KEY", s.get("api_key"))
        allp += fetch_s2(q, s.get("limit", 40), api_key=s2_key)

    # 跨源去重（按标题）
    seen = {}
    for p in allp:
        key = norm_title(p["title"])
        if key and key not in seen:
            seen[key] = p
    papers = [p for p in seen.values()
              if not p["published"] or p["published"] >= since_str]
    log(f"近 {lookback} 天候选: {len(papers)} 篇")

    with open(README_PATH, encoding="utf-8") as f:
        readme_text = f.read()
    papers = [p for p in papers if not already_in_readme(p, readme_text)]
    log(f"README 去重后待添加: {len(papers)} 篇")

    lines = readme_text.split("\n")
    uncat_head = "## 🆕 paper-tracker (uncategorized)"
    has_uncat = any(l.strip() == uncat_head for l in lines)
    n_added = 0

    for p in papers:
        cat = classify(p, categories)
        if cat is None:
            if not has_uncat:
                lines.append("")
                lines.append(uncat_head)
                lines.append("")
                has_uncat = True
            lines.append(row_for({"row_template": "| [{title}]({url}) | {venue} | {year} |"}, p))
            n_added += 1
            continue
        pos = locate_target(lines, cat["target_summary"])
        if pos is None:
            log(f"未找到目标表格: {cat['target_summary']}，跳过《{p['title'][:40]}》")
            continue
        lines.insert(pos + 1, row_for(cat, p))
        n_added += 1

    if n_added == 0:
        log("没有需要新增的论文，结束。")
        return
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    log(f"已写入 README：新增 {n_added} 行。")
    if debug:
        log("调试模式：不提交。")
        return
    commit_and_open_pr(n_added)
    log("完成。")


if __name__ == "__main__":
    main()
