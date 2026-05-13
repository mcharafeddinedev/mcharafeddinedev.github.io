"""
Regenerate CONTENT_MASTER.md = visitor-facing copy only (no front matter,
no iframe/embed HTML). Run: python _scripts/build_content_master.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "CONTENT_MASTER.md"

HEADER = """# Site copy — text only

Page wording only (plus a few sidebar/SEO phrases). Embeds and raw HTML are omitted; screenshot lines show alt text.

**Rebuild this file from the live pages:** `python _scripts/build_content_master.py`  

**Push edits live:** paste changed sections here, then ask Cursor to sync into `index.md`, `projects.md`, etc.

---
"""


def yaml_quoted_strings_for_display(raw: str) -> dict[str, str]:
    """Pull a few `_config.yml` strings shown in chrome / SEO."""
    out: dict[str, str] = {}
    for label, pattern in (
        ("Site title", r'^title:\s*"([^"]*)"'),
        ("SEO / subtitle", r'^description:\s*"([^"]*)"'),
        ("Header tagline", r'^tagline:\s*"([^"]*)"'),
        ("Back to top", r'^back_to_top_text:\s*"([^"]*)"'),
    ):
        m = re.search(pattern, raw, re.MULTILINE)
        if m:
            out[label] = m.group(1)
    return out


def strip_front_matter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].lstrip("\n\r")
    return text


def replace_itch_blocks(body: str) -> str:
    body = re.sub(
        r'<div\s+class="itch-embed-wrap"[^>]*>.*?</div>',
        "",
        body,
        flags=re.DOTALL | re.IGNORECASE,
    )
    body = re.sub(
        r"<iframe[^>]*>.*?</iframe>", "", body, flags=re.DOTALL | re.IGNORECASE
    )
    return body


def inline_semantic_tags(body: str) -> str:
    body = re.sub(
        r"<strong>(.*?)</strong>",
        r"**\1**",
        body,
        flags=re.DOTALL | re.IGNORECASE,
    )
    body = re.sub(r"<b>(.*?)</b>", r"**\1**", body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r"<em>(.*?)</em>", r"_\1_", body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r"<i>(.*?)</i>", r"_\1_", body, flags=re.DOTALL | re.IGNORECASE)
    return body


def linked_images_to_notes(body: str) -> str:
    """Wrap-only links around a screenshot → short note + itch URL."""
    pat = re.compile(
        r'<a\b[^>]+\bhref=(["\'])([^"\']+)\1[^>]*>'
        r"\s*<img\b[^>]+/\s*>"
        r"\s*</a>",
        re.IGNORECASE | re.DOTALL,
    )

    def one(m: re.Match) -> str:
        href = m.group(2).strip().replace("&amp;", "&")
        alt_m = re.search(r'alt="([^"]*)"', m.group(0), re.I)
        alt = alt_m.group(1).strip() if alt_m else "screenshot"
        return f"\n\n_Screenshot:_ {alt} — [{href}]({href})\n\n"

    body = pat.sub(one, body)
    pat2 = re.compile(
        r'<a\b[^>]+\bhref=(["\'])([^"\']+)\1[^>]*>'
        r"\s*<img\b[^>]*>"
        r"\s*</a>",
        re.IGNORECASE | re.DOTALL,
    )
    return pat2.sub(one, body)


def imgs_to_notes(body: str) -> str:

    def one(m: re.Match) -> str:
        alt_m = re.search(r'alt="([^"]*)"', m.group(0), re.I)
        alt = alt_m.group(1).strip() if alt_m else "screenshot"
        return f"\n\n_Screenshot:_ {alt}\n\n"

    return re.sub(r"<img\b[^>]*/?\s*>", one, body, flags=re.IGNORECASE)


def anchors_to_md(body: str) -> str:
    pattern = re.compile(
        r'<a\s+[^>]*\bhref=(["\'])([^"\']+)\1[^>]*>(.*?)</a>',
        re.DOTALL | re.IGNORECASE,
    )

    def repl(m: re.Match) -> str:
        href = m.group(2).strip().replace("&amp;", "&")
        inner = m.group(3)
        inner = re.sub(r"<[^>]+>", "", inner)
        inner = inner.replace("&nbsp;", " ").strip()
        if not inner:
            return ""
        return f"[{inner}]({href})"

    prev = None
    while prev != body:
        prev = body
        body = pattern.sub(repl, body)
    return body


def strip_remaining_html(body: str) -> str:
    body = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", body, flags=re.DOTALL | re.I)
    body = body.replace("</p>", "\n").replace("</div>", "\n")
    body = re.sub(r"<p\b[^>]*>", "\n", body, flags=re.I)
    body = re.sub(r"<br\s*/?>", "\n", body, flags=re.I)
    body = re.sub(r"<[^>]+>", "", body)
    body = html_entity_light(body)
    body = re.sub(r"[ \t]+\n", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def html_entity_light(s: str) -> str:
    return (
        s.replace("&mdash;", "—")
        .replace("&nbsp;", " ")
        .replace("&amp;", "&")
        .replace("&quot;", '"')
        .replace("&#8217;", "’")
        .replace("&apos;", "'")
    )


def page_body(path: Path) -> str:
    raw = strip_front_matter(path.read_text(encoding="utf-8"))
    raw = replace_itch_blocks(raw)
    raw = inline_semantic_tags(raw)
    raw = linked_images_to_notes(raw)
    raw = imgs_to_notes(raw)
    raw = anchors_to_md(raw)
    raw = strip_remaining_html(raw)
    raw = strip_remaining_html(raw)
    raw = html_entity_light(raw)
    raw = re.sub(r"\n +\*\*", "\n**", raw)
    return re.sub(r"\n{3,}", "\n\n", raw).strip()


def main() -> None:
    chunks = [HEADER]

    cfg_raw = (ROOT / "_config.yml").read_text(encoding="utf-8")
    cfg_kv = yaml_quoted_strings_for_display(cfg_raw)
    chunks.append("## Nav labels (shown in sidebar / SEO)\n")
    for k in ("Site title", "SEO / subtitle", "Header tagline", "Back to top"):
        if k in cfg_kv:
            chunks.append(f"- **{k}:** {cfg_kv[k]}")
    chunks.append("")
    chunks.append("---")
    chunks.append("")

    pages: list[tuple[str, Path]] = [
        ("Home", ROOT / "index.md"),
        ("Work History", ROOT / "work-history.md"),
        ("Projects", ROOT / "projects.md"),
        ("Current Pursuits", ROOT / "activedev.md"),
        ("My Library", ROOT / "mylib.md"),
    ]

    for title, p in pages:
        chunks.append(f"## {title}")
        chunks.append("")
        chunks.append(page_body(p))
        chunks.append("")
        chunks.append("---")
        chunks.append("")

    OUT.write_text("\n".join(chunks).strip() + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
