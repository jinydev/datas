# 2주차 2강: 선 그래프 그리기 (Simple -> Styled)
# 파일명: 02_line_plot_progressive.py

import matplotlib.pyplot as plt

# 공통 데이터
time = [0, 1, 2, 3, 4, 5]
mp = [100, 80, 60, 40, 20, 0]

# ---------------------------------------------------------
# [단계 1] 간단한 선 차트 (Simple)
# ---------------------------------------------------------
plt.figure() # 캔버스(Window) 생성
plt.plot(time, mp)
plt.show()

# ---------------------------------------------------------
# [단계 2] 스타일 꾸미기 (Styled)
# ---------------------------------------------------------
# 그래프 크기 설정 (가로 8, 세로 5)
plt.figure(figsize=(8, 5))

# 색상(color), 마커(marker), 선 스타일(linestyle), 라벨(label) 설정
plt.plot(time, mp, color='purple', marker='o', linestyle='--', label='Mana Point')

# 제목 및 축 이름 설정 (폰트 크기 조절)
plt.title("Time vs Mana (Battle)", fontsize=15)
plt.xlabel("Time (sec)", fontsize=12)
plt.ylabel("Mana Point", fontsize=12)

# 부가 요소
plt.grid(True)  # 격자
plt.legend()    # 범례

plt.show()
