---
layout: numpy
title: "4.8.3 numpy.hstack()"
---

# 4.8.3 numpy.hstack()

## 4.6.3 numpy.hstack()

**[수학적 의미: 종속 변수 벡터의 통폐합]**
선형방정식 $$Ax = B$$ 시스템을 풀기 위해, 계수만 모은 거대한 $$A$$ 행렬의 맨 오른쪽 끝에 결과 벡터 $$B$$를 한 줄의 보너스 열(Column)로 찰싹 붙여서 큰 덩어리를 만드는 수학적 기법(첨가 행렬)을 구현할 때 쓰입니다. 

**[비유로 이해하기: 기차의 객차 확장]**
배열을 햄버거 쌓듯 위로 올리는 `vstack`과 반대로, 기차의 꼬리에 새로운 객차를 붙이거나 스마트폰 파노라마 사진을 옆으로 쭉 이어 붙이듯 데이터를 **옆(수평, Horizontal)** 방향으로 나란히 결합하여 길이를 늘입니다.

다음 배열 `a`는 모양이 (3, 2)인 2차원 배열이다.

```python
import numpy as np

a = np.arange(6).reshape(3, 2)
a
```
**출력:**
```
array([[0, 1],
       [2, 3],
       [4, 5]])
```

다음 배열 `b`는 모양이 (3, 3)인 2차원 배열이다.

```python
b = np.arange(10, 19).reshape(3, 3)
b
```
**출력:**
```
array([[10, 11, 12],
       [13, 14, 15],
       [16, 17, 18]])
```

행이 3으로 같은 위 두 배열을 `np.hstack((a, b))`로 수평으로 합칠 수 있다.

```python
np.hstack((a, b))
```
**출력:**
```
array([[ 0,  1, 10, 11, 12],
       [ 2,  3, 13, 14, 15],
       [ 4,  5, 16, 17, 18]])
```

`a = np.hstack((a, b))`로 수평으로 합치려면 2차원 이상의 배열 `a`, `b`가 두 번째 축을 제외하고 동일한 모양을 가져야 한다. 2차원 배열이라면 행이 같아야 한다. 1차원 배열은 무조건 수평으로 합쳐진다.

```python
c = np.array([[10, 20], [30, 40]])
c
```
**출력:**
```
array([[10, 20],
       [30, 40]])
```

위처럼 모양이 (2, 2)인 배열 `c`는 (3, 3)인 배열 `b`와 수평으로 합칠 수 없다. 행이 다르기 때문이다.

```python
np.hstack((a, c))
```
**오류:**
```
ValueError: all the input array dimensions except for the concatenation axis
must match exactly, but along dimension 0, the array at index 0 has size 3
and the array at index 1 has size 2
```

다음 코드처럼 1차원 배열은 원소 수에 상관없이 무조건 수평으로 합칠 수 있다.

```python
np.hstack((np.arange(3), np.arange(10, 15)))
```
**출력:**
```
array([ 0,  1,  2, 10, 11, 12, 13, 14])
```
