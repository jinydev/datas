---
layout: mathplotlib
title: "5.4.1 상자그림"
---

# 5.4.1 상자그림과 히스토그램

## 5.4.1 상자그림

### ① 상자그림 그리기 함수 boxplot()

데이터의 분포 값을 알 수 있도록 메소드 `quantile([0., .25, .50, .75, 1])`를 사용해 변수 `mtc.mpg`의 사분위수를 알 수 있다.

```python
from pydataset import data

mtc = data('mtcars')
mtc.mpg.quantile([0., .25, .50, .75, 1])
```
물론 다음으로도 간단히 사분위수를 알 수 있다.

```python
mtc.mpg.describe()[3:]
```

상자그림(boxplot)은 데이터의 대략적인 분포와 개별적인 이상치들을 동시에 보여줄 수 있는 차트(chart)이다. 또한, 서로 다른 그룹의 분포를 쉽게 비교할 수 있도록 도와주는 시각화 기법으로 가장 널리 쓰이는 시각화 형태이다. 상자그림은 상자수염그림이라고도 부른다.

다음 `boxplot(mtc.mpg)`는 변수 `mtc.mpg`와 사분위수에서 Q1, Q2, Q3를 상자로 표현하는 상자그림을 그릴 수 있다.

```python
import matplotlib.pyplot as plt

plt.boxplot(mtc.mpg)
plt.show()
```

물론 다음처럼 열 `mpg`에 속한 `plot.box`로도 간단히 상자그림을 그릴 수 있다.

```python
mtc.mpg.plot.box();
```

### ② 이상값 outlier

**[실전 꿀팁]: 이상치(Outlier) 사냥꾼, 박스 플롯**
박스 플롯(Box Plot)은 한가운데 박스 안에 데이터의 중심 50%가 모여 있다는 것을 직관적으로 보여줍니다. 특히 수염(Whisker) 바깥으로 벗어난 점(o)들은 정상 범위를 훌쩍 벗어난 **이상치(Outlier)**일 확률이 높기 때문에, 데이터 전처리 단계에서 튀는 값을 찾아낼 때 가장 먼저 그려보는 필수 차트입니다.

함수 `boxplot([mtc.disp, mtc.hp])`를 사용하여 변수 `disp`(배기량)와 `hp`(마력)의 분포를 동시에 알 수 있도록 상자그림을 함께 그릴 수 있다.

```python
import numpy as np
plt.boxplot([mtc.disp, mtc.hp])

plt.title("배기량과 마력 상자그림(boxplot)")
plt.xticks(ticks=np.arange(1, 3), labels=["배기량", "마력"])

plt.show()
```

위 변수 `hp`의 상자그림에서 맨 위의 o 표시는 이상값(outlier)을 나타낸다. 이상값이란 박스상자의 위나 아래에서 박스상자의 길이의 1.5배 이상 떨어져 있는 매우 크거나 작은 특이한 값을 말한다. 데이터 분석에서 이상값의 처리가 매우 중요하므로 최대나 최소 값 밖으로 표시한다.

다음처럼 데이터프레임의 메소드 `plot()`으로도 간단히 상자그림을 그릴 수 있다.

```python
mtc[['disp', 'hp']].plot(title="배기량과 마력 비교(boxplot)", kind='box')

plt.xticks(ticks=np.arange(1, 3), labels=["배기량", "마력"])
plt.show()
```