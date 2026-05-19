#!/usr/bin/env python3
"""Scrape PyMOL wiki command pages into docs/ for RAG indexing.

Fetches all pages in Category:Commands via the MediaWiki API, converts
wikitext to clean markdown, and writes one file per command into docs/.
Run this once; then run `pmrag build` inside PyMOL to re-index.

Usage:
    python scripts/scrape_pymol_wiki.py
    python scripts/scrape_pymol_wiki.py --limit 20 --delay 0.3
    python scripts/scrape_pymol_wiki.py --output-dir /path/to/docs --force
"""

import argparse
import os
import re
import sys
import time

try:
    import requests
except ImportError:
    print("requests not installed. Run: pip install requests")
    sys.exit(1)

WIKI_API = "https://pymolwiki.org/api.php"
CATEGORY = "Category:Commands"  # default

SECTIONS_TO_SKIP = {
    "see also", "notes", "references", "external links",
    "history", "troubleshooting", "credits", "authors",
    "version history", "changelog",
}


# ── MediaWiki API helpers ──────────────────────────────────────────────────────

def get_command_pages(limit=None, category=CATEGORY):
    """Return all page titles in the given wiki category."""
    pages = []
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": category,
        "cmlimit": 500,
        "cmtype": "page",
        "format": "json",
    }
    while True:
        resp = requests.get(WIKI_API, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        pages.extend(m["title"] for m in data["query"]["categorymembers"])
        if "continue" not in data or (limit and len(pages) >= limit):
            break
        params["cmcontinue"] = data["continue"]["cmcontinue"]
    return pages[:limit] if limit else pages


def get_wikitext(title):
    """Fetch raw wikitext for a page. Returns None if the page is missing."""
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvslots": "main",
        "format": "json",
    }
    resp = requests.get(WIKI_API, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    page = next(iter(data["query"]["pages"].values()))
    if "missing" in page:
        return None
    return page["revisions"][0]["slots"]["main"]["*"]


# ── Wikitext → Markdown conversion ────────────────────────────────────────────

def wikitext_to_markdown(title, wikitext):
    text = wikitext

    # Remove <ref> citations
    text = re.sub(r"<ref[^>]*>.*?</ref>", "", text, flags=re.DOTALL)
    text = re.sub(r"<ref[^>]*/>", "", text)

    # Remove {{templates}} (two passes for simple nesting)
    text = re.sub(r"\{\{[^{}]*\}\}", "", text)
    text = re.sub(r"\{\{[^{}]*\}\}", "", text)

    # <source> and <syntaxhighlight> code blocks → fenced markdown
    def _code_block(lang_hint=""):
        fence = "```python" if "python" in lang_hint.lower() else "```"
        def _replace(m):
            # group(1) = tag attributes, group(2) = code content
            return f"\n{fence}\n{m.group(2).strip()}\n```\n"
        return _replace

    for tag in ("source", "syntaxhighlight"):
        text = re.sub(
            rf'<{tag}([^>]*)>(.*?)</{tag}>',
            lambda m: _code_block(m.group(1))(m),
            text, flags=re.DOTALL | re.IGNORECASE,
        )

    # <pre> blocks
    text = re.sub(
        r"<pre>(.*?)</pre>",
        lambda m: f"\n```\n{m.group(1).strip()}\n```\n",
        text, flags=re.DOTALL,
    )

    # Strip remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Remove category / file links
    text = re.sub(r"\[\[(Category|File|Image):[^\]]*\]\]", "", text, flags=re.IGNORECASE)

    # [[Page|display]] → display,  [[Page]] → Page
    text = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)

    # [URL display text] → display text,  [URL] → (removed)
    text = re.sub(r"\[https?://\S+\s+([^\]]+)\]", r"\1", text)
    text = re.sub(r"\[https?://\S+\]", "", text)

    # Bold / italic
    text = re.sub(r"'''(.+?)'''", r"**\1**", text)
    text = re.sub(r"''(.+?)''", r"*\1*", text)

    # == Headers ==
    text = re.sub(r"^====(.+?)====\s*$", r"#### \1", text, flags=re.MULTILINE)
    text = re.sub(r"^===(.+?)===\s*$",  r"### \1",  text, flags=re.MULTILINE)
    text = re.sub(r"^==(.+?)==\s*$",    r"## \1",   text, flags=re.MULTILINE)

    # Wiki lists → markdown lists
    # Use negative lookahead so ## headers aren't converted to numbered list items
    text = re.sub(r"^\*\s*", "- ", text, flags=re.MULTILINE)
    text = re.sub(r"^#(?!#)\s*", "1. ", text, flags=re.MULTILINE)

    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    lines = [l.rstrip() for l in text.splitlines()]
    return f"# {title}\n\n" + "\n".join(lines).strip()


def filter_sections(text):
    """Drop boilerplate sections (See Also, Notes, References, etc.)."""
    lines = text.splitlines()
    result = []
    keep = True  # always keep the lead section

    for line in lines:
        if line.startswith("## "):
            section_name = line.lstrip("#").strip().lower()
            keep = not any(skip in section_name for skip in SECTIONS_TO_SKIP)
        if keep:
            result.append(line)

    return "\n".join(result).strip()


def title_to_filename(title):
    safe = re.sub(r"[^\w\- ]", "_", title).strip().replace(" ", "_").lower()
    return f"wiki_{safe}.md"


# ── Main scrape loop ───────────────────────────────────────────────────────────

def scrape(output_dir, category=CATEGORY, limit=None, delay=0.5, force=False):
    os.makedirs(output_dir, exist_ok=True)

    print(f"Fetching page list from {category}…")
    try:
        titles = get_command_pages(limit=limit, category=category)
    except Exception as e:
        print(f"Failed to fetch page list: {e}")
        sys.exit(1)
    print(f"Found {len(titles)} pages.\n")

    written = skipped = failed = 0

    for i, title in enumerate(titles, 1):
        fname = title_to_filename(title)
        out_path = os.path.join(output_dir, fname)

        if not force and os.path.exists(out_path):
            skipped += 1
            continue

        print(f"  [{i:3d}/{len(titles)}] {title}…", end=" ", flush=True)

        try:
            wikitext = get_wikitext(title)
            if wikitext is None:
                print("missing — skipped")
                failed += 1
                continue

            # Detect redirects
            if wikitext.strip().lower().startswith("#redirect"):
                print("redirect — skipped")
                failed += 1
                continue

            markdown = wikitext_to_markdown(title, wikitext)
            markdown = filter_sections(markdown)

            # Skip thin stubs
            if len(markdown.strip()) < 200:
                print("stub — skipped")
                failed += 1
                continue

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(markdown + "\n")
            print("ok")
            written += 1

        except requests.RequestException as e:
            print(f"network error — {e}")
            failed += 1
        except Exception as e:
            print(f"error — {e}")
            failed += 1

        time.sleep(delay)

    print(f"\nDone: {written} written, {skipped} already existed, {failed} skipped/failed.")
    print(f"Output directory: {output_dir}")
    print("\nNext step — rebuild the RAG index inside PyMOL:")
    print("  pmrag build")


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape PyMOL wiki pages into docs/ for RAG indexing."
    )
    parser.add_argument(
        "--output-dir", default=None,
        help="Directory to write .md files (default: docs/ adjacent to this script's parent)",
    )
    parser.add_argument(
        "--category", default="Category:Commands",
        help="Wiki category to scrape (default: Category:Commands)",
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Max pages to scrape, useful for testing (default: all)",
    )
    parser.add_argument(
        "--delay", type=float, default=0.5,
        help="Seconds between HTTP requests (default: 0.5)",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-scrape pages that already exist in output-dir",
    )
    args = parser.parse_args()

    if args.output_dir is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        args.output_dir = os.path.normpath(os.path.join(script_dir, "..", "docs"))

    scrape(args.output_dir, category=args.category, limit=args.limit,
           delay=args.delay, force=args.force)
