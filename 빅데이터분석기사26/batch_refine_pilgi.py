
import os
import subprocess
import glob
import re

def batch_refine_pilgi():
    base_dir = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26"
    
    # Explicit loop for 1 to 10
    for i in range(1, 11): 
        dir_name = f"빅데이터분석기사26_필기{i}"
        dir_path = os.path.join(base_dir, dir_name)
        
        # Check if dir exists
        if not os.path.exists(dir_path):
            print(f"Skipping {dir_name}, not found.")
            continue
            
        # Find PDF in this dir
        pdf_files = glob.glob(os.path.join(dir_path, "*.pdf"))
        if not pdf_files:
            print(f"No PDF found in {dir_name}")
            continue
            
        pdf_path = pdf_files[0] # Take first PDF
        output_md = os.path.splitext(pdf_path)[0] + ".md"
        ocr_md = os.path.splitext(pdf_path)[0] + "_ocr.md"
        
        print(f"Processing {pdf_path}...")
        
        # Run advanced refinement script
        cmd = ["python3", "refine_pilgi_advanced.py", pdf_path, output_md]
        subprocess.run(cmd, check=True)
        
        # Clean up OCR file if exists
        if os.path.exists(ocr_md):
            print(f"Removing {ocr_md}")
            os.remove(ocr_md)

        # Apply secondary text cleanup (broken lines)
        cmd_cleanup = ["python3", "cleanup_silgi_2.py", output_md]
        subprocess.run(cmd_cleanup, check=True)
        
        print(f"Finished {dir_name}")

if __name__ == "__main__":
    batch_refine_pilgi()
