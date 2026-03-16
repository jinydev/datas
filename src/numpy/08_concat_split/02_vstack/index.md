---
layout: numpy
title: "4.6.2 numpy.vstack()"
---

# 4.6.2 numpy.vstack()

## 4.6.2 numpy.vstack()

**[수학적 의미: 연립방정식의 확장 (Augmented Matrix)]**
수학에서 미지수가 하나 늘어나 식 한 줄을 통째로 밑에 더 추가해야 할 때가 있습니다. 이렇게 기존 행렬의 아래쪽에 새로운 행(Row) 데이터를 통째로 가져다 붙여 체급(행의 개수)을 늘리는 수학적 조립 과정입니다.

**[비유로 이해하기: 햄버거 쌓기]**
블록이나 햄버거 재료를 1층, 2층, 3층 차곡차곡 쌓듯이 데이터를 **위아래(수직, Vertical)** 방향으로 층층이 쌓아 올려 하나의 거대한 타워 구조체를 만듭니다.

다음 모양 (3, 2)로 같은 2차원 배열 `a`, `b`가 있다.

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

```python
b = np.arange(6, 12).reshape(3, 2)
b
```
**출력:**
```
array([[ 6,  7],
       [ 8,  9],
       [10, 11]])
```

위 두 배열을 수직(또는 세로, vertically)으로 합쳐서 모양이 (6, 2)가 되는 배열을 만들어 보자. `a = np.vstack((a, b))` 호출하면 가능하다.

```python
np.vstack((a, b))
```
**출력:**
```
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11]])
```

`np.vstack(tup)`에서 첫 인자인 `tup`은 튜플 자료형이다. `tup`은 합칠 여러 배열이다. 이 배열들은 첫 축을 제외한 모양이 같아야 한다.

```python
c = np.arange(20, 24).reshape(2, 2)
c
```
**출력:**
```
array([[20, 21],
       [22, 23]])
```

그러므로 위에서 모양이 (2, 2)인 배열 `c`는 다음 코드처럼 배열 `a`와 수직으로 합칠 수 있다.

```python
np.vstack((a, c))
```
**출력:**
```
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [20, 21],
       [22, 23]])
```

다음 코드처럼 열이 모두 2인 배열 `a`, `b`, `c`를 함께 수직으로 합칠 수 있다.

```python
np.vstack((a, b, c))
```
**출력:**
```
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [20, 21],
       [22, 23]])
```

검음 코드처럼 차수가 첫 축을 제외한 나머지 축의 모양이 같으면 수직으로 합칠 수 있다. 1차원 배열 `d`가 (1, 2)으로 2차원으로 확장되어 연산에 참여한다고 생각하자.

```python
d = np.array([100, 200])
np.vstack((a, d))
```
**출력:**
```
array([[ 0,   1],
       [ 2,   3],
       [ 4,   5],
       [100, 200]])
```

다음 코드처럼 모양이 (2, 2)인 배열 `a`와 원소가 3개인 1차원 배열과는 수직으로 합칠 수 없다. 다음처럼 오류가 발생한다.

```python
d = np.array([100, 200, 300])
np.vstack((a, d))
```
**오류:**
```
ValueError: all the input array dimensions except for the concatenation axis
must match exactly, but along dimension 1, the array at index 0 has size 2
and the array at index 1 has size 3
```

다음처럼 배열이 1차원이면 길이가 같아야 수직으로 합칠 수 있다.

```python
import numpy as np
x = np.array([1, 2, 3])
y = np.array([5, 6, 7])
np.vstack((x, y))
```
**출력:**
```
array([[1, 2, 3],
       [5, 6, 7]])
```
