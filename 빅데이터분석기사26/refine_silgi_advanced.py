
import fitz
import sys
import os
import re

def clean_code_text(text):
    # Fix common OCR/Text-layer artifacts in Python code
    
    # 1. Fix print function
    # Matches "printC", "print(", "print (", "print '" (if missing paren)
    # Replaces with "print("
    # Note: "print" followed by ' or " without paren is invalid in Python 3.
    # We assume it should be "print(..."
    text = re.sub(r'print\s*[C(]\s*', 'print(', text)
    text = re.sub(r"print\s+(?=['\"])", "print(", text)
    
    # Fix "print ('..." -> "print('"
    text = re.sub(r"print\(\s+", "print(", text)

    # 2. Fix operators
    # "I/" or "ll" or "II" -> "//"
    # match space around it to avoid killing words
    text = re.sub(r'(\s+)[Il1]/\s+', r'\1// ', text)
    text = re.sub(r'(\s+)[Il]{2}\s+', r'\1// ', text)
    # Fix "I%" -> "%"?
    
    # 3. Fix quotes
    text = text.replace('“', '"').replace('”', '"').replace("‘", "'").replace("’", "'")
    # Fix "’" -> "'" specifically
    text = text.replace('’', "'")
    
    # 4. Fix inequality
    text = text.replace('》', '>')
    text = text.replace('《', '<')
    
    return text

def refine_pdf_to_markdown(pdf_path, output_md_path):
    doc = fitz.open(pdf_path)
    md_content = []
    
    output_dir = os.path.dirname(output_md_path)
    img_dir = os.path.join(output_dir, "img")
    os.makedirs(img_dir, exist_ok=True)

    # Expanded code patterns
    # Added 'print' without paren (for "printC"), assignments, comments
    code_pattern = re.compile(r'^\s*(import\s+|from\s+|class\s+|def\s+|print|#|[a-zA-Z_]\w*\s*=[^=]|if\s+|for\s+|while\s+|return\s+)', re.MULTILINE)

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        blocks.sort(key=lambda b: (b["bbox"][1], b["bbox"][0]))
        
        for block in blocks:
            if block["type"] == 0: # Text
                lines_list = []
                # Reconstruct text with font analysis
                block_text_lines = []
                heading_level = 0
                
                for line in block["lines"]:
                    line_text = ""
                    max_size = 0
                    for span in line["spans"]:
                        line_text += span["text"]
                        if span["size"] > max_size:
                            max_size = span["size"]
                    block_text_lines.append(line_text)

                    # Determine header level based on max font size in the block
                    if max_size > 20: heading_level = 1
                    elif max_size > 16: heading_level = 2
                    elif max_size > 14: heading_level = 3
                
                full_block_text = "\n".join(block_text_lines).strip()
                if not full_block_text:
                    continue

                code_matches = len(code_pattern.findall(full_block_text))
                total_lines = len(block_text_lines)
                is_code_block = False
                
                if total_lines > 0:
                    first_line = block_text_lines[0].strip()
                    if first_line.startswith(("import ", "from ", "def ", "class ", "```")):
                         is_code_block = True
                    elif code_matches >= 1 and total_lines <= 3:
                         is_code_block = True
                    elif code_matches / total_lines > 0.3:
                         is_code_block = True
                        
                if is_code_block:
                    full_block_text = clean_code_text(full_block_text)
                    md_content.append(f"\n```python\n{full_block_text}\n```\n")
                else:
                    if heading_level > 0:
                        md_content.append(f"\n{'#' * heading_level} {full_block_text}\n")
                    else:
                        formatted_text = re.sub(r'^[•·]\s*', '- ', full_block_text, flags=re.MULTILINE)
                        md_content.append(f"{formatted_text}\n")

            elif block["type"] == 1: # Image
                img_filename = f"page_{page_num+1:03d}_img_{block['number']}.png"
                img_path = os.path.join(img_dir, img_filename)
                rect = fitz.Rect(block["bbox"])
                pix = page.get_pixmap(clip=rect)
                pix.save(img_path)
                rel_path = os.path.join("img", img_filename)
                md_content.append(f"\n![Image]({rel_path})\n")

    full_text = "\n".join(md_content)
    
    # Remove Page X
    full_text = re.sub(r'(?i)^#*\s*Page\s*\d+\s*$', '', full_text, flags=re.MULTILINE)
    
    # Merge Adjacent Code Blocks
    # Loop until no changes to catch multiple merges
    while True:
        new_text = re.sub(r'```python\s*\n(.*?)\n```\s*\n+```python\s*\n', r'```python\n\1\n', full_text, flags=re.DOTALL)
        if new_text == full_text:
            break
        full_text = new_text

    # Clean newlines
    full_text = re.sub(r'\n{3,}', '\n\n', full_text)

    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(full_text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
         print("Usage: python refine_silgi_advanced.py <input_pdf> [output_md]")
         sys.exit(1)
         
    input_pdf = sys.argv[1]
    if len(sys.argv) >= 3:
        output_md = sys.argv[2]
    else:
        folder = os.path.dirname(input_pdf)
        base = os.path.splitext(os.path.basename(input_pdf))[0]
        output_md = os.path.join(folder, base + ".md")

    print(f"Refining {input_pdf} -> {output_md}")
    refine_pdf_to_markdown(input_pdf, output_md)
    print("Done.")
