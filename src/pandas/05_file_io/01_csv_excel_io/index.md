---
layout: pandas
title: "6.5.1 csv와 엑셀 파일 활용"
---

# 6.5.1 외부 파일 활용

## 6.5.1 csv와 엑셀 파일 활용

### ① 다양한 파일 읽기

판다스는 다양한 데이터 파일(csv, excel, sql, json, parquet 등)을 읽어오고 쓰는 방식을 제공한다. 각 파일 형식에 맞는 접미사가 붙는 함수 `read_*()`와 `to_*()`를 제공한다. 즉, 함수 `pd.read_excel()`과 `pd.to_excel()` 등으로 간편히 엑셀 파일의 입출력이 가능하다.

![다양한 형식 입출력 함수](img/page_016.jpg)

### ② 유명한 타이타닉 파일 읽기와 쓰기

판다스는 excel 파일로 저장된 데이터를 판다스의 데이터프레임으로 읽어오는 `read_excel()`을 제공한다.

다음은 타이타닉 파일 `titanic.xlsx`을 읽어오는 코드이다. 내용의 처음과 마지막을 생략하고 있다.

```python
import pandas as pd

titanic = pd.read_excel("data/titanic.xlsx")
print(titanic)
```

함수 `head()`로 처음 5행을 표시한다.

```python
titanic.head()
```

함수 `tail()`로는 마지막 5행을 표시할 수 있다.

```python
titanic.tail()
```

속성 `dtypes`는 각 열에 대한 자료형을 알 수 있다. 정수는 `int64`, 실수는 `float64`, 문자열은 `object`로 표시된다.

```python
titanic.dtypes
```

다음 함수 `info()`로 14개의 열과 1309개의 행이 있음을 확인할 수 있다. 또한, non-null 값의 수와 자료형을 알 수 있다.

```python
titanic.info()
```

### ③ csv 파일로 쓰기와 읽기

**[비유로 이해하기: CSV는 데이터 분석의 표준 포맷]**
**CSV (Comma Separated Values)**는 데이터가 쉼표(,)로 구분된 단순한 텍스트 파일입니다. 엑셀 파일보다 가볍고 호환성이 뛰어나 수천만 건의 데이터를 주고받을 때 사실상의 **표준(Standard)**으로 쓰입니다. 파일로 내보낼 때 `index=False` 옵션을 주면, 의미 없는 숫자 인덱스(0, 1, 2...)가 저장되는 것을 막을 수 있습니다.

다음 `to_csv()` 함수로 작업하던 데이터프레임을 콤마로 자료를 구분하는 파일 `titanic.csv`에 저장할 수 있다. 다음은 타이타닉 데이터프레임을 다시 CSV 파일로 저장하는 코드이다.

```python
titanic.to_csv("data/titanic.csv")
```

저장된 파일 `titanic.csv`를 다시 `read_csv()` 함수로 읽어와 데이터프레임 `tt`에 저장해 보자. 다음 코드 `tt.head(8)`로 데이터프레임에서 위 8개의 행을 출력하자.

```python
tt = pd.read_csv("data/titanic.csv")
tt.head(8)
```

다음으로 데이터프레임의 전체 행과 열 정보를 파악할 수 있다.

```python
tt.info()
```