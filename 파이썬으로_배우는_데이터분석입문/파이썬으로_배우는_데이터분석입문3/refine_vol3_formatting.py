
import re
import os

input_file = "파이썬으로_배우는_데이터분석입문3.md"
output_file = "파이썬으로_배우는_데이터분석입문3_refined.md"

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_next = False

# Patterns
header_h2_pattern = re.compile(r'^\s*(\d+\.\d+)\s+(.*)') # 3.1 ...
header_h3_pattern = re.compile(r'^\s*(\d+|@®|68|@|®)\s+(.*)') # 68 내장함수... or @® ...
section_footer_pattern = re.compile(r'^\s*(Section \d+|Chapter \d+).*')
page_number_pattern = re.compile(r'^\s*\d+\s*$')

# Known H2 titles from index
h2_titles = [
    "패키지 numpy 개요와 자료형 ndarray",
    "내장함수 arange( )와 linspace( )",
    "내장함수 zeros( )와 ones( ) , empty( )",
    "배열 연산",
    "배열 슬라이싱과 형태 수정",
    "브로드캐스팅",
    "고급 색인"
]

# Helper to check if line matches a known H2 title roughly
def is_h2_title(text):
    for title in h2_titles:
        # Simple fuzzy match: clean special chars and spaces
        clean_text = re.sub(r'[^\w]', '', text)
        clean_title = re.sub(r'[^\w]', '', title)
        if clean_title in clean_text:
            return True
    return False

in_code_block = False

for i, line in enumerate(lines):
    line = line.strip()
    
    # Skip empty lines if previous was empty (reduce multiple newlines)
    if not line:
        if new_lines and not new_lines[-1]:
            continue
        new_lines.append("")
        continue

    # Code block detection
    if line.startswith("```"):
        in_code_block = not in_code_block
        new_lines.append(line)
        continue
    
    if in_code_block:
        new_lines.append(line)
        continue

    # Remove Page Headers/Footers
    if section_footer_pattern.match(line):
        continue
    if page_number_pattern.match(line):
        continue
    if "Chapter 03" in line and "과학용 컴퓨팅 패키지" in line:
        continue
    
    # Latex/OCR garbage cleanup
    line = line.replace("|", "") # remove vertical bars often found in margins
    
    # H2 Detection
    # Check for "3.x Title"
    m_h2 = header_h2_pattern.match(line)
    if m_h2:
        # check if it looks like a valid title
        if is_h2_title(m_h2.group(2)) or "개요" in m_h2.group(2) or "함수" in m_h2.group(2):
            new_lines.append(f"\n## {m_h2.group(1)} {m_h2.group(2)}\n")
            continue
            
    # H3 Detection (often OCR'd as 68, @®, etc followed by text)
    # common patterns: "68 내장함수...", "@® ...", "® ..."
    # But be careful not to match code variables or math
    m_h3 = header_h3_pattern.match(line)
    if m_h3:
        prefix = m_h3.group(1)
        title = m_h3.group(2)
        # Verify it's not just a small number or variable
        if len(title) > 2 and (prefix in ['68', '@®', '®', '@'] or (prefix.isdigit() and int(prefix) > 10)):
             # Additional check: does it look like a title?
             if "함수" in title or "배열" in title or "개요" in title or "자료형" in title or "연산" in title or "인덱싱" in title:
                 new_lines.append(f"\n### {title}\n")
                 continue

    # Clean up image tags text
    if line.startswith("![Image]"):
        # Ensure spacing
        if new_lines and new_lines[-1]:
            new_lines.append("")
        new_lines.append(line)
        new_lines.append("")
        continue

    # Tables: [표 3-x]
    if line.startswith("[표 3-") or line.startswith("[그림 3-"):
        new_lines.append(f"\n**{line}**\n")
        continue

    new_lines.append(line)

# Write output
with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(l + '\n' for l in new_lines)

print(f"Created {output_file}")
