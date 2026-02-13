
import re

input_file = "파이썬으로_배우는_데이터분석입문6.md"
output_file = "파이썬으로_배우는_데이터분석입문6.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix "비름" -> "이름"
    content = content.replace("열 비름을", "열 이름을")
    
    # 2. Fix "BES" context
    # Context: "index= 1부터 시작하는 BES ES 번호이다." -> "index는 1부터 시작하는 일련 번호이다." (Guessing "일련" or similar)
    # Actually "BES" appeared in Vol 5 as "모양은". Here it might be different.
    # "BES ES 번호" -> "블록의 번호" or "배열의 번호"
    # Let's try "일련 번호" for safety or just "번호".
    content = content.replace("BES ES 번호", "일련 번호")
    
    # 3. Fix "pf.loc[pf.index[0]]" output check
    # ensure "int64" is correct (already done in step 2 but harmless to double check if any persisted)
    
    # 4. Fix "pf.loc[:, pf.columns[0]]" text
    # "pf.columns[0]은 첫 번째 열 비름을 반환한다" -> Fixed above.

    # 5. Fix "Section" / "Chapter" artifacts again just in case
    content = re.sub(r"Section \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 3 fixes.")

if __name__ == "__main__":
    main()
