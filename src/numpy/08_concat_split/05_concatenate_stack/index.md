---
layout: numpy
title: "4.6.5 배열 결합 연산 concatenate()와 stack()"
---

# 4.6.5 배열 결합 연산 concatenate()와 stack()

## ① numpy.concatenate()

배열을 쉽게 합치는 함수 `numpy.concatenate((a1, a2, ...), axis=0, ...)`는 기본적으로 축 0을 중심으로 합치는 기능을 수행한다.

다음 배열 `a`, `b`, `c`는 모양이 (2, )인 1차원 벡터 배열이다.

```python
import numpy as np
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
```

다음으로 배열 `a`, `b`, `c`를 `concatenate((a, b, c))`로 합치면 인자인 배열이 1차원 벡터이므로 축 0을 중심으로 추가된다.

```python
np.concatenate((a, b, c))
```
**출력:**
```
array([1, 2, 3, 4, 5, 6])
```

키워드 인자 `axis=0`를 기술해도 결과는 같다.

```python
np.concatenate((a, b, c), axis=0)
```
**출력:**
```
array([1, 2, 3, 4, 5, 6])
```

기본이 `axis=0`이 아닌 `None`인 것으로 지정할 수 있다. `axis=None`으로 지정하는 경우, 배열은 사용 전에 모두 평면화되어 연산된다.

```python
np.concatenate((a, b, c), axis=None)
```
**출력:**
```
array([1, 2, 3, 4, 5, 6])
```

다음 2차원 배열 `x`, `y`, `z`가 있다.

```python
import numpy as np

x = np.arange(6).reshape(2, 3)
x
```
**출력:**
```
array([[0, 1, 2],
       [3, 4, 5]])
```

```python
y = np.arange(10, 16).reshape(2, 3)
y
```
**출력:**
```
array([[10, 11, 12],
       [13, 14, 15]])
```

```python
z = np.arange(20, 24).reshape(2, 2)
z
```
**출력:**
```
array([[20, 21],
       [22, 23]])
```

다음 코드로 축 0으로 합칠 수 있다. 즉, 열 수가 같으면 축 0인 수직으로 합칠 수 있다.

```python
np.concatenate((x, y))
```
**출력:**
```
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [10, 11, 12],
       [13, 14, 15]])
```

그러나, 모양 (2, 2)로 열 수가 다른 `z`는 수직으로 합칠 수 없다. 그러므로 오류가 발생한다.

```python
np.concatenate((x, y, z))
```
**오류:**
```
ValueError: all the input array dimensions except for the concatenation axis
must match exactly, but along dimension 1, the array at index 0 has size 3
and the array at index 2 has size 2
```

다음 코드로는 축 1로 합치므로 수평으로 합쳐진다. 즉 수평으로 합치려면 행 수가 같아야 한다.

```python
np.concatenate((x, y), axis=1)
```
**출력:**
```
array([[ 0,  1,  2, 10, 11, 12],
       [ 3,  4,  5, 13, 14, 15]])
```

다음 코드로는 3개의 배열 `x`, `y`, `z`가 수평으로 합쳐진다. 배열 `z`는 모양 (2, 2)로 행 수가 2이므로 다음 코드가 가능하다.

```python
np.concatenate((x, y, z), axis=1)
```
**출력:**
```
array([[ 0,  1,  2, 10, 11, 12, 20, 21],
       [ 3,  4,  5, 13, 14, 15, 22, 23]])
```

`axis=None`으로 지정하는 경우, 배열은 사용 전에 모두 평면화되어 연산한다.

```python
np.concatenate((x, y), axis=None)
```
**출력:**
```
array([ 0,  1,  2,  3,  4,  5, 10, 11, 12, 13, 14, 15])
```

## ② numpy.stack()

**[비유로 이해하기: 얇은 종이를 겹쳐 두꺼운 책 만들기]**
`concatenate`는 기존의 차원(평면)을 그대로 유지하면서 데이터를 옆으로 혹은 아래로 이어 붙인다면, `stack`은 아예 **새로운 차원(축)을 하나 더 만들면서** 데이터를 묶습니다. 2차원 종이들을 겹쳐서 3차원의 두꺼운 책으로 만드는 과정과 같습니다.

`np.stack()` 함수는 주어진 둘 이상의 배열을 합쳐(쌓아) 하나의 배열로 만든다. `concatenate()` 함수와 달리 `stack()` 함수는 1차원 배열을 결합하여 하나의 2차원 배열을 만들고 2차원 배열을 결합하여 하나의 3차원 배열로 만든다. 또한, `np.stack`에 참여하는 배열은 모두 모양이 같아야 하며 `np.stack()`의 결과는 `axis`로 지정한 축으로 차수가 하나 증가하게 된다.

다음 그림은 1차원 배열인 벡터 `arr_1`과 `arr_2`를 인자로 사용한 `np.stack((arr_1, arr_2), axis=0 | 1)`을 설명하는 그림이다.

![배열 스택 연산](img/page_013.png)

다음 모양 (3, )의 1차원 배열 `a`, `b`가 있다.

```python
import numpy as np

a = np.array([1, 2, 3])
a
```
**출력:**
```
array([1, 2, 3])
```

```python
b = np.array([4, 5, 6])
b
```
**출력:**
```
array([4, 5, 6])
```

`np.stack()`은 지정한 새로운 축을 따라 동일한 차원의 여러 배열을 결합한다. 그러므로 입력 배열보다 1차원 더 많은 배열을 반환한다. 다음 코드로 `axis=0` 수직으로 차원 배열을 만든다.

```python
np.stack((a, b))
```
**출력:**
```
array([[1, 2, 3],
       [4, 5, 6]])
```

다음 코드로 축 `axis=1`, 수평으로 2차원 배열을 만든다.

```python
np.stack((a, b), axis=1)
```
**출력:**
```
array([[1, 4],
       [2, 5],
       [3, 6]])
```

다음 코드처럼 축 `axis=-1`로 지정해도 결과는 위와 같다. -1은 마지막 축을 의미한다.

```python
np.stack((a, b), axis=-1)
```
**출력:**
```
array([[1, 4],
       [2, 5],
       [3, 6]])
```

다음은 모양 (2, 3)의 2차원 행렬 `x`, `y`, `z`가 있다.

```python
x = np.arange(6).reshape(2, 3)
x
```
**출력:**
```
array([[0, 1, 2],
       [3, 4, 5]])
```

```python
y = np.arange(10, 16).reshape(2, 3)
y
```
**출력:**
```
array([[10, 11, 12],
       [13, 14, 15]])
```

```python
z = np.arange(20, 26).reshape(2, 3)
z
```
**출력:**
```
array([[20, 21, 22],
       [23, 24, 25]])
```

다음은 `np.stack()`으로 배열 `x`, `y`, `z`를 축 0으로 합친다.

```python
ax0 = np.stack((x, y, z), axis=0)
ax0
```
**출력:**
```
array([[[ 0,  1,  2],
        [ 3,  4,  5]],

       [[10, 11, 12],
        [13, 14, 15]],

       [[20, 21, 22],
        [23, 24, 25]]])
```

위 결과를 보면 배열 `x`, `y`, `z`를 수직으로 쌓은 모양이다. 축 0으로 합쳐지므로 축 0이 3이 되어 전체 모양은 (3, 2, 3)이 된다.

```python
ax0.shape
```
**출력:**
```
(3, 2, 3)
```

다음은 배열 `x`, `y`, `z`를 축 1 방향으로 합치는 코드이다.

```python
ax1 = np.stack((x, y, z), axis=1)
ax1
```
**출력:**
```
array([[[ 0,  1,  2],
        [10, 11, 12],
        [20, 21, 22]],

       [[ 3,  4,  5],
        [13, 14, 15],
        [23, 24, 25]]])
```

위 결과를 보면 배열 `x`, `y`, `z`를 행에 따라 수직으로 쌓은 모양이다. 행이 합쳐지므로 축 1이 3이 되어 전체 모양은 (2, 3, 3)이 된다.

```python
ax1.shape
```
**출력:**
```
(2, 3, 3)
```

다음은 배열 `x`, `y`, `z`를 축 2 방향으로 합치는 코드이다.

```python
ax2 = np.stack((x, y, z), axis=2)
ax2
```
**출력:**
```
array([[[ 0, 10, 20],
        [ 1, 11, 21],
        [ 2, 12, 22]],

       [[ 3, 13, 23],
        [ 4, 14, 24],
        [ 5, 15, 25]]])
```

위 결과를 보면 배열 `x`, `y`, `z`를 열로 바꿔 열에 따라 수평으로 쌓은 모양이다. 축 2로 합쳐지므로 축 2가 3이 되어 전체 모양은 (2, 3, 3)이 된다.

```python
ax2.shape
```
**출력:**
```
(2, 3, 3)
```

위 `np.stack((x, y, z), axis=2)` 과정을 좀 더 이해하기 쉽게 살펴보자. 다음은 배열 `x`이다.

```python
x
```
**출력:**
```
array([[0, 1, 2],
       [3, 4, 5]])
```

다음은 `x`를 마지막 축 2로 확장한 3차원 배열이다.

```python
x[:, :, np.newaxis]
```
**출력:**
```
array([[[0],
        [1],
        [2]],

       [[3],
        [4],
        [5]]])
```

이제 축 2로 확장한 위 3개의 배열을 축 2로 결합하면 3차원 배열을 얻을 수 있다.

```python
np.expand_dims(x, axis=2)
```

```python
np.expand_dims(y, axis=2)
```

```python
np.expand_dims(z, axis=2)
```

다음이 `np.stack((x, y, z), axis=2)` 결과이다.

```python
np.stack((x, y, z), axis=2)
```
