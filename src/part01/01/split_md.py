import os
import re
import shutil

base_dir = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/src/part01/01"
original_file = os.path.join(base_dir, "index.md")

with open(original_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

header_pattern = re.compile(r"^##\s+(\d+)\.\s+(.*)")
img_pattern = re.compile(r"!\[(.*?)\]\((.*?)\)")

sections = []
current_section = []
current_folder = ""
title_counter = 1
intro_lines = []

def make_folder_name(title, counter):
    mapping = {
        "Colab 개요": "colab_overview",
        "코랩(colab.research.google.com) 접속": "colab_access",
        "노트북 파일 생성": "create_notebook",
        "데이터 시각화 준비": "data_visualization_ready",
        "파일 데이터 처리": "file_data_processing",
        "노트북 파일 저장": "save_notebook",
        "VS Code 개요": "vscode_overview",
        "VS Code 설정": "vscode_settings",
        "파이썬 확장 설치와 소스 파일 실행": "python_extension_and_run"
    }
    eng_name = mapping.get(title.strip(), "section")
    return f"{counter:02d}_{eng_name}"

for line in lines:
    match = header_pattern.match(line)
    if match:
        if current_folder:
            sections.append((current_folder, current_section))
        
        title = match.group(2)
        current_folder = make_folder_name(title, title_counter)
        title_counter += 1
        
        if intro_lines:
            current_section = intro_lines + [line]
            intro_lines = []
        else:
            current_section = [line]
    else:
        if current_folder:
            current_section.append(line)
        else:
            intro_lines.append(line)

if current_folder:
    sections.append((current_folder, current_section))

count = 0
for folder, content_lines in sections:
    target_dir = os.path.join(base_dir, folder)
    img_dir = os.path.join(target_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    
    new_content = []
    
    for line in content_lines:
        def replace_img(match):
            img_alt = match.group(1)
            img_path = match.group(2)
            
            if os.path.exists(img_path):
                img_filename = os.path.basename(img_path)
                dest_img_path = os.path.join(img_dir, img_filename)
                shutil.copyfile(img_path, dest_img_path)
                return f"![{img_alt}](./img/{img_filename})"
            return match.group(0)
            
        new_line = img_pattern.sub(replace_img, line)
        new_content.append(new_line)
    
    out_file = os.path.join(target_dir, "index.md")
    
    title_str = "Untitled"
    for l in content_lines:
        if l.startswith("## "):
            title_str = l.replace("## ", "").strip()
            break
            
    header = f"---\nlayout: docs\ntitle: \"{title_str}\"\n---\n\n"
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(header)
        f.writelines(new_content)
    
    count += 1

print(f"Split {count} folders successfully.")
