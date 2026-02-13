---
layout: default
title: "2주차 7강: 피규어와 서브플롯 (Figure & Subplots)"
---

# 2주차 7강: 피규어와 서브플롯 (Figure & Subplots)

> **학습목표**: Matplotlib의 도화지(`Figure`)와 그래프 영역(`Axes`)을 이해하고, 여러 개의 그래프를 한 화면에 배치(`Subplot`)하는 다양한 방법을 익힙니다.

## 2.7.1. Figure와 Axes (Anatomy Revisited)

지난 시간에 배운 `Figure`와 `Axes`의 개념을 다시 한번 확실하게 짚고 넘어갑시다.

### 2.7.1.1. 개념도 (Concept)

```mermaid
graph TD
    subgraph Figure [Figure (전체 창)]
        Axes1[Axes 1 (그래프 1)]
        Axes2[Axes 2 (그래프 2)]
        Axes3[Axes 3 (그래프 3)]
        Axes4[Axes 4 (그래프 4)]
    end
    
    Figure --- Title[(Figure Title)]
    Axes1 --- SubTitle1[(Subtitle 1)]
```

*   **Figure**: 가장 큰 틀입니다. (예: 윈도우 창 전체)
*   **Axes**: 그래프가 그려지는 영역입니다. (예: 창 안의 작은 그림들)
*   **Subplot**: `Figure` 안에 있는 `Axes`를 의미합니다.

---

## 2.7.2. 서브플롯 생성 방법 3가지

### 2.7.2.1. [방법 1] plt.subplot() (State-based)
가장 간단하게 하나씩 순서대로 만들 때 사용합니다. `plt.subplot(행, 열, 인덱스)`

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4)) # 전체 크기 설정

# 1. 첫 번째 그래프 (1행 2열 중 1번째)
plt.subplot(1, 2, 1) 
plt.plot([1, 2, 3], [10, 20, 30])
plt.title("Plot 1")

# 2. 두 번째 그래프 (1행 2열 중 2번째)
plt.subplot(1, 2, 2)
plt.bar(['A', 'B', 'C'], [5, 3, 7])
plt.title("Plot 2")

plt.show()
```

### 2.7.2.2. [방법 2] plt.subplots() (Object-oriented) **(추천)**
**Figure와 Axes를 동시에 생성**합니다. 객체 지향 방식으로, 가장 많이 사용되는 현대적인 방법입니다.

```python
# fig는 전체 창, ax는 그래프 영역들의 리스트(배열)입니다.
fig, ax = plt.subplots(2, 2, figsize=(8, 8)) # 2행 2열 (총 4개)

# ax[행, 열]로 접근합니다.
ax[0, 0].plot([1, 2, 3], [1, 4, 9])
ax[0, 0].set_title("Line Plot (0, 0)")

ax[0, 1].scatter([1, 2, 3], [1, 2, 3])
ax[0, 1].set_title("Scatter Plot (0, 1)")

ax[1, 0].bar(['X', 'Y'], [10, 20])
ax[1, 0].set_title("Bar Plot (1, 0)")

ax[1, 1].hist([1, 1, 2, 3, 3, 3, 4, 5])
ax[1, 1].set_title("Histogram (1, 1)")

# 레이아웃 자동 정리 (겹침 방지)
plt.tight_layout() 
plt.show()
```
> **Tip**: `ax`를 쓸 때는 `plt.title()` 대신 `ax.set_title()`을 사용합니다. (`set_xlabel`, `set_ylabel` 등)

### 2.7.2.3. [방법 3] fig.add_subplot()
`Figure` 객체를 먼저 만들고, 나중에 `Axes`를 하나씩 추가할 때 씁니다.

```python
fig = plt.figure(figsize=(8, 4))

ax1 = fig.add_subplot(1, 2, 1) # 1행 2열 중 1번째
ax1.plot([1, 2, 3])

ax2 = fig.add_subplot(1, 2, 2) # 1행 2열 중 2번째
ax2.scatter([1, 2], [1, 2])

plt.show()
```

---

## 2.7.3. 레이아웃 관리 (Layout)

여러 그래프를 그리면 글자가 겹치는 경우가 많습니다. 이때 마법의 주문을 사용하세요.

### 2.7.3.1. plt.tight_layout()
그래프 간의 간격을 자동으로 조절하여 겹치지 않게 해줍니다. `plt.show()` 직전에 호출하면 됩니다.

```python
plt.subplot(2, 1, 1)
plt.plot([1, 2, 3])
plt.title("Very Long Title That Might Overlap With The Plot Below")

plt.subplot(2, 1, 2)
plt.plot([3, 2, 1])
plt.title("Another Plot")

plt.tight_layout() # 마법의 주문!
plt.show()
```

### 2.7.3.2. plt.subplots_adjust()
수동으로 여백을 조절하고 싶을 때 사용합니다.

```python
plt.subplots_adjust(wspace=0.5, hspace=0.5) # 가로(w), 세로(h) 간격 조절
```
