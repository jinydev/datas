
import re

input_file = "파이썬으로_배우는_데이터분석입문3.md"
output_file = "파이썬으로_배우는_데이터분석입문3.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix "내내장함수" -> "내장함수" (Regression from step 4)
    content = content.replace("내내장함수", "내장함수")
    
    # 2. Fix "2]" -> "의" Regression
    # Many array closings like [1, 2] became [1, 의]
    # We will try to revert commonly affected patterns.
    # Pattern: Digit + ", " + "의" -> Digit + ", " + "2"
    content = re.sub(r"(\d+), 의", r"\1, 2", content)
    content = re.sub(r"(\d+),의", r"\1, 2", content)
    content = re.sub(r"\[의", r"[2", content)
    
    # Fix Table header [표 3-의]
    content = content.replace("[표 3-의", "[표 3-2")
    
    # Fix specific number corruption
    # "223696의" -> "2236962"
    content = content.replace("223696의", "2236962")
    
    # 3. Fix "7}" -> "가" / "elements)7는"
    # "elements)7는" -> "요소가" or "elements)가"
    content = content.replace("elements)7는", "요소가")
    content = content.replace("elements)7}", "요소가")
    content = content.replace("array7}", "array가")
    content = content.replace("ndarray7}", "ndarray가")
    content = content.replace("data7}", "data가")
    
    # 4. Fix "step는" -> "step은" (If any)
    content = content.replace("step는", "step은")
    
    # 5. Fix "array]" -> "array()"
    content = content.replace("함수 array] 인자", "함수 array() 인자")
    
    # 6. Fix "Little-endian를" -> "Little-endian을" (Josa fix)
    content = content.replace("Little-endian를", "Little-endian을")
    
    # 7. "unicode_array" line cleanup if needed
    
    # 8. "float7는" -> "float가" or "float는"
    # If "float7}" was original, and I mapped "7}" to something?
    # Context: "dtype=float7는 된다" -> "dtype=float가 된다"
    content = content.replace("float7는", "float가")
    content = content.replace("1081는", "int는") # "1081" -> "int" (scan error for int?)
    content = content.replace("1081", "int")

    # 9. "bE" -> "b는", "xE" -> "x는" (Step 2 did this, verify)
    
    # 10. "2081778" -> "ndarray" (Step 2 check)
    
    # 11. "24489796," -> lines looking like split numbers in linspace output
    # Consolidate linspace output if it's too broken?
    # For now, leave it if it's just OCR noise in output block.
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with polish fixes.")

if __name__ == "__main__":
    main()
