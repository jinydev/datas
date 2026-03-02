import os
import re

base_dir = r"d:\site\jinydev\datas\src\python"
yml_path = r"d:\site\jinydev\datas\src\_data\python.yml"

def get_title(md_path):
    if not os.path.exists(md_path): return "제목 없음"
    with open(md_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("title: "):
                return line.replace("title: ", "").strip().strip('"')
    return "제목 없음"

res = ["main:"]

# Get chapters (01_..., 02_..., 03_...)
chapters = []
for entry in os.scandir(base_dir):
    if entry.is_dir() and re.match(r'^\d+_.+', entry.name):
        chapters.append(entry.name)

chapters.sort()

for chapter in chapters:
    chap_dir = os.path.join(base_dir, chapter)
    chap_md = os.path.join(chap_dir, "index.md")
    
    chap_title = get_title(chap_md)
    res.append(f"  - title: \"{chap_title}\"")
    res.append(f"    url: /python/{chapter}/")
    res.append(f"    children:")
    
    subdirs = []
    for sub in os.scandir(chap_dir):
        if sub.is_dir() and re.match(r'^\d+_.+', sub.name):
            subdirs.append(sub.name)
            
    subdirs.sort()
    for sub in subdirs:
        sub_md = os.path.join(chap_dir, sub, "index.md")
        sub_title = get_title(sub_md)
        res.append(f"      - title: \"{sub_title}\"")
        res.append(f"        url: /python/{chapter}/{sub}/")

with open(yml_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(res))

print("python.yml rebuilt.")
