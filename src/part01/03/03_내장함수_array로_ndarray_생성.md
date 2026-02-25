---
layout: docs
title: "03. 내장함수 array()로 ndarray 생성"
---

## 03. 내장함수 array()로 ndarray 생성

내장함수 `array()`로 간편히 `ndarray`를 만들 수 있다. 다음처럼 함수 인자로 값이 있는 리스트나 튜플로 기술한다. 키워드 인자 `dtype`은 항목의 자료형으로 선택 사항이다.

```python
import numpy as np

a = np.array([1, 2, 3], dtype=int)
a
```
**출력:**
```
array([1, 2, 3])
```

```python
type(a)
```
**출력:**
```
numpy.ndarray
```

위 `ndarray` 객체 `a`는 `shape`, `ndim` 등 여러 속성을 참조할 수 있다.

```python
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.size)
print(a.itemsize)
print(a.nbytes)
```
**출력 (예시):**
```
(3,)
1
int32
3
4
12
```

다음은 `numpy`의 `ndarray`(다차원 배열)의 주요 속성을 설명한 표이다.

| 속성               | 설명                                               |
| :----------------- | :------------------------------------------------- |
| `ndarray.shape`    | 배열의 차원을 나타내는 튜플. 각 차원의 크기를 표현 |
| `ndarray.ndim`     | 배열의 차원 수                                     |
| `ndarray.size`     | 배열의 총 요소 수                                  |
| `ndarray.dtype`    | 배열 요소의 데이터 형식                            |
| `ndarray.itemsize` | 배열의 각 요소의 크기(바이트)                      |
| `ndarray.nbytes`   | 배열의 전체 크기(바이트)                           |

함수 `array()`의 인자는 배열을 표현하는 리스트나 튜플 하나이며 다음처럼 수를 나열하면 오류가 발생한다.

```python
import numpy as np
np.array(1, 2, 3)
```
**오류:**
```
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
```

`ndarray`는 모든 원소(elements)가 단일한 자료형으로 구성된다. 그러므로 다음 코드처럼 하나라도 항목이 문자열이면 모든 항목이 동일하게 문자열 자료형인 `<U32`으로 지정된다.

```python
np.array([1, 'py', 3.14])
```
**출력:**
```
array(['1', 'py', '3.14'], dtype='<U32')
```

`numpy`의 자료형은 데이터의 저장 방식과 크기를 지정하는 데 사용되며, 배열의 요소는 이러한 자료형 중 하나만을 가질 수 있다. `numpy`에서 배열의 빠른 계산 처리를 위한 방법이다.

> [!NOTE]
> **문자열 자료형 `<U32`**
>
> `<U32`와 같은 자료형은 `numpy`에서 사용되는 유니코드 문자열 자료형을 나타낸다. 이 자료형은 길이가 32(32개의 문자를 포함할 수 있는)인 Unicode 문자열을 표현한다. 여기서 `<`는 Little-endian을 나타내고, `U`는 Unicode를, 32는 문자열의 최대 길이를 나타낸다. Little-endian은 숫자의 표현 방식 중 하나로, 숫자를 메모리에 저장할 때 가장 낮은 자릿수부터 저장하는 방식을 말한다.

```python
import numpy as np
unicode_array = np.array(['가나다', '라마바', '사아자'], dtype='<U32')

unicode_array
```
**출력:**
```
array(['가나다', '라마바', '사아자'], dtype='<U32')
```

물론 `dtype`은 생략하거나 우리가 알고 있는 `str`을 적을 수 있다.

```python
lang = np.array(['파이썬', '자바', '씨'])
lang
```
**출력:**
```
array(['파이썬', '자바', '씨'], dtype='<U3')
```

```python
lang = np.array(['파이썬', '자바', '씨'], dtype=str)
lang
```
**출력:**
```
array(['파이썬', '자바', '씨'], dtype='<U3')
```

다음처럼 `dtype=float`로 명시하면 모든 항목 자료형이 `float`가 된다.

```python
a = np.array((1, 2, 3), dtype=float)
a
```
**출력:**
```
array([1., 2., 3.])
```

다음처럼 `dtype=float`가 없더라도 배열 원소 중에 하나라도 `float`이면 자동으로 더 큰 범주인 `float`가 `dtype`이 된다.

```python
b = np.array((1, 2.5, 3))
b
```
**출력:**
```
array([1. , 2.5, 3. ])
```
