---
layout: docs
title: "06. 일정한 간격의 값으로 배열을 만드는 linspace()"
---

## 06. 일정한 간격의 값으로 배열을 만드는 linspace()

내장함수 `numpy.arange()`와 비슷한 `numpy.linspace()`는 하나의 간격을 동일한 길이의 하위 간격으로 분할하는(arrays with regularly-spaced) 수가 나열된 1차원 배열을 반환한다. 함수 `linspace()`에서 전체 구간은 `[start, stop]`으로 기본적으로 양쪽을 모두 포함한다. 끝점인 `stop`은 인자 `endpoint=False`로 제외할 수 있다. 일정한 간격을 구성하는 값인 배열의 수를 매개변수 `num`에 지정하며 기본값은 50이다.

- `numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)`
    - 지정된 간격에 걸쳐 균등한 간격의 숫자를 반환하며, 간격의 끝점은 `endpoint`로 선택적으로 제외될 수 있음

주요 매개변수:
- `start`: 시퀀스의 시작 값
- `stop`: 시퀀스의 마지막 값. `endpoint=False`이면 제외되며, 구간의 크기도 변경됨
- `num`: 생성되는 샘플 수로 기본값은 50
- `endpoint`: `True`이면 `stop`이 마지막 값이 되며 `False`이면 제외됨
- `retstep`: `True`이면 `(samples, step)`이 반환되며 아니면 `samples`만 반환되고 `step`은 샘플 수 사이의 간격을 말함

```python
import numpy as np

np.linspace(2.0, 3.0, num=5)
```
**출력:**
```
array([2.  , 2.25, 2.5 , 2.75, 3.  ])
```

### 내장함수 linspace() 활용

다음 코드는 `[2, 3]` 구간에서 3을 포함해 인자 `num`의 기본값인 50개의 수로 등분하는 수의 배열을 생성한다.

```python
np.linspace(2.0, 3.0)
```
**출력 (일부):**
```
array([2.        , 2.02040816, 2.04081633, ... , 2.97959184, 3.        ])
```

`retstep=True`로 반환받을 수 있다.

```python
np.linspace(2.0, 3.0, retstep=True)
```
**출력 (일부):**
```
(array([2.        , ... , 3.        ]), 0.02040816326530612)
```

위 결과인 반환 튜플에서 두 번째 값인 0.020408이 등분하는 간격으로 다음으로 직접 계산해 볼 수 있다.

```python
print( (3-2) / (50-1) )
```
**출력:**
```
0.02040816326530612
```

다음 코드로 끝점 3을 제외하면 `[2, 3)` 구간에서 3을 제외하고 50개의 수로 등분한다. 결국, 등분의 간격도 0.02로 위처럼 3을 포함하는 경우와 다르다.

```python
np.linspace(2.0, 3.0, endpoint=False, retstep=True)
```
**출력 (일부):**
```
(array([2.  , 2.02, ... , 2.98]), 0.02)
```

끝점을 제외한다면 `(stop - start) / num` 이 등분하는 간격 값이 된다.

```python
print( (3-2) / 50 )
```
**출력:**
```
0.02
```

다음 코드로 `[2, 3]`을 5개의 수로 4 등분하여 간격이 0.25임을 알 수 있다.

```python
np.linspace(2.0, 3.0, num=5, retstep=True)
```
**출력:**
```
(array([2.  , 2.25, 2.5 , 2.75, 3.  ]), 0.25)
```

다음 코드는 `[2, 3]`에서 3을 제외하고 5개의 수로 5 등분하여 간격이 0.2임을 알 수 있다.

```python
np.linspace(2.0, 3.0, num=5, endpoint=False, retstep=True)
```
**출력:**
```
(array([2. , 2.2, 2.4, 2.6, 2.8]), 0.2)
```
