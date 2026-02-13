import matplotlib.pyplot as plt

# 1. 시각화 핵심 복습
x = [1, 2, 3]
y = [10, 20, 15]

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Line', linestyle='--')
plt.scatter(x, y, color='red', label='Point', s=100)
plt.title("Summary Plot")
plt.legend()
plt.grid(True)
plt.show()

# 2. [응용 예제] 성적 등급 시각화
scores = [65, 90, 85, 45, 95, 100, 70, 88]
ids = range(len(scores)) # 0 ~ 7번 학생

# 색상 리스트 만들기
colors = []
for s in scores:
    if s >= 90:
        colors.append('blue') # 우등생
    else:
        colors.append('gray') # 일반

plt.figure(figsize=(8, 4))
plt.bar(ids, scores, color=colors)
plt.axhline(90, color='red', linestyle=':', label='Cutline (90)')
plt.title("Student Scores (Blue >= 90)")
plt.xlabel("Student ID")
plt.ylabel("Score")
plt.legend()
plt.show()
