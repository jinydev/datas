# 1주차 3강: 데이터 시각화 맛보기 (Line Plot)
# 파일명: 01_basic_plot.py

# 1. Matplotlib 라이브러리 불러오기
# 'plt'라는 별명으로 부르는 것이 관례입니다.
import matplotlib.pyplot as plt

# 2. 데이터 준비 (Data Preparation)
# X축: 순서 시간 (1~5)
# Y축: 값 (데이터)
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 40]

# 3. 그래프 그리기 (Plotting)
# plt.plot(): 선 그래프(Line Plot)를 그리는 함수입니다.
plt.plot(x, y)

# 4. 그래프 꾸미기 (Styling)
# 제목을 추가합니다.
plt.title("My First Plot")

# 5. 그래프 출력 (Show)
# 화면에 그래프를 보여줍니다.
plt.show()
