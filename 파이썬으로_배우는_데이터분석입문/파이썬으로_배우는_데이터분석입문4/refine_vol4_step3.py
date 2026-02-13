
import re

input_file = "파이썬으로_배우는_데이터분석입문4.md"
output_file = "파이썬으로_배우는_데이터분석입문4.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix broken key terms and function names
    content = content.replace("parray", "array")
    content = content.replace("anray", "array")
    content = content.replace("arrpav", "array")
    content = content.replace("arrayvil", "array")
    
    # 2. Fix spacing in numpy functions
    content = content.replace("np. split", "np.split")
    content = content.replace("np. hsplit", "np.hsplit")
    content = content.replace("np. vsplit", "np.vsplit")
    content = content.replace("np. hstack", "np.hstack")
    content = content.replace("np. column_stack", "np.column_stack")
    content = content.replace("np. stack", "np.stack")
    content = content.replace("np,column_", "np.column_")

    # 3. Fix specific context garbage words
    # "함수 SS" -> "함수"
    content = content.replace("함수 SS", "함수")
    content = content.replace("AHS", "사용하는")
    content = content.replace("HRS", "함수")
    content = content.replace("BES", "모양은") # Context: "전체 BES (3, 2, 8)이 된다." -> "전체 모양은"
    content = content.replace("YHEct", "반환한다") # Context: "...하나의 배열로 YHEct" -> "반환한다"
    content = content.replace("86800", "stack()") # Context: "concatenate() 함수와 달리 86800 함수는" -> "stack() 함수는"
    content = content.replace("np.stack(에", "np.stack()에")
    
    # 4. Fix axis/shape context
    # "S 00] 30] 되어" -> "축 0이 3이 되어" (Context: "축 0으로 합쳐지므로...")
    content = content.replace("S 00] 30]", "축 0이 3이")
    content = content.replace("축 10] 3", "축 1이 3")

    # 5. Fix variable names
    content = content.replace("ax®", "ax0") # Context: ax0 = np.stack...

    # 6. Fix "BY]" -> "모양이" or "배열" ?
    # Context: "다음 배열 a, 6, c= BY] (2, )인..." -> "c는 모양이"
    content = content.replace("BY]", "모양이")
    content = content.replace("c=", "c는") # "c= BY]" -> "c는 모양이"
    
    # 7. Fix "False7}" -> "False가"
    content = content.replace("False7}", "False가")
    content = content.replace("True7}", "True가")
    
    # 8. Fix "np.r_[3:10:3, [@]*2, 5, 6]" -> "[0]*2"
    content = content.replace("[@]*2", "[0]*2")
    
    # 9. Fix garbled 1111) -> ]])
    content = content.replace("1111)", "]])")
    content = content.replace("2111)", "2]]])") # Context dependent, safe-ish guess

    # 10. Fix "A+" -> "함수" or similar?
    # Context: "A+ np.row_stack(" -> "함수 np.row_stack("
    content = content.replace("A+ np.row_stack", "함수 np.row_stack")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 3 fixes.")

if __name__ == "__main__":
    main()
