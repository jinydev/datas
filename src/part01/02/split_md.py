import os
import re

base_dir = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/src/part01/02"
original_file = os.path.join(base_dir, "index.md")

with open(original_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

header_pattern = re.compile(r"^##\s+(\d+)\.\s+(.*)")

sections = []
current_section = []
current_title = ""
current_num = ""

intro_lines = []
global_counter = 1

for line in lines:
    match = header_pattern.match(line)
    if match:
        if current_title:
            sections.append((global_counter - 1, current_num, current_title, current_section))
        
        current_num = match.group(1)
        current_title = match.group(2).strip()
        
        if intro_lines:
            current_section = intro_lines + [line]
            intro_lines = []
        else:
            current_section = [line]
        global_counter += 1
    else:
        if current_title:
            current_section.append(line)
        else:
            intro_lines.append(line)

if current_title:
    sections.append((global_counter - 1, current_num, current_title, current_section))

count = 0
for g_num, num, title, content_lines in sections:
    safe_title = re.sub(r'[\\/*?:"<>|()]', "", title)
    safe_title = safe_title.replace(" ", "_")
    
    filename = f"{g_num:02d}_{safe_title}.md"
    out_file = os.path.join(base_dir, filename)
    
    header = f"---\nlayout: docs\ntitle: \"{num}. {title}\"\n---\n\n"
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(header)
        f.writelines(content_lines)
    
    count += 1

with open(os.path.join(base_dir, "split_success.txt"), "w") as f:
    f.write(f"Split {count} files successfully.\n")
