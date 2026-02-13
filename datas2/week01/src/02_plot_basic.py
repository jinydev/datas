# 02_plot_basic.py
import matplotlib.pyplot as plt

# 4. Python 문법 집중: 주석
# 주석은 코드의 의도를 설명하는 중요한 도구입니다.

# 9. 사각형 그리기
# x좌표와 y좌표를 분리해서 리스트로 만듭니다.
# 순서: 좌하단 -> 좌상단 -> 우상단 -> 우하단 -> 좌하단
x_square = [1, 1, 2, 2, 1]
y_square = [1, 2, 2, 1, 1]

# 15. Python 문법 집중: 함수의 인자
plt.figure(figsize=(6, 6)) # figsize는 키워드 인자입니다.

# 사각형 그리기 (마커와 색상 지정)
plt.plot(x_square, y_square, marker='s', color='blue', label='Square')

# 19. 응용 예제: 집 그리기
# 지붕 (삼각형)
x_roof = [1, 1.5, 2]
y_roof = [2, 2.8, 2] # 사각형보다 위에 위치 (y > 2)
plt.plot(x_roof, y_roof, marker='^', color='red', label='Roof')

# 꾸미기
plt.title("A Simple House Construction")
plt.xlabel("Width")
plt.ylabel("Height")
plt.grid(True)
plt.legend() # 범례 표시

# 비율을 맞추기 위해 축 범위 고정
plt.xlim(0.5, 2.5)
plt.ylim(0.5, 3.5)

plt.show()
