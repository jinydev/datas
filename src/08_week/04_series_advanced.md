---
layout: home
title: "8주차 4강: 시리즈 심화 (Advanced Series)"
---

# 8주차 4강: 시리즈 심화 (Advanced Series)

> **학습목표**: 시리즈(Series)의 데이터를 분석하는 핵심 함수들을 익히고, `Matplotlib`를 활용해 데이터를 시각화하는 방법을 배웁니다.

## 8.4.1. 데이터 파악하기

데이터가 어떤 값들로 구성되어 있는지 확인하는 함수들입니다. (범주형 데이터에 특히 유용!)


<br>

---

<br>

### 1. 고유값 확인: `unique()`, `nunique()`
중복을 제거한 값들의 목록과 개수를 확인합니다.

```python
import pandas as pd

gender = pd.Series(['남', '여', '남', '남', '여'])

print(gender.unique())   # ['남' '여'] (종류 확인)
print(gender.nunique())  # 2 (종류 개수)
```


<br>

---

<br>

### 2. 빈도수 세기: `value_counts()`
각 값이 몇 번 등장했는지 세어줍니다. **데이터 분석에서 가장 많이 쓰는 함수 Top 3** 안에 듭니다.

```python
print(gender.value_counts())
# 남    3
# 여    2
# dtype: int64
```

<br>

---

<br>

## 8.4.2. 함수 적용하기: `map()`, `apply()`

### 1. 데이터 매핑: `map()`
딕셔너리를 사용해 데이터를 1:1로 변환할 때 씁니다.

```python
# '남' -> 0, '여' -> 1 로 변경
gender_map = {'남': 0, '여': 1}
encoded = gender.map(gender_map)

print(encoded)
# 0    0
# 1    1
# ...
```


<br>

---

<br>

### 2. 함수 적용: `apply()`
모든 원소에 복잡한 함수를 적용하고 싶을 때 씁니다.

```python
def mask_name(name):
    return name[0] + "*" + name[2:]

names = pd.Series(['홍길동', '임꺽정', '신사임당'])
masked = names.apply(mask_name)

print(masked)
# 0    홍*동
# 1    임*정
# 2    신*임당
```

<br>

---

<br>

## 8.4.3. 시리즈 시각화 (Visualization)

판다스는 `matplotlib`와 찰떡궁합입니다. 시리즈 뒤에 `.plot()`만 붙이면 바로 그림이 그려집니다.

### 1. 막대 그래프 (Bar Plot)
범주형 데이터의 빈도수를 시각화할 때 최고입니다. `value_counts()`와 함께 쓰세요.

```python
import matplotlib.pyplot as plt

# 1. 데이터 준비
favorite_fruit = pd.Series(['사과', '바나나', '사과', '포도', '바나나', '사과'])

# 2. 빈도수 계산 및 시각화
counts = favorite_fruit.value_counts()
counts.plot(kind='bar', color=['red', 'yellow', 'purple'], alpha=0.7)

# 3. 꾸미기
plt.title("과일 선호도 조사")
plt.xlabel("과일")
plt.ylabel("인원 수")
plt.xticks(rotation=0) # x축 글자 똑바로
plt.show()
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: `value_counts()`는 데이터의 분포를 확인하는 가장 강력한 도구입니다.
*   **[핵심 2]**: `map()`과 `apply()`를 사용하면 데이터를 내 입맛대로 변환할 수 있습니다.
*   **[핵심 3]**: `Series.plot()`을 사용하면 복잡한 코드 없이도 데이터를 바로 시각화할 수 있습니다.
