import os
import re

base_dir = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/src/part01/01"
original_file = os.path.join(base_dir, "index.md")

with open(original_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

header_pattern = re.compile(r"^##\s+(\d+)\.\s+(.*)")

sections = []
current_section = []
current_title = ""
current_num = ""

intro_lines = []

for line in lines:
    match = header_pattern.match(line)
    if match:
        if current_title:
            sections.append((current_num, current_title, current_section))
        
        current_num = match.group(1)
        current_title = match.group(2).strip()
        
        if intro_lines:
            # intro_lines are added to the first section
            current_section = intro_lines + [line]
            intro_lines = []
        else:
            current_section = [line]
    else:
        if current_title:
            current_section.append(line)
        else:
            intro_lines.append(line)

if current_title:
    sections.append((current_num, current_title, current_section))

count = 0
for num, title, content_lines in sections:
    # clean title for filename
    safe_title = re.sub(r'[\\/*?:"<>|()]', "", title)
    safe_title = safe_title.replace(" ", "_")
    
    filename = f"{num}_{safe_title}.md"
    out_file = os.path.join(base_dir, filename)
    
    header = f"---\nlayout: docs\ntitle: \"{title}\"\n---\n\n"
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(header)
        f.writelines(content_lines)
    
    count += 1

print(f"Split {count} files successfully.")
