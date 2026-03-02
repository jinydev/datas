---
layout: mathplotlib
title: "5.2.4 seaborn으로 그래프 그리기"
---

# 5.2.4 seaborn으로 그래프 그리기

### ① seaborn 설치

다음 패키지 설치 명령 `pip install seaborn`으로 간단하게 설치할 수 있다.

```bash
!pip install seaborn
```

### ② 연비 데이터 그리기

다음은 연비 데이터 `mpg`를 로드한 데이터프레임이다.

```python
from pydataset import data
df_mpg = data('mpg')
print(df_mpg)
```

패키지 `seaborn`의 `sns`로 `sns.histplot(df_mpg['manufacturer'])`은 열 'manufacturer'인 자동차 생산 회사의 빈도수를 표시한다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df_mpg['manufacturer'])
plt.xticks(rotation=90)
plt.show()
```

다음 코드는 열 'displ'인 자동차 배기량(displacement)에 따른 빈도수를 표시한다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df_mpg['displ'])
plt.show()
```

다음 코드는 열 'hwy'인 고속도로 연비(highway miles per gallon)에 따른 빈도수를 표시한다.

```python
sns.histplot(df_mpg['hwy'])
plt.show()
```

다음 코드는 열 'cyl'인 자동차 엔진 실린더 수에 따른 빈도수를 표시한다.

```python
sns.histplot(df_mpg['cyl'])
plt.show()
```

다음 코드는 열 'year'인 자동차 생산 연도에 따른 빈도수를 표시한다.

```python
sns.histplot(df_mpg['year'])
plt.show()
```