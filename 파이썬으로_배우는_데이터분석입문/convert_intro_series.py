
import fitz
import os
import re
import glob
import pytesseract
from PIL import Image
import sys

# Set Tesseract cmd if needed (usually handled by PATH)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract' 

def clean_ocr_text(text):
    # Basic cleanup for OCR artifacts
    text = text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    return text.strip()

def process_volume_ocr(vol_num, base_dir):
    folder_name = f"파이썬으로_배우는_데이터분석입문{vol_num}"
    folder_path = os.path.join(base_dir, folder_name)
    img_dir = os.path.join(folder_path, "img")
    
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    # Find PDF for basename
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    if not pdf_files:
        print(f"No PDF found in {folder_path}")
        return
    
    pdf_path = pdf_files[0]
    pdf_basename = os.path.splitext(os.path.basename(pdf_path))[0]
    output_md_path = os.path.join(folder_path, f"{pdf_basename}.md")
    
    print(f"Processing Vol {vol_num}: {pdf_path} -> {output_md_path} (OCR Mode)")
    
    # Get images from img directory
    if not os.path.exists(img_dir):
        print(f"Image directory not found: {img_dir}")
        return
        
    # Get all image files
    image_files = glob.glob(os.path.join(img_dir, "*"))
    # Filter for known extensions
    image_files = [f for f in image_files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Sort by page number extracted from filename (assumes BASENAME_PAGENUM.ext)
    # Be careful with NFD normalization. We rely on the trailing number.
    def get_page_num(filename):
        try:
            name = os.path.splitext(os.path.basename(filename))[0]
            parts = name.split('_')
            return int(parts[-1])
        except ValueError:
            return 999999
            
    image_files.sort(key=get_page_num)
    
    md_content = []
    
    for img_path in image_files:
        img_filename = os.path.basename(img_path)
        page_num = get_page_num(img_filename)
        
        print(f"  Processing Page {page_num}: {img_filename}")
        
        # 1. Insert Image
        md_content.append(f"![Image](img/{img_filename})\n\n")
        
        # 2. OCR Text Extraction
        try:
            text = pytesseract.image_to_string(Image.open(img_path), lang='kor+eng')
        except Exception as e:
            print(f"    OCR Failed for {img_filename}: {e}")
            text = ""
            
        # 3. Format Text
        lines = text.split('\n')
        formatted_lines = []
        in_code_block = False
        
        code_indicators = ["import ", "def ", "class ", "print(", "return ", "if __name__", "pd.DataFrame", "np.array", "plt.", "sns."]
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            
            # Simple code block detection
            is_code_line = any(stripped.startswith(ind) for ind in code_indicators) or (in_code_block and (stripped.startswith("    ") or stripped.startswith("\t")))
            
            if is_code_line:
                if not in_code_block:
                    formatted_lines.append("\n```python")
                    in_code_block = True
            elif in_code_block:
                # If we were in code block but this line doesn't look like code (and is not indented)
                # This heuristic is weak for OCR text which might lose indentation.
                # Use a specific check: if previous line was code, and this one is clearly text (Hangul)
                if re.search(r'[가-힣]', stripped):
                     formatted_lines.append("```\n")
                     in_code_block = False

            formatted_lines.append(stripped)
            
        if in_code_block:
            formatted_lines.append("```\n")
            
        md_content.append("\n".join(formatted_lines) + "\n\n")

    # Save
    full_text = "\n".join(md_content)
    
    # Basic cleanup of excessive newlines
    full_text = re.sub(r'\n{3,}', '\n\n', full_text)

    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"Saved {output_md_path}")

def main():
    base_dir = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/파이썬으로_배우는_데이터분석입문"
    
    # If args provided
    if len(sys.argv) > 1:
        try:
            vol = int(sys.argv[1])
            process_volume_ocr(vol, base_dir)
        except ValueError:
            print("Usage: python3 convert_intro_series.py [vol_num]")
            # Default to all if invalid arg or loop
    else:
        # Default to only Vol 1 as requested first, or loop all?
        # User said "Markdown을 다시 작성해 주세요" for Vol 1 files.
        # But logically I should support all.
        # Let's verify Vol 1 first.
        process_volume_ocr(1, base_dir)

if __name__ == "__main__":
    main()
