import tkinter as tk

# 1. 메인 윈도우(도화지) 생성
root = tk.Tk() 
root.title("나의 첫 GUI 프로그램") # 창의 상단 타이틀 바 이름 지정
root.geometry("300x200")       # 창의 가로x세로 해상도 크기

# 2. 위젯(글자 스티커) 만들어서 도화지에 붙이기
label = tk.Label(root, text="Hello, GUI World!", font=("Helvetica", 16))
label.pack() # 윈도우 화면 정중앙 최상단에 위에서부터 블록처럼 배치

# 3. 메인 루프 (심장) 작동 시작! 
# 주의: 사용자가 X(닫기) 버튼을 누를 때까지 코드가 여기서 멈춰서 기다립니다.
print("터미널: 윈도우 창이 켜졌습니다. (창을 닫을 때까지 프로그램은 종료되지 않습니다)")
root.mainloop() 

print("터미널: 윈도우 창이 닫혔습니다. 프로그램 종료.")
