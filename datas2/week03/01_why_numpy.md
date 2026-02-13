# 3-1. [이론] 왜 파이썬 리스트로는 부족한가?

## 1. 빅데이터는 무겁다
지난 시간에 배운 리스트(List)는 참 편리합니다. 하지만 데이터가 100만 개, 1000만 개가 되면 어떨까요?
파이썬 리스트는 **느립니다.** 그리고 메모리를 많이 차지합니다.

## 2. 넘파이(Numpy)의 등장
Numerical Python의 약자인 Numpy는 **"빠르고 효율적인 계산"**을 위해 만들어졌습니다.
C언어로 만들어져 있어서 파이썬보다 훨씬 빠릅니다.

## 3. 속도 비교 (체감해보기)
실제로 얼마나 차이가 나는지 코드로 확인해봅시다. (지금은 이해 못해도 괜찮아요!)

```python
import numpy as np
import time

# 100만 개의 데이터
size = 1000000

# 리스트 준비
py_list = list(range(size))
# 넘파이 배열 준비
np_arr = np.arange(size)

# 리스트 계산 시간 측정
start = time.time()
py_list = [x * 2 for x in py_list]
print("리스트 걸린 시간:", time.time() - start)

# 넘파이 계산 시간 측정
start = time.time()
np_arr = np_arr * 2
print("넘파이 걸린 시간:", time.time() - start)
```

## 4. 핵심 정리
*   **Numpy**: 수치 계산에 특화된 파이썬 라이브러리.
*   빅데이터 분석에서는 리스트 대신 무조건 **Numpy 배열(Array)**을 사용합니다.
