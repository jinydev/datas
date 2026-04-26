import tkinter as tk

root = tk.Tk()
root.title("Layout 비교")
root.geometry("300x250")

# 1. pack() 방식: 마트료시카 블록처럼 위에서 아래로 중앙 정렬 쑤셔 넣기
tk.Label(root, text="--- Pack 배열 ---").pack()
tk.Button(root, text="버튼 1-1").pack()
tk.Button(root, text="버튼 1-2").pack()

# 2. grid() 방식: 정교하게 엑셀 행(Row)과 열(Column) 셀 나누기
tk.Label(root, text="--- Grid 배열 ---").pack(pady=(20, 0)) # 여백 꼼수

# 별도의 뼈대 프레임(투명한 액자)을 만들고, 그 안에 그리드를 칩니다.
frame = tk.Frame(root) 
frame.pack()

tk.Label(frame, text="ID:").grid(row=0, column=0)
tk.Entry(frame).grid(row=0, column=1) # 글자를 입력받는 빈칸

tk.Label(frame, text="PW:").grid(row=1, column=0)
tk.Entry(frame).grid(row=1, column=1)

root.mainloop()
