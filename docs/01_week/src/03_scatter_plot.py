# 1주차 3강: 바이브 코딩 실습 - 산점도 (Scatter Plot)
# 파일명: 03_scatter_plot.py

import matplotlib.pyplot as plt
import random  # 랜덤 데이터를 만들기 위한 라이브러리

# [Vibe Coding 요청]
# "키(150~190)와 몸무게(50~100)의 상관관계를 보여주는 산점도를 그려줘. 데이터는 랜덤으로 50개 생성해."

# 1. 랜덤 데이터 생성 (List Comprehension 사용)
# 150부터 190 사이의 랜덤한 정수 50개 생성
heights = [random.randint(150, 190) for _ in range(50)]
# 50부터 100 사이의 랜덤한 정수 50개 생성
weights = [random.randint(50, 100) for _ in range(50)]

# 2. 산점도 그리기 (Scatter Plot)
# 두 변수 간의 관계(상관관계)를 볼 때 유용합니다.
plt.scatter(heights, weights)

# 3. 그래프 꾸미기
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")

# 4. 출력
plt.show()
