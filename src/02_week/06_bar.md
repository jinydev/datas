---
layout: default
title: "2주차 5강: 막대그래프 (Bar Plot)"
---

# 2주차 5강: 막대그래프 (Bar Plot)

> **학습목표**: 범주형 데이터(Category)의 크기를 비교하는 막대그래프를 이해하고, 세로형(Vertical)과 가로형(Horizontal)으로 표현하는 방법을 익힙니다.

## 2.5.1. 막대그래프란 무엇인가? (Definition)

**막대그래프(Bar Plot)**는 데이터의 수치나 값을 **막대의 길이**로 표현하는 그래프입니다.
여러 항목(Item) 간의 크기나 양을 한눈에 **비교(Comparison)**할 때 가장 많이 사용됩니다.

### 2.5.1.1. 언제 사용하나요? (Usage)
*   **Ranking**: 누가 1등이고 꼴등인가? (예: 반별 성적, 국가별 GDP)
*   **Comparison**: A와 B 중 누가 더 높나? (예: 매출 비교)

---

## 2.5.2. 막대그래프 실습 예제 (Examples)

### 2.5.2.1. [예제 1] 세로 막대그래프 (Vertical Bar Plot)
가장 일반적인 형태입니다. `plt.bar()`를 사용합니다.

```python
import matplotlib.pyplot as plt

# 데이터 준비: 과일 판매량
fruits = ['Apple', 'Banana', 'Orange', 'Grape']
sales = [50, 80, 40, 60]

# 그래프 그리기
plt.figure(figsize=(6, 4))
plt.bar(fruits, sales, color='orange') # 색상은 오렌지로 통일

plt.title("Fruit Sales Comparison")
plt.xlabel("Fruit")
plt.ylabel("Sales (Qty)")
plt.show()
```
> **해석**: Banana(바나나)가 가장 많이 팔렸고, Orange(오렌지)가 가장 적게 팔렸습니다.

### 2.5.2.2. [예제 2] 가로 막대그래프 (Horizontal Bar Plot)
항목 이름이 길거나(텍스트가 겹칠 때), 순위를 강조하고 싶을 때 유용합니다. `plt.barh()`를 사용합니다.

```python
# 데이터 준비: 영화 선호도 투표
movies = ['Harry Potter', 'Lord of the Rings', 'Star Wars', 'Avengers']
votes = [120, 150, 90, 200]

# 그래프 그리기 (barh 사용)
plt.figure(figsize=(8, 4))
plt.barh(movies, votes, color='skyblue')

plt.title("Movie Preference Poll")
plt.xlabel("Votes") # X축과 Y축이 바뀝니다!
plt.ylabel("Movie Title")
plt.show()
```
> **Tip**: `barh`를 쓸 때는 X축과 Y축의 라벨 의미가 반대가 됩니다.

### 2.5.2.3. [예제 3] 색상 다르게 지정하기
각 막대마다 다른 색상을 입힐 수도 있습니다.

```python
colors = ['red', 'green', 'blue', 'purple']
plt.bar(fruits, sales, color=colors)
plt.title("Colorful Fruits")
plt.show()
```
