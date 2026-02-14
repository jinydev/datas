---
layout: home
title: "7주차 3강: 정답 및 해설 (Solutions)"
---

# 7주차 3강: 정답 및 해설 (Solutions)

## 7.3.1. 문제 1. 시각화 기초

```python
import matplotlib.pyplot as plt

scores = [80, 90, 70, 60, 100]
students = ['A', 'B', 'C', 'D', 'E'] # X축 라벨용 (없어도 됨)

plt.bar(students, scores)
plt.title("Math Scores")
plt.show()
```


<br>

---

<br>

## 7.3.2. 문제 2. Numpy 배열 생성

```python
import numpy as np

# 0부터 21전까지(20까지), 2씩 건너뛰기
evens = np.arange(0, 21, 2)
print(evens)
# 출력: [ 0  2  4  6  8 10 12 14 16 18 20]
```


<br>

---

<br>

## 7.3.3. 문제 3. 배열 변환 (Reshape)

```python
arr = np.arange(12)
matrix = arr.reshape(3, 4)
print(matrix)
```


<br>

---

<br>

## 7.3.4. 문제 4. 브로드캐스팅

```python
matrix = np.array([[1, 2], [3, 4]])
result = matrix + 10
print(result)
# [[11 12]
#  [13 14]]
```


<br>

---

<br>

## 7.3.5. 문제 5. 불리언 인덱싱 (필터링)

```python
scores = np.array([55, 88, 92, 70, 65, 82])

# 마스크 생성 (80점 이상)
mask = scores >= 80

# 필터링
high_scores = scores[mask]
print(high_scores)
# 출력: [88 92 82]
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: (내용 채우기)
*   **[핵심 2]**: (내용 채우기)
*   **[핵심 3]**: (내용 채우기)
