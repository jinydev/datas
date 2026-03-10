import matplotlib.pyplot as plt
import os

days = []
sales = []

# 현재 파이썬 파일의 위치 기준으로 sales.csv 경로 찾기 (실행 위치 무관하게 방어 코드)
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "sales.csv")

# 1. 파일 열어 데이터 읽어오기 (안전한 with 파이프)
try:
    with open(csv_path, "r", encoding="utf-8") as f:
        header = f.readline() # 첫 번째 줄(Day,Sales 헤더)은 숫자 연산을 못하니 날려버림
        
        # 2. 파일의 끝까지 한 줄씩 읽기 (for 루프의 폭탄 세일)
        for line in f:
            # 공백 제거 후 쉼표(,) 쪼개기
            row = line.strip().split(',') 
            
            # 문자를 숫자로 형변환(Casting)하여 리스트 비커에 조심스럽게 담기
            days.append(int(row[0]))
            sales.append(int(row[1]))
except FileNotFoundError:
    print("경고: sales.csv 파일을 찾지 못했습니다!")
    exit()

# 3. 도화지(fig)와 액자(ax) 한 번에 생성하기 (마법의 문법)
fig, ax = plt.subplots(figsize=(6, 4))

# 4. 액자 위에 리스트 들이붓고 그림 그리기 (Plot)
ax.plot(days, sales, marker='o', color='red', linestyle='--')

# 5. 차트 화장하기
ax.set_title("1 Week Sales Analysis")
ax.set_xlabel("Day")
ax.set_ylabel("Sales ($)")

# 6. 캔버스 화면에 대공개!
print("터미널: Matplotlib 차트 윈도우가 열렸습니다. (Matplotlib 패키지가 설치되어 있어야 함)")
plt.show() 
