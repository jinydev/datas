# 10주차 3강: 화려한 시각화 (Seaborn)

## 10.3.1. Pandas 내장 그래프 (`plot`)

Pandas는 Matplotlib을 내장하고 있어서, `df.plot()`만 해도 바로 그래프가 그려집니다. EDA 단계에서 빠르게 확인하고 싶을 때 좋습니다.

```python
# 선 그래프 (기본)
df.plot()

# 막대 그래프
df.plot(kind='bar', x='Name', y='Score')
```

## 10.3.2. 통계 시각화 라이브러리 (Seaborn)

> **Seaborn**: Matplotlib을 기반으로 더 예쁘고 통계적인 그래프를 쉽게 그리도록 도와주는 라이브러리입니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 산점도 + 회귀선 (lmplot)
# 데이터셋의 추세를 확인할 때 강력합니다.
sns.lmplot(x='HP', y='Attack', data=df)

# 2. 히트맵 (heatmap)
# 상관계수를 색깔로 표현할 때 필수입니다.
plt.figure(figsize=(10, 8)) # 그림 크기 설정
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# annot=True: 숫자 표시
# cmap='coolwarm': 파란색(낮음) ~ 빨간색(높음)

plt.show()
```

> **Seaborn의 장점**:
> - 색감이 예쁩니다.
> - 복잡한 통계 그래프(박스플롯, 바이올린 플롯 등)를 한 줄로 그립니다.
> - 데이터프레임과 호환이 매우 잘 됩니다.
