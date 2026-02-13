# 1주차 3강: 바이브 코딩 실습 - 막대그래프 (Bar Chart)
# 파일명: 02_bar_chart.py

import matplotlib.pyplot as plt

# [Vibe Coding 요청]
# "요일별 커피 판매량(월: 50, 화: 60, 수: 55, 목: 70, 금: 90)을 막대그래프로 그려줘. 색상은 커피색으로 해줘."

# 1. 데이터 정의
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
sales = [50, 60, 55, 70, 90]

# 2. 막대그래프 그리기 (Bar Chart)
# color='brown': 막대 색상을 갈색(커피색)으로 지정
plt.bar(days, sales, color='brown')

# 3. 그래프 제목 및 축 레이블 설정
plt.title("Coffee Sales by Day")  # 제목
plt.xlabel("Day")                 # X축 레이블 (요일)
plt.ylabel("Sales")               # Y축 레이블 (판매량)

# 4. 출력
plt.show()
