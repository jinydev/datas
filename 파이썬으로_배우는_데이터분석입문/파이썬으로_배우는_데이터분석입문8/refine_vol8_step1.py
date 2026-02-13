
import re

input_file = "파이썬으로_배우는_데이터분석입문8.md"
output_file = "파이썬으로_배우는_데이터분석입문8.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix pydataset terms and artifacts
    content = content.replace("m pg", "mpg")
    content = content.replace("t itanic", "titanic")
    content = content.replace("PyDataset Documentation", "PyDataset Documentation") # seems ok, but just in case of weird spacing
    
    # 2. Fix Seaborn terms
    content = content.replace("s ns", "sns")
    content = content.replace("se aborn", "seaborn")
    
    # 3. Fix General OCR Artifacts
    content = content.replace("Ist class", "1st class")
    content = content.replace("I st class", "1st class")
    content = content.replace("2nd class", "2nd class") # check for Znd or similar if needed
    content = content.replace("3rd class", "3rd class") # check for 3 rd
    
    # 4. Fix Code Output Markers
    # Sometimes output is marked as python but should be text or vice versa.
    # The inspection showed ```text for output, which is good.
    
    # 5. Fix "Section" / "Chapter" footers/headers
    content = re.sub(r"Section \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"Chapter \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"PYTHON PROGRAMMING.*", "", content)
    
    # 6. Fix specific typos found or anticipated
    content = content.replace("080ㅁ0889", "pandas") # carried over from Vol 6/7 just in case
    content = content.replace("DataFrame", "DataFrame")
    
    # 7. Table formatting cleanup (simple replacements for common table issues)
    # Remove lines that are just dashes types if they are broken
    content = re.sub(r"^[-—]+$", "", content, flags=re.MULTILINE)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 1 fixes.")

if __name__ == "__main__":
    main()
