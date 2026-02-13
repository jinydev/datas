
import re

input_file = "파이썬으로_배우는_데이터분석입문3.md"
output_file = "파이썬으로_배우는_데이터분석입문3.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix user specific report: "ㅁ41ㅁ7》에서 배열을] 빠른 계산 처리를 위한 방법이다."
    # Context: "numpy의 자료형 ... 이러한 자료형 중 하나만을 가질 수 있다. [이것은] 배열을 빠른 계산 처리를 위한 방법이다."
    # "ㅁ41ㅁ7》" likely maps to "이는" or "이것은" or "단일" based on context.
    # From context: "ndarray는 모든 요소가 단일한 자료형... 그러므로 ... 이것은 배열의 빠른 계산 처리를 위한 방법이다."
    content = content.replace("ㅁ41ㅁ7》에서 배열을] 빠른", "이것은 배열의 빠른")

    # 2. Fix "내장함수 8096()" -> "내장함수 arange()"
    content = content.replace("내장함수 8096()", "내장함수 arange()")
    
    # 3. Fix "ndarray7》" -> "ndarray"
    content = content.replace("ndarray7》", "ndarray")
    
    # 4. Fix "70ㅁ6" -> "706" or "view" ? 
    # Context: "일반 대입은 단지 Ge 복사로서 ... 16 연산 결과가 '70ㅁ6이다."
    # "Ge" -> "얕은(shallow)"? "view"?
    # "16 연산 결과" -> "id" ?
    # Let's clean up broadly.
    content = content.replace("70ㅁ6", "동일하") # Guessing "동일하다" based on "copy vs view" context
    content = content.replace("Ge 복사", "참조(Reference) 복사") 
    
    # 5. Fix "08.002》(로 orgs는" -> "slice()로 org는" or "slicing으로"
    # Context: "다음 코드처럼 ... 새로운 배열 v가 생성된다." imply slicingcopy.
    # "08.002》(로" -> "슬라이싱(slicing)으로" seems appropriate for creating new array (if it's a copy)
    # But wait, slicing usually returns a view in numpy. But "다른 복사된 새로운 배열 v가 생성된다" implies fancy indexing or explicit copy.
    # "org[...]"
    # Let's put "인덱싱(indexing)으로" or "슬라이싱으로". OCR "08.002" looks like "array" or "slice".
    # Let's map "08.002》(로" to "슬라이싱으로"
    content = content.replace("08.002》(로", "슬라이싱으로")
    
    # 6. Fix "다 코트 함수 Z를 x.reshape(2, 3)로"
    # "다 코트" -> "다음 코드" 
    # "함수 Z를" -> "함수" or "변수 x를"
    content = content.replace("다 코트 함수 Z를", "다음 코드는")
    
    # 7. Fix "Zt 사이의 간격은 6160으로 지정" -> "값 사이의 간격은 step으로 지정"
    content = content.replace("Zt 사이의 간격은 6160으로", "값 사이의 간격은 step으로")

    # 8. Fix "수 목록에 콤마가 없다."
    # This is correct observation for numpy default print.
    
    # 9. Fix "20.ㅁ6\8338(새로운 축)" -> "np.newaxis"
    # "20.ㅁ6\8338" -> "np.newaxis"
    content = content.replace("20.ㅁ6\8338", "np.newaxis")
    
    # 10. Fix "3318 1" -> "축 1" or "axis 1"
    content = content.replace("3318 1", "축 1")
    
    # 11. Fix "numpy 7ㅁ08178》에서" -> "numpy 배열에서" or "ndarray에서"
    content = content.replace("numpy 7ㅁ08178》에서", "numpy ndarray에서")
    
    # 12. Fix "정수 배열 또는 리스트 [2와 [2, 3]은" -> "[1, 2]와 ..."
    # "첨자 열을를" -> "첨자 열을"
    content = content.replace("첨자 열을를", "첨자 열을")

    # 13. Fix "함수 ㅁ0.1\880ㅁ820086(3, 8start)" -> "함수 reshape(3, start)" or similar?
    # Context: "3차원 행렬에서는 다음 6가 지 방식이 있을 수 있다."
    # "8start" -> "start"
    # Maybe "indexing" related?
    # Let's try to make it readable: "함수(매개변수)"
    # Replacing just the garbage part if possible.
    content = re.sub(r"함수 ㅁ0\.1\\880ㅁ820086", "함수", content)

    # 14. Fix "8start" -> "start"
    content = content.replace("8start", "start")
    
    # 15. Fix "3start" -> "start"
    content = content.replace("3start", "start")
    
    # 16. Fix "A\AA2)" -> "생성하여" or similar
    # "내장함수 np.arangel= 수 A\AA2) ndarray를 반환한다."
    # -> "내장함수 np.arange()는 수열을 생성하여 ndarray를 반환한다."
    content = content.replace("np.arangel=", "np.arange()는")
    content = content.replace("수 A\\AA2)", "수열을 생성하여")
    
    # 17. Fix "ㅁ40.8782ㅁ86(는" -> "이 함수는"
    content = re.sub(r"ㅁ40\.8782ㅁ86\(는", "이 함수는", content)

    # 18. Fix "(3096(/와 거의 동일하지만 ra                ro 아닌" 
    # -> "range()와 거의 동일하지만 range 객체가 아닌"
    content = content.replace("(3096(/와", "range()와")
    content = re.sub(r"ra\s+ro", "range 객체가", content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with Step 8 artifact cleanup.")

if __name__ == "__main__":
    main()
