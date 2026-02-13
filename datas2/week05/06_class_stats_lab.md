# 5-6. [실습] 우리 반 키/몸무게 데이터 분석

## 1. 데이터 생성 (가상 데이터)
실제 데이터가 없으므로 넘파이의 랜덤 기능을 이용해 가상의 우리 반 친구들을 만들어봅시다.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 재현을 위해 시드 고정
np.random.seed(0)

# 30명의 학생
heights = np.random.normal(170, 5, 30) # 평균 170, 표준편차 5
weights = np.random.normal(65, 10, 30) # 평균 65, 표준편차 10
names = ['Student_' + str(i) for i in range(1, 31)]

# 데이터프레임 조립
df = pd.DataFrame({
    '이름': names,
    '키': heights,
    '몸무게': weights
})

# 정수로 변환 (보기 좋게)
df = df.astype({'키': 'int', '몸무게': 'int'})
print(df.head())
```

## 2. 미션 1: 통계 확인하기
*   우리 반 키의 평균은?
*   몸무게가 가장 많이 나가는 친구는 몇 kg?

```python
print(df.describe())
```

## 3. 미션 2: 우량아 찾기 (필터링)
*   키가 175 이상이고, 몸무게가 70 이상인 학생을 찾아보세요.

```python
# 코드 작성...
big_students = df[ (df['키'] >= 175) & (df['몸무게'] >= 70) ]
print(big_students)
```

## 4. 미션 3: 키와 몸무게는 관계가 있을까? (시각화)
*   산점도(Scatter Plot)를 그려보세요.
*   x축: 키, y축: 몸무게

```python
plt.scatter(df['키'], df['몸무게'])
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Height vs Weight')
plt.grid(True)
plt.show()
```

## 5. 결과 해석
점들이 오른쪽 위로 올라가는 모양인가요? (키가 크면 몸무게도 많이 나간다)
