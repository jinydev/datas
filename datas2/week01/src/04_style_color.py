# 04_style_color.py
import matplotlib.pyplot as plt
import numpy as np # 데이터 생성을 위해 Numpy를 잠시 사용

# 데이터 준비
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]

# 15. 그림 크기
plt.figure(figsize=(8, 5))

# 3. & 4. 색상 (이름 vs Hex)
# 6. & 7. 선 스타일
plt.plot(x, y1, color='red', linestyle='--', linewidth=2, label='Growth')
plt.plot(x, y2, color='#33FF57', linestyle='-.', linewidth=3, label='Decay')

# 8. 마커 커스터마이징
plt.plot([3], [9], marker='o', ms=15, mfc='yellow', mec='black', label='Intersection')

# 16. 축 범위 제한
plt.xlim(0, 6)
plt.ylim(0, 30)

# 17. 레이블 스타일링
plt.title("Styled Growth vs Decay", fontsize=16, fontweight='bold')
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Velocity (m/s)", fontsize=12)

# 13. 범례
plt.legend(loc='upper center')

# 10. 투명도
plt.grid(True, alpha=0.3)

plt.show()

# 19. 응용 예제: 하트 그리기
t = np.linspace(0, 2*np.pi, 100)
x_heart = 16 * np.sin(t)**3
y_heart = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

plt.figure(figsize=(6, 6))
plt.plot(x_heart, y_heart, color='hotpink', linewidth=4, alpha=0.8)
plt.fill(x_heart, y_heart, color='pink', alpha=0.3) # 내부 채우기
plt.title("Mathematical Heart", color='purple')
plt.axis('equal') # 비율 유지
plt.show()
