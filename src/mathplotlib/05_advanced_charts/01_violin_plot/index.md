---
layout: mathplotlib
title: "5.5.1 바이올린 플롯"
---

# 5.5.1 바이올린과 상관관계 시각화

## 5.5.1 바이올린 플롯

### ① 바이올린 개요와 함수 violinplot()

**[비유로 이해하기: 박스 플롯 + 밀도 추정 곡선]**
박스 플롯이 데이터의 "통계적 요약(최소/최대/중앙값)"을 단단한 상자로 보여준다면, **바이올린 플롯(Violin Plot)**은 거기에 더해 "데이터가 실제 어디에 뚱뚱하게 뭉쳐있는지" 그 부드러운 곡선(KDE)까지 한눈에 보여주는 강력한 차트입니다. `split=True` 옵션을 쓰면 두 집단을 반반씩 합쳐서 등 맞대고 비교하기 좋습니다.

바이올린 플롯(violin plot)은 상자그림(boxplot)에 데이터 분포의 밀도를 보다 구체적으로 표현하는 방법이다. 바이올린 플롯은 분포 밀도(kernel density)를 좌우 대칭의 항아리 모양으로 그리는 방식으로 데이터의 분포를 표현한다. 패키지 `numpy`의 함수 `np.random.randn(d0, d1, ..., dn)`는 평균이 0, 표준 편차가 1인 정규분포에 대한 난수(random number)를 차원 (d0, d1, ..., dn) 배열을 생성한다.

다음으로 평균이 0, 표준편차가 1인 정규분포 난수 5개를 확인한다. 난수이므로 실행할 때마다 값이 다르다.

```python
import numpy as np
np.random.randn(5)
```

다음 코드는 2행 3열의 6개 난수를 생성한다.

```python
np.random.randn(2, 3)
```

다음은 함수 `violinplot()`으로 정규분포 난수 2000개로 바이올린을 그린 결과이다. 바이올린 플롯은 항아리 모양의 너비로 분포의 밀도를 나타내고 4분위수의 박스 상자를 내부에 그리는 방식이다.

```python
data = np.random.randn(2000)
plt.violinplot(data);
```

다음 인자 `vert=False`를 사용해 바이올린을 가로로 그릴 수 있다. 인자 `quantiles=[.25, .5, .75]`로 사분위수에 선을 그을 수 있다.

```python
plt.violinplot(data, quantiles=[.25, .5, .75], vert=False);
```

### ② 패키지 seaborn의 함수 sns.violinplot()

바이올린을 위해 패키지 `seaborn`의 `violinplot()`을 사용할 수도 있다. `sns.stripplot(data, color='palegreen')`을 사용하면 이미 그린 바이올린 플롯에 데이터 분포를 추가할 수 있다.

```python
import seaborn as sns
sns.violinplot(data, color='gold');
sns.stripplot(data, color='palegreen');
```

붓꽃 데이터 `iris`에서 품종 `Species`에 따라 꽃받침 길이 `Sepal.Length`의 바이올린 플롯을 그려보자. 함수 `sns.violinplot()`에서 인자 `x='Species'`, `y='Sepal.Length'`, `hue='Species'`를 사용하면 품종에 따라 색상이 달라진다.

```python
from pydataset import data
iris = data('iris')

import seaborn as sns
sns.violinplot(data=iris, x='Species', y='Sepal.Length', hue='Species');
```

다음 코드 `legend='full'`을 지정해 그림 위에 범례를 추가한다.

```python
sns.violinplot(data=iris, x='Species', y='Sepal.Length', hue='Species', legend='full');
```