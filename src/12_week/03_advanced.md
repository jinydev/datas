---
layout: default
title: "12주차 3강: 문자를 숫자로 (Feature Engineering)"
---

# 12주차 3강: 문자를 숫자로 (Feature Engineering)

컴퓨터는 '사과', '바나나' 같은 글자를 이해하지 못합니다. 숫자로 바꿔줘야 합니다.

## 12.3.1. 레이블 인코딩 (Label Encoding)

문자열을 가나다 순서대로 **숫자 번호**를 매깁니다.

- Apple -> 0
- Banana -> 1
- Cherry -> 2

```python
from sklearn.preprocessing import LabelEncoder

items = ['Apple', 'Banana', 'Cherry', 'Apple']
encoder = LabelEncoder()
encoded = encoder.fit_transform(items)
print(encoded) # [0 1 2 0]
```
> **문제점**: 2번(Cherry)이 1번(Banana)보다 '크다'고 오해할 수 있습니다. (순서가 없는 데이터에는 비추천)

## 12.3.2. 원-핫 인코딩 (One-Hot Encoding)

각 단어마다 전구 스위치를 하나씩 만들어줍니다. 해당 단어면 스위치를 켜고(1), 아니면 끕니다(0).

- Apple -> `[1, 0, 0]`
- Banana -> `[0, 1, 0]`
- Cherry -> `[0, 0, 1]`

```python
import pandas as pd

df = pd.DataFrame({'Fruit': ['Apple', 'Banana', 'Cherry']})
one_hot = pd.get_dummies(df['Fruit'])
print(one_hot)
```
> **장점**: 숫자 간의 크기 비교 오해가 없습니다. 가장 많이 사용되는 방식입니다.
