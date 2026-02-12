import re
import os

def cleanup_ocr_markdown(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    cleaned_lines = []
    
    # Code detection heuristics
    code_keywords = ['def ', 'class ', 'import ', 'from ', 'if ', 'else:', 'elif ', 'for ', 'while ', 'return ', 'print(', 'print (', '#', '    ', '\t']
    
    in_code_block = False
    code_buffer = []
    
    def flush_code(buffer, content_list):
        if buffer:
            # Simple check to avoid wrapping single lines of garbage as code, 
            # but for now let's be generous to capture snippets.
            content_list.append("```python\n")
            content_list.extend(buffer)
            content_list.append("```\n")
        return []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # 1. Structural Elements (Headers, Images, Separators)
        if stripped.startswith('#') or stripped.startswith('![') or stripped == '---':
            code_buffer = flush_code(code_buffer, cleaned_lines)
            in_code_block = False
            cleaned_lines.append(line)
            i += 1
            continue
            
        # 2. Empty lines
        if not stripped:
            if in_code_block:
                code_buffer.append(line)
            else:
                cleaned_lines.append(line)
            i += 1
            continue

        # 3. Code Detection
        is_code = False
        
        # Fix OCR spacing error in print
        if 'print (' in line:
            line = line.replace('print (', 'print(')
            stripped = line.strip()

        # Check for code signals
        # Indentation (often lost in OCR, but if present, use it)
        if line.startswith('    ') or line.startswith('\t'):
            is_code = True
        
        # Keywords
        if not is_code:
            for kw in code_keywords:
                if stripped.startswith(kw):
                    is_code = True
                    break
        
        # Assignment (var = val) - regex
        if not is_code and re.search(r'^\w+\s*=\s*.+', stripped):
            # Exclude lines that look like text: "Meaning = something"
            # Code usually has short var names.
            if len(stripped.split('=')[0].strip()) < 20:
                is_code = True

        # Comments
        if not is_code and stripped.startswith('#'):
            is_code = True

        if is_code:
            if not in_code_block:
                in_code_block = True
            code_buffer.append(line)
        else:
            if in_code_block:
                code_buffer = flush_code(code_buffer, cleaned_lines)
                in_code_block = False
            
            # Text Merging
            # OCR often breaks sentences.
            # Merge if previous line is text (not header/image) and doesn't end in typical sentence enders (.?!:)
            # Also OCR sometimes ends lines with hyphen - e.g. "import-\nant" -> "important"
            if cleaned_lines and cleaned_lines[-1].strip() and not cleaned_lines[-1].strip().startswith('#') and not cleaned_lines[-1].strip().startswith('!['):
                prev = cleaned_lines.pop().rstrip()
                
                # Check for hyphenation
                if prev.endswith('-'):
                    prev = prev[:-1] # Remove hyphen
                    cleaned_lines.append(f"{prev}{stripped}\n")
                else:
                    # Space merge
                    cleaned_lines.append(f"{prev} {stripped}\n")
            else:
                cleaned_lines.append(line)
                
        i += 1

    flush_code(code_buffer, cleaned_lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    print(f"Cleaned generic OCR markdown saved to: {output_path}")

if __name__ == "__main__":
    target_file = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26/빅데이터분석기사26_실기1/빅데이터분석기사26_실기1_ocr.md"
    cleanup_ocr_markdown(target_file, target_file)
