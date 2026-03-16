---
layout: numpy
title: "4.2.11 내장함수 zeros_like()와 ones_like(), full_like()"
---

# 4.2.11 내장함수 zeros_like()와 ones_like(), full_like()

## ① 원소값이 0인 주어진 형태의 배열을 생성하는 zeros_like()

`np.zeros_like(a)`는 인자인 `a` 형태의 배열로 원소 값은 모두 0인 배열을 반환한다.

```python
import numpy as np

a = np.arange(8).reshape(2, 4)
a
```
**출력:**
```
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
```

```python
np.zeros_like(a)
```
**출력:**
```
array([[0, 0, 0, 0],
       [0, 0, 0, 0]])
```

## ② 원소값이 1인 주어진 형태의 배열을 생성하는 ones_like()

내장함수 `ones_like()`는 `ones()`나 `zeros()`처럼 모두 1인 배열을 반환하는 함수이다.

```python
np.ones_like(a)
```
**출력:**
```
array([[1, 1, 1, 1],
       [1, 1, 1, 1]])
```

## ③ 원소값이 주어진 값이며 주어진 형태의 배열을 생성하는 full_like()

내장함수 `full_like()`는 주어진 값으로 배열을 반환하는 함수이다.

```python
np.full_like(a, 5)
```
**출력:**
```
array([[5, 5, 5, 5],
       [5, 5, 5, 5]])
```
