# 10주차 2강: 시본 기초 및 관계 시각화 (Seaborn Basics)

> **학습목표**: Matplotlib보다 더 예쁘고 강력한 **Seaborn** 라이브러리의 기초를 다지고, 두 변수 간의 관계(Relational Plot)를 그리는 법을 배웁니다.

## 10.2.1. Seaborn 소개


<br>

---

<br>

### "Why Seaborn?"
Matplotlib는 강력하지만, 예쁜 그래프를 그리려면 설정할게 너무 많습니다. Seaborn은:
1.  **기본 스타일이 예쁩니다.** (색감, 격자 등)
2.  **데이터프레임과 찰떡궁합**입니다. 컬럼 이름만 던져주면 알아서 그립니다.
3.  **통계적 기능**이 강력합니다. (추세선, 분포 등 자동 계산)

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn 테마 적용 (이거 한 줄이면 Matplotlib 그래프도 예뻐짐!)
sns.set_theme(style="darkgrid")
```

<br>

---

<br>

## 10.2.2. 산점도: `scatterplot`

두 숫자 변수 사이의 관계(상관관계)를 점으로 찍어 보여줍니다.

```python
from pydataset import data
tips = data('tips')

# x축: 총 청구액, y축: 팁
# hue: 색깔로 구분할 기준 (성별)
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')
plt.show()
```
> **포인트**: `hue` 옵션이 핵심입니다. 색상을 통해 제3의 변수(성별)까지 3차원 정보를 2차원에 표현합니다.

<br>

---

<br>

## 10.2.3. 선 그래프: `lineplot`

시간의 흐름에 따른 변화(시계열)를 볼 때 유용합니다.
Seaborn의 `lineplot`은 같은 x값에 여러 y값이 있으면 **자동으로 평균과 신뢰구간(그림자)**을 그려줍니다!

```python
fmri = sns.load_dataset("fmri") # Seaborn 내장 예제

# 시간(timepoint)에 따른 신호(signal)의 변화
# hue='event': 사건별로 선 색깔 다르게
# style='event': 사건별로 선 모양(실선/점선) 다르게
sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event", style="event")
plt.show()
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: `sns.set_theme()`로 전체 그래프 스타일을 세련되게 바꿀 수 있습니다.
*   **[핵심 2]**: `scatterplot`은 두 변수의 관계를 볼 때, `hue`를 써서 그룹별 차이를 확인합니다.
*   **[핵심 3]**: `lineplot`은 데이터의 추세를 보여주며, 자동으로 평균과 신뢰구간을 계산해 줍니다.
