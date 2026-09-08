#!/usr/bin/env python3
"""
paper-tracker: 自动检索 + 自动开 PR（无需手动粘贴）
====================================================
每天（GitHub Actions 定时）检索 arXiv + Semantic Scholar 的新论文，
按 config.yaml 的「既有分类」归类，把新行直接插入 README 对应的
<details> 表格（列数由每个分类的 row_template 决定），然后推到一个
新分支并开 Pull Request。你只需审阅 diff、点一下 Merge。

依赖: requests, pyyaml
环境变量: GITHUB_TOKEN, GITHUB_REPOSITORY
          S2_API_KEY（可选，提高 Semantic Scholar 限额）
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

# arXiv 官方要求：User-Agent 必带；且建议 < 1 请求/3 秒
UA = "paper-tracker-bot/1.0 (github.com/yangyang9912/Awesome-Human-Centered-Relationship)"


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


# ---------------------------------------------------------------- arXiv
def _arxiv_id(raw):
    m = re.search(r"abs/([0-9]+\.[0-9]+)", raw)
    return m.group(1) if m else raw


def fetch_arxiv(queries, cats, max_results):
    base = "https://export.arxiv.org/api/query"  # 用 https
    out = []
    catf = "+OR+".join(f"cat:{c}" for c in cats)
    for q in queries:
        params = {"search_query": f"({catf}) AND (abs:{q} OR ti:{q})",
                  "start": 0, "max_results": max_results,
                  "sortBy": "submittedDate", "sortOrder": "descending"}
        try:
            r = http_get(base, params=params)
        except Exception as e:
            log(f"arXiv 失败 ({q}): {e}")
            continue
        for e in re.findall(r"<entry>(.*?)</entry>", r.text, re.S):
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
        except Exception as e:
            log(f"S2 失败 ({q}): {e}")
            continue
        for d in r.json().get("data", []):
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
    return p["id"].split(":", 1)[1] in text


def year_of(p):
    return p["published"][:4] if p.get("published") else str(datetime.date.today().year)


def row_for(cat, p):
    return cat["row_template"].format(
        title=p["title"], url=p["url"],
        venue="arXiv" if p["source"] == "arXiv" else "Preprint",
        year=year_of(p))


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

    allp = []
    if "arxiv" in sources:
        a = sources["arxiv"]
        q = [x for c in categories for x in c.get("arxiv_queries", c.get("keywords", []))]
        allp += fetch_arxiv(q, a.get("categories", ["cs.CV", "cs.AI", "cs.MM", "cs.RO"]),
                            a.get("max_results", 40))
    if sources.get("semantic_scholar", {}).get("enabled", True):
        s = sources["semantic_scholar"]
        q = [x for c in categories for x in c.get("s2_queries", c.get("keywords", []))]
        s2_key = os.environ.get("S2_API_KEY", s.get("api_key"))
        allp += fetch_s2(q, s.get("limit", 40), api_key=s2_key)

    seen = {}
    for p in allp:
        seen.setdefault(p["id"], p)
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
