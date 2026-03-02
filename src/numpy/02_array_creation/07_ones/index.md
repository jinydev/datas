---
layout: numpy
title: "4.2.7 원소가 모두 1인 배열을 생성하는 ones()"
---

# 4.2.7 원소가 모두 1인 배열을 생성하는 ones()

내장함수 `np.ones()`는 `zeros()`처럼 모두 실수 1.0인 배열을 반환하는 함수이다.

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
