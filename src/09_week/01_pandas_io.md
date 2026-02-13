# 9주차 1강: 데이터 불러오기/저장하기 (I/O)

## 9.1.1. 파일 읽어오기 (`read_csv`)

> **CSV (Comma Separated Values)**: 쉼표(,)로 데이터가 구분된 텍스트 파일입니다. 가장 가볍고 호환성이 좋아 데이터 분석의 표준처럼 쓰입니다.


<br>

---

<br>

### 9.1.1.1. 파일 읽기 코드

```python
import pandas as pd

# titanic.csv 파일 읽어오기
df = pd.read_csv('titanic.csv')

# 잘 읽혔는지 확인
print(df.head())
```

> **참고**: Colab을 사용한다면 왼쪽 폴더 아이콘을 누르고 파일을 드래그해서 업로드해야 합니다.


<br>

---

<br>

## 9.1.2. 파일로 저장하기 (`to_csv`)

열심히 분석하고 전처리한 데이터를 날려버리면 안 되겠죠? 파일로 저장하는 법도 아주 간단합니다.

```python
# 전처리가 끝난 데이터
result_df = df.head(10) # 10개만 저장해 봅시다

# CSV 파일로 내보내기
# index=False: 앞에 붙은 0, 1, 2... 번호는 저장하지 않겠다 (보통 이렇게 씁니다)
result_df.to_csv('my_result.csv', index=False)
```


<br>

---

<br>

## 9.1.3. 엑셀 파일 다루기 (`read_excel`)

엑셀 파일도 읽을 수 있습니다. 단, `openpyxl` 라이브러리가 필요할 수 있습니다.

```python
# 엑셀 읽기
df_excel = pd.read_excel('data.xlsx')

# 엑셀 저장
df.to_excel('result.xlsx', index=False)
```

<br>

---

<br>

## 정리 (Summary)

이 강의에서 배운 핵심 내용을 요약해 봅시다.

*   **[핵심 1]**: (내용 채우기)
*   **[핵심 2]**: (내용 채우기)
*   **[핵심 3]**: (내용 채우기)
