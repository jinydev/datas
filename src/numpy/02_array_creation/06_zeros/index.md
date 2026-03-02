---
layout: numpy
title: "4.2.6 원소가 모두 0인 배열을 생성하는 zeros()"
---

# 4.2.6 내장함수 zeros()와 ones(), empty()

## 4.2.6 원소가 모두 0인 배열을 생성하는 zeros()

내장함수 `np.zeros()`는 주어지는 `shape` 형태로 0이 채워진 `ndarray`를 반환하는 함수이다.

`numpy.zeros(shape, dtype=float, order='C', *, like=None)`
- 주어진 모양과 유형의 0으로 채워진 새 배열의 반환
- `shape`: `int` 모양 또는 `int`의 튜플, 즉 배열의 모양 예, `(2, 3)` 또는 `2` 등
- `dtype`: 데이터 유형, 선택 사항. 배열에 대해 원하는 데이터 유형(예: `numpy.int8`), 기본값은 `numpy.float64`
- `order`: 순서 `{'C', 'F'}`, 선택 사항, 기본값: `'C'`. 다차원 데이터를 행 중심(C 스타일) 또는 열 중심(포트란 스타일) 순서로 메모리에 저장할지 여부를 지정

인자 `shape`가 정수 5이면 0이 5개인 배열이 생성되며, 원소의 `dtype`은 기본인 `float64`이다.

```python
import numpy as np
a = np.zeros(5)
a
```
**출력:**
```
array([0., 0., 0., 0., 0.])
```

```python
a.dtype
```
**출력:**
```
dtype('float64')
```

다음처럼 `shape=(5,)`, `dtype=int`로 지정하면 `shape=5`와 같으며 정수 0이 채워지는 배열이 생성된다.

```python
np.zeros((5,), dtype=int)
```
**출력:**
```
array([0, 0, 0, 0, 0])
```

다음처럼 `shape=(2, 1)`으로 지정하면 모든 원소가 0이 채워진 2행 1열의 2차원 배열이 생성된다.

```python
b = np.zeros((2, 1))
b
```
**출력:**
```
array([[0.],
       [0.]])
```

```python
b.shape
```
**출력:**
```
(2, 1)
```
