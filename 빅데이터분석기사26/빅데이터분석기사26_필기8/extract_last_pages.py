
import os
from pypdf import PdfReader, PdfWriter

def extract_pages(pdf_path, start_page, end_page, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")
    
    # Adjust for 0-based index
    start_idx = start_page - 1
    end_idx = min(end_page, total_pages)
    
    for i in range(start_idx, end_idx):
        page = reader.pages[i]
        # Extract images from page
        count = 0
        for image_file_object in page.images:
            with open(os.path.join(output_dir, f"page_{i+1:03d}_{count}.png"), "wb") as fp:
                fp.write(image_file_object.data)
                count += 1
        print(f"Extracted images from page {i+1}")

pdf_path = "빅데이터분석기사26_필기8.pdf"
output_dir = "temp_images_86_90"
extract_pages(pdf_path, 86, 90, output_dir)
