
import os
from pypdf import PdfReader

def extract_images_from_pdf(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Opening PDF: {pdf_path}")
    try:
        reader = PdfReader(pdf_path)
    except Exception as e:
        print(f"Error opening PDF: {e}")
        return

    extracted_count = 0
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")

    for i, page in enumerate(reader.pages):
        page_num = i + 1
        try:
            images = page.images
            if not images:
                # print(f"No images found on page {page_num}")
                continue
            
            for j, image in enumerate(images):
                name = image.name
                ext = os.path.splitext(name)[1]
                if not ext:
                    ext = ".png" # Default to png if unknown
                
                # Check for common image extensions and correct if needed
                if ext.lower() not in ['.jpg', '.jpeg', '.png', '.webp']:
                     ext = ".png"

                filename = f"page_{page_num:03d}{ext}"
                if len(images) > 1:
                     filename = f"page_{page_num:03d}_img_{j}{ext}"
                
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "wb") as fp:
                    fp.write(image.data)
                extracted_count += 1
                print(f"Extracted {filename}")
                
        except Exception as e:
            print(f"Error extracting from page {page_num}: {e}")

    print(f"Extraction complete. Total images extracted: {extracted_count}")

if __name__ == "__main__":
    base_path = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26"
    file_path = os.path.join(base_path, "빅데이터분석기사26_필기7/빅데이터분석기사26_필기7.pdf")
    output_path = os.path.join(base_path, "빅데이터분석기사26_필기7/img")
    
    extract_images_from_pdf(file_path, output_path)
