# 9-2. 날짜와 시간 다루기 (Datetime)

## 1. 컴퓨터에게 시간 가르쳐주기
"2024-01-01"은 사람 눈에는 날짜지만, 컴퓨터에게는 그저 문자열(String)입니다.
계산(예: 어제 날짜 구하기)을 하려면 **Datetime** 형식으로 바꿔줘야 합니다.

## 2. pd.to_datetime
마법의 함수입니다. 문자열을 시간 객체로 바꿔줍니다.

```python
import pandas as pd
df['date'] = pd.to_datetime(df['date_string'])
```

## 3. 날짜에서 정보 뽑아내기
Datetime 형식이 되면 연/월/일/요일을 쉽게 뽑을 수 있습니다.
*   `dt.year`
*   `dt.month`
*   `dt.day_name()`

## 4. [응용 예제] 요일 맞추기
여러분의 생년월일을 입력하면 무슨 요일인지 알려주는 코드를 작성해봅시다.

[소스 코드 실행하기](src/02_datetime.py) | [Colab에서 열기](src/02_datetime.ipynb)
