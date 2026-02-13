import matplotlib.pyplot as plt
import seaborn as sns

# 데이터: 연도별 판매량
years = [2020, 2021, 2022, 2023]
sales = [100, 120, 150, 180]

# 1. 나쁜 그래프 (Matplotlib Default)
# 축 이름도 없고, 제목도 없고, 선만 띡 있음
plt.figure(figsize=(4, 3))
plt.plot(years, sales)
plt.show()

# 2. 좋은 그래프 (Seaborn Style)
# 그리드, 스타일, 명확한 라벨링
sns.set_theme(style="whitegrid") # 배경에 그리드 추가

plt.figure(figsize=(4, 3))
sns.lineplot(x=years, y=sales, marker='o', linewidth=3, color='green')
plt.title("Yearly Sales Growth", fontsize=15)
plt.xlabel("Year")
plt.ylabel("Sales (Units)")
plt.xticks(years) # x축 눈금 정수로 딱딱 끊기
plt.show()
