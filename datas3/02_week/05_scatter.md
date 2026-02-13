# 2주차 4강: 산점도 (Scatter Plot)

> **학습목표**: 두 변수 간의 관계(상관관계)를 파악하는 데 가장 강력한 도구인 산점도를 깊이 있게 이해하고, 다양한 옵션(색상, 크기)을 활용해 봅니다.

## 2.4.1. 산점도란 무엇인가? (Definition)

**산점도(Scatter Plot)**는 직교 좌표계(X축, Y축)를 이용해 두 변수 간의 관계를 점(Point)으로 나타내는 그래프입니다.
데이터가 어떻게 퍼져 있는지(산포)를 확인할 수 있어 **'산포도'**라고도 부릅니다.

### 2.4.1.1. 언제 사용하나요? (Usage)
주로 두 데이터 간의 **상관관계(Correlation)**를 확인할 때 사용합니다.

*   **양의 상관관계**: 키가 크면 몸무게도 많이 나간다. (우상향 ↗️)
*   **음의 상관관계**: 자동차 속도가 빠르면 연비가 떨어진다. (우하향 ↘️)
*   **상관관계 없음**: 점들이 아무 규칙 없이 퍼져 있다.

---

## 2.4.2. 산점도 실습 예제 (Examples)

### 2.4.2.1. [예제 1] 기본 산점도: 공부 시간과 성적
공부를 많이 하면 성적이 오를까요? 10명의 학생 데이터를 그려봅시다.

```python
import matplotlib.pyplot as plt

# 데이터 준비
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
score = [20, 30, 35, 45, 50, 65, 70, 85, 90, 95]

# 그래프 그리기
plt.figure(figsize=(6, 4))
plt.scatter(study_hours, score, color='blue')

plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.grid(True)
plt.show()
```
> **해석**: 점들이 오른쪽 위로 올라가는 **양의 상관관계**를 보입니다.

### 2.4.2.2. [예제 2] 그룹별 색상 구분 (Color Mapping)
남녀 성별에 따라 색상을 다르게 표시해 봅시다.

```python
# 데이터 준비
height = [160, 170, 155, 180, 165, 175] # 키
weight = [55, 70, 50, 85, 60, 75]       # 몸무게
gender_color = ['r', 'b', 'r', 'b', 'r', 'b'] # 여자(Red), 남자(Blue)

plt.figure(figsize=(6, 4))
plt.scatter(height, weight, c=gender_color) # c 옵션으로 색상 리스트 전달

plt.title("Height vs Weight by Gender")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()
```

### 2.4.2.3. [예제 3] 버블 차트 (Size Variation)
점의 **크기(s)**를 다르게 하여 3개의 변수를 표현할 수 있습니다. (X축, Y축, 크기)
예를 들어, **[인구 수, GDP, 만족도]**를 표현할 때, 만족도를 점의 크기로 나타낼 수 있습니다.

```python
# 데이터 준비
x = [10, 20, 30, 40, 50]
y = [20, 30, 10, 50, 40]
size = [100, 200, 500, 1000, 300] # 점의 크기 (면적)

plt.figure(figsize=(6, 4))
# s: 점 크기, alpha: 투명도 (점이 겹칠 때 유용)
plt.scatter(x, y, s=size, c='green', alpha=0.5) 

plt.title("Bubble Chart Example")
plt.show()
```
> **Tip**: 이렇게 점의 크기로 정보를 표현하는 그래프를 **버블 차트(Bubble Chart)**라고도 합니다.
