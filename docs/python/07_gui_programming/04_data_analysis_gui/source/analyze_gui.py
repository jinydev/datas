import tkinter as tk
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------
# 1. 핵심 비즈니스 로직 (데이터 읽고 차트 그리기 함수)
# ---------------------------------------------------------
def analyze_and_show_chart():
    days = []
    sales = []

    # 현재 파일 위치에서 sales.csv 찾기 (파일 I/O)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "sales.csv")

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            f.readline() # 헤더 버리기
            for line in f:
                row = line.strip().split(',')
                days.append(int(row[0]))
                sales.append(int(row[1]))
    except FileNotFoundError:
        # 파일이 없으면 라벨에 에러 메시지를 띄우는 GUI 피드백!
        lbl_status.config(text="🚨 에러: sales.csv 파일을 찾을 수 없습니다!", fg="red")
        return # 함수 강제 종료

    # 여기까지 무사히 왔다면 차트 그리기 (Matplotlib)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(days, sales, marker='o', color='blue', linestyle='-')
    ax.set_title("Sales Analysis Data")
    ax.set_xlabel("Day")
    ax.set_ylabel("Sales ($)")
    
    # GUI 라벨 업데이트 및 차트 팝업 띄우기
    lbl_status.config(text="✅ 분석 완료! 차트가 별도 창으로 생성되었습니다.", fg="blue")
    plt.show() 

# ---------------------------------------------------------
# 2. GUI 화면 설계 로직 (Tkinter 껍데기)
# ---------------------------------------------------------
root = tk.Tk()
root.title("내 인생 첫 데이터 분석 앱")
root.geometry("400x200") # 가로상자 크게

# 타이틀 라벨 (팩 레이아웃으로 중앙 정렬)
lbl_title = tk.Label(root, text="🚀 파이썬 원클릭 데이터 분석기", font=("Arial", 16, "bold"))
lbl_title.pack(pady=(20, 10))

# 상태 알림 라벨 (이벤트가 터지면 글씨가 바뀔 곳)
lbl_status = tk.Label(root, text="버튼을 눌러 분석을 시작하세요.", font=("Arial", 10))
lbl_status.pack(pady=5)

# 실행 버튼 (command에 위의 거대한 분석 함수를 장전!)
btn_run = tk.Button(root, text="📊 데이터 읽어오기 및 차트 보기", 
                    font=("Arial", 12),
                    bg="#4CAF50", fg="white", # 버튼 색상 꾸미기
                    command=analyze_and_show_chart)
btn_run.pack(pady=20)

# 심장 박동(무한 대기 루프) 시작
root.mainloop()
