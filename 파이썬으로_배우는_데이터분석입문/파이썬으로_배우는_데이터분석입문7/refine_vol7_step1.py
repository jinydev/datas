
import re

input_file = "파이썬으로_배우는_데이터분석입문7.md"
output_file = "파이썬으로_배우는_데이터분석입문7.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Pandas Terms
    content = content.replace("080ㅁ0889", "pandas")
    content = content.replace("8360168", "Series")
    content = content.replace("aj2|Z", "Series")
    content = content.replace("08181'78106", "DataFrame")
    content = content.replace("0818178008", "DataFrame")
    content = content.replace("08라1806", "DataFrame")
    content = content.replace("1006×", "index")
    content = content.replace("1ㅁ06※", "index")
    content = content.replace("1106※", "index")
    content = content.replace("1106x", "index")
    content = content.replace("08161", "label")
    content = content.replace("1406※", "index")
    content = content.replace("12106※", "index")
    content = content.replace("12106", "index")
    
    # 2. Fix Data Types
    content = content.replace("11064", "int64")
    content = content.replace("10164", "int64")
    content = content.replace("10264", "int64")
    content = content.replace("floate4", "float64")
    content = content.replace("intG4e]ch", "int64")
    
    # 3. Fix Code Artifacts
    content = content.replace("s[@]", "s[0]")
    content = content.replace("s[@:]", "s[0:]")
    content = content.replace("s[@:", "s[0:")
    content = content.replace("[@, :]", "[0, :]")
    content = content.replace("df.sum(axis=@)", "df.sum(axis=0)")
    content = content.replace("df.mean(axis=@)", "df.mean(axis=0)")
    content = content.replace("df.max(axis=@)", "df.max(axis=0)")
    content = content.replace("df.min(axis=@)", "df.min(axis=0)")
    content = content.replace("axis=@", "axis=0") # General case
    
    # 4. Fix General Text Garbage
    content = content.replace("Rangelndex", "RangeIndex")
    content = content.replace("Rangelndex#}", "RangeIndex는")
    content = content.replace("A]BA", "Sequence")
    
    # 5. Fix "Section" / "Chapter" footers/headers
    content = re.sub(r"Section \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"Chapter \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"PYTHON PROGRAMMING.*", "", content)

    # 6. Fix "NaN" representations if any new ones appear
    # Checking for specific ones found in Vol 6 just in case
    content = content.replace("020 021", "NaN") 

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 1 fixes.")

if __name__ == "__main__":
    main()
