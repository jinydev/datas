
import re

input_file = "파이썬으로_배우는_데이터분석입문4.md"
output_file = "파이썬으로_배우는_데이터분석입문4.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix "@" in numbers and arrays
    # "@" -> "0" usually in this OCR context
    content = content.replace("array([@,", "array([0,")
    content = content.replace("array([[@,", "array([[0,")
    content = content.replace(" @.", " 0.")
    content = content.replace("-@.", "-0.")
    content = content.replace("(@.", "(0.")
    content = content.replace("=@.", "=0.")
    
    # 2. Fix specific garbage lines observed
    content = content.replace("np.   6 ,   ©)?", "")
    content = re.sub(r"np\.   \d+ ,   ©\)\?", "", content)

    # 3. Fix "68" used as Bullet/Header? 
    # "68 numpy.vstack()" -> "### numpy.vstack()" or just "numpy.vstack()"
    # Context: "배열 결합 개요와 )|본 함수 68 배열 결합 개요"
    # It seems "68" might be "01" (Chapter 01) or similar.
    # Let's clean it up to Markdown headers where appropriate.
    content = re.sub(r"^68\s+(numpy\.[a-z_]+)", r"### \1", content, flags=re.MULTILINE)
    
    # "68 numpy.hstack()" -> "### numpy.hstack()"
    
    # 4. Fix "apray", "arnay", "arpay" -> "array"
    content = content.replace("apray", "array")
    content = content.replace("arnay", "array")
    content = content.replace("arpay", "array")

    # 5. Fix "HHS", "HAS", "WHS" -> "배열", "배열을" etc?
    # Context: "위 두 HSS 수직... 쌓아... 합쳐서" -> "위 두 배열을"
    # "HHS" -> "배열을" or "배열"
    # "HAS" -> "배열을"
    # "WHS" -> "배열"
    content = content.replace("HHS", "배열")
    content = content.replace("HSS", "배열을")
    content = content.replace("HAS", "배열을")
    content = content.replace("WHS", "배열")
    content = content.replace("BZS", "배열을") # Guessing

    # 6. Fix "BY" -> "배열"
    # Context: "다음 배열 8는 모양이 (3, 2)인..." -> "8는" is likely "a는"
    content = content.replace("8는", "a는")
    content = content.replace("be ", "b는 ") # "다음 배열 be" -> "b는"
    content = content.replace("ce ", "c는 ")
    
    # 7. Fix "78180(", "186180(/" -> "함수는", "함수" words ending with 0( ?
    # "numpy.vstack()-S" -> "numpy.vstack()은"
    content = content.replace("-S ", "은 ")
    content = content.replace("-S\n", "은\n")
    content = content.replace("()S", "()은")
    content = content.replace("()Z}", "()와")
    content = content.replace("()2}", "()의")
    
    # 8. Fix "Section 01 ..." footers
    content = re.sub(r"Section \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"Chapter \d+.*?\d+\s*$", "", content, flags=re.MULTILINE)
    content = re.sub(r"PYTHON PROGRAMMING.*", "", content)

    # 9. Fix garbled text "ㅁ04140”.78180()" -> "numpy.vstack()"
    # "numpy.vstack(3}" -> "numpy.vstack()과"
    content = content.replace("numpy.vstack(3}", "numpy.vstack()과")
    
    # 10. Fix array output noise
    # "array({[@, 1]," -> "array([[0, 1],"
    content = content.replace("array({[", "array([[")
    
    # 11. Fix "®" -> "0" or bullet
    # "array([[ ® 1]," -> "array([[ 0, 1],"
    content = content.replace(" ®", " 0")
    
    # 12. Fix "× =" -> "x ="
    content = content.replace("× =", "x =")
    content = content.replace("× ", "x ") # Be careful, matrix mult?
    # Usually in code blocks it's x.
    
    # 13. Fix "1[3.8. 721)" -> "[3., 8., 7.]]"
    # "721)" -> "7.]]"
    content = content.replace("721)", "7.]]")
    
    # 14. Fix "Generator(PCG64) at @x..." -> Code comment or remove
    # It's output. formatted as code or left alone.
    
    # 15. Fix "Index는rror" -> "IndexError"
    content = content.replace("Index는rror", "IndexError")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 1 fixes.")

if __name__ == "__main__":
    main()
