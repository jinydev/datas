import sys
import os

def organize_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    
    # Divider pattern
    divider = ["\n", "<br>\n", "\n", "---\n", "\n", "<br>\n", "\n"]
    
    first_header_found = False
    
    # Section check
    has_summary = False
    
    for i, line in enumerate(lines):
        # Check for headers
        if line.strip().startswith('##') or line.strip().startswith('###'):
            # Skip if it's the very first line or close to it (Title)
            if i < 5 and line.startswith('# '):
                # Title, skip
                pass
            elif not first_header_found:
                 # First section header, usually don't need huge divider before it if it follows title/intro immediately
                 # But let's check if there is a big gap
                 first_header_found = True
            else:
                # Check if preceding lines already have a divider
                # Look back 10 lines
                lookback = "".join(lines[max(0, i-10):i])
                if "---" not in lookback:
                    # check if previous line is also a header (header stack)
                    prev_line = lines[i-1].strip() if i > 0 else ""
                    if not (prev_line.startswith('#')):
                        # Insert divider
                        new_lines.extend(divider)
        
        new_lines.append(line)
        
        if line.strip().startswith("##") and ("정리" in line or "Summary" in line):
            has_summary = True

    # 2. Add Summary if missing
    # We only add it if it's a lecture file (not index.md)
    if "index.md" not in filepath and not has_summary:
        # Determine the section number for Summary
        # Find the last header to increment or just use "정리"
        # Using a generic header for now
        
        # Try to find the last H2 number
        last_h2 = "0"
        for line in reversed(new_lines):
            if line.strip().startswith("## "):
                # Extract number like ## 3.1.1.
                parts = line.strip().split()
                if len(parts) > 1 and parts[1][0].isdigit():
                    last_h2 = parts[1]
                    break
        
        summary_section = "\n<br>\n\n---\n\n<br>\n\n## 정리 (Summary)\n\n이 강의에서 배운 핵심 내용을 요약해 봅시다.\n\n*   **[핵심 1]**: (내용 채우기)\n*   **[핵심 2]**: (내용 채우기)\n*   **[핵심 3]**: (내용 채우기)\n"
        new_lines.append(summary_section)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Processed {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python organize_md.py <file_path>")
        sys.exit(1)
    
    organize_file(sys.argv[1])
