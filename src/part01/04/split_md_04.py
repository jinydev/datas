import os
import re

base_dir = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/src/part01/04"
original_file = os.path.join(base_dir, "index.md")

with open(original_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

header_pattern = re.compile(r"^###\s+(\d+)\.\s+(.*)")
section_pattern = re.compile(r"^##\s+SECTION")

sections = []
current_section_content = []
current_title = ""
current_num = ""

intro_lines = []
global_count = 1

for line in lines:
    match = header_pattern.match(line)
    if match:
        if current_title:
            sections.append((global_count - 1, current_num, current_title, current_section_content))
            
        current_num = match.group(1)
        current_title = match.group(2).strip()
        
        if intro_lines:
            current_section_content = intro_lines + [line]
            intro_lines = []
        else:
            current_section_content = [line]
        global_count += 1
    elif section_pattern.match(line):
        intro_lines.append(line)
    else:
        if current_title:
            current_section_content.append(line)
        else:
            intro_lines.append(line)

if current_title:
    sections.append((global_count - 1, current_num, current_title, current_section_content))

count = 0
for gnum, num, title, content_lines in sections:
    # safe title for filename
    safe_title = re.sub(r'[\\/*?:"<>|()\']', "", title)
    safe_title = safe_title.replace(" ", "_").replace("()", "")
    
    gNumStr = str(gnum).zfill(2)
    filename = f"{gNumStr}_{safe_title}.md"
    out_file = os.path.join(base_dir, filename)
    
    header = f"---\nlayout: docs\ntitle: \"{num}. {title}\"\n---\n\n"
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(header)
        f.writelines(content_lines)
    
    count += 1

print(f"Split {count} files successfully.")
