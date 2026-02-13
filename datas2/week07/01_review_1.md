# 7-1. 전반기 핵심 요약 1 (Python & Matplotlib)

## 1. 우리가 걸어온 길
1주차부터 6주차까지 숨 가쁘게 달려왔습니다.
*   **1~2주차**: 파이썬 기초(리스트, 반복문)와 Matplotlib 시각화
*   **3~4주차**: Numpy와 Pandas 데이터 구조
*   **5~6주차**: 데이터 탐색, 통계, 그리고 전처리

## 2. 시각화 (Matplotlib) 핵심 코드
```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 15]

plt.plot(x, y, label='Line')
plt.scatter(x, y, color='red', label='Point')
plt.title("Summary Plot")
plt.legend()
plt.show()
```

## 3. 리스트와 반복문 핵심
```python
scores = [80, 90, 100]
for s in scores:
    if s >= 90:
        print("Excellent!")
```

## 4. [응용 예제] 성적 등급 그래프 그리기
학생들의 점수 리스트가 있을 때, 90점 이상인 학생과 그렇지 않은 학생을 색깔로 구분해서 그려봅시다.

[소스 코드 실행하기](src/01_review_1.py) | [Colab에서 열기](src/01_review_1.ipynb)
