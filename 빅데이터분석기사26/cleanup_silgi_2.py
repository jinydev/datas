
import re
import sys

def clean_markdown_logic(content):
    # 1. Merge Headers just in case
    content = re.sub(r'(#\s+PART)\s*\n+\s*(\d+)', r'\1 \2', content, flags=re.IGNORECASE)
    content = re.sub(r'(#\s+SECTION)\s*\n+\s*(\d+)', r'\1 \2', content, flags=re.IGNORECASE)

    lines = content.split('\n')
    new_lines = []
    
    # We will accumulate "paragraph text" in a list, then join them.
    text_buffer = [] 
    
    in_code_block = False
    
    def flush_buffer(buf, output_list):
        if not buf:
            return
        # Join the buffer. 
        # Check if we need spaces between lines.
        # Usually yes, unless it's Korean where sometimes it's ambiguous, but space is safe.
        full_text = " ".join([x.strip() for x in buf if x.strip()])
        output_list.append(full_text)
        output_list.append("") # Add a blank line after paragraph
        buf.clear()

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check Code Block
        if stripped.startswith('```'):
            flush_buffer(text_buffer, new_lines)
            new_lines.append(line)
            in_code_block = not in_code_block
            i += 1
            continue
            
        if in_code_block:
            new_lines.append(line)
            i += 1
            continue
            
        # Check Special Lines (Headers, Images, List Items, Blockquotes)
        # Note: ' - ' or '* ' or '1. ' for lists
        is_list = re.match(r'^(\s*[-*+]|\s*\d+\.)\s+', line)
        is_header = stripped.startswith('#')
        is_image = stripped.startswith('![')
        is_quote = stripped.startswith('>')
        is_table = stripped.startswith('|')
        
        if is_list or is_header or is_image or is_quote or is_table:
            flush_buffer(text_buffer, new_lines)
            new_lines.append(line)
            i += 1
            continue
            
        # Empty Line
        if not stripped:
            # If our buffer ends with a sentence ending punctuation, this empty line is REAL paragraph break.
            # If not, it's a false break, so we ignore it and keep accumulating in buffer.
            if text_buffer:
                last_segment = text_buffer[-1].strip()
                if last_segment.endswith(('.', '?', '!', ':', '。')):
                     flush_buffer(text_buffer, new_lines)
                     # new_lines.append("") # flush adds one, maybe add another?
            i += 1
            continue
            
        # Regular Text Line
        # If previous buffer ended with definitive punctuation, flush it before starting new one.
        if text_buffer:
            last_segment = text_buffer[-1].strip()
            if last_segment.endswith(('.', '?', '!', ':', '。')):
                 flush_buffer(text_buffer, new_lines)
        
        text_buffer.append(line)
        i += 1
        
    flush_buffer(text_buffer, new_lines)
    
    return "\n".join(new_lines)

def apply_specific_fixes(content):
    # Fixes from previous script
    content = content.replace("to_datetimeO", "to_datetime()")
    content = content.replace("headO", "head()")
    content = content.replace("read csv", "read_csv")
    content = content.replace("read_ csv", "read_csv")
    content = content.replace("scikit-Iearn", "scikit-learn")
    content = content.replace("Mmn-Max", "Min-Max")
    content = content.replace("SE CTtO N", "SECTION")
    content = content.replace("to_dtetimeO", "to_datetime()")
    
    content = re.sub(r'\. \s*head\(\)', '.head()', content)
    content = re.sub(r'\. \s*shape', '.shape', content)
    content = re.sub(r'\. \s*columns', '.columns', content)
    content = re.sub(r'\. \s*info', '.info', content)
    
    # Collapse multiple newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cleanup_silgi_2.py <input_md>")
        sys.exit(1)
        
    input_path = sys.argv[1]
    
    with open(input_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()
        
    cleaned_content = clean_markdown_logic(raw_content)
    final_content = apply_specific_fixes(cleaned_content)
    
    with open(input_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print(f"Cleaned {input_path}")
