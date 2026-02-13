---
layout: default
title: "10주차 5강: 시각화 종합 실습 (Seaborn Practice)"
---

# 10주차 5강: 시각화 종합 실습 (Seaborn Practice)

> **학습목표**: 기니피그의 치아 성장 데이터(`ToothGrowth`)를 사용하여 히스토그램, 산점도, 상자 그림, 바이올린 플롯, 히트맵 등 다양한 그래프를 직접 그려보고 데이터를 분석합니다.

## 10.5.1. 데이터 불러오기

`pydataset`을 이용해 실습 데이터를 불러옵니다.

*   **데이터셋**: `ToothGrowth` (비타민 C 투여량이 기니피그의 치아 성장에 미치는 영향)
*   **컬럼 설명**:
    *   `len`: 치아 길이 (Length)
    *   `supp`: 보충제 종류 (VC: 비타민 C, OJ: 오렌지 주스)
    *   `dose`: 투여량 (0.5, 1.0, 2.0 mg/day)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

# 데이터 불러오기
df = data('ToothGrowth')

# 데이터 정보 확인
print(df.info())
print(df.head())
```

<br>

---

<br>

## 10.5.2. 데이터 분포 확인 (Distribution)

치아 길이(`len`)가 어떻게 분포되어 있는지 히스토그램으로 확인해 봅시다.

```python
# 히스토그램과 밀도 곡선(KDE) 그리기
sns.histplot(data=df, x='len', kde=True, color='skyblue')
plt.title("Distribution of Tooth Length")
plt.show()
```

<br>

---

<br>

## 10.5.3. 상관관계 확인 (Relational Plot)

투여량(`dose`)이 늘어나면 치아 길이(`len`)도 길어질까요? 산점도로 확인해 봅니다.

```python
# 투여량(x)과 치아 길이(y)의 관계
# 보충제 종류(hue)에 따라 점의 색깔을 다르게 표시
sns.scatterplot(data=df, x='dose', y='len', hue='supp', s=100)
plt.title("Dose vs Tooth Length")
plt.show()
```

<br>

---

<br>

## 10.5.4. 집단 간 비교 (Categorical Plot)

보충제 종류(`supp`)와 투여량(`dose`)에 따라 치아 길이가 어떻게 다른지 비교해 봅시다.

### 1. 상자 그림 (Box Plot)
데이터의 최소, 최대, 중앙값 등을 한눈에 비교합니다.

```python
# x축: 투여량, y축: 치아 길이, 색상: 보충제 종류
sns.boxplot(data=df, x='dose', y='len', hue='supp')
plt.title("Tooth Length by Dose and Supplement")
plt.show()
```


<br>

---

<br>

### 2. 바이올린 플롯 (Violin Plot)
상자 그림보다 분포 모양을 더 자세히 볼 수 있습니다. `split=True`를 쓰면 두 집단을 하나로 합쳐서 보여줍니다.

```python
# split=True: 두 hue(VC, OJ)를 반반씩 합쳐서 그림
sns.violinplot(data=df, x='dose', y='len', hue='supp', split=True)
plt.show()
```

<br>

---

<br>

## 10.5.5. 상관계수 히트맵 (Heatmap)

각 변수들 간의 상관관계를 숫자로 계산하고 색깔로 표현합니다.

```python
# 문자열 컬럼(supp)은 상관계수 계산에서 제외해야 함
numeric_df = df[['len', 'dose']]

# 상관계수 계산
corr = numeric_df.corr()

# 히트맵 그리기
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.show()
```
> **해석**: `dose`와 `len`의 상관계수가 높게 나온다면, 투여량이 많을수록 치아 길이가 길어진다는 뜻입니다.

<br>

---

<br>

## 정리 (Summary)

이번 실습을 통해 우리는 다음과 같은 분석 과정을 거쳤습니다.

1.  **히스토그램**으로 데이터 전체의 생김새를 파악했습니다.
2.  **산점도**로 투여량과 치아 길이의 양의 상관관계를 확인했습니다.
3.  **박스 플롯/바이올린 플롯**으로 보충제 종류(OJ가 VC보다 효과가 좋은 구간 등)에 따른 차이를 비교했습니다.
4.  **히트맵**으로 변수 간의 관계를 수치로 증명했습니다.
