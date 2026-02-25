import re
import os

source_file = "index.md"

def clean_line(line):
    # Remove artifacts
    line = re.sub(r'\((그래프|이미지) (설명|출력)? ?(생략|없음)\)', '', line)
    return line

def refine_header(line):
    stripped = line.strip()
    
    # **Digit. ...** -> ### Digit. ...
    match_bold_digit = re.match(r'^\*\*\s*(\d+\..*?)\s*\*\*$', stripped)
    if match_bold_digit:
        return f"### {match_bold_digit.group(1)}\n"
    
    # **Digit) ...** -> #### Digit) ...
    match_bold_paren = re.match(r'^\*\*\s*(\d+\).*?)\s*\*\*$', stripped)
    if match_bold_paren:
        return f"#### {match_bold_paren.group(1)}\n"
        
    return line

def process_content(lines):
    processed_lines = []
    in_code_block = False
    
    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            processed_lines.append(line)
            continue
            
        if in_code_block:
            processed_lines.append(line)
            continue
            
        line = clean_line(line)
        line = refine_header(line)
        processed_lines.append(line)
        
    return processed_lines

with open(source_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Identify Split Points
section1_idx = -1
section2_idx = -1
questions_idx = -1

for i, line in enumerate(lines):
    if line.strip().startswith("# SECTION 01") or line.strip().startswith("**SECTION 01"):
        section1_idx = i
    elif line.strip().startswith("# SECTION 02") or line.strip().startswith("**SECTION 02"):
        section2_idx = i
    elif "**합격을 다지는 예상문제**" in line:
        questions_idx = i

print(f"Indices: S1={section1_idx}, S2={section2_idx}, Q={questions_idx}")

files_to_create = []

# Section 01
if section1_idx != -1:
    end_idx = section2_idx if section2_idx != -1 else (questions_idx if questions_idx != -1 else len(lines))
    content = lines[section1_idx:end_idx]
    
    # Extract title
    header_line = content[0]
    title_match = re.search(r'SECTION 01\s+(.*)', header_line)
    title = title_match.group(1).strip() if title_match else "데이터 수집 및 전환"
    
    new_content = [f"# 3.1 {title}\n"] + process_content(content[1:])
    files_to_create.append({
        "filename": "3.1_데이터_수집_및_전환.md",
        "content": new_content
    })

# Section 02
if section2_idx != -1:
    end_idx = questions_idx if questions_idx != -1 else len(lines)
    content = lines[section2_idx:end_idx]
    
    header_line = content[0]
    title_match = re.search(r'SECTION 02\s+(.*)', header_line)
    title = title_match.group(1).strip() if title_match else "데이터 적재 및 저장"
    
    new_content = [f"# 3.2 {title}\n"] + process_content(content[1:])
    files_to_create.append({
        "filename": "3.2_데이터_적재_및_저장.md",
        "content": new_content
    })

# Questions
if questions_idx != -1:
    content = lines[questions_idx:]
    # Add title
    new_content = ["# 3.3 예상문제\n", "\n"] + process_content(content)
    files_to_create.append({
        "filename": "3.3_예상문제.md",
        "content": new_content
    })

# Write sub-files
for item in files_to_create:
    with open(item['filename'], 'w', encoding='utf-8') as f:
        f.writelines(item['content'])
    print(f"Created {item['filename']}")

# Update index.md
index_content = """---
layout: post
title: 빅데이터분석기사 필기 3과목
---

# 데이터 수집 및 저장 계획

## 3.1 데이터 수집 및 전환
- [데이터 수집 및 전환](./3.1_데이터_수집_및_전환.md)

## 3.2 데이터 적재 및 저장
- [데이터 적재 및 저장](./3.2_데이터_적재_및_저장.md)

## 3.3 예상문제
- [예상문제](./3.3_예상문제.md)
"""

with open("index.md", 'w', encoding='utf-8') as f:
    f.write(index_content)
print("Updated index.md")
