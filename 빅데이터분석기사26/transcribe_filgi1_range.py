import os
import fitz  # pymupdf
import pytesseract
from PIL import Image
import io

def transcribe_range(pdf_path, start_page, end_page):
    # 1. Setup paths
    base_dir = os.path.dirname(pdf_path)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Target directory (reuse existing)
    target_dir = os.path.join(base_dir, pdf_name)
    images_dir = os.path.join(target_dir, "img")
    
    os.makedirs(images_dir, exist_ok=True)
    
    output_md_path = os.path.join(target_dir, f"transcription_{start_page}_{end_page}.md")
    
    print(f"Processing PDF: {pdf_path}")
    print(f"Range: {start_page} to {end_page}")
    print(f"Output: {output_md_path}")
    
    # 2. Open PDF
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF: {e}")
        return

    markdown_content = f"# Transcription Pages {start_page}-{end_page}\n\n"
    
    # 3. Iterate through pages
    for i in range(start_page - 1, end_page):
        if i >= len(doc):
            print(f"Page {i+1} out of range (Total: {len(doc)})")
            break
            
        page = doc[i]
        page_num = i + 1
        print(f"Processing Page {page_num}...", end='\r')
        
        # Render page to image (High DPI for OCR)
        mat = fitz.Matrix(2.5, 2.5) 
        pix = page.get_pixmap(matrix=mat)
        
        # Convert to PIL Image
        img_data = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_data))
        
        # Save image
        image_filename = f"page_{page_num:03d}.png"
        image_path = os.path.join(images_dir, image_filename)
        pix.save(image_path)
        
        # Run OCR
        try:
            text = pytesseract.image_to_string(image, lang='kor+eng')
        except Exception as e:
            print(f"OCR Error on page {page_num}: {e}")
            text = "[OCR Failed]"
        
        # Basic cleanup
        lines = text.split('\n')
        cleaned_lines = [line.rstrip() for line in lines if line.strip()]
        cleaned_text = '\n'.join(cleaned_lines)
        
        # Relative path for markdown
        relative_image_path = f"img/{image_filename}"
        
        # Append to markdown
        markdown_content += f"## Page {page_num}\n\n"
        markdown_content += f"{cleaned_text}\n\n"
        markdown_content += f"![Page {page_num}]({relative_image_path})\n\n"
        markdown_content += "---\n\n"

    print("\nSaving Markdown...")
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Done! Saved to {output_md_path}")

if __name__ == "__main__":
    pdf_file = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26/빅데이터분석기사26_필기1/빅데이터분석기사26_필기1.pdf"
    start_page = 51
    end_page = 62
    
    if os.path.exists(pdf_file):
        transcribe_range(pdf_file, start_page, end_page)
    else:
        print(f"Error: PDF file not found at {pdf_file}")
