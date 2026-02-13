# 06_initials_lab.py
import matplotlib.pyplot as plt

# 1. 캔버스 설정
plt.figure(figsize=(10, 6))

# 4. 'M' 설계
# (0,0) -> (0,10) -> (5,5) -> (10,10) -> (10,0)
mx = [0, 0, 5, 10, 10]
my = [0, 10, 5, 10, 0]

# 12. 'M' 그리기
plt.plot(mx, my, color='navy', linewidth=8, marker='o', mfc='white', label='M')

# 7. 오프셋 정의
offset = 12 # 글자 사이 간격

# 9. 'A' 설계 (텐트 모양 메인)
# (0,0) -> (5, 10) -> (10, 0) + offset
ax_main = [0 + offset, 5 + offset, 10 + offset]
ay_main = [0, 10, 0]

# 14. 'A' 메인 그리기
plt.plot(ax_main, ay_main, color='crimson', linewidth=8, marker='o', mfc='white', label='A')

# 14. 'A' 가로 획 그리기
# (2.5, 5) -> (7.5, 5) + offset
ax_cross = [2.5 + offset, 7.5 + offset]
ay_cross = [5, 5]

plt.plot(ax_cross, ay_cross, color='crimson', linewidth=8)

# 16. 비율 고정
plt.axis('equal')

# 17. 문맥 추가
plt.title("Vectorized Project: M.A.", fontsize=20, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()

# 디자인을 위해 눈금 제거
plt.xticks([])
plt.yticks([])

plt.show()
