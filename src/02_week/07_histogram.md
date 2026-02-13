---
layout: default
title: "2주차 6강: 히스토그램 (Histogram)"
---

# 2주차 6강: 히스토그램 (Histogram)

> **학습목표**: 데이터의 **분포(Distribution)**를 파악하는 히스토그램을 이해하고, 도수분포표(Frequency Distribution)의 개념과 함께 실습해 봅니다.

## 2.6.1. 히스토그램이란 무엇인가? (Definition)

**히스토그램(Histogram)**은 연속된 데이터를 일정한 구간(**Bin**, 통)으로 나누고, 각 구간에 속한 데이터의 개수(**Frequency**, 도수)를 막대 높이로 표현한 그래프입니다. 
데이터가 어디에 몰려 있는지 파악하는 데 유용합니다.

### 2.6.1.1. 도수분포표 (Frequency Distribution Table)
데이터를 구간별로 정리한 표입니다.

| 점수 구간 (Bin) | 학생 수 (Frequency) |
| :-------------: | :-----------------: |
|     0 ~ 20      |         2명         |
|     21 ~ 40     |         5명         |
|     41 ~ 60     |        10명         |
|     61 ~ 80     |        20명         |
|    81 ~ 100     |         8명         |

히스토그램은 이 표를 그림으로 그린 것입니다.

### 2.6.1.2. 막대그래프와의 차이점
*   **막대그래프**: **범주(Category)** 사이를 띄워서 그립니다. (순서가 상관없음. 사과, 포도)
*   **히스토그램**: **구간(Interval)** 사이를 붙여서 그립니다. (순서와 연속성이 중요함. 0~10, 10~20)

---

## 2.6.2. 히스토그램 실습 예제 (Examples)

### 2.6.2.1. [예제 1] 기본 히스토그램: 시험 점수 분포
학생들의 점수가 어디에 가장 많이 몰려있는지 확인해 봅시다. `plt.hist()`를 사용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np # 랜덤 데이터 생성을 위해

# 데이터 준비: 학생 1000명의 시험 점수 (평균 70, 표준편차 10인 정규분포)
scores = np.random.normal(70, 10, 1000)

# 그래프 그리기
plt.figure(figsize=(8, 5))
plt.hist(scores, bins=20, color='skyblue', edgecolor='black')

plt.title("Exam Score Distribution (Student Count: 1000)")
plt.xlabel("Score")
plt.ylabel("Frequency (Count)")
plt.grid(axis='y', alpha=0.5)

plt.show()
```
> **bins=20**: 데이터를 담을 통(Bin)을 20개로 나누겠다는 뜻입니다. 숫자가 클수록 막대가 촘촘해집니다.
> **edgecolor='black'**: 막대의 테두리를 검은색으로 그려서 구분을 명확하게 합니다.

### 2.6.2.2. [예제 2] 구간(Bin) 설정에 따른 차이
`bins` 값을 조절하면 데이터 분포를 다르게 해석할 수 있습니다.

```python
# bins=5: 너무 뭉뚱그려 보임
plt.hist(scores, bins=5, color='lightgreen', edgecolor='black')
plt.title("Bins = 5")
plt.show()

# bins=100: 너무 복잡해 보임
plt.hist(scores, bins=100, color='salmon', edgecolor='black')
plt.title("Bins = 100")
plt.show()
```
> **Insight**: 적절한 `bins` 값을 찾는 것이 중요합니다. 보통 10~30 사이를 많이 사용합니다.
