# 02_lists.py
import matplotlib.pyplot as plt

# 2. 리스트의 도입
grades_sem1 = [85, 90, 88, 75, 92]

# 5. 인덱싱
print(f"첫 시험 점수: {grades_sem1[0]}")
print(f"마지막 시험 점수: {grades_sem1[-1]}")

# 11. 데이터 추가 (보너스 시험)
grades_sem1.append(95)
print(f"업데이트된 성적: {grades_sem1}")

# 15. range() 함수 활용
# 성적 개수만큼 주차(Week) 자동 생성
weeks = list(range(1, len(grades_sem1) + 1))
print(f"시험 주차: {weeks}")

# 13. 리스트 시각화
plt.figure(figsize=(8, 4))
plt.plot(weeks, grades_sem1, marker='o', label='1학기')

# 17. 리스트 병합 (시뮬레이션)
grades_sem2 = [80, 85, 90]
all_grades = grades_sem1 + grades_sem2
all_weeks = list(range(1, len(all_grades) + 1))

plt.plot(all_weeks, all_grades, linestyle='--', color='gray', label='전체 흐름(예측)')

plt.title("Academic Performance Trend")
plt.xlabel("Week")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.ylim(0, 100)
plt.show()
