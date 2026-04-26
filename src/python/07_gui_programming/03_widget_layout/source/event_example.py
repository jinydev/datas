import tkinter as tk

# 동작할 함수 (총알) 미리 장전!
def force_on_click():
    # 사용자가 버튼을 클릭하면, 이 회로로 전기가 흐르며 함수 발동!
    print("터미널: 앗! 찌릿찌릿! 버튼이 클릭되었습니다!")
    
    # GUI 화면의 라벨 내용을 강제 수정
    label_status.config(text="🔥 미사일 발사 완료! 🔥", fg="red") 

root = tk.Tk()
root.geometry("300x150")

# 1. 라벨 만들기 (처음 상태)
label_status = tk.Label(root, text="현재 평화로운 멍때림 상태...", font=("Arial", 12))
label_status.pack(pady=20)

# 2. 버튼 만들기 (command=force_on_click)
# 절대 주의: 함수명 뒤에 괄호를 치는 순간 프로그램이 뜨기도 전에 미리 실행됨
btn = tk.Button(root, text="빨간 버튼을 누르지 마시오", command=force_on_click)
btn.pack()

root.mainloop()
