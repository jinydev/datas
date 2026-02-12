import os
from convert_bigdata_pdf_ocr import convert_pdf_to_markdown_ocr
from cleanup_ocr_markdown import cleanup_ocr_markdown

def match_convert_and_cleanup_pilgi():
    base_dir = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26"
    
    # List of files to process (Pilgi 1 to 10)
    files_to_process = [
        f"빅데이터분석기사26_필기{i}.pdf" for i in range(1, 11)
    ]
    
    for filename in files_to_process:
        pdf_path = os.path.join(base_dir, filename)
        
        if not os.path.exists(pdf_path):
            print(f"Skipping {filename} (not found)")
            continue
            
        print(f"\n[{filename}] Starting Conversion...")
        
        # 1. OCR Conversion
        # This function creates {filename_no_ext}/{filename_no_ext}_ocr.md
        try:
            convert_pdf_to_markdown_ocr(pdf_path)
        except Exception as e:
            print(f"Error converting {filename}: {e}")
            continue

        # Derived paths
        name_no_ext = os.path.splitext(filename)[0]
        target_dir = os.path.join(base_dir, name_no_ext)
        md_path = os.path.join(target_dir, f"{name_no_ext}_ocr.md")
        
        # 2. Cleanup
        if os.path.exists(md_path):
            print(f"[{filename}] Cleaning up Markdown...")
            cleanup_ocr_markdown(md_path, md_path)
            print(f"[{filename}] Done.")
        else:
            print(f"[{filename}] Warning: Output Markdown not found at {md_path}")

if __name__ == "__main__":
    match_convert_and_cleanup_pilgi()
