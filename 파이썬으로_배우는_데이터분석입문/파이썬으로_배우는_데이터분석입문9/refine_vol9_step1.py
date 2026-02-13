
import re

input_file = "파이썬으로_배우는_데이터분석입문9.md"
output_file = "파이썬으로_배우는_데이터분석입문9.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix General OCR garbage found in previous volumes (defensive)
    content = content.replace("080ㅁ0889", "pandas")
    content = content.replace("08181'78106", "DataFrame")
    content = content.replace("DataFrame", "DataFrame") # Normalize if accents exist
    
    # 2. Fix specific terms for Vol 9 (Visualization)
    # Checking for common typos in pydataset names or seaborn args
    content = content.replace("ToothGrowth", "ToothGrowth") # seems correct in text, just ensuring
    content = content.replace("AirPassengers", "AirPassengers")
    
    # 3. Fix Code Syntax Artifacts
    # Sometimes quotes get messed up
    content = content.replace("levels=4,", "levels=4,") 
    content = content.replace("color=\".2\"", "color='.2'")
    
    # 4. Fix "Section" / "Chapter" footers/headers
    content = re.sub(r"Section \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"Chapter \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"PYTHON PROGRAMMING.*", "", content)
    
    # 5. Fix Table formatting (dashed lines)
    content = re.sub(r"^[-—]+$", "", content, flags=re.MULTILINE)

    # 6. Fix specific spacing issues seen in inspection
    content = content.replace("Index(['mpg', ‘cyl', ‘disp', ‘hp'],", "Index(['mpg', 'cyl', 'disp', 'hp'],")
    content = content.replace("['mpg', ‘cyl', ‘disp’, ‘hp']", "['mpg', 'cyl', 'disp', 'hp']")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 1 fixes.")

if __name__ == "__main__":
    main()
