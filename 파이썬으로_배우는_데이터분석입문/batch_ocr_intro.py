
import os
import subprocess
import sys

def run_batch():
    base_dir = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/파이썬으로_배우는_데이터분석입문"
    converter_script = os.path.join(base_dir, "convert_intro_series.py")
    cleanup_script = "/Users/hojin8/docs/070.강의/c01.빅데이터분석/빅데이터분석기사26/cleanup_silgi_2.py"

    for i in range(1, 10):
        print(f"=== Processing Volume {i} ===")
        
        # 1. Run OCR Conversion
        cmd_convert = [sys.executable, converter_script, str(i)]
        print(f"Running: {' '.join(cmd_convert)}")
        ret = subprocess.call(cmd_convert)
        if ret != 0:
            print(f"Error converting Vol {i}")
            continue

        # 2. Identify Output File
        vol_dir = os.path.join(base_dir, f"파이썬으로_배우는_데이터분석입문{i}")
        # The MD file should be named same as the folder mostly, or derived from PDF basename.
        # Let's find the .md file that matches the volume name pattern
        # Usually "파이썬으로_배우는_데이터분석입문{i}.md" or similar.
        # But wait, PDF basename might differ slightly (Hangul NFD/NFC).
        # We can glob for *.md
        import glob
        md_files = glob.glob(os.path.join(vol_dir, "*.md"))
        # Filter out _ocr.md if any left, but convert_intro_series makes the main one.
        if not md_files:
            print(f"No MD file found in {vol_dir}")
            continue
            
        target_md = md_files[0] # Assume the one we just made
        
        # 3. Run Cleanup
        cmd_clean = [sys.executable, cleanup_script, target_md]
        print(f"Running Cleanup: {' '.join(cmd_clean)}")
        ret = subprocess.call(cmd_clean)
        if ret != 0:
            print(f"Error cleaning Vol {i}")
            
    print("Batch Processing Complete.")

if __name__ == "__main__":
    run_batch()
