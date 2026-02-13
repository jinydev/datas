
import re

input_file = "파이썬으로_배우는_데이터분석입문3.md"
output_file = "파이썬으로_배우는_데이터분석입문3.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- Section: Heuristic Regex Cleaning ---

    # 1. Remove isolated "]" or "[" or "》" appearing at start of lines or words
    # e.g. " ] 다음은" -> "다음은"
    content = re.sub(r"^\s*[\]\[》]\s+", "", content, flags=re.MULTILINE)
    content = re.sub(r"\s+[\]\[》]\s+", " ", content)

    # 2. Fix "08." or "20." patterns that seem like noise before words
    # e.g. "08.002" -> handled, but "08." might appear elsewhere
    # "20.ㅁ6" -> handled
    
    # 3. Fix "H를", "BA를", "Wola", "BA열을" -> "리스트를", "배열을", "오류가", "배열을"
    # Specific OCR misinterpretations of Korean words
    content = content.replace("BA를", "오류가") # Context: "BA를 Wola" -> "오류가 발생한다"
    content = content.replace("Wola", "발생한다")
    content = content.replace("BA열을", "배열을")
    content = content.replace("H를", "리스트를") # Context: "리스트나 H를"
    content = content.replace("HA를", "배열을") # Context: "ndarray HA를"

    # 4. Fix "Z는O)M" -> "파이썬" (Context: lang array example)
    # The user image showed: ['파이썬', '자바', '씨']
    # The OCR had: ['Z는O)M', '자바', '씨']
    content = content.replace("Z는O)M", "파이썬")
    content = content.replace("D는OM", "파이썬")
    content = content.replace("는O)M", "파이썬")

    # 5. Fix "Section ..." headers
    # "Section 02 + LHAtSI를 ... 87" -> Remove
    content = re.sub(r"Section \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"PYTHON PROGRAMMING.*", "", content) # Remove header branding
    
    # 6. Fix "int는이면" -> "int이면" (Already in step 9, but ensure)
    content = content.replace("int는이면", "int이면")

    # 7. Fix "Qo", "Qt", "Ex", "xL", "HE는"
    # Context: "첨자 [1, Qt [3, Qo" -> "[1, 0]과 [3, 0]"?
    # Context: "indexing arrays ... shapes (3,) (2,)" output check
    # Let's fix specific weird variable references
    content = content.replace("Qt", "0]과") # Guessing context: [1, 0]
    content = content.replace("Qo", "0]에")
    
    # "Ex[1, 3])" -> "(=x[1, 3])"
    content = content.replace("Ex", "(=x")
    content = content.replace("xL", "(=x")

    # 8. Fix "apray", "arnay", "arrav" -> "array"
    content = content.replace("apray", "array")
    content = content.replace("arnay", "array")
    content = content.replace("arrav", "array")
    
    # 9. Fix "Index는rror" -> "IndexError"
    content = content.replace("Index는rror", "IndexError")
    
    # 10. Fix "[2와" -> "[2]와" ?
    # Context: "리스트 [2와 [2, 3]은" -> "리스트 [2]와 [2, 3]은"
    content = content.replace(" [2와", " [2]와")
    content = content.replace(" [2, 2 ", " [2, 2] ")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 10 final sweep.")

if __name__ == "__main__":
    main()
