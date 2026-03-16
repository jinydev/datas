---
layout: numpy
title: "4.6.4 배열 결합 연산 column_stack()과 row_stack()"
---

# 4.6.4 배열 결합 연산 column_stack()과 row_stack()

## ① numpy.column_stack()

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

다음 배열 `b`는 모양이 (3, 4)인 2차원 배열이다.

```python
b = np.arange(10, 22).reshape(3, 4)
b
```
**출력:**
```
array([[10, 11, 12, 13],
       [14, 15, 16, 17],
       [18, 19, 20, 21]])
```

함수 `np.column_stack((a, b))`는 2차원 배열 `a`, `b`를 수평으로(columns wise) 합친다.

```python
np.column_stack((a, b))
```
**출력:**
```
array([[ 0,  1, 10, 11, 12, 13],
       [ 2,  3, 14, 15, 16, 17],
       [ 4,  5, 18, 19, 20, 21]])
```

2차원 배열에서 함수 `np.column_stack((a, b))`는 바로 `np.hstack((a, b))`와 같다.

```python
np.hstack((a, b))
```
**출력:**
```
array([[ 0,  1, 10, 11, 12, 13],
       [ 2,  3, 14, 15, 16, 17],
       [ 4,  5, 18, 19, 20, 21]])
```

1차원 배열 `a`, `b`로 함수 `numpy.column_stack((a, b))`의 결과는 배열 `a`와 `b`를 먼저 축 1로 확장한 이후, 열로 쌓아 만든 2차원 배열을 반환한다.

```python
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])
np.column_stack((x, y))
```
**출력:**
```
array([[ 1, 10],
       [ 2, 20],
       [ 3, 30]])
```

위 1차원 배열의 `np.column_stack((a, b))`의 이해를 위해 다음 `x`의 1축을 증가시킨 2차원 배열을 생각해 보자. 1차원 배열에서 두 번째 축인 1축을 증가시키는 것은 다음 코드로 가능하다. 1차원 배열이 2차원으로 원소값이 `(N, 1)`인 열값으로 모양이 변형되었다.

```python
x[:, np.newaxis]
```
**출력:**
```
array([[1],
       [2],
       [3]])
```

마찬가지로 1차원 배열 `y`의 1축을 증가시킨 2차원 배열은 다음과 같다.

```python
y[:, np.newaxis]
```
**출력:**
```
array([[10],
       [20],
       [30]])
```

다음 코드와 같이 1차원 배열 `x`와 `y`에서 함수 `np.column_stack((x, y))`는 `np.column_stack((x[:, np.newaxis], y[:, np.newaxis]))`와 같은 결과를 얻는다.

```python
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])
np.column_stack((x[:, np.newaxis], y[:, np.newaxis]))
```
**출력:**
```
array([[ 1, 10],
       [ 2, 20],
       [ 3, 30]])
```

하지만 `np.hstack((x, y))`의 결과는 함수 `np.column_stack((x, y))`의 결과와 전혀 다르다. 결국, 1차원에서의 `np.hstack`과 `np.column_stack`은 그 결과가 다르다.

```python
np.hstack((x, y))
```
**출력:**
```
array([ 1,  2,  3, 10, 20, 30])
```

`np.column_stack`과 `np.hstack`의 결과는 항상 같은 것은 아니다. 그러므로 다음으로도 `False`가 반환된다.

```python
np.column_stack == np.hstack
```
**출력:**
```
False
```

## ② numpy.row_stack()

다음 배열 `a`는 모양이 (2, 3)인 2차원 배열이다.

```python
import numpy as np

a = np.arange(6).reshape(2, 3)
a
```
**출력:**
```
array([[0, 1, 2],
       [3, 4, 5]])
```

다음 배열 `b`는 모양이 (4, 3)인 2차원 배열이다.

```python
b = np.arange(10, 22).reshape(4, 3)
b
```
**출력:**
```
array([[10, 11, 12],
       [13, 14, 15],
       [16, 17, 18],
       [19, 20, 21]])
```

함수 `np.row_stack((a, b))`는 2차원 배열 `a`, `b`를 수직(vertically)으로 쌓는다.

```python
np.row_stack((a, b))
```
**출력:**
```
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [10, 11, 12],
       [13, 14, 15],
       [16, 17, 18],
       [19, 20, 21]])
```

함수 `np.row_stack()`은 `np.vstack()`과 그 기능이 같다.

```python
np.vstack((a, b))
```
**출력:**
```
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [10, 11, 12],
       [13, 14, 15],
       [16, 17, 18],
       [19, 20, 21]])
```

원소 수가 3개인 1차원 배열 `a`와 `b`의 함수 `np.row_stack((a, b))` 결과는 다음과 같다.

```python
a = np.array([4., 2., 1.])
b = np.array([3., 8., 7.])
print(np.row_stack((a, b)))
```
**출력:**
```
[[4. 2. 1.]
 [3. 8. 7.]]
```

함수 `np.vstack((a, b))` 결과도 위와 같다.

```python
print(np.vstack((a, b)))
```
**출력:**
```
[[4. 2. 1.]
 [3. 8. 7.]]
```

함수 `np.row_stack`과 `np.vstack`의 결과는 항상 같다. 다음으로도 `True`가 반환된다.

```python
np.row_stack == np.vstack
```
**출력:**
```
True
```
