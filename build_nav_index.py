import os
import re

src_dir = r"d:\site\jinydev\datas\src"

def extract_meta(md_path):
    title = ""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', content, re.MULTILINE)
        if match:
            title = match.group(1).strip()
    return title

def build_nav(section):
    section_dir = os.path.join(src_dir, section)
    yml_lines = ["main:", "  - title: 학습목차", "    subitems:"]
    
    subdirs = sorted([d for d in os.listdir(section_dir) if os.path.isdir(os.path.join(section_dir, d))])
    
    for d in subdirs:
        md_file = os.path.join(section_dir, d, "index.md")
        if os.path.exists(md_file):
            title = extract_meta(md_file)
            if not title:
                title = d
            
            # Remove leading numbers and formatting from title in nav
            clean_title = re.sub(r'^\d+\.\s*', '', title)
            clean_title = re.sub(r'^\[\d+\]\s*', '', clean_title)
            # Escape double quotes if any
            clean_title = clean_title.replace('"', '\\"')
            
            yml_lines.append(f'      - title: "{clean_title}"')
            yml_lines.append(f'        url: "/{section}/{d}/"')
            
    # Write nav yaml
    yml_path = os.path.join(src_dir, "_data", f"{section}.yml")
    with open(yml_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(yml_lines) + "\n")
    print(f"Generated {yml_path}")

def build_index(section, main_title):
    section_dir = os.path.join(src_dir, section)
    subdirs = sorted([d for d in os.listdir(section_dir) if os.path.isdir(os.path.join(section_dir, d))])
    
    index_md_content = f"""---
layout: {section}
title: {main_title}
permalink: /{section}/
---

# {main_title} 핵심 가이드

아래의 링크를 클릭하여 해당 학습 내용으로 이동하세요.

## 학습목차
"""
    for d in subdirs:
        md_file = os.path.join(section_dir, d, "index.md")
        if os.path.exists(md_file):
            title = extract_meta(md_file)
            if not title:
                title = d
            index_md_content += f"\n### [{title}](/{section}/{d}/)\n"
            
    index_path = os.path.join(section_dir, "index.md")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_md_content)
    print(f"Generated {index_path}")

if __name__ == "__main__":
    build_nav("pandas")
    build_nav("mathplotlib")
    build_index("pandas", "판다스 (Pandas)")
    build_index("mathplotlib", "데이터 시각화 (Matplotlib/Seaborn)")
