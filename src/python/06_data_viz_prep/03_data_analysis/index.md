---
layout: python
title: "3.6.3 데이터 분석 실습 (Matplotlib 맛보기)"
---

# 3.6.3 데이터 분석 실습 (Matplotlib 맛보기)

## 학습목표
앞서 배운 파이썬의 핵심 3대장 (제어문, 리스트, 그리고 파일 `open()`)을 총동원하여 미니 데이터 분석을 수행합니다. 내 하드디스크에 저장된 `sales.csv` 매출 데이터를 가져와 파이썬 리스트로 정제한 뒤, 데이터 시각화의 꽃인 **`Matplotlib`** 차트로 띄워보는 황홀한 경험을 해봅니다.

---

## 💡 TL;DR (1분 핵심 요약): 하드디스크에서 예쁜 차트까지

1. **파일 읽기 (`open`)**: `sales.csv` 파일을 스트림으로 엽니다.
2. **데이터 파싱 (`split`)**: 엑셀의 한 줄(문자열)을 쪼개서 `[일자, 매출액]` 두 덩어리 숫자로 변환하고 리스트에 쌓습니다.
3. **도화지 깔기 (`plt.subplots()`)**: 텅 빈 거대한 캔버스(`Figure`) 위에 차트를 그릴 액자 영역(`Axes`)을 배정합니다.
다음 코드를 실행하기 전에, VS Code 하단 터미널을 열어 1차 시각화 라이브러리인 `matplotlib`을 반드시 설치해야 합니다. 파이썬은 이런 모듈을 쉽게 깔 수 있는 `pip` 라는 훌륭한 앱스토어를 가지고 있습니다.

```bash
python -m pip install matplotlib
```

데이터가 7줄짜리이므로 가볍게 파이썬 기본 기능(`open`)으로 읽어보겠습니다.
4. **그림 그리기 (`ax.plot`)**: 리스트를 들이부어 아름다운 꺾은선(Plot) 차트를 생성합니다.

---

## 1. 뼈대 잡기: 화가와 도화지 (Figure & Axes)

하드디스크에서 데이터를 긁어왔다면, 이제 그림을 그려야 합니다. `Matplotlib`이 그리는 방식을 완벽히 이해해 봅시다.

![Matplotlib Anatomy Webtoon](./img/matplotlib_anatomy_webtoon.png)

*(웹툰 비유: 화면 왼쪽에는 좌표 픽셀을 일일이 C언어 코드로 찍느라 땀을 삐질삐질 흘리는 학생이 있습니다. 오른쪽에는 'Matplotlib' 베레모를 쓴 프로 학생이 상단에 거대한 빈 캔버스(`Figure`)를 이젤에 올려놓고, 그 위에 예쁜 눈금자가 쳐진 차트 프레임(`Axes`)을 딱! 붙인 뒤 여유롭게 붓(`plot`)을 들고 데이터를 슥슥 문지르고 있습니다.)*

*   코딩을 할 때 항상 "먼저 도화지(`Figure`)를 깔고, 그 위에 차트 한 장(`Axes`)을 올린다!"라고 속으로 되뇌어야 합니다.

---

## 2. 통합 실습: CSV 읽어서 차트 띄우기

**사전 준비 (터미널)**: 가상환경을 켜고 `pip install matplotlib` 패키지를 설치해야 그래프 마법을 부릴 수 있습니다. 그리고 같은 위치에 아래의 `sales.csv` 샘플 데이터 파일이 있어야 합니다.

### [가상 데이터: `sales.csv`]
```csv
Day,Sales
1,100
2,110
3,105
4,120
5,135
6,180
```

### [파이썬 스크립트: 데이터 분석과 시각화]

<img src="./img/matplotlib_vs_java_plot.svg" width="100%">

```python
import matplotlib.pyplot as plt

days = []
sales = []

# 1. 파일 열어 데이터 읽어오기 (안전한 with 파이프)
with open("sales.csv", "r", encoding="utf-8") as f:
    header = f.readline() # 첫 번째 줄(Day,Sales 헤더)은 숫자 연산을 못하니 날려버림
    
    # 2. 파일의 끝까지 한 줄씩 읽기 (for 루프의 폭탄 세일)
    for line in f:
        # 공백 제거 후 쉼표(,) 쪼개기 -> ['1', '100'] 배열 탄생
        row = line.strip().split(',') 
        
        # 문자를 숫자로 형변환(Casting)하여 리스트 비커에 조심스럽게 담기
        days.append(int(row[0]))
        sales.append(int(row[1]))

# 3. 도화지(fig)와 액자(ax) 한 번에 생성하기 (마법의 문법)
fig, ax = plt.subplots(figsize=(6, 4))

# 4. 액자 위에 리스트 들이붓고 그림 그리기 (Plot)
# marker: 점 / color: 선 색 / linestyle: 점선
ax.plot(days, sales, marker='o', color='red', linestyle='--')

# 5. 차트 화장하기
ax.set_title("1 Week Sales Analysis")
ax.set_xlabel("Day")
ax.set_ylabel("Sales ($)")

# 6. 완성된 캔버스 화면에 대공개!
plt.show() 
```

---

## ☕ Java vs 🐍 Python 스나이퍼 대결

### 데이터 파일 파싱부터 시각화까지의 험난함 차이
*   **Java**: 파일 하나를 한 줄씩 쪼개려면 `BufferedReader`부터 시작해서 `while(readline() != null)` 루프를 돌고, `Integer.parseInt` 하다 에러나면 또 `try-catch`를 발라야 합니다. 거기에 외부 시각화 패키지(`JFreeChart`)를 엎으면 `DataSet` 도메인을 생성하고 50줄의 인터페이스 지옥에 빠져 허우적거리다 차트 보기도 전에 수강생의 멘탈이 깨집니다.
*   **Python (`Matplotlib`)**: 위 예제처럼, 기본 내장함수 `open`에 `split()` 하나 얹어 던지면 파싱이 끝납니다. 그리고 그 파싱된 파이썬 순정 리스트를 그대로 `ax.plot()` 함수 입속으로 곧바로 다이렉트로 집어던져버리면 차트가 렌더링 됩니다. 이 미칠듯한 호환성과 짧은 코드가 파이썬이 데이터 분석계를 천하 통일한 이유입니다.

---

## 🎧 Vibe Coding

> **🗣️ 학생 프롬프트 (AI에게 이렇게 피드백해보세요):**
> "방금 썼던 파이썬 시각화 코드에서 꺾은선 그래프 아래 빈 공간을 빨간색 투명한 물감으로 꽉 채워서 색칠해진 면적 그래프(Area chart)처럼 만들고 싶어! `ax.fill_between()` 이라는 함수를 써야 할 것 같은데 수정해 줘."

---

## 코딩 영단어 학습 📝

*   **Parse (파싱)**: 구문 분석, 뜯어고치다. (하나의 거대하고 더러운 텍스트 문자열 데이터 덩어리(`"1,100\n"`)를 컴퓨터 시스템이 씹어 넘길 수 있도록 가치 있는 숫자나 변수 형태(`1`, `100`)로 해체하고 소화하는 전처리 작업을 뜻합니다.)
*   **Figure (피겨)**: 도면, 공간, 전체 도화지. (Matplotlib 세계관에서 모든 차트들을 품는 가장 거대한 캔버스 윈도우 창 그 자체를 부르는 말입니다. 흔히 `fig`로 줄여 씁니다.)
*   **Axes (액시즈)**: Axis(축)의 복수형. (단순한 선반이 아니라, `X-Y` 이중 축 레이더를 가지고 있어 데이터를 실질적으로 그려내는 '진짜 차트 영역 액자' 전체를 지칭합니다. 흔히 `ax` 로 줄여 쓰며 파이썬 객체지향 시각화의 99%를 차지합니다.)
