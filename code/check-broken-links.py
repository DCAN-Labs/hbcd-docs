import os
import re
from pathlib import Path
from urllib.parse import urlparse, unquote

RE_MD_LINK = re.compile(r'\[.*?\]\((.*?)\)')

def find_md_files(base_path):
    return [f for f in Path(base_path).rglob("*.md")]

def extract_links(md_text):
    return RE_MD_LINK.findall(md_text)

def is_internal(link):
    parsed = urlparse(link)
    return not parsed.scheme and not link.startswith('#')

def check_heading_anchor(file_path, anchor):
    """Check if a heading matching the anchor exists in the file."""
    anchor = anchor.lower().replace(' ', '-')
    try:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                if line.startswith("#"):
                    heading = line.strip("# ").strip().lower().replace(" ", "-")
                    if heading == anchor:
                        return True
    except Exception:
        return False
    return False

def check_link(base_path, current_file, link):
    full_path = (current_file.parent / unquote(link.split('#')[0])).resolve()
    if not full_path.exists():
        return False

    if '#' in link:
        anchor = link.split('#')[1]
        return check_heading_anchor(full_path, anchor)

    return True

def main(base_path):
    broken_links = []

    for md_file in find_md_files(base_path):
        with open(md_file, encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines, 1):
            for link in extract_links(line):
                if is_internal(link):
                    if not check_link(base_path, md_file, link):
                        broken_links.append((md_file, i, link))

    if broken_links:
        print("❌ Broken internal links found:")
        for file, line, link in broken_links:
            print(f"{file} (line {line}): {link}")
    else:
        print("✅ No broken internal links found.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python check_internal_links.py /path/to/docs")
        sys.exit(1)
    main(Path(sys.argv[1]).resolve())
