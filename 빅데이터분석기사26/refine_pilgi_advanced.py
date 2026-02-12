
import fitz
import sys
import os
import re

def clean_code_text(text):
    # Basic cleanup for code-like text or general text
    text = re.sub(r'print\\s*[C(]\\s*', 'print(', text)
    text = re.sub(r"print\\s+(?=[\'\\\"])", "print(", text)
    text = text.replace('“', '"').replace('”', '"').replace("‘", "'").replace("’", "'")
    return text

def refine_pdf_to_markdown(pdf_path, output_md_path):
    doc = fitz.open(pdf_path)
    md_content = []
    
    output_dir = os.path.dirname(output_md_path)
    img_dir = os.path.join(output_dir, "img")
    os.makedirs(img_dir, exist_ok=True)

    # Threshold for dividing columns (based on analysis of Page 2)
    COLUMN_SPLIT_X = 350 

    for page_num, page in enumerate(doc):
        # 1. Image Extraction
        image_list = page.get_images(full=True)
        # Use page.get_pixmap() for better quality if possible, but get_images is faster for checks
        # We will iterate blocks anyway

        blocks = page.get_text("dict")["blocks"]
        
        # Sort by Column (Left < 350, Right >= 350), then by Y, then X
        # This ensures Left Column is read first top-to-bottom, then Right Column
        blocks.sort(key=lambda b: (1 if b["bbox"][0] > COLUMN_SPLIT_X else 0, b["bbox"][1], b["bbox"][0]))
        
        # md_content.append(f"\\n<!-- Page {page_num+1} -->\\n") # User requested to remove this
        
        # 2. Table Extraction (Try to detect tables)
        # fitz 'tables' API (if available in this env)
        try:
            tabs = page.find_tables()
            # We can't easily interleave tables with blocks unless we check bbox overlap
            # For now, we'll try to process tables if they exist, but simple text extraction might duplicate content
            # A better strategy: if a block overlaps with a table, skip the block and use the table.
            table_rects = [t.bbox for t in tabs]
        except:
            tabs = []
            table_rects = []

        processed_blocks = set()

        for tab_idx, tab in enumerate(tabs):
             # Convert table to markdown
             md_table = tab.to_markdown()
             # Find where this table fits in the flow. 
             # It's hard to place exactly without complex logic. 
             # We will place it when we encounter a text block that *would* have been inside.
             pass

        for block in blocks:
            # Check if block is inside a table
            is_in_table = False
            block_rect = fitz.Rect(block["bbox"])
            for t_rect in table_rects:
                if fitz.Rect(t_rect).intersects(block_rect):
                    # Check coverage? If mostly detailed, maybe it IS the table content.
                    # fitz text blocks usually break down table cells. 
                    # If we use find_tables, we should rely on that for the table area.
                    is_in_table = True
                    break
            
            # If we decide to use the table tool, we should output the table *once*.
            # This logic is complex. For now, let's stick to text blocks for reliability 
            # unless the user *really* needs perfect tables, which 'find_tables' provides.
            # Let's try to detect if we are hitting a table area.
            
            if block["type"] == 0: # Text
                block_text_lines = []
                heading_level = 0
                is_code_block = False
                
                # Check formatting for headers
                for line in block["lines"]:
                    line_text = ""
                    max_size = 0
                    for span in line["spans"]:
                        line_text += span["text"]
                        if span["size"] > max_size:
                            max_size = span["size"]
                    block_text_lines.append(line_text)

                    if max_size > 20: heading_level = 1
                    elif max_size > 16: heading_level = 2
                    elif max_size > 14: heading_level = 3
                    elif max_size > 12: heading_level = 4
                
                full_block_text = "\n".join(block_text_lines).strip()
                if not full_block_text:
                    continue

                # Heuristic for Code Blocks
                code_indicators = ["import ", "def ", "class ", "print(", "return ", "if __name__"]
                if (any(full_block_text.startswith(ind) for ind in code_indicators) or 
                    "```" in full_block_text or
                    (len(block_text_lines) > 1 and "=" in full_block_text and "(" in full_block_text and ":" in full_block_text)):
                    is_code_block = True

                # Check if it's a side note (Right Column)
                is_side_note = block["bbox"][0] > COLUMN_SPLIT_X
                
                if is_code_block:
                    full_block_text = clean_code_text(full_block_text)
                    md_content.append(f"\n```python\n{full_block_text}\n```\n")
                elif heading_level > 0:
                    # Remove any existing # from OCR
                    clean_text = full_block_text.lstrip('#').strip()
                    md_content.append(f"\n{'#' * heading_level} {clean_text}\n")
                else:
                    # Treat bullet points
                    formatted_text = re.sub(r'^[•·]\s*', '- ', full_block_text, flags=re.MULTILINE)
                    # Treat numbered lists (basic)
                    formatted_text = re.sub(r'^(\d+)\.\s*', r'\1. ', formatted_text, flags=re.MULTILINE)

                    # Simple LaTeX replacement heuristics (very basic)
                    formatted_text = formatted_text.replace("alpha", "$\\alpha$")
                    formatted_text = formatted_text.replace("beta", "$\\beta$")
                    formatted_text = formatted_text.replace("theta", "$\\theta$")
                    formatted_text = formatted_text.replace("delta", "$\\delta$")
                    formatted_text = formatted_text.replace("sigma", "$\\sigma$")
                    
                    if is_side_note:
                        # Append as quote or separate block
                        formatted_text = f"> {formatted_text}"
                    
                    md_content.append(f"{formatted_text}\n")

            elif block["type"] == 1: # Image
                img_filename = f"page_{page_num+1:03d}_img_{block['number']}.png"
                img_path = os.path.join(img_dir, img_filename)
                rect = fitz.Rect(block["bbox"])
                try:
                    pix = page.get_pixmap(clip=rect)
                    pix.save(img_path)
                    rel_path = os.path.join("img", img_filename)
                    md_content.append(f"\n![Image]({rel_path})\n")
                except:
                    pass

    full_text = "\n".join(md_content)
    
    # Post-processing cleanup
    # Remove "Page X" headers anywhere
    full_text = re.sub(r'(?i)^#*\s*Page\s*\d+\s*$', '', full_text, flags=re.MULTILINE)
    
    # Clean up excessive newlines
    full_text = re.sub(r'\n{3,}', '\n\n', full_text)
    
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(full_text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
         print("Usage: python refine_pilgi_advanced.py <input_pdf> [output_md]")
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
