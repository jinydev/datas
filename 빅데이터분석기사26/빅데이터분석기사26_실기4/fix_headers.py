
import re

file_path = "index.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    original_line = line
    stripped_line = line.strip()
    
    # Check for **Digit. ...** pattern
    # Regex: ^\*\*(\d+\..*?)\*\*$
    match_dot = re.match(r'^\*\*(\d+\..*?)\*\*$', stripped_line)
    if match_dot:
        # Promote to ###
        content = match_dot.group(1)
        new_line = f"### {content}\n"
        new_lines.append(new_line)
        continue

    # Check for **Digit) ...** pattern
    # Regex: ^\*\*(\d+\).*?)\*\*$
    match_paren = re.match(r'^\*\*(\d+\).*?)\*\*$', stripped_line)
    if match_paren:
        # Promote to ####
        content = match_paren.group(1)
        new_line = f"#### {content}\n"
        new_lines.append(new_line)
        continue
        
    new_lines.append(original_line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Header refinement complete.")
