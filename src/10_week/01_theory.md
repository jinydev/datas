# 10주차 1강: 구멍 난 데이터 수리하기 (Missing Values)

## 10.1.1. 결측치(NaN)란?

> **NaN (Not a Number)**: 비어있는 값, 알 수 없는 값을 의미합니다.

현실의 데이터는 결코 깨끗하지 않습니다. 설문조사에서 답변을 안 했거나, 센서가 고장 나서 기록이 안 된 경우가 많습니다.
이 구멍 난 데이터를 그대로 두면 분석 결과가 엉망이 되거나 에러가 발생합니다.


<br>

---

<br>

## 10.1.2. 결측치 확인하기 (`isnull`)

```python
import pandas as pd
import numpy as np

# 데이터 생성 (NaN 포함)
data = {
    'Name': ['Hero', 'Mage', 'Thief'],
    'HP': [100, np.nan, 80],  # Mage의 HP가 비어있음
    'MP': [50, 200, np.nan]   # Thief의 MP가 비어있음
}
df = pd.DataFrame(data)

# 결측치 확인 (True면 비어있음)
print(df.isnull())

# 결측치 개수 세기 (컬럼별)
print(df.isnull().sum())
# Name    0
# HP      1
# MP      1
```


<br>

---

<br>

## 10.1.3. 결측치 처리하기


<br>

---

<br>

### 10.1.3.1. 방법 1: 삭제하기 (`dropna`)
"정보가 없는 데이터는 그냥 버리자!" (데이터가 충분히 많을 때 사용)

```python
# 결측치가 하나라도 있는 행 삭제
df_dropped = df.dropna()
print(df_dropped) # Hero만 남음
```


<br>

---

<br>

### 10.1.3.2. 방법 2: 채우기 (`fillna`)
"버리기 아까우니 평균값 등으로 메우자!" (데이터가 소중할 때 사용)

```python
# HP의 평균 구하기
mean_hp = df['HP'].mean() # 90.0

# 비어있는 HP를 평균값으로 채우기
df['HP'] = df['HP'].fillna(mean_hp)
print(df)
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: (내용 채우기)
*   **[핵심 2]**: (내용 채우기)
*   **[핵심 3]**: (내용 채우기)
