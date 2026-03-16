---
layout: numpy
title: "4.2.7 원소가 모두 1인 배열을 생성하는 ones()"
---

## 4.2.7 원소가 모두 1인 배열을 생성하는 ones()

**[수학적 의미: 일행렬(All-ones Matrix)의 등장]**
영행렬이 백지상태라면, 모든 칸이 1로 채워진 행렬은 데이터를 균일하게 증폭시키거나 마스킹(Masking) 연산을 할 때 유용하게 쓰이는 **일행렬(All-ones Matrix)**이라고 부릅니다.

**[Numpy 강림: ones() 팩토리]**
내장함수 `np.ones()`는 `zeros()`와 완전히 똑같은 문법 구조를 가지며 반환하는 배열의 모든 칸을 순수한 `1.0` 실수(또는 정수)로 꽉 채워냅니다.

```python
import numpy as np
np.ones((2, 4))
```
**출력:**
```
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.]])
```

인자 `dtype=int`로 정수 1로 원소가 채워지는 배열이 생성된다.

```python
import numpy as np
np.ones((2, 4), dtype=int)
```
**출력:**
```
array([[1, 1, 1, 1],
       [1, 1, 1, 1]])
```
