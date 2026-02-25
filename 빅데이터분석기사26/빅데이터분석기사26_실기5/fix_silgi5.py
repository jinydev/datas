
import re

file_path = "index.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_code_block = False
code_block_fence_pattern = re.compile(r'^\s*```')

for i, line in enumerate(lines):
    original_line = line
    stripped_line = line.strip()
    
    # Handle Unclosed Code Block before SECTION 03
    # If we are hitting "## SECTION 03" and we think we might be in a code block (logic difficult stateless)
    # Instead, let's target the specific context we saw.
    # Context: line 725 "    df1 = len(x) - 1", line 726 "## SECTION 03"
    # We will insert "```\n" if we see "## SECTION 03" and the previous non-empty line was indented code.
    
    if stripped_line.startswith("## SECTION 03") and lines[i-1].strip().startswith("df1 ="):
         new_lines.append("```\n\n")
    
    # Remove artifacts
    if re.search(r'\((그래프|이미지) (설명|출력)? ?(생략|없음)\)', stripped_line):
        continue
        
    # Promote Headers
    # ## 1. -> ### 1.
    match_h2_digit = re.match(r'^## (\d+\..*)', line)
    if match_h2_digit:
        new_lines.append(f"### {match_h2_digit.group(1)}\n")
        continue

    # ### 1) -> #### 1)
    match_h3_paren = re.match(r'^### (\d+\).*)', line)
    if match_h3_paren:
        new_lines.append(f"#### {match_h3_paren.group(1)}\n")
        continue
        
    # **Digit. ...** -> ### Digit. ... (Start of line)
    match_bold_digit = re.match(r'^\*\*(\d+\..*?)\*\*\s*$', stripped_line)
    if match_bold_digit:
        new_lines.append(f"### {match_bold_digit.group(1)}\n")
        continue

    # **Digit) ...** -> #### Digit) ... (Start of line)
    match_bold_paren = re.match(r'^\*\*(\d+\).*?)\*\*\s*$', stripped_line)
    if match_bold_paren:
        new_lines.append(f"#### {match_bold_paren.group(1)}\n")
        continue

    new_lines.append(original_line)

# Safety check for unclosed code blocks?
# If needed, but let's trust the specific fix first.

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Silgi 5 Refinement complete.")
