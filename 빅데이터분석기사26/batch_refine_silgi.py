
import os
import subprocess
import glob

def batch_refine():
    base_dir = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26"
    
    # Pattern: 빅데이터분석기사26_실기X (directory) / 빅데이터분석기사26_실기X.pdf (file)
    for i in range(1, 9): # 1 to 8
        dir_name = f"빅데이터분석기사26_실기{i}"
        dir_path = os.path.join(base_dir, dir_name)
        
        pdf_name = f"빅데이터분석기사26_실기{i}.pdf"
        pdf_path = os.path.join(dir_path, pdf_name)
        
        md_name = f"빅데이터분석기사26_실기{i}.md"
        md_path = os.path.join(dir_path, md_name)
        
        if os.path.exists(pdf_path):
            print(f"[{i}/8] Processing {pdf_name}...")
            # Run refinement script
            cmd = [
                "python3", 
                "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26/refine_silgi_advanced.py",
                pdf_path,
                md_path
            ]
            subprocess.run(cmd, check=True)
            
            # Remove _ocr.md if it exists
            ocr_path = os.path.join(dir_path, f"빅데이터분석기사26_실기{i}_ocr.md")
            if os.path.exists(ocr_path):
                print(f"Removing {ocr_path}")
                os.remove(ocr_path)
        else:
            print(f"Skipping {i}: PDF not found at {pdf_path}")

if __name__ == "__main__":
    batch_refine()
