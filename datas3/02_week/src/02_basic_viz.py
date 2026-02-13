# 2주차 2강: 기본 그래프 그리기
# 파일명: 02_basic_viz.py

import matplotlib.pyplot as plt

# 데이터 준비
weight = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
power =  [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]

# 그래프 크기 설정 (가로 10인치, 세로 6인치)
plt.figure(figsize=(10, 6))

# 산점도 그리기
# c='red': 색상 빨강
# alpha=0.5: 투명도 50%
plt.scatter(weight, power, c='red', alpha=0.5, s=100) # s=100: 점 크기

# 꾸미기
plt.title("Weapon Weight vs Power", fontsize=16)
plt.xlabel("Weight (kg)", fontsize=12)
plt.ylabel("Power", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7) # 격자 추가

plt.show()
