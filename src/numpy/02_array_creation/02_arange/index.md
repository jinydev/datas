---
layout: numpy
title: "4.2.2 numpy의 내장함수 arange() 개요"
---

# 4.2.2 내장함수 arange()와 linspace()

## 4.2.2 numpy의 내장함수 arange() 개요

**[비유로 이해하기: 징검다리 건너기 (Step)]**
`np.arange`는 시작점에서 목표 지점(끝점) 전까지, 정해진 보폭(Step)으로 껑충껑충 뛰어가는 **개구리 점프**와 같습니다. (단, 끝점은 포함하지 않고 도착 바로 앞에서 멈춥니다!)

내장함수 `np.arange()`는 수 나열의 `ndarray`를 반환한다. `np.arange()`는 표준 파이썬의 내장함수 `range()`와 유사하며 매개변수 `start`, `stop`, `step`은 모두 정수뿐 아니라 실수도 가능하다.

`numpy.arange([start=0, ]stop, [step=1, ]dtype=None, *, like=None)`

주어진 간격 내에서 균등한 간격의 값을 반환하며, 다양한 수의 위치 인수를 사용하여 호출하고, 정수 인수의 경우 함수는 파이썬 내장함수 `range()`와 거의 동일하지만 range 인스턴스가 아닌 `ndarray`를 반환

- `arange(stop)`: 반 개방 구간 `[0, stop)` (즉, 시작은 포함하고 정지는 제외한 구간) 내에서 값이 생성되며, `step`은 1
- `arange(start, stop)`: 반 개방 구간 `[start, stop)` 내에서 값이 생성되며, `step`은 1
- `arange(start, stop, step)`: 반 개방 간격 `[start, stop)` 내에서 생성되며 값 사이의 간격은 `step`으로 지정

### 내장함수 arange() 활용

다음은 인자로 정수를 사용한 예이다. 결과로 출력된 `ndarray`에서 수 목록에 콤마가 없다.

```python
import numpy as np

print(np.arange(3))
print(np.arange(3, 7))
print(np.arange(3, 7, 2))
```
**출력:**
```
[0 1 2]
[3 4 5 6]
[3 5]
```

다음은 인자로 실수를 사용한 예이다. 함수 `arange()`는 배열의 수를 정확히 알기 힘들 수 있다.

```python
import numpy as np

print(np.arange(2.0))
print(np.arange(2.0, 6.5))
print(np.arange(2.0, 6.5, 0.8))
```
**출력:**
```
[0. 1.]
[2. 3. 4. 5. 6.]
[2.  2.8 3.6 4.4 5.2 6. ]
```
