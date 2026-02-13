# 05_coordinates.py
import matplotlib.pyplot as plt

# 데이터
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 100] # 마지막에 이상치(Outlier) 존재

# 13. 서브플롯 활용
plt.figure(figsize=(10, 5))

# 그래프 1: 자동 스케일 (기본값)
plt.subplot(1, 2, 1)
plt.plot(x, y, marker='o')
plt.title("1. Auto Scaled")
plt.grid(True)

# 그래프 2: 수동 한계 설정
plt.subplot(1, 2, 2)
plt.plot(x, y, marker='o', color='red')
plt.title("2. Manually Limited (0-10)")
# 4. 한계 설정
plt.ylim(0, 10) # 100이라는 이상치를 화면에서 잘라냄
# 10. 텍스트 추가
plt.text(4, 9, "Outlier Hidden!", color='red')

plt.show()

# 19. 응용 예제: 축 직접 그리기
plt.figure(figsize=(6, 6))

# X축, Y축을 검은 선으로 직접 그리기
plt.axhline(0, color='black', linewidth=2) # y=0 수평선
plt.axvline(0, color='black', linewidth=2) # x=0 수직선

# 다이아몬드 모양 그리기 (원을 흉내)
circle_x = [1, 0, -1, 0, 1]
circle_y = [0, 1, 0, -1, 0]

plt.plot(circle_x, circle_y, 'b--')

# 5. 균등 비율
# 이 설정이 없으면 다이아몬드가 찌그러져 보일 수 있음
plt.axis('equal') 
plt.title("Center Origin (0,0)")
plt.grid(True, linestyle=':')
plt.show()
