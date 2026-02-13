# 8주차 5강: 데이터프레임 심화 (Advanced DataFrame)

> **학습목표**: 데이터프레임을 내 마음대로 정렬하고, 수정하고, 요약하는 고급 기술을 익히고 시각화까지 연결해 봅니다.

## 8.5.1. 데이터 정렬 및 수정


<br>

---

<br>

### 1. 정렬하기: `sort_values()`
특정 컬럼을 기준으로 데이터를 줄 세웁니다.

```python
import pandas as pd

data = {
    '이름': ['철수', '영희', '민수'],
    '수학': [90, 80, 70],
    '영어': [85, 95, 60]
}
df = pd.DataFrame(data)

# 수학 점수 기준 오름차순 (낮은 순 -> 높은 순)
print(df.sort_values(by='수학'))

# 영어 점수 기준 내림차순 (높은 순 -> 낮은 순)
print(df.sort_values(by='영어', ascending=False))
```


<br>

---

<br>

### 2. 삭제하기: `drop()`
필요 없는 행이나 열을 제거합니다. **`axis` 설정이 중요합니다!**

*   `axis=0`: 행(Row) 삭제 (가로줄)
*   `axis=1`: 열(Column) 삭제 (세로줄)

```python
# '영어' 컬럼 삭제
df_no_eng = df.drop('영어', axis=1)

# 0번 인덱스 행 삭제
df_no_row0 = df.drop(0, axis=0)
```


<br>

---

<br>

### 3. 이름 바꾸기: `rename()`
컬럼 이름을 보기 좋게 바꿉니다.

```python
# 수학 -> Math, 영어 -> Eng
df_new = df.rename(columns={'수학': 'Math', '영어': 'Eng'})
```

<br>

---

<br>

## 8.5.2. 데이터 요약 (Statistics)

### 상관계수: `corr()`
두 변수가 얼마나 관련이 있는지 (-1 ~ 1) 보여줍니다.

```python
# 수학 점수와 영어 점수의 관계
print(df.corr())
#       수학      영어
# 수학  1.000000 -0.188982 (상관관계가 낮음)
# 영어 -0.188982  1.000000
```

<br>

---

<br>

## 8.5.3. 데이터프레임 시각화

데이터프레임도 `plot()` 하나면 훌륭한 그래프가 됩니다.

### 산점도 (Scatter Plot)
두 변수 간의 관계(상관관계)를 볼 때 유용합니다.

```python
import matplotlib.pyplot as plt

# 가상의 키, 몸무게 데이터
body_data = {
    '키': [170, 160, 180, 175, 165],
    '몸무게': [70, 55, 85, 75, 60]
}
df_body = pd.DataFrame(body_data)

# kind='scatter' 지정
df_body.plot(kind='scatter', x='키', y='몸무게', color='green', s=100)

plt.title("키와 몸무게의 관계")
plt.grid(True) # 격자 표시
plt.show()
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: `sort_values`로 데이터를 정렬하고, `drop`과 `rename`으로 모양을 다듬습니다.
*   **[핵심 2]**: `corr()`을 사용하면 변수들 사이의 숨겨진 관계(상관관계)를 숫자로 확인할 수 있습니다.
*   **[핵심 3]**: 데이터프레임의 컬럼을 x축, y축으로 지정하여 `plot()`을 그리면 데이터의 관계가 한눈에 보입니다.
