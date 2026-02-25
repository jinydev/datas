---
layout: docs
title: "02. 다차원 배열 자료형 ndarray"
---

## 02. 다차원 배열 자료형 ndarray

`numpy`에서 가장 많이 다루는 대표적인 자료형은 `ndarray`이다. 용어 앞의 `n`은 다차원(multi dimension)을 의미하며 `ndarray`는 다차원 배열을 지원하는 자료형이다. `ndarray` 배열 객체는 고정된 크기(fixed-size)의 동일한(homogeneous) 자료형의 항목들로 이루어진 다차원의 배열이다.

`ndarray`는 클래스이므로 `ndarray`의 생성자인 다음 코드를 사용해 만들 수 있다. 그러나 일반적으로 더 편리한 `numpy` 함수 `array()`, `arange()`, `linspace()` 등을 사용한다.

```python
import numpy as np

a = np.ndarray(shape=(2,2), dtype=int)
a
```
**출력 (예시):**
```
array([[184086720,       583],
       [        0,         0]])
```

### numpy의 다양한 기본 자료형

`numpy`는 표준 파이썬보다 다양한 기본 자료형을 제공한다. 다음은 NumPy의 주요 자료형과 간단한 설명을 담은 표이다.

| 자료형                                | 설명                                                 |
| :------------------------------------ | :--------------------------------------------------- |
| `bool`                                | 부울 (참(`True`) 또는 거짓(`False`))                 |
| `int`                                 | 기본 정수형 (일반적으로 `int32` 또는 `int64`)        |
| `float`                               | 부동 소수점 수 (일반적으로 `float32` 또는 `float64`) |
| `complex`                             | 복소수 (일반적으로 `complex64` 또는 `complex128`)    |
| `int8`, `int16`, `int32`, `int64`     | 8비트, 16비트, 32비트, 64비트 정수                   |
| `uint8`, `uint16`, `uint32`, `uint64` | 부호 없는 8비트, 16비트, 32비트, 64비트 정수         |
| `float16`, `float32`, `float64`       | 16비트, 32비트, 64비트 부동 소수점 수                |
| `complex64`, `complex128`             | 64비트, 128비트 복소수                               |
