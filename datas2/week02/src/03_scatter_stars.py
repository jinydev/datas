# 03_scatter_stars.py
import matplotlib.pyplot as plt
import random

# 8. 데이터의 무작위성
# 50개의 별 데이터를 생성 (리스트 내포 사용)
# 가상의 우주 공간 좌표
x = [random.randint(0, 100) for _ in range(50)]
y = [random.randint(0, 100) for _ in range(50)]

# 4. 크기를 차원으로 (별의 밝기)
sizes = [random.randint(10, 200) for _ in range(50)]

# 5. 색상을 차원으로 (별의 온도)
colors = [random.randint(0, 100) for _ in range(50)]

plt.figure(figsize=(8, 6))

# 2. scatter() 함수 활용
# 15. 컬러맵 (plasma: 불꽃/별 느낌)
sc = plt.scatter(x, y, s=sizes, c=colors, cmap='plasma', alpha=0.7)

# 16. 컬러바
plt.colorbar(sc, label='Temperature (Kelvin)')

plt.title("Galaxy Star Map Simulation")
plt.xlabel("Light Years (X)")
plt.ylabel("Light Years (Y)")

# 13. 그룹별 시각화 (특정 행성 추가)
# 지구 기지를 별도로 표시
plt.scatter([50], [50], s=500, c='blue', marker='*', label='Earth Base')

plt.grid(True, linestyle=":", color='gray')
plt.legend()
plt.show()
