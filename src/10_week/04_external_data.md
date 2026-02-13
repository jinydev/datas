---
layout: default
title: "10주차 4강: 외부 데이터 활용하기 (External Data)"
---

# 10주차 4강: 외부 데이터 활용하기 (External Data)

> **학습목표**: 내 컴퓨터에 파일이 없어도 웹(URL)에서 바로 데이터를 가져오거나, 엑셀에서 복사한 데이터를 클립보드에서 바로 읽어오는 실전 꿀팁을 배웁니다.

## 10.4.1. 웹에서 바로 읽기 (URL)

인터넷 주소(URL)만 알면 파일을 다운로드할 필요 없이 `read_csv`로 바로 읽을 수 있습니다. GitHub에 있는 예제 데이터를 쓸 때 매우 유용합니다.

```python
import pandas as pd

# GitHub Raw 데이터 주소
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

# 바로 읽기
df = pd.read_csv(url)
print(df.head())
```

<br>

---

<br>

## 10.4.2. 클립보드 읽기 (`read_clipboard`)

엑셀이나 웹페이지의 표를 드래그해서 `Ctrl+C` (복사) 한 뒤, 파이썬에서 바로 데이터프레임으로 만들 수 있습니다. **급하게 데이터를 테스트해볼 때 마법 같은 기능입니다.**

1.  엑셀이나 웹에서 표 영역을 복사합니다.
2.  아래 코드를 실행합니다.

```python
# 복사한 내용이 이미 클립보드에 있다고 가정
df_clip = pd.read_clipboard()

print(df_clip)
```

<br>

---

<br>

## 10.4.3. 한글 인코딩 문제 해결

한국 공공데이터 포털 등에서 받은 CSV 파일을 열면 글자가 `` 처럼 깨지는 경우가 많습니다. 이는 인코딩 방식(UTF-8 vs CP949)이 다르기 때문입니다.

이럴 땐 `encoding` 옵션을 사용해 보세요.

```python
# 기본 (UTF-8)로 읽었는데 깨진다면?
# 1. cp949 시도 (윈도우 엑셀 저장 방식)
df = pd.read_csv('korean_data.csv', encoding='cp949')

# 2. 그래도 안 되면 euc-kr 시도
df = pd.read_csv('korean_data.csv', encoding='euc-kr')
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: `read_csv`에 파일 경로 대신 **URL**을 넣으면 웹 데이터를 바로 로드할 수 있습니다.
*   **[핵심 2]**: `read_clipboard()`를 사용하면 복사/붙여넣기 신공으로 빠르게 데이터프레임을 만들 수 있습니다.
*   **[핵심 3]**: 한글이 깨질 때는 `encoding='cp949'` 옵션을 기억하세요.
