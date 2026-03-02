---
layout: pandas
title: "6.5.2 인터넷 자료 활용"
---

# 6.5.2 인터넷 자료 활용

**[실전 꿀팁]: 웹(URL) 데이터와 클립보드 바로 읽기**
- **URL에서 바로 읽기**: 인터넷 주소(URL)만 알면 파일을 다운로드할 권한 없이 `pd.read_csv("https://...")` 형태로 바로 데이터를 로드할 수 있습니다. (예: GitHub Raw 데이터 등)
- **클립보드 읽기**: 엑셀이나 웹페이지의 표를 마우스로 드래그해서 `Ctrl+C` (복사) 한 뒤, 파이썬에서 `pd.read_clipboard()`를 실행하면 마법처럼 데이터프레임이 생성됩니다. 급하게 표 데이터를 테스트할 때 매우 유용합니다.
- **한글 인코딩**: 공공데이터 포털 등에서 받은 CSV 파일을 열 때 글자가 깨지면, `encoding='cp949'` 또는 `encoding='euc-kr'` 옵션을 주면 깔끔하게 해결됩니다.

### ① 인터넷 자료의 파일 읽기와 쓰기

```python
import pandas 상 pd

traffic = pd.read_csv("data/2022년도시도별교통사고.csv", encoding='cp949')
print(traffic)
```

다음처럼 csv 파일의 첫 행에 제목이 있고 다음 행에 열 제목이 있으므로 위 코드로는 열 명을 맞게 지정할 수 없다.

![2022년도시도별교통사고.csv 파일 내용](img/page_021.jpg)

다음 코드와 같이 키워드 인자 `skiprows=1`을 지정하면 위에서 첫 행을 무시하고 읽으므로 정상적으로 열 명이 지정된 데이터프레임에 저장할 수 있다. 데이터프레임 `traffic`의 인덱스는 자동으로 `RangeIndex`인 0부터 차례대로 순번이 붙는다.

```python
traffic = pd.read_csv("data/2022년도시도별교통사고.csv", encoding='cp949', skiprows=1)
print(traffic)
```

다음처럼 `index_col=0`을 지정하면 인덱스 레이블이 기본 정수가 아닌 첫 열 '시도'를 인덱스 레이블로 지정한 데이터프레임을 얻을 수 있다.

```python
traffic = pd.read_csv("data/2022년도시도별교통사고.csv", encoding='cp949', skiprows=1, index_col=0)
traffic.head()
```

**주의:** `traffic.info()`를 보면 수에 콤마가 붙은 수를 정수로 인식하지 못하고 문자열로 인식해 열의 자료형이 `object`로 표시되는 것을 볼 수 있다.

```python
traffic.info()
```

다음처럼 간편하게 `thousands=','`를 지정하면 간단히 콤마 `,`가 붙은 수를 수로 읽어 데이터프레임에 저장할 수 있다.

```python
import pandas as pd

traffic = pd.read_csv("data/2022년도시도별교통사고.csv", encoding='cp949', skiprows=1, index_col=0, thousands=',')
traffic.head()
```

이제 `info()`를 보면 모든 열의 자료형이 `int64`인 것을 알 수 있다.

```python
traffic.info()
```

다음 `traffic.describe()`로 모든 열의 기초 통계량을 확인할 수 있다.

```python
traffic.describe()
```

### ② 데이터프레임의 간편한 데이터 시각화

패키지 `seaborn`을 활용해 간편히 데이터 시각화가 가능하다. 다음 코드는 패키지 `seaborn`의 `sns.barplot()`을 사용해 세로 막대그래프를 그릴 수 있다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

sns.barplot(traffic)
plt.show()
```

다음 코드 `traffic[['사망자수(명)']].T`로는 '사망자수(명)'의 행과 열을 바꾼 데이터프레임을 반환한다. 이를 `sns.barplot()`의 인자로 사용하면 '사망자수(명)'를 시도 지역별로 막대그래프를 그릴 수 있다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(traffic[['사망자수(명)']].T)
plt.show()
```

다음 코드 `sns.barplot(traffic[[traffic.columns[0]]].T)`과 같이 `traffic.columns[0]`인 '사고건수(건)'의 행과 열을 바꿔 '사고건수(건)'를 시도 지역별로 막대그래프를 그릴 수 있다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(traffic[[traffic.columns[0]]].T)
plt.show()
```

다음 코드 `sns.barplot(traffic[[traffic.columns[2]]].T)`과 같이 `traffic.columns[2]`인 '부상자수(명)'의 행과 열을 바꿔 '부상자수(명)'을 시도 지역별로 막대그래프를 그릴 수 있다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(traffic[[traffic.columns[2]]].T)
plt.show()
```