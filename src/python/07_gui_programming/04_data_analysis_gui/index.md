---
layout: python
title: "3.7.4 미니 프로젝트: CSV 데이터를 GUI로 띄우기"
---

# 3.7.4 미니 프로젝트: CSV 데이터를 GUI로 띄우기

## 학습목표
지금까지 배운 파이썬의 핵심 3대장 기술을 하나로 융합하는 최종 보스급 미니 프로젝트입니다. 
1) **파일 I/O (`open()`)** 기술로 `sales.csv` 파일을 읽어 리스트로 가공하고, 
2) **데이터 시각화 (`Matplotlib`)** 기술로 차트를 그려낸 다음, 
3) 이 모든 결과를 **GUI 프로그래밍 (`Tkinter`)** 창 위에 버튼과 함께 아름답게 띄워 넣는 완벽한 통합 애플리케이션을 완성해 봅니다.

---

## 💡 TL;DR (1분 핵심 요약): 3종 신기의 결합

1. 순수 파이썬의 검은색 터미널 창을 벗어나, "결과 보기" 웹 버튼이 달린 번듯한 윈도우 UI(Tkinter)를 먼저 만듭니다.
2. 사용자가 버튼을 누르면(`command=`), 숨겨두었던 데이터 분석 함수가 발동합니다.
3. 함수는 하드디스크의 `.csv` 파일을 열고 파싱하여 `Matplotlib`으로 차트를 생성해 화면에 팝업시킵니다!

---

## 1. 프로젝트 아키텍처 (어떻게 합칠 것인가?)

자바(Java)였다면 이 세 가지(버튼UI, 파일읽기, 차트그리기)를 합치기 위해 수십 개의 클래스 파일과 아키텍처 설계가 필요했을 것입니다. 하지만 파이썬에서는 이 모든 것이 단일 `.py` 파일 안에서 함수 블록(`def`) 하나로 우아하게 통일됩니다.

우리는 윈도우 창(`Tk()`)을 먼저 하나 띄워놓고, 그 안에 커다란 버튼을 하나 박아둘 것입니다. 그리고 이 버튼의 전선(`command`)을 방금 전 데이터 분석 챕터(`06_data_viz_prep`)에서 배웠던 차트 생성 함수에 곧바로 연결해버리면 끝입니다!

---

## 2. 통합 애플리케이션 코드

> **🚨 (필수) 패키지 설치 안내**
> 파이썬 기본 내장 모듈인 `tkinter`와 달리, `matplotlib`은 외부 시각화 라이브러리입니다. 코드를 실행하기 전 VS Code 하단 터미널을 열고 아래 명령어로 패키지를 먼저 설치해 주셔야 합니다.
> ```bash
> python -m pip install matplotlib
> ```

*이 코드를 실행하려면 `sales.csv` 파일이 같은 폴더에 있어야 하며, 오류가 날 경우 위 명령어로 `matplotlib`을 설치해 주세요.*

```python
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
                days.append(int(row[0]))   # [1, 2, 3...]
                sales.append(int(row[1]))  # [100, 110, 105...]
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
```

---

## 3. 코드 해부: 파이썬의 무서운 실전 압축력

위 코드는 불과 40여 줄에 불과하지만, 현업에서 쓰이는 **"데이터 파이프라인 + 프론트엔드 버튼 + 백엔드 처리(시각화)"** 아키텍처의 필수 요소를 모두 갖추고 있습니다.

1.  **UI 렌더링**: `tk.Tk()` 와 `pack()`을 통해 클라이언트 모니터에 시각적인 조종석을 제공합니다.
2.  **예외 처리 연동**: 파일이 없을 경우 무식하게 터미널에 에러를 뱉고 뻗는 것이 아니라, `try-except` 블록을 통과하면서 `lbl_status.config()`라는 GUI 함수를 조종해 사용자에게 시각적으로 "🚨 에러가 났습니다"라고 예쁘게 알려줍니다. (완전한 상용 프로그램의 디테일)
3.  **이벤트 모듈화**: `command=analyze_and_show_chart` 단 한 줄로, 버튼 위젯이라는 빈 껍데기가 거대한 데이터 분석 머신으로 탈바꿈했습니다.

---

## ☕ Java vs 🐍 Python 스나이퍼 대결

자바 개발자라면 위 40줄짜리 파이썬 코드를 자바로 구현하기 위해 머릿속에 수많은 패키지 분리를 상상했을 것입니다.

*   `Swing` / `JavaFX` 로 UI 프레임워크 객체 작성 (100줄 이상)
*   사용자 버튼 클릭을 감지하는 `ActionListener` 와 쓰레드 분리 설계
*   `FileReader`, `BufferedReader` 로 CSV 파싱 객체 구현 (50줄 구조)
*   `JFreeChart` 등에 데이터셋 주입하기 위해 `while` 루프 돌리며 DTO 변환 (50줄 구조)
*   **결과**: 자바로는 파일 3~4개가 쪼개어지고 총 300줄이 넘어가는 숨 막히는 프로젝트가 되어버리지만, **파이썬은 단일 흐름의 절차지향적 코딩으로 프론트와 백엔드 로직이 40줄에 우아하게 결합**됩니다.

---

## 🎧 Vibe Coding

> **🗣️ 학생 프롬프트 (AI에게 이렇게 명령해 보세요):**
> "파이썬 `Tkinter`를 써서 내가 방금 짠 데이터 분석 프로그램에 기능을 추가해줘!
> 지금은 버튼이 한 개인데, 이 버튼 옆에 텍스트 입력칸(`Entry`) 창을 하나 뚫어줘. 그리고 내가 거기에 'sales2.csv' 처럼 어떤 파일 이름을 치고 분석 버튼을 누르면, 코드가 입력칸에서 그 이름을 읽어와서(`get()`) 그 이름에 맞는 파일 데이터를 분석하게 동적인 기능을 가진 GUI로 뜯어고쳐 줘."

---

## 코딩 영단어 학습 📝

*   **Integration (인티그레이션)**: 통합, 결합. (따로따로 노는 A, B, C의 부품을 엮어 하나의 시스템으로 완성하는 것을 뜻합니다. 여기서는 GUI 인프라 위에서 파일 읽기와 그래프 그리기를 인티그레이션(통합)했습니다.)
*   **Pipeline (파이프라인)**: 정보 전달의 관. (원유를 나르는 송유관처럼, 하드디스크의 텍스트 한 줄이 코드를 타고 들어와 -> 리스트로 변형되고 -> 마지막엔 차트 이미지로 출력되는 이 일련의 컨베이어 벨트 처리 과정을 '데이터 파이프라인'이라 부릅니다.)
*   **Try / Except (트라이/익셉트)**: 예외 처리 덫. (파일이 없거나 데이터가 꼬여 프로그램이 강제 폭발하는 것을 막기 위해 쳐놓는 덫입니다. 에러가 나면 팅기지 않고 사용자의 화면 라벨을 예쁜 빨간 글씨로 바꿔주어 고객 경험(UX)을 극대화합니다.)
