---
layout: home
title: "10주차 6강: 파이썬 GUI 프로그래밍 (Tkinter)"
---

# 10주차 6강: 파이썬 GUI 프로그래밍 (Tkinter)

> **학습목표**: 파이썬 기본 내장 라이브러리인 **Tkinter**를 사용하여 마우스로 클릭할 수 있는 **윈도우 프로그램**을 만들어 봅니다. 분석한 데이터를 친구에게 보여줄 때, 검은 화면(터미널)보다는 윈도우 창이 훨씬 멋지겠죠?

## 10.6.1. 첫 번째 윈도우 만들기

`tkinter`는 파이썬을 설치하면 같이 설치되는 표준 라이브러리입니다.

```python
import tkinter as tk

# 1. 메인 윈도우 생성
root = tk.Tk()
root.title("나의 첫 GUI 프로그램")
root.geometry("300x200") # 가로x세로 크기

# 2. 메인 루프 실행 (창이 꺼지지 않게 계속 돌림)
root.mainloop()
```

<br>

---

<br>

## 10.6.2. 위젯(Widget) 배치하기

화면을 구성하는 부품을 **위젯**이라고 합니다. 라벨(글자), 버튼, 입력창 등이 있습니다.

### 1. 라벨(Label)과 버튼(Button)
가장 기본이 되는 위젯입니다. `pack()`을 사용하면 위에서 아래로 차곡차곡 쌓입니다.

```python
import tkinter as tk

def on_click():
    print("버튼이 클릭되었습니다!")
    label.config(text="클릭 완료!") # 라벨 내용 바꾸기

root = tk.Tk()
root.geometry("300x200")

# 라벨 만들기
label = tk.Label(root, text="안녕하세요!")
label.pack()

# 버튼 만들기 (command에 실행할 함수 연결)
btn = tk.Button(root, text="누르세요", command=on_click)
btn.pack()

root.mainloop()
```

### 2. 입력창(Entry)과 레이아웃(Grid)
사용자에게 글자를 입력받을 때는 `Entry`를 씁니다.
`pack()` 대신 `grid()`를 쓰면 엑셀처럼 행(row)과 열(column) 번호로 위치를 잡을 수 있습니다.

```python
import tkinter as tk

root = tk.Tk()

# 0행 0열: 라벨
tk.Label(root, text="이름:").grid(row=0, column=0)

# 0행 1열: 입력창
entry = tk.Entry(root)
entry.grid(row=0, column=1)

# 1행 0열: 버튼 (columnspan=2는 두 칸을 합친다는 뜻)
tk.Button(root, text="확인").grid(row=1, column=0, columnspan=2)

root.mainloop()
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: `Tk()`로 창을 만들고 `mainloop()`로 실행하여 윈도우 프로그램을 띄웁니다.
*   **[핵심 2]**: `Label`(글자), `Button`(클릭), `Entry`(입력) 등의 **위젯**을 조합하여 화면을 구성합니다.
*   **[핵심 3]**: `pack()`(단순 쌓기)이나 `grid()`(격자 배치) 같은 **레이아웃 매니저**를 사용해 위젯의 위치를 정합니다.
