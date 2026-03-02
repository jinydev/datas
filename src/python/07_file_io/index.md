---
layout: python
title: "3.7 파일 입출력 (File I/O)"
---

# 3.7 파이썬 기초 활용

## 7. 파이썬 파일 입출력 (File I/O)

판다스를 쓰지 않고도 파이썬의 기본 기능만으로 텍스트 파일을 읽고 쓰는 방법을 익힙니다. 텍스트 로그를 시스템에 남기거나 간단한 설정 파일(.txt, .ini 등)을 다룰 때 필수적입니다.

### 파일 열고 닫기 (`open`, `close`)

파일을 다룰 때는 **'열기 -> 쓰기/읽기 -> 닫기'** 의 3단계를 꼭 지켜야 합니다.

*   `open(파일명, 모드)`: 파일을 엽니다.
*   `close()`: 파일을 닫습니다. (안 닫으면 파일이 깨지거나 메모리 누수가 발생할 수 있습니다!)

**주요 모드 (Mode)**
*   **`'w'` (Write)**: 쓰기 모드. 파일이 없으면 만들고, 있으면 **내용을 다 지우고 새로 씁니다.**
*   **`'r'` (Read)**: 읽기 모드. 파일이 없으면 에러가 납니다. (기본값)
*   **`'a'` (Append)**: 추가 모드. 기존 파일 내용 뒤에 **결과를 이어 씁니다.**

```python
# 3.7 파일 열기 (쓰기 모드)
f = open("hello.txt", "w", encoding="utf-8")

# 3.7 파일 쓰기
f.write("Hello, Python!\n")
f.write("파일 입출력 연습 중입니다.")

# 3.7 파일 닫기
f.close()
```

### 자동으로 닫아주는 `with` 문

매번 `close()`를 코드 밑에 쓰는 건 귀찮고 에러로 인해 도중에 종료되면 파일이 닫히지 않는 치명적인 단점이 있습니다. `with` 문을 쓰면 블록이 끝날 때 **알아서 안전하게 닫아줍니다.** (권장 방법)

```python
# 3.7 with 블록을 벗어나면 코드가 자동으로 f.close()를 대신 호출해줌
with open("hello.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)
```

### 파일 읽기 삼총사

**1. `read()`**
파일의 **모든 내용**을 하나의 거대한 문자열 덩어리로 통째로 읽어옵니다.

**2. `readline()`**
**한 줄만** 읽어옵니다. 파일 전체를 메모리에 올리지 않고 반복문과 함께 쓰면 메모리를 아끼며 수 기가바이트(GB)에 달하는 큰 파일을 처리할 수 있습니다.

```python
with open("hello.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line: break # 더 읽을 줄이 없으면 종료 (EOF)
        print(line.strip()) # 줄바꿈 문자(\n) 보이지 않게 제거
```

**3. `readlines()`**
모든 줄을 순서대로 읽어서 한 줄 한 줄을 아이템으로 삼아 전체를 **리스트(List)** 형태로 반환해줍니다. 데이터 줄 단위 처리가 편합니다.

```python
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines) 
    # ['Hello, Python!\n', '파일 입출력 연습 중입니다.']
```
