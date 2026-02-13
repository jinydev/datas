
import re

input_file = "파이썬으로_배우는_데이터분석입문6.md"
output_file = "파이썬으로_배우는_데이터분석입문6.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix "values" and "name" context
    content = content.replace("8360168", "Series") # duplicated check
    content = content.replace("8682168", "Series") # another variant
    content = content.replace("8861", "Series")
    content = content.replace("2087", "missing") # context: "0.2087이나 None" -> "missing values"
    content = content.replace("069079", "missing")
    
    # 2. Fix "index" context
    content = content.replace("1406※", "index")
    content = content.replace("1ㅁ06※", "index")
    content = content.replace("1006※", "index")
    content = content.replace("1106※", "index")
    content = content.replace("10161", "label") # context: "열 레이블08161"
    content = content.replace("08161", "label")
    
    # 3. Fix "NaN" and "None"
    content = content.replace("020 021", "NaN") # specific OCR artifact?
    content = content.replace("NoneS", "None은")
    content = content.replace("AS", "값을") # context dependent, risky but frequent "AS" -> "것을" or "값을"
    
    # "위에서 수정된 내용은 원본 8에도 반영이 된 AS 확인할 수 있다." -> "반영이 된 것을"
    content = content.replace("반영이 된 AS", "반영이 된 것을")
    content = content.replace("조건 AAS", "조건 값을")

    # 4. Fix specific broken strings
    content = content.replace("AuPWNHeR DON YN", "")
    content = content.replace("NRPWRNEP!", "")
    content = content.replace("dandyrilla.github.io", "") # footer garbage
    
    # 5. Fix "columns" 
    content = content.replace("coli", "col1")
    content = content.replace("coll", "col1")
    
    # 6. Fix "int64" variants
    content = content.replace("10164", "int64")
    content = content.replace("1064", "int64")
    content = content.replace("into4", "int64")
    
    # 7. Fix "Section" headers specifically
    content = re.sub(r"^Section \d+.*", "### ", content, flags=re.MULTILINE)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 2 fixes.")

if __name__ == "__main__":
    main()
