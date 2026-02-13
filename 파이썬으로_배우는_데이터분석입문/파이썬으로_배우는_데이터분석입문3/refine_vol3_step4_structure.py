
import re

input_file = "파이썬으로_배우는_데이터분석입문3.md"
output_file = "파이썬으로_배우는_데이터분석입문3.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix user reported typo
    content = content.replace("리스 Eu", "리스트나")
    
    # 2. Fix specific merged headers identified via grep
    
    # Line 124 approx
    content = content.replace(
        "### 내장함수 array()= ndarray 생성 장함수 array는",
        "### 내장함수 array()로 ndarray 생성\n\n내장함수 array는"
    )
    
    # Fix arange typo in header and split
    content = content.replace(
        "### 내장함수 2096()와 linspace() 비교 내장함수",
        "### 내장함수 arange()와 linspace() 비교\n\n내장함수"
    )
    
    # ones_like split
    content = content.replace(
        "### 원소값이 1인 주어진 형태의 배열을 생성하는 ones_like() 내장함수",
        "### 원소값이 1인 주어진 형태의 배열을 생성하는 ones_like()\n\n내장함수"
    )
    
    # full_like split
    content = content.replace(
        "### 원소값이 주어진 값이며 주어진 형태의 배열을 생성하는 full_like() 내장함수",
        "### 원소값이 주어진 값이며 주어진 형태의 배열을 생성하는 full_like()\n\n내장함수"
    )
    
    # 3D array slicing split + typo fix (8 -> a)
    content = content.replace(
        "### 3차원 배열의 첨자와 슬라이싱 다음 8는",
        "### 3차원 배열의 첨자와 슬라이싱\n\n다음 a는"
    )
    
    # Broadcasting overview
    content = content.replace(
        "### 브로드캐스팅 개요 브로드캐스팅(broadcasting)이라는",
        "### 브로드캐스팅 개요\n\n브로드캐스팅(broadcasting)이라는"
    )
    
    # Scalar operation
    content = content.replace(
        "### 스칼라 또는 단일 값과 배열의 연산 단일 값",
        "### 스칼라 또는 단일 값과 배열의 연산\n\n단일 값"
    )
    
    # Garbage header cleanup (Line 308 approx)
    # ### .02040816326530612) -> just remove ###
    content = re.sub(r"^### (\.?020408)", r"\1", content, flags=re.MULTILINE)
    
    # Fix ndarray view header
    # "### ndarray2 27/2 같은 구조만 수정 가능 다음" -> "### ndarray의 뷰(view)와 같은 구조만 수정 가능\n\n다음"
    # This is a bit risky guess, but "27/2" -> "뷰" or "구조" is likely. 
    # Let's try to match exactly what's there.
    # Found in grep: "### ndarray2 27/2 같은 구조만 수정 가능 다음 파이썬의"
    content = content.replace(
        "### ndarray2 27/2 같은 구조만 수정 가능 다음",
        "### ndarray의 뷰(view)와 같은 구조만 수정 가능\n\n다음"
    )
    
    # Additional generic fix provided in user feedback pattern "Header = Body" if any remain?
    # Maybe "내장함수 array()= ndarray 생성" left over if replace failed?
    # The first replacement handles it.
    
    # 3. Last polish
    content = content.replace("장함수", "내장함수") # fix specific typo left behind if any
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} with structural fixes.")

if __name__ == "__main__":
    main()
