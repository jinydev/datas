---
layout: numpy
title: "4.6.6 column_stack()과 hstack()"
---

# 4.6.6 column_stack()과 hstack()

**[비유로 이해하기: 데이터 기둥 세워 표(Table) 완성하기]**
1차원 리스트 데이터들(예: 학생들의 아이디 목록, 수학 점수 목록 등)을 바닥에 눕혀두지 않고, 마치 꼿꼿한 **기둥(Column)**처럼 세운 다음 서로 옆으로 나란히 본드 붙이듯 합치는 기능입니다. 실무에서 여러 스칼라 값들을 하나의 2차원 표(DataFrame 꼴)로 만들 때 가장 요긴하게 쓰입니다.

다음 그림의 배열 `a`와 `c`를 수평으로 합쳐보자. 배열 `a`는 모양 (3, 4) 2차원 배열이며, 배열 `c`는 모양 (3, )의 1차원 배열이다.

![column_stack()과 hstack() 비교](img/page_019.png)

다음은 위 그림의 배열 `a`이다.

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

다음은 위 그림의 배열 `c`이다.

```python
c = np.arange(1, 6, 2)
c
```
**출력:**
```
array([1, 3, 5])
```

다음은 위 그림의 `np.hstack((a, c[:, np.newaxis]))` 연산을 위해 먼저 `c[:, np.newaxis]`의 결과를 알아보자. 축 1이 증가해 모든 원소가 열의 첫 번째 값이 된다.

```python
c[:, np.newaxis]
```
**출력:**
```
array([[1],
       [3],
       [5]])
```

다음 `np.hstack((a, c[:, np.newaxis]))` 호출로 배열 `a`와 `c`가 수평으로 합쳐진 결과를 얻을 수 있다.

```python
np.hstack((a, c[:, np.newaxis]))
```
**출력:**
```
array([[ 1,  2,  3,  4,  1],
       [ 5,  6,  7,  8,  3],
       [ 9, 10, 11, 12,  5]])
```

다음 코드처럼 2차원 배열 `a`와 1차원 배열 `c`는 `np.hstack((a, c))` 함수 호출로 바로 수평으로 합칠 수 없다. 오류가 발생한다. 위 코드처럼 2차원으로 확장해 호출해야 한다.

```python
np.hstack((a, c))
```
**오류:**
```
ValueError: all the input arrays must have same number of dimensions, but
the array at index 0 has 2 dimension(s) and the array at index 1 has 1
dimension(s)
```

배열의 차수를 늘리는 또 다른 방법은 `np.expand_dims(c, axis=0 | 1)`도 가능하다.

```python
np.hstack((a, np.expand_dims(c, axis=1)))
```
**출력:**
```
array([[ 1,  2,  3,  4,  1],
       [ 5,  6,  7,  8,  3],
       [ 9, 10, 11, 12,  5]])
```

다음 `np.column_stack((a, c))` 호출로 1차원 배열 `c`를 바로 사용해 수평으로 합칠 수 있다.

```python
np.column_stack((a, c))
```
**출력:**
```
array([[ 1,  2,  3,  4,  1],
       [ 5,  6,  7,  8,  3],
       [ 9, 10, 11, 12,  5]])
```
