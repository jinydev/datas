# 1주차 3강: 바이브 코딩 실습 - 원 그래프 (Pie Chart)
# 파일명: 04_pie_chart.py

import matplotlib.pyplot as plt

# [Vibe Coding 요청]
# "우리 반 좋아하는 과일 비율(사과, 바나나, 딸기, 포도)을 원 그래프로 그려줘. 비율 퍼센트도 표시해줘."

# 1. 데이터 정의
fruits = ['Apple', 'Banana', 'Strawberry', 'Grape']
votes = [30, 20, 35, 15]

# 2. 원 그래프 그리기 (Pie Chart)
# autopct='%1.1f%%': 비율을 소수점 첫째 자리까지 %로 표시하라는 옵션입니다.
plt.pie(votes, labels=fruits, autopct='%1.1f%%')

# 3. 제목 설정
plt.title("Favorite Fruits")

# 4. 출력
plt.show()
