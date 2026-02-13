# 6주차 2강: 운에 맡기세요 (Random & Visualization)

## 6.3.1. 난수 생성 삼총사

게임에서 "확률"은 필수 요소입니다. Numpy의 `random` 모듈이 이 역할을 합니다.

1.  `np.random.rand()`: 0 ~ 1 사이의 실수 (균등 분포).
2.  `np.random.randn()`: 평균 0, 표준편차 1인 실수 (표준 정규 분포).
3.  `np.random.randint()`: 특정 범위의 정수.


<br>

---

<br>

### 6.3.1.1. 실습: 아이템 강화 시뮬레이션 (주사위 굴리기)

```python
import numpy as np

# 1부터 100까지의 숫자 중 5개를 뽑음
dice_rolls = np.random.randint(1, 101, 5)
print("강화 주사위 결과:", dice_rolls)

# 강화 성공 여부 (예: 80 이상이면 성공)
success = dice_rolls >= 80
print("성공 여부:", success)
```


<br>

---

<br>

## 6.3.2. 랜덤 데이터 시각화 (Scatter Plot)

무작위 좌표를 생성해서 밤하늘의 별처럼 찍어봅시다.

```python
import matplotlib.pyplot as plt

# 별 100개의 X, Y 좌표 생성
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100) # 색상도 랜덤
sizes = np.random.rand(100) * 1000 # 크기도 랜덤 (0~1000)

# 산점도 그리기
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.title("Random Stars Visualization")
plt.colorbar() # 색상표 표시
plt.show()
```


> **설명**: `alpha=0.5`는 반투명하게 만들어서 점들이 겹쳐 보이게 합니다. `cmap`은 색상 테마(Colormap)입니다.
> 이렇게 난수를 이용해 데이터를 생성하고 시각화하면, 데이터의 **분포(Distribution)**를 이해하는 데 큰 도움이 됩니다.


<br>

---

<br>

### 6.2.2.1. 분포 비교 (Histogram)

`rand`(균등)와 `randn`(정규)의 차이를 눈으로 확인해 봅시다.

```python
# 데이터 생성 (10000개)
data_rand = np.random.rand(10000)   # 0 ~ 1 사이 균등
data_randn = np.random.randn(10000) # 평균 0, 표준편차 1 정규분포

# 히스토그램 그리기
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(data_rand, bins=50, color='blue', alpha=0.7)
plt.title("Uniform (rand)")

plt.subplot(1, 2, 2)
plt.hist(data_randn, bins=50, color='red', alpha=0.7)
plt.title("Normal (randn)")

plt.show()
```
*   **Uniform**: 모든 값이 평평하게 분포합니다. (네모 모양)
*   **Normal**: 0(평균) 근처에 데이터가 몰려 있습니다. (종 모양)

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: `np.random` 모듈은 데이터 분석과 시뮬레이션에 필요한 다양한 **난수(Random Number)**를 생성합니다.
*   **[핵심 2]**: `rand`(균등 분포), `randn`(정규 분포), `randint`(정수)의 차이를 이해하고 상황에 맞게 사용해야 합니다.
*   **[핵심 3]**: **시드(Seed)**를 설정하면 난수 생성 패턴을 고정하여 **결과를 재현**할 수 있습니다.
