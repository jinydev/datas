---
layout: python
title: "3.8 GUI 프로그래밍 (Tkinter)"
---

# 3.8 파이썬 기초 활용

## 8. 파이썬 GUI 프로그래밍 (Tkinter)

파이썬 기본 내장 라이브러리인 **Tkinter**를 사용하여 마우스로 클릭할 수 있는 **윈도우 프로그램**을 만들어 봅니다. 분석한 데이터를 친구에게 보여주거나 고객용 툴을 만들 때, 검은 화면(터미널)보다는 윈도우 UI 창이 훨씬 대중적이고 멋집니다.

### 첫 번째 윈도우 만들기

`tkinter`는 별도의 `pip` 설치 없이 파이썬을 설치하면 같이 설치되는 막강한 표준 라이브러리입니다.

```python
import tkinter as tk

# 3.8 메인 윈도우 생성
root = tk.Tk()
root.title("나의 첫 GUI 프로그램")
root.geometry("300x200") # 가로x세로 해상도 크기

# 3.8 메인 루프 실행 (사용자가 X 버튼을 눌러 창이 꺼질 때까지 계속 대기하며 돌림)
root.mainloop()
```

### 위젯(Widget) 배치하기

화면을 구성하는 개별적인 부품을 **위젯**이라고 합니다. 글자를 띄우는 라벨, 클릭 가능한 버튼, 텍스트 입력창 등이 있습니다.

**1. 라벨(Label)과 버튼(Button)**
가장 기본이 되는 상태 위젯입니다. `pack()` 함수를 사용하면 요소들이 화면에서 위에서 아래로 차곡차곡 중앙에 쌓입니다.

```python
import tkinter as tk

def on_click():
    print("터미널: 버튼이 클릭되었습니다!")
    label.config(text="클릭 완료!") # GUI 화면의 라벨 내용 바꾸기

root = tk.Tk()
root.geometry("300x200")

# 3.8 라벨 만들기
label = tk.Label(root, text="안녕하세요!")
label.pack()

# 3.8 버튼 만들기 (command 매개변수에 버튼 클릭 시 실행할 함수를 연결)
btn = tk.Button(root, text="누르세요", command=on_click)
btn.pack()

root.mainloop()
```

**2. 입력창(Entry)과 레이아웃(Grid)**
사용자에게 글자를 직접 입력받을 때는 `Entry`를 씁니다.
화면 구조가 복잡해지면 `pack()` 대신 `grid()`를 쓰는 것이 좋습니다. `grid()`는 액셀 시트처럼 격자 모양의 2차원 행(row)과 열(column) 좌표 번호를 잡아 직관적으로 위치를 잡을 수 있습니다.

```python
import tkinter as tk

root = tk.Tk()

# 3.8 행 0열: "이름:" 라벨 작성
tk.Label(root, text="이름:").grid(row=0, column=0)

# 3.8 행 1열: 글자 입력창 작성
entry = tk.Entry(root)
entry.grid(row=0, column=1)

# 3.8 행 0열: 확인 버튼 생성 (columnspan=2 옵션 지정 시 두 칸 분량을 가로로 쫙 합침)
tk.Button(root, text="확인").grid(row=1, column=0, columnspan=2)

root.mainloop()
```
