---
layout: default
title: "10주차 3강: 분포와 범주형 시각화 (Distribution & Categorical Plot)"
---

# 10주차 3강: 분포와 범주형 시각화 (Distribution & Categorical Plot)

> **학습목표**: 데이터가 어떻게 퍼져있는지(분포) 확인하고, 그룹(범주) 간의 차이를 비교하는 고급 시각화 기법을 익힙니다.

## 10.3.1. 분포 확인하기: `histplot`

데이터의 빈도수를 막대로 보여주는 히스토그램입니다. `kde=True`를 쓰면 부드러운 곡선(밀도)도 같이 그려줍니다.

```python
import seaborn as sns
from pydataset import data
tips = data('tips')

# 팁 금액의 분포 확인
sns.histplot(data=tips, x='tip', kde=True, color='green')
```

<br>

---

<br>

## 10.3.2. 범주형 데이터 비교

그룹별로 데이터를 비교할 때 쓰는 3대장입니다.

### 1. 막대 그래프: `barplot` / `countplot`
*   `barplot`: 그룹별 **평균**을 막대 높이로 표시 (오차 막대 포함)
*   `countplot`: 그룹별 **데이터 개수**를 셉니다. (`value_counts`의 시각화 버전)

```python
# 요일(day)별 팁(tip)의 평균
sns.barplot(data=tips, x='day', y='tip')

# 요일(day)별 손님 수
sns.countplot(data=tips, x='day')
```


<br>

---

<br>

### 2. 박스 플롯: `boxplot`
데이터의 통계적 분포(최소, 25%, 50%, 75%, 최대, 이상치)를 한 번에 보여줍니다. **이상치(Outlier) 찾을 때 최고**입니다.

```python
# 흡연 여부(smoker)에 따른 팁의 분포
sns.boxplot(data=tips, x='smoker', y='tip')
```


<br>

---

<br>

### 3. 바이올린 플롯: `violinplot`
박스 플롯에 분포 곡선(KDE)을 합친 형태입니다. 데이터가 어디에 많이 뭉쳐있는지 더 잘 보입니다.

```python
sns.violinplot(data=tips, x='smoker', y='tip')
```

<br>

---

<br>

## 10.3.3. 상관관계 히트맵: `heatmap`

숫자 데이터들끼리의 상관계수(`corr()`)를 색깔로 예쁘게 보여줍니다.

```python
# 상관계수 계산 (숫자 컬럼만)
corr = tips[['total_bill', 'tip', 'size']].corr()

# 히트맵 그리기 (annot=True: 숫자 표시)
sns.heatmap(corr, annot=True, cmap='coolwarm')
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: 데이터의 생김새(분포)를 볼 때는 `histplot`을 사용합니다.
*   **[핵심 2]**: 그룹 간 비교에는 `barplot`(평균), `countplot`(개수), `boxplot`(분포/이상치)을 상황에 맞게 골라 씁니다.
*   **[핵심 3]**: 여러 변수의 상관관계를 한눈에 볼 때는 `heatmap`이 가장 효과적입니다.
