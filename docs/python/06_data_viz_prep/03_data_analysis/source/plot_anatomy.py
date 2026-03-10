import matplotlib.pyplot as plt

# 1. 가상의 데이터 마트 (리스트 구조)
days = [1, 2, 3, 4, 5]
prices = [100, 110, 105, 120, 135]

# 2. 도화지(fig)와 1개의 액자(ax) 생성
# figsize=(6, 4)는 가로 세로 비율을 뜻함
fig, ax = plt.subplots(figsize=(6, 4)) 

# 3. 그림 붓칠하기 (점 o를 찍고, 색은 빨간색 점선으로)
ax.plot(days, prices, marker='o', color='red', linestyle='--')

# 4. 차트 꾸미기기 제목, 라벨 붙이기
ax.set_title("My First Growth Chart")
ax.set_xlabel("Days progressing")
ax.set_ylabel("Power Level")

# 5. 화면에 차트 윈도우 띄우기!
print("터미널: 차트 창 윈도우가 열렸습니다. 확인해 보세요.")
plt.show() 
print("터미널: 차트 윈도우가 닫혔습니다. 프로그램 종료.")
