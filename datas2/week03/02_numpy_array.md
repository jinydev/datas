# 3-2. 넘파이 배열 만들기 (Array Creation)

## 1. 배열(Array) 생성하기
리스트와 비슷하지만 다릅니다. `np.array()`로 리스트를 감싸주면 됩니다.

```python
import numpy as np

# 리스트
my_list = [1, 2, 3]

# 넘파이 배열
my_array = np.array([1, 2, 3])

print(my_array)
```

## 2. 가장 큰 차이점: 사칙연산
리스트는 `+` 하면 이어 붙여졌죠?
넘파이 배열은 **수학적인 덧셈**이 됩니다.

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)
# 결과: [5 7 9]  (1+4, 2+5, 3+6)
```

> **중요**: 이것을 **벡터화 연산(Vectorization)**이라고 합니다. 반복문(`for`) 없이 한 번에 계산하므로 매우 빠릅니다.

## 3. 핵심 정리
*   `import numpy as np`: 넘파이를 불러오고 `np`라는 별명으로 부르겠다.
*   `np.array(리스트)`: 리스트를 넘파이 배열로 변환.
*   배열끼리 더하면 **같은 위치의 값끼리 더해진다.**
