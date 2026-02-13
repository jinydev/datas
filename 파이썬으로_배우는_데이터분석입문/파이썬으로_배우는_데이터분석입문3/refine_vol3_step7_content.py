
import re

input_file = "파이썬으로_배우는_데이터분석입문3.md"
output_file = "파이썬으로_배우는_데이터분석입문3.md"

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the target bad block using a unique enough substring or regex
    # The bad block starts around "unicode_array = np.array(['7fLtCt'..." and ends around "float가 설정이 된다."
    
    # We'll construct a replacement block based on the user's provided image.
    
    correct_content = """
다음은 문자열을 요소로 갖는 배열을 생성하는 구문이다.

```python
import numpy as np

unicode_array = np.array(['가나다', '라마바', '사아자'], dtype='<U32')
unicode_array
array(['가나다', '라마바', '사아자'], dtype='<U32')
```

물론 dtype은 생략하거나 우리가 알고 있는 str을 적을 수 있다.

```python
lang = np.array(['파이썬', '자바', '씨'])
lang
array(['파이썬', '자바', '씨'], dtype='<U3')

lang = np.array(['파이썬', '자바', '씨'], dtype=str)
lang
array(['파이썬', '자바', '씨'], dtype='<U3')
```

다음처럼 dtype=float으로 명시하면 모든 항목 자료형이 float가 된다.

```python
a = np.array((1, 2, 3), dtype=float)
a
array([1., 2., 3.])
```

다음처럼 dtype=float가 없더라도 배열 원소 중에 하나라도 float이면 자동으로 더 큰 범주인 float가 dtype이 된다.

```python
b = np.array((1, 2.5, 3))
b
array([1. , 2.5, 3. ])
```
"""
    
    # Identify unique start and end points in the messy text to replace.
    # Start: "unicode_array = np.array(['7fLtCt'"
    # End: "float가 설정이 된다."
    
    # We need to be careful with regex because of newlines and garbage.
    # Let's try to match the whole range.
    
    pattern = re.compile(r"unicode_array = np\.array\(\['7fLtCt'.*?float가 설정이 된다\.", re.DOTALL)
    
    # Check if pattern exists
    if pattern.search(content):
        content = pattern.sub(correct_content.strip(), content)
        print("Replaced garbled text block successfully.")
    else:
        print("Could not find the specific garbled text block. Trying looser match.")
        # Fallback: maybe just match parts?
        # "unicode_array = np.array(['7fLtCt'" is very specific.
        # "7fLtCt" might be enough?
        
    # Also clean up the "zl 석 물론 0[776은 ..." garbage line if it wasn't caught
    # It should be caught by .*? in regex if the end phrase is correct.
    # End phrase in file: "float가 설정이 된다." (Line 204 in view)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Refined {output_file} content.")

if __name__ == "__main__":
    main()
