# 9주차 2강: 데이터 확인 및 통계 (Info & Statistics)

> **학습목표**: 불러온 데이터의 구조를 파악하고, 합계나 평균 같은 기초적인 통계량을 계산하여 데이터의 전체적인 특징을 이해합니다.

## 9.2.1. 데이터 명세 확인 (Inspection)

데이터를 분석하기 전, 이 데이터가 어떻게 생겼는지 확인하는 필수 과정입니다.


<br>

---

<br>

### 1. 요약 정보: `info()`
행/열 개수, 결측치 유무, 데이터 타입(dtype)을 한눈에 확인합니다.

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [90.5, 88.0, 92.5]
})

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   Name    3 non-null      object 
#  1   Age     3 non-null      int64  
#  2   Score   3 non-null      float64
```

### 2. 데이터 타입: `dtypes`
각 컬럼이 어떤 자료형인지 확인합니다.
*   `object`: 문자열 (String)
*   `int64`: 정수 (Integer)
*   `float64`: 실수 (Float)
*   `datetime64`: 날짜/시간

```python
print(df.dtypes)
```

<br>

---

<br>

## 9.2.2. 기술 통계량 계산 (Statistics)

숫자로 된 데이터들의 특징을 요약해 본다.

### 1. 주요 집계 함수
*   `sum()`: 합계
*   `mean()`: 평균
*   `median()`: 중앙값
*   `max()` / `min()`: 최댓값 / 최솟값
*   `count()`: 데이터 개수 (결측치 제외)

```python
print("나이 평균:", df['Age'].mean())
print("점수 합계:", df['Score'].sum())
```


<br>

---

<br>

### 2. 축(Axis)의 이해 (매우 중요!)
데이터프레임은 2차원이므로 방향을 지정해야 할 때가 있습니다.

*   `axis=0` (기본값): **위아래로(행 방향)** 계산 -> 결과는 **각 열(Column)의 통계**가 나옵니다.
*   `axis=1`: **좌우로(열 방향)** 계산 -> 결과는 **각 행(Row)의 통계**가 나옵니다.

```python
# 각 과목(열)의 평균 점수 (일반적인 사용법)
df.mean(axis=0) 

# 각 학생(행)의 평균 점수 (특수한 경우)
df.mean(axis=1)
```

> **Tip**: 헷갈린다면? `axis=0`은 "Row를 뭉갠다", `axis=1`은 "Column을 뭉갠다"라고 생각하세요!

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: `info()`함수로 데이터의 전체적인 구조와 결측치, 타입을 가장 먼저 확인해야 합니다.
*   **[핵심 2]**: `sum`, `mean` 등의 집계 함수로 데이터의 특징을 숫자로 요약할 수 있습니다.
*   **[핵심 3]**: 통계 연산 시 `axis=0`은 열 단위(세로), `axis=1`은 행 단위(가로) 계산을 수행합니다.
