import os
import fitz  # pymupdf
import pytesseract
from PIL import Image
import io

def convert_pdf_to_markdown_ocr(pdf_path):
    # 1. Setup paths
    base_dir = os.path.dirname(pdf_path)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Target directory (reuse existing)
    target_dir = os.path.join(base_dir, pdf_name)
    images_dir = os.path.join(target_dir, "img")
    
    os.makedirs(images_dir, exist_ok=True)
    
    md_path = os.path.join(target_dir, f"{pdf_name}_ocr.md")
    
    print(f"Processing PDF: {pdf_path}")
    print(f"Output Markdown: {md_path}")
    
    # 2. Open PDF
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF: {e}")
        return

    markdown_content = f"# {pdf_name} (OCR)\n\n"
    
    # 3. Iterate through pages
    total_pages = len(doc)
    for i, page in enumerate(doc):
        page_num = i + 1
        print(f"Processing Page {page_num}/{total_pages}...", end='\r')
        
        # Render page to image (High DPI for OCR)
        # zoom = 2 (approx 144 dpi) or 3 (216 dpi). Let's use 2.5 (~180 dpi) which is usually good enough for OCR without being too huge.
        mat = fitz.Matrix(2.5, 2.5) 
        pix = page.get_pixmap(matrix=mat)
        
        # Convert to PIL Image
        img_data = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_data))
        
        # Save image for Markdown referencing (we can reuse the filename pattern)
        # Note: We are overwriting the previous images with higher resolution versions.
        image_filename = f"page_{page_num:03d}.png"
        image_path = os.path.join(images_dir, image_filename)
        pix.save(image_path)
        
        # Run OCR
        text = pytesseract.image_to_string(image, lang='kor+eng')
        
        # Basic cleanup of OCR text
        # Remove multiple blank lines
        lines = text.split('\n')
        cleaned_lines = [line.rstrip() for line in lines if line.strip()]
        cleaned_text = '\n'.join(cleaned_lines)
        
        # Relative path for markdown
        relative_image_path = f"img/{image_filename}"
        
        # Append to markdown
        markdown_content += f"## Page {page_num}\n\n"
        markdown_content += f"{cleaned_text}\n\n"
        markdown_content += f"![Page {page_num} Original]({relative_image_path})\n\n"
        markdown_content += "---\n\n"

    print("\nSaving Markdown...")
    # 4. Save Markdown
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Done! Saved to {md_path}")

if __name__ == "__main__":
    pdf_file = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26/빅데이터분석기사26_실기1.pdf"
    
    if os.path.exists(pdf_file):
        convert_pdf_to_markdown_ocr(pdf_file)
    else:
        print(f"Error: PDF file not found at {pdf_file}")
