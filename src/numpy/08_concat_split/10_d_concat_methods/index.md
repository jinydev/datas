---
layout: numpy
title: "4.8.10 1차원 배열, 벡터의 다양한 결합 방법"
---

# 4.8.10 1차원 배열, 벡터의 다양한 결합 방법

## ① 여러 1차원 배열을 수평으로 나열하는 다양한 방법

다음 그림과 같이 벡터 `a`와 `b`를 그대로 1차원 배열에 수평으로 나열하는 다양한 방법을 알아보자.

![벡터 a와 b를 그대로 1차원 배열에 수평으로 나열하는 다양한 방법](img/page_028.png)

1차원 배열인 벡터 `a`, `b`가 있다.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a.shape)
print(b.shape)
```
**출력:**
```
(3,)
(3,)
```

벡터 `a`, `b`를 수평 방향으로 합치는 방법은 `np.hstack((a, b))`으로 가능하다.

```python
np.hstack((a, b))
```
**출력:**
```
array([1, 2, 3, 4, 5, 6])
```

수평 방향으로 합치는 방법은 `np.r_[a, b]`로도 가능하다.

```python
np.r_[a, b]
```
**출력:**
```
array([1, 2, 3, 4, 5, 6])
```

`np.concatenate((a, b))`로도 가능하다.

```python
np.concatenate((a, b))
```
**출력:**
```
array([1, 2, 3, 4, 5, 6])
```

## ② 여러 1차원 배열을 수직 방향으로 합치는 방법

다음 그림과 같이 벡터 `a`와 `b`를 그대로 수직으로 쌓아 2차원 배열을 만드는 다양한 방법을 알아보자.

1차원 배열인 벡터 `a`, `b`가 있다.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a.shape)
print(b.shape)
```
**출력:**
```
(3,)
(3,)
```

벡터 `a`, `b`를 수직 방향으로 합치는 방법은 `np.vstack((a, b))`으로 가능하다.

```python
np.vstack((a, b))
```
**출력:**
```
array([[1, 2, 3],
       [4, 5, 6]])
```

벡터 `a`, `b`를 수직 방향으로 합치는 방법 `np.row_stack((a, b))`으로도 가능하다.

```python
np.row_stack((a, b))
```
**출력:**
```
array([[1, 2, 3],
       [4, 5, 6]])
```

벡터 `a`, `b`를 수직 방향으로 합치는 방법 `np.r_[a[np.newaxis, :], b[np.newaxis, :]]`으로도 가능하다.

```python
np.r_[a[np.newaxis, :], b[np.newaxis, :]]
```
**출력:**
```
array([[1, 2, 3],
       [4, 5, 6]])
```

벡터 `a`, `b`를 수직 방향으로 합치는 방법 `np.concatenate((a[np.newaxis, :], b[np.newaxis, :]))`으로도 가능하다.

```python
np.concatenate((a[np.newaxis, :], b[np.newaxis, :]))
```
**출력:**
```
array([[1, 2, 3],
       [4, 5, 6]])
```

![1차원 배열을 수직 방향으로 합치는 방법](img/page_030.png)

1차원 배열인 벡터 `a`, `b`가 있다.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a.shape)
print(b.shape)
```
**출력:**
```
(3,)
(3,)
```


벡터 `a`, `b`를 열로 바꿔 수평 방향으로 합치는 방법은 `np.column_stack((a, b))`으로 가능하다.

```python
np.column_stack((a, b))
```
**출력:**
```
array([[1, 4],
       [2, 5],
       [3, 6]])
```

벡터 `a`, `b`를 열로 바꿔 수평 방향으로 합치는 방법은 `np.hstack((a[:, np.newaxis], b[:, np.newaxis]))`으로 가능하다.

```python
np.hstack((a[:, np.newaxis], b[:, np.newaxis]))
```
**출력:**
```
array([[1, 4],
       [2, 5],
       [3, 6]])
```

벡터 `a`, `b`를 열로 바꿔 수평 방향으로 합치는 방법은 `np.r_[a, b]`로도 가능하다.

```python
np.r_[a, b]
```
**출력:**
```
array([[1, 4],
       [2, 5],
       [3, 6]])
```

벡터 `a`, `b`를 열로 바꿔 수평 방향으로 합치는 방법은 `np.concatenate(((a[:, np.newaxis], b[:, np.newaxis])), axis=1)`로도 가능하다.

```python
np.concatenate(((a[:, np.newaxis], b[:, np.newaxis])), axis=1)
```
**출력:**
```
array([[1, 4],
       [2, 5],
       [3, 6]])
```
