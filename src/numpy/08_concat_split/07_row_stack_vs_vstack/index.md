---
layout: numpy
title: "4.8.7 row_stack()과 vstack()"
---

# 4.8.7 row_stack()과 vstack()

`row_stack()`과 `vstack()`은 완전히 같은 함수이다. 이를 다음 그림과 함께 알아보자.

다음은 배열 `a`이다.

```python
import numpy as np

a = np.arange(1, 13).reshape(3, 4)
a
```
**출력:**
```
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

```python
b = np.arange(1, 5)
b
```
**출력:**
```
array([1, 2, 3, 4])
```

다음 함수 `np.row_stack((a, b))`로 수직으로 두 배열을 합칠 수 있다.

```python
np.row_stack((a, b))
```
**출력:**
```
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [ 1,  2,  3,  4]])
```

물론, 다음 함수 `np.vstack((a, b))`로도 수직으로 두 배열을 합칠 수 있다.

```python
np.vstack((a, b))
```
**출력:**
```
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [ 1,  2,  3,  4]])
```
