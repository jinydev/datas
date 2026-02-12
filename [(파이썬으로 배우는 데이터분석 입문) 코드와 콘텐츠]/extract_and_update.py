import os
import fitz  # pymupdf
import re

def extract_images_and_update_md(pdf_path, md_path):
    # 1. Setup paths
    base_dir = os.path.dirname(pdf_path)
    images_dir = os.path.join(base_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # 2. Open PDF
    doc = fitz.open(pdf_path)
    print(f"Opened PDF: {pdf_path} with {len(doc)} pages")
    
    # 3. Read Markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 4. Iterate through pages and update Markdown
    new_md_content = md_content
    
    for i, page in enumerate(doc):
        page_num = i + 1
        
        # Render page to image
        pix = page.get_pixmap()
        image_filename = f"{pdf_name}_slide_{page_num}.png"
        image_path = os.path.join(images_dir, image_filename)
        pix.save(image_path)
        print(f"Saved image: {image_path}")
        
        # Prepare image link
        # Use relative path for markdown
        relative_image_path = f"images/{image_filename}"
        image_markdown = f"\n![Slide {page_num}]({relative_image_path})\n"
        
        # Find the slide header in Markdown
        # Pattern: ## Slide X
        # We want to insert the image AFTER the slide header
        slide_header = f"## Slide {page_num}"
        
        if slide_header in new_md_content:
            # Replace "## Slide X" with "## Slide X\n![Slide X](path)"
            # But we need to be careful not to replace it multiple times or wrongly
             new_md_content = new_md_content.replace(slide_header, f"{slide_header}{image_markdown}", 1)
        else:
            print(f"Warning: Header '{slide_header}' not found in Markdown.")
            
    # 5. Save updated Markdown
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_md_content)
    print(f"Updated Markdown file: {md_path}")

if __name__ == "__main__":
    pdf_file = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/[(파이썬으로 배우는 데이터분석 입문) 코드와 콘텐츠]/ch04 다차원 배열 결합과 분리(p74).pdf"
    md_file = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/[(파이썬으로 배우는 데이터분석 입문) 코드와 콘텐츠]/ch04 다차원 배열 결합과 분리(p74).md"
    
    if os.path.exists(pdf_file) and os.path.exists(md_file):
        extract_images_and_update_md(pdf_file, md_file)
    else:
        print("Error: PDF or Markdown file not found.")
