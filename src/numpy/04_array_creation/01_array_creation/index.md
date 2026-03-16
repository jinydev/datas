---
layout: numpy
title: "4.2.1 내장함수 array()로 ndarray 생성"
---

# 4.4.1 내장함수 array()로 ndarray 생성

![다차원 배열 생성 공장](../img/array_creation.png)

<div style="text-align: center; margin: 30px 0;">
  <!-- SVG ndarray 팩토리 애니메이션 -->
  <svg width="450" height="250" viewBox="0 0 450 250" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- 금속 기계 파이프 질감 -->
      <linearGradient id="pipeGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#718096" />
        <stop offset="50%" stop-color="#cbd5e0" />
        <stop offset="100%" stop-color="#4a5568" />
      </linearGradient>
      
      <!-- 넘파이 데이터 블록 그라데이션 -->
      <linearGradient id="dataGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#4fd1c5" />
        <stop offset="100%" stop-color="#2c7a7b" />
      </linearGradient>

      <!-- 빛나는 에너지 볼 효과 -->
      <filter id="energyGlow" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="5" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
      </filter>
    </defs>

    <!-- 1. 파이썬 리스트 원자재 투입구 (위치: 왼쪽) -->
    <g transform="translate(40, 60)">
      <rect x="0" y="0" width="80" height="100" fill="#edf2f7" stroke="#a0aec0" stroke-width="2" rx="5"/>
      <text x="40" y="-10" font-family="Arial" font-size="12" font-weight="bold" fill="#4a5568" text-anchor="middle">Python List</text>
      <text x="40" y="30" font-family="monospace" font-size="14" fill="#2d3748" text-anchor="middle">[1, 2, 3]</text>
      <!-- 떨어지는 리스트 데이터 애니메이션 -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0,40; 0,90" dur="2s" repeatCount="indefinite" />
        <circle cx="40" cy="0" r="10" fill="#f6ad55" filter="url(#energyGlow)"/>
        <text x="40" y="4" font-family="monospace" font-size="10" fill="white" text-anchor="middle">1,2,3</text>
      </g>
    </g>

    <!-- 2. 중앙 np.array() 변환 엔진 (용광로) -->
    <g transform="translate(190, 80)">
      <!-- 원통형 엔진 본체 -->
      <path d="M0,0 L60,0 L70,80 L-10,80 Z" fill="url(#pipeGrad)" stroke="#2d3748" stroke-width="2"/>
      <ellipse cx="30" cy="0" rx="30" ry="10" fill="#a0aec0" stroke="#2d3748" stroke-width="2"/>
      <ellipse cx="30" cy="80" rx="40" ry="15" fill="#4a5568" stroke="#2d3748" stroke-width="2"/>
      
      <!-- 중앙 코어 깜빡임 효과 -->
      <circle cx="30" cy="40" r="15" fill="#ed8936" filter="url(#energyGlow)">
        <animate attributeName="fill" values="#ed8936; #f6ad55; #ed8936" dur="1s" repeatCount="indefinite"/>
        <animate attributeName="r" values="15; 18; 15" dur="1s" repeatCount="indefinite"/>
      </circle>
      <text x="30" y="-20" font-family="monospace" font-size="14" font-weight="bold" fill="#e53e3e" text-anchor="middle">np.array()</text>
    </g>

    <!-- 파이프라인 (리스트 -> 엔진) -->
    <path d="M120,110 L180,110" stroke="#cbd5e0" stroke-width="8" stroke-linecap="round"/>
    <!-- 전송되는 에너지 선 -->
    <line x1="120" y1="110" x2="180" y2="110" stroke="#f6ad55" stroke-width="3" stroke-dasharray="10,5">
      <animate attributeName="stroke-dashoffset" from="15" to="0" dur="0.5s" repeatCount="indefinite"/>
    </line>

    <!-- 파이프라인 (엔진 -> ndarray) -->
    <path d="M260,110 L300,110" stroke="#cbd5e0" stroke-width="8" stroke-linecap="round"/>
    <line x1="260" y1="110" x2="300" y2="110" stroke="#4fd1c5" stroke-width="3" stroke-dasharray="10,5">
      <animate attributeName="stroke-dashoffset" from="15" to="0" dur="0.5s" repeatCount="indefinite"/>
    </line>

    <!-- 3. 완성된 ndarray (오른쪽 컨베이어 벨트) -->
    <g transform="translate(320, 60)">
      <!-- 컨베이어 벨트 베이스 -->
      <rect x="-10" y="80" width="120" height="15" fill="#a0aec0" rx="5"/>
      <circle cx="0" cy="87.5" r="5" fill="#4a5568">
        <animateTransform attributeName="transform" type="rotate" values="0; 360" dur="2s" repeatCount="indefinite" additive="sum"/>
      </circle>
      <circle cx="50" cy="87.5" r="5" fill="#4a5568">
         <animateTransform attributeName="transform" type="rotate" values="0; 360" dur="2s" repeatCount="indefinite" additive="sum"/>
      </circle>
      <circle cx="100" cy="87.5" r="5" fill="#4a5568">
         <animateTransform attributeName="transform" type="rotate" values="0; 360" dur="2s" repeatCount="indefinite" additive="sum"/>
      </circle>

      <text x="50" y="-10" font-family="Arial" font-size="12" font-weight="bold" fill="#319795" text-anchor="middle">Numpy ndarray</text>
      
      <!-- 단단하게 결합된 배열 블록들 (출력물) -->
      <g stroke="#234e52" stroke-width="2">
        <animateTransform attributeName="transform" type="translate" values="-10,50; 30,50" dur="2s" repeatCount="indefinite" />
        <rect x="0" y="0" width="25" height="25" fill="url(#dataGrad)" rx="3"/>
        <text x="12.5" y="17" font-family="monospace" font-size="14" fill="white" stroke="none" text-anchor="middle">1</text>
        
        <rect x="25" y="0" width="25" height="25" fill="url(#dataGrad)" rx="3"/>
        <text x="37.5" y="17" font-family="monospace" font-size="14" fill="white" stroke="none" text-anchor="middle">2</text>
        
        <rect x="50" y="0" width="25" height="25" fill="url(#dataGrad)" rx="3"/>
        <text x="62.5" y="17" font-family="monospace" font-size="14" fill="white" stroke="none" text-anchor="middle">3</text>
      </g>
    </g>

    <text x="225" y="220" font-family="Arial" font-size="14" font-weight="bold" fill="#4a5568" text-anchor="middle">
      가장 원시적인 형태(List)를 연속된 고속 메모리 덩어리(ndarray)로 압축 및 조립
    </text>
  </svg>
  <p style="color: #718096; font-size: 0.9em; margin-top: -10px;"><em>[그림] 느슨한 리스트 원자재를 압축하여 ndarray 장갑차로 생산해 내는 array() 엔진</em></p>
</div>

## 4.4.1 내장함수 array()로 ndarray 생성

**[수학적 의미: 무에서 유를 창조하는 공간 선언]**
선형대수학에서는 어떤 연산을 시작하기 전, 스케치북에 "나는 가로 3칸, 세로 3칸짜리 2차원 공간을 쓰겠다"고 차원(Dimension)을 선언합니다. `numpy`에서도 마찬가지로 가장 뼈대가 되는 배열 생성자 팩토리(Factory)를 가동해야 합니다.

**[Numpy 강림: array() 엔진]**
파이썬의 가장 원시적인 자료구조인 리스트(List) 재료를 `array()` 공장의 파이프에 밀어 넣으면, 내부적으로 메모리를 압축하여 막강한 `ndarray` 장갑차로 변환되어 나옵니다.

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

---

### 내장함수 repeat()과 tile()을 활용한 배열 생성

동일한 숫자를 여러 번 반복해서 배열을 만들고 싶을 때는 수작업으로 입력하는 대신 `np.repeat()`과 `np.tile()` 함수를 사용하면 매우 편리합니다.

**① np.repeat() 함수**
`np.repeat()` 함수는 배열의 각 개별 요소를 지정한 횟수만큼 반복하여 늘려줍니다.

> **np.repeat(a, repeats)**
> - **a**: 반복할 입력 배열 또는 스칼라 값
> - **repeats**: 각 요소를 반복할 횟수

```python
import numpy as np

# 4.2.1 단일 값 8을 4번 반복
print("단일 값 반복:", np.repeat(8, 4))
# 4.2.1 출력: [8 8 8 8]

# 4.2.1 배열 [1, 2, 4]를 통째로 2번씩 반복 (각 원소가 2번씩 연달아 나옴)
print("배열 원소 각각 반복:", np.repeat([1, 2, 4], 2))
# 4.2.1 출력: [1 1 2 2 4 4]

# 4.2.1 배열 요소마다 다르게 반복 횟수 지정 ([1은 1번, 2는 2번, 4는 3번])
print("각기 다른 횟수 반복:", np.repeat([1, 2, 4], repeats=[1, 2, 3]))
# 4.2.1 출력: [1 2 2 4 4 4]
```

**② np.tile() 함수**
`np.tile()` 함수는 `repeat()`과 달리 패턴 단위로 묶어서(블록 전체를) 통째로 복사해서 이어 붙입니다. 타일(Tile)을 바닥에 깔아 나가는 방식을 생각하면 이해하기 쉽습니다.

> **np.tile(a, reps)**
> - **a**: 반복할 패턴이 담긴 배열
> - **reps**: 전체 패턴을 반복 복사할 횟수

```python
# 4.2.1 배열 [1, 2, 4] 패턴 전체를 통째로 2번 반복
repeated_whole = np.tile([1, 2, 4], 2)
print("패턴 전체를 타일처럼 두 번 이어붙이기:", repeated_whole)
# 4.2.1 출력: [1 2 4 1 2 4]
```
