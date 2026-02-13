# 6-2. 빠진 값 채우기 (Missing Values)

## 1. NaN (Not a Number)
판다스에서는 빈 값을 `NaN`으로 표시합니다.

```python
import pandas as pd
import numpy as np

# 중간에 빈 값이 있는 리스트
data = {'이름': ['A', 'B', 'C'], '점수': [100, np.nan, 80]}
df = pd.DataFrame(data)

print(df)
# 점수에 NaN이 보일 겁니다.
```

## 2. 빈 값 찾기 (isnull)
데이터가 많으면 눈으로 못 찾습니다.

```python
# 빈 칸이 있으면 True
print(df.isnull())

# 빈 칸이 총 몇 개인지 세기 (⭐⭐⭐)
print(df.isnull().sum())
```

## 3. 방법 1: 지워버리기 (dropna)
"데이터도 많은데 그냥 빈 거 있는 줄은 다 버려!"

```python
clean_df = df.dropna()
```

## 4. 방법 2: 채워넣기 (fillna)
"아까우니까 평균 점수나 0점으로 채우자."

```python
# 0으로 채우기
df['점수'] = df['점수'].fillna(0)

# 평균으로 채우기
# mean_score = df['점수'].mean()
# df['점수'] = df['점수'].fillna(mean_score)
```

## 5. 핵심 정리
*   `isnull().sum()`: 빈 값 개수 확인.
*   `dropna()`: 삭제.
*   `fillna(값)`: 채우기.
