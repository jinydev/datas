---
layout: numpy
title: "4.8.8 np.c_[]와 np.column_stack()"
---

# 4.8.8 np.c_[]와 np.column_stack()

**[실전 꿀팁]: 마법의 단축키 `np.c_` (Column-wise 기둥 세우기)**
`np.column_stack`과 완전히 같은 기능을 하지만, 이름이 너무 길어 쓰기 귀찮을 때 사용하는 초고수용 단축 문법입니다. 괄호 `()` 대신 대괄호 `[]`를 쓴다는 점이 특이하며, **C**는 Column(기둥)을 뜻합니다.

다음 모양 (3, )의 1차원 배열 `a`와 `b`가 있다.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

객체 `np.c_[]`는 함수 `np.column_stack()`과 유사하게 1차원 배열을 1축으로 늘려 수평으로 합친 결과를 반환한다. 즉, `np.c_[]`는 인자인 슬라이스 객체를 두 번째 축(axis=1)을 따라 연결해 반환한다(Translates slice objects to concatenation along the second axis).

```python
np.c_[a, b]
```
**출력:**
```
array([[1, 4],
       [2, 5],
       [3, 6]])
```

결국, 위 결과와 `np.column_stack((a, b))`의 결과는 같다.

```python
np.column_stack((a, b))
```
**출력:**
```
array([[1, 4],
       [2, 5],
       [3, 6]])
```

다음은 모양 (1, 3)의 2차원 배열 `x`, `y`이다.

```python
x = np.array([[1, 2, 3]])
y = np.array([[4, 5, 6]])
```

`np.c_[x, y]`는 수평으로 배열 `x`와 `y`를 합친다.

```python
np.c_[x, y]
```
**출력:**
```
array([[1, 2, 3, 4, 5, 6]])
```

`np.c_[x, y]`는 `np.column_stack((x, y))` 함수 호출과 결과가 같다.

```python
np.column_stack((x, y))
```
**출력:**
```
array([[1, 2, 3, 4, 5, 6]])
```

`np.c_[x, 10, 20, y]`는 수평으로 배열 `x`와 10, 20, `y`를 함께 합친다.

```python
np.c_[x, 10, 20, y]
```
**출력:**
```
array([[ 1,  2,  3, 10, 20,  4,  5,  6]])
```

`np.c_[x, 10, 20, y]`는 `np.column_stack([x, 10, 20, y])` 함수 호출과 결과가 같다.

```python
np.column_stack([x, 10, 20, y])
```
**출력:**
```
array([[ 1,  2,  3, 10, 20,  4,  5,  6]])
```
