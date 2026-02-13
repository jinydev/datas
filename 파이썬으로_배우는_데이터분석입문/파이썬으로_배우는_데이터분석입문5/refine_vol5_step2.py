
import re

input_file = "파이썬으로_배우는_데이터분석입문5.md"
output_file = "파이썬으로_배우는_데이터분석입문5.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix "p1t", "pit" -> "plt"
    content = re.sub(r"p[1l]t\.", "plt.", content)
    content = content.replace("pit.", "plt.")

    # 2. Fix "subplots" garbage
    # "0ㅁ1[.341621018(02, 7)" -> "plt.subplots(2, 2)" context?
    # Context: "다음은 ... 으로 ... 서브플롯을 그린 그림이다."
    content = re.sub(r"0ㅁ1\[\.341621018\(.*?\)", "plt.subplots()", content)
    content = content.replace("pit subplots", "plt.subplots")

    # 3. Fix "HHS", "HHBSS", "HSS" -> "서브플롯을" or "배열을" depending on context
    # In Vol 5, it seems to refer to "Figures" or "Subplots" often?
    # "다음은 2행 3열의 HHSSS" -> "서브플롯을" or "행렬을"
    content = content.replace("HHSSS", "서브플롯을")
    content = content.replace("HHBSS", "서브플롯을")
    
    # 4. Fix "68" -> "###" or bullet
    # "68 그래프의 여러 속성" -> "### 그래프의 여러 속성"
    content = re.sub(r"68\s+(.*?)", r"### \1", content)
    
    # 5. Fix "So]", "Yo]", "Bo]" -> "는" or "이"
    # "y So] 소수를" -> "y는 소수를"
    content = content.replace("So]", "는")
    content = content.replace("Yo]", "는")
    content = content.replace("Bo]", "는")
    
    # 6. Fix "ASA" -> "계층적" ?
    # "figure2} axes 구성 요소는 ASA 구조이다." -> "계층적 구조이다."
    content = content.replace("ASA", "계층적")
    
    # 7. Fix "QAO]" -> "객체이다"
    # "중요한 역할을 하는 QAO] 다." -> "객체이다."
    content = content.replace("QAO] 다.", "객체이다.")
    content = content.replace("QAO]", "객체")

    # 8. Fix "00160" -> "Object" or "객체"
    # "Axes 객체(00160):" -> "Axes 객체(Axes):"
    content = content.replace("00160", "Axes")
    
    # 9. Clean up image text garbage (simple removal of obvious OCR failures)
    # "9” 304 a 「 4 때 ..."
    content = re.sub(r"^9” 304.*", "", content, flags=re.MULTILINE)
    content = re.sub(r"^407 «.*", "", content, flags=re.MULTILINE)
    
    # 10. Fix "12061=" -> "label="
    # "12061='소수...'"
    content = content.replace("12061=", "label=")

    # 11. Fix "008" -> "png" or "jpg" ?
    # "주사위.008" -> "주사위.png"
    content = content.replace(".008", ".png")
    content = content.replace(".0ㅁ08", ".png")
    
    # 12. Fix "EERE HOC}, SE" -> "방법을 알아보자. 우선"
    content = content.replace("EERE HOC}, SE", "방법을 알아보자. 우선")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 2 fixes.")

if __name__ == "__main__":
    main()
