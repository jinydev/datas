---
layout: home
title: "6주차 3강: 모듈과 라이브러리 (Modules & Libraries)"
---

# 6주차 3강: 모듈과 라이브러리 (Modules & Libraries)

> **학습목표**: 다른 사람이 만든 코드를 가져다 쓰는 **모듈(Module)**과 **라이브러리(Library)**의 개념을 이해하고, `import` 구문을 능숙하게 사용합니다.

## 5.4.1. 바퀴를 다시 발명하지 마라 (Don't reinvent the wheel)

이미 전 세계의 개발자들이 만들어 놓은 훌륭한 도구들이 있습니다. 우리는 직접 구현할 필요 없이 `import`만 하면 됩니다.


<br>

---

<br>

### [비유] 요리사와 밀키트
*   **직접 코딩**: 재료 손질부터 소스 만들기까지 전부 다 함.
*   **모듈 사용**: 잘 손질된 '밀키트'를 사와서 조리만 함.

<br>

---

<br>

## 5.4.2. 내장 모듈 사용하기 (Standard Library)

파이썬을 설치하면 기본적으로 포함된 '무료 밀키트'입니다.

```python
import math
import random

# 원주율 (pi)
print(math.pi) # 3.141592...

# 랜덤 정수 뽑기 (1부터 100 사이)
print(random.randint(1, 100)) 
```

<br>

---

<br>

## 5.4.3. 외부 라이브러리 (External Library)

누군가(설치해야 하는)가 만든 강력한 도구 모음입니다. 대표적인 예가 바로 **Numpy** 판다스(Pandas) 등입니다.

### 5.4.3.1. Numpy 불러오기
데이터 분석의 핵심 라이브러리인 Numpy를 불러와 봅시다.
관례적으로 `as np`라는 별칭(Alias)을 붙여서 사용합니다.

```python
import numpy as np

# 리스트와 비슷하지만 훨씬 강력한 배열(Array)
arr = np.array([1, 2, 3])

# 리스트에서는 불가능한 연산!
print(arr * 10) 
# [10 20 30] 
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: **모듈(Module)**은 변수, 함수, 클래스를 모아놓은 파이썬 파일(.py)이며, **라이브러리(Library)**는 이런 모듈들의 집합입니다.
*   **[핵심 2]**: `import`로 모듈 전체를 가져오거나, `from ... import`로 특정 기능만 가져올 수 있습니다.
*   **[핵심 3]**: `as` 키워드를 사용하면 모듈에 **별명(Alias)**을 붙여 코드를 더 짧고 편하게 쓸 수 있습니다. (예: `import numpy as np`)
