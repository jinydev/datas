---
layout: numpy
title: "4.12.4 기초 시각화 연동"
---

# 4.12.4 파이썬 그래프 시각화 맛보기

데이터를 숫자로만 보는 것을 넘어 `matplotlib`을 이용해 시각화하는 기초 연습을 해봅니다.

---

## 📝 [문제]

> **문제 9 (시각화 연동)** 
> 시험 점수가 `[80, 90, 70, 60, 100]`인 5명의 학생 데이터가 있습니다. matplotlib을 활용하여 이 데이터를 **막대그래프(Bar Plot)**로 그리고, 제목을 "Math Scores"로 띄워보세요.

<br><br><br>

*(정답은 충분히 고민한 후 아래로 스크롤하세요!)*

<br><br><br>

---

## 🎯 [정답 및 해설]

### [문제 9 정답]
넘파이와 Matplotlib 라이브러리는 사실상 한 몸처럼 같이 붙어 다니는 바늘과 실 같은 존재입니다. 배열 인덱싱 과정을 거쳐 정제된 데이터는 흔히 이렇게 시각화 도구로 전달됩니다.
```python
import matplotlib.pyplot as plt

scores = [80, 90, 70, 60, 100]
students = ['A', 'B', 'C', 'D', 'E'] # X축 그룹 라벨용

plt.bar(students, scores)
plt.title("Math Scores")
plt.show()
```
