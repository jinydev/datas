
import re

input_file = "파이썬으로_배우는_데이터분석입문6.md"
output_file = "파이썬으로_배우는_데이터분석입문6.md"

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
    content = content.replace("gs[®, :]", "gs[0, :]")
    content = content.replace("gs[-1, @]", "gs[-1, 0]")
    content = content.replace("np.arange(1, 3, .5)", "np.arange(1, 3, 0.5)")
    
    # 4. Fix General Text Garbage
    content = content.replace("Rangelndex", "RangeIndex")
    content = content.replace("Rangelndex#}", "RangeIndex는")
    content = content.replace("A]BA", "Sequence")
    content = content.replace("Sequences2]", "Sequence의")
    content = content.replace("68 ", "### ")
    
    # 5. Fix "NaN" representations
    content = content.replace("NaN", "NaN") # Just to be sure, duplicate check
    content = content.replace("069079 value", "missing value")

    # 6. Fix "Section" / "Chapter" footers/headers
    content = re.sub(r"Section \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"Chapter \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"PYTHON PROGRAMMING.*", "", content)

    # 7. Fix Table Structure (Basic)
    # Remove lines that are just "| :--- | :--- |" if they are orphan or broken
    # But usually we want to keep them if they are part of a valid table.
    # Let's fix specific table headers if known.
    pass 

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 1 fixes.")

if __name__ == "__main__":
    main()
