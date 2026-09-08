#!/usr/bin/env python3
"""
论文自动检索 + 开 Issue 草稿 (paper-tracker)
===========================================
适配 yangyang9912/Awesome-Human-Centered-Relationship：
读取 config.yaml 中的「既有分类」(categories) 与关键词，
分别检索 arXiv 与 Semantic Scholar，按关键词把新论文归入对应分类，
与仓库已有 Issue 中记录过的论文去重后，为每个分类开一个 Issue 草稿。
Issue 正文直接生成「可粘贴进 README 的 Markdown 表格行」。

依赖: requests, pyyaml
环境变量:
  GITHUB_TOKEN       (Actions 自动注入, 用于创建 Issue)
  GITHUB_REPOSITORY  (owner/repo, Actions 自动注入)
未设置 GITHUB_TOKEN 时进入「调试模式」，仅打印草稿、不调用接口。
"""
import os
import re
import time
import datetime
import yaml
import requests

CONFIG_PATH = os.environ.get("CONFIG_PATH", "config.yaml")
API_BASE = "https://api.github.com"


def log(msg):
    print(f"[paper-tracker] {msg}", flush=True)


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------- arXiv
def _clean_arxiv_id(raw):
    m = re.search(r"abs/([0-9]+\.[0-9]+)", raw)
    return m.group(1) if m else raw


def fetch_arxiv(queries, cat_list, max_results):
    base = "http://export.arxiv.org/api/query"
    papers = []
    cat_filter = "+OR+".join(f"cat:{c}" for c in cat_list)
    for q in queries:
        search = f"({cat_filter}) AND (abs:{q} OR ti:{q})"
        params = {
            "search_query": search,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        try:
            r = requests.get(base, params=params, timeout=30)
            r.raise_for_status()
        except Exception as e:
            log(f"arXiv 查询失败 ({q}): {e}")
            continue
        entries = re.findall(r"<entry>(.*?)</entry>", r.text, re.S)
        for e in entries:
            pid = _clean_arxiv_id(re.search(r"<id>(.*?)</id>", e).group(1))
            title = re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", e, re.S).group(1)).strip()
            summary = re.sub(r"\s+", " ", re.search(r"<summary>(.*?)</summary>", e, re.S).group(1)).strip()
            authors = [a.strip() for a in re.findall(r"<name>(.*?)</name>", e)]
            pub = re.search(r"<published>(.*?)</published>", e).group(1)
            pub_date = pub[:10] if pub else ""
            papers.append({
                "id": f"arxiv:{pid}",
                "title": title,
                "authors": authors[:5],
                "url": f"https://arxiv.org/abs/{pid}",
                "abstract": summary,
                "published": pub_date,
                "source": "arXiv",
            })
        time.sleep(1.5)
    return papers


# ---------------------------------------------------------- Semantic Scholar
def fetch_s2(queries, limit):
    base = "https://api.semanticscholar.org/graph/v1/paper/search"
    fields = "title,abstract,authors,year,publicationDate,externalIds,url"
    papers = []
    for q in queries:
        params = {"query": q, "limit": limit, "fields": fields}
        try:
            r = requests.get(base, params=params, timeout=30)
            r.raise_for_status()
        except Exception as e:
            log(f"S2 查询失败 ({q}): {e}")
            continue
        for d in r.json().get("data", []):
            doi = (d.get("externalIds") or {}).get("DOI")
            pid = f"doi:{doi}" if doi else f"s2:{d.get('paperId')}"
            pub = d.get("publicationDate") or ""
            papers.append({
                "id": pid,
                "title": d.get("title") or "",
                "authors": [a.get("name") for a in (d.get("authors") or [])][:5],
                "url": d.get("url") or (f"https://doi.org/{doi}" if doi else ""),
                "abstract": d.get("abstract") or "",
                "published": pub,
                "source": "SemanticScholar",
            })
        time.sleep(1)
    return papers


# ----------------------------------------------------------- classify
def classify(paper, categories):
    text = (paper["title"] + " " + paper["abstract"]).lower()
    return [c["name"] for c in categories
            if any(k.lower() in text for k in c.get("keywords", []))]


# ----------------------------------------------------------- github issues
def get_existing_ids(token, repo):
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    ids = set()
    for state in ("open", "closed"):
        page = 1
        while True:
            r = requests.get(f"{API_BASE}/repos/{repo}/issues",
                             params={"state": state, "per_page": 100,
                                     "page": page, "labels": "paper-tracker"},
                             headers=headers, timeout=30)
            if r.status_code != 200:
                break
            issues = r.json()
            if not issues:
                break
            for it in issues:
                for m in re.findall(r"<!--\s*id:\s*([^\s]+)\s*-->", it.get("body", "")):
                    ids.add(m)
            page += 1
    return ids


def open_issue(token, repo, title, body):
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    r = requests.post(f"{API_BASE}/repos/{repo}/issues",
                      json={"title": title, "body": body, "labels": ["paper-tracker"]},
                      headers=headers, timeout=30)
    return r.status_code, r.text[:200]


# ----------------------------------------------------------- format
def year_of(p):
    return p["published"][:4] if p.get("published") else str(datetime.date.today().year)


def fmt_row(p):
    venue = "arXiv" if p["source"] == "arXiv" else "Preprint"
    return f"| [{p['title']}]({p['url']}) | {venue} | {year_of(p)} |"


def emit(title, plist, lookback, debug, token, repo):
    body = f"自动检索到 **{title}** 下 {len(plist)} 篇新论文（近 {lookback} 天）。\n\n"
    body += "可直接将下方表格复制进 README 对应分类（Venue / Year 为预填，按需修正）：\n\n"
    body += "| Paper | Venue | Year |\n| --- | --- | --- |\n"
    ids = []
    for p in plist:
        body += fmt_row(p) + "\n"
        ids.append(p["id"])
    body += "\n" + "\n".join(f"<!-- id:{i} -->" for i in ids)
    body += "\n\n---\n*由 paper-tracker 自动生成 · 分类: " + title + "*"
    if debug:
        log(f"[草稿] {title}\n{body}\n")
    else:
        code, _ = open_issue(token, repo, f"[paper-tracker] {title} ({len(plist)}篇)", body)
        log(f"Issue 创建 -> {code}")


# ----------------------------------------------------------- main
def main():
    cfg = load_config()
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    debug = not (token and repo)
    if debug:
        log("未检测到 GITHUB_TOKEN/REPOSITORY → 调试模式（仅打印，不创建 Issue）。")

    lookback = int(cfg.get("lookback_days", 30))
    since = datetime.date.today() - datetime.timedelta(days=lookback)
    since_str = since.isoformat()
    categories = cfg.get("categories", [])
    sources = cfg.get("sources", {})

    all_papers = []
    if "arxiv" in sources:
        a = sources["arxiv"]
        q = [x for c in categories for x in c.get("arxiv_queries", c.get("keywords", []))]
        all_papers += fetch_arxiv(q, a.get("categories", ["cs.CV", "cs.AI", "cs.MM", "cs.RO"]),
                                  a.get("max_results", 40))
    if sources.get("semantic_scholar", {}).get("enabled", True):
        s = sources["semantic_scholar"]
        q = [x for c in categories for x in c.get("s2_queries", c.get("keywords", []))]
        all_papers += fetch_s2(q, s.get("limit", 40))

    # 运行内去重 + 时间窗过滤
    seen = {}
    for p in all_papers:
        seen.setdefault(p["id"], p)
    papers = [p for p in seen.values()
              if not p["published"] or p["published"] >= since_str]
    log(f"近 {lookback} 天候选论文: {len(papers)} 篇")

    # 与已有 Issue 去重
    if not debug:
        known = get_existing_ids(token, repo)
        papers = [p for p in papers if p["id"] not in known]
    log(f"去重后待报告论文: {len(papers)} 篇")

    # 按既有分类分组
    groups = {c["name"]: [] for c in categories}
    unclassified = []
    for p in papers:
        matched = classify(p, categories)
        if not matched:
            unclassified.append(p)
            continue
        for m in matched:
            groups[m].append(p)

    for name, plist in groups.items():
        if plist:
            emit(f"新论文 · {name}", plist, lookback, debug, token, repo)

    if unclassified:
        emit("未分类新论文", unclassified, lookback, debug, token, repo)

    log("完成。")


if __name__ == "__main__":
    main()
