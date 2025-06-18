import os
import re

def find_warning_banners(source_dir, output_html_root="/"):
    warning_paths = []

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                    # Look for a <div id="warning" ...> block
                    if re.search(r'<div\s+id=["\']alert["\']', content):
                        # Build relative path to markdown file
                        rel_md_path = os.path.relpath(file_path, source_dir)
                        rel_html_path = os.path.splitext(rel_md_path)[0]

                        # ReadTheDocs usually renders .md files into /path/to/file/ index.html
                        # So "foo/bar.md" → "/foo/bar/"
                        html_url = os.path.join(output_html_root, rel_html_path, "#alert").replace("\\", "/")
                        warning_paths.append(html_url)

    return warning_paths

# Example usage
if __name__ == "__main__":
    source_markdown_dir = "docs"  # or your MkDocs source folder
    warnings = find_warning_banners(source_markdown_dir)

    print("Found warning banners in the following locations:")
    for path in warnings:
        print(path)
