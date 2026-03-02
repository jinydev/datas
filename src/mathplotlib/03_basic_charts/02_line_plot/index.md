---
layout: mathplotlib
title: "5.3.2 선 그리기"
---

## 5.3.2 선 그리기

#### ① 선 그리기 함수 plot()

함수 `plot()`으로 간단히 지정한 좌표를 지나는 선을 그릴 수 있다. 선 종류는 인자 `linestyle` 또는 간단히 `ls`로 지정할 수 있다.

> `plot([x], y, linestyle="-", ...)` 인자: `linestyle="-"`는 실선(solid line) 표시

다음은 인자 하나인 y축의 값을 지정한 연결선 그림이다. x축 자료가 6개이므로 지정하지 않은 x축은 기본으로 0에서 5까지가 된다.

```python
import matplotlib.pyplot as plt
plt.plot(range(10, 16));
```

다음은 x 값 -5에서 5까지의 그래프 $y = x^2$을 그린 그림이다. x축에서 이웃한 좌표의 거리를 0.1로 지정해서 그린다. 0.1을 더 작게 하면 곡선이 더 부드러워진다. 실수의 배열을 위해 `numpy`의 `arange()` 함수를 활용한다. 인자 `ls`는 `linestyle`과 같으며 `":"`은 점선(dotted line)이다.

```python
import numpy as np

x = np.arange(-5, 5.1, 0.1)
plt.plot(x, x**2, ls=":");
plt.xlabel('$x$') # 레이블에서 앞 뒤의 $는 레이텍(LaTex) 형식의 수식으로 표현한다
plt.ylabel('$y = x^2$');
```

내장 데이터 `AirPassengers`는 1949년부터 1960년까지 월별 국제선 승객 자료이다.

```python
airpsngr = data('AirPassengers')
airpsngr.info()
```

데이터 `AirPassengers`는 `time`과 `AirPassengers`로 구성된 데이터프레임이다.

```python
airpsngr.head()
```

데이터프레임 `airpsngr`에서 x축은 연도별 시간 `airpsngr.time`이며 y축은 승객 수인 `airpsngr.AirPassengers`이다. 그래프를 통해 국제선 승객 성장 추세를 바로 알 수 있다.

```python
plt.plot(airpsngr.time, airpsngr.AirPassengers, color='darkgreen');
plt.xlabel('연도')
plt.ylabel('승객수');
```

#### ② 함수 plot()의 패러미터 linestyle과 marker

함수 `plt.plot(x, y, linestyle='-')`에서 `linestyle`(간단히 `ls`)은 선 종류를 지정하는 패러미터이다. 지정하지 않으면 기본적으로 선 종류는 실선인 `'-'`이다.

**[표 9-1] 함수 plot()의 선 종류 패러미터 linestyle**

| 선 스타일 이름           | linestyle 값 | 선 스타일 기호 | 예제 코드                        |
| :----------------------- | :----------- | :------------- | :------------------------------- |
| 실선(Solid line)         | `'-'`        | ─              | `plt.plot(x, y, linestyle='-')`  |
| 대시선(Dashed line)      | `'--'`       | - -            | `plt.plot(x, y, linestyle='--')` |
| 점선(Dotted line)        | `':'`        | · ·            | `plt.plot(x, y, linestyle=':')`  |
| 대시 점선(Dash-dot line) | `'-.'`       | - ·            | `plt.plot(x, y, linestyle='-.')` |

다음 코드로 함수 `plot`의 4가지 선 종류의 `linestyle`을 확인할 수 있다.

```python
import matplotlib.pyplot as plt

# 5.3.2 데이터 준비
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [2, 4, 6, 8]
y3 = [3, 6, 9, 12]
y4 = [4, 8, 12, 16]

# 5.3.2 선 스타일별로 그래프 그리기
plt.plot(x, y1, linestyle='-', label='Solid line')    # 실선
plt.plot(x, y2, linestyle='--', label='Dashed line')  # 대시선
plt.plot(x, y3, linestyle=':', label='Dotted line')   # 점선
plt.plot(x, y4, linestyle='-.', label='Dash-dot line') # 대시 점선

# 5.3.2 그래프 제목과 축 레이블
plt.title("Line Styles in Matplotlib")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# 5.3.2 범례 추가
plt.legend()

# 5.3.2 그래프 보여주기
plt.show()
```

Matplotlib의 `plt.plot()` 메소드를 사용할 때 마커(marker)를 사용하여 각 데이터 포인트를 강조할 수 있다. 마커는 데이터 포인트를 시각적으로 더 쉽게 구분할 수 있게 해준다. 마커의 종류는 다음의 다양한 마커 기호로 인자 `marker`에 지정한다.

**[표 9-2] 마커 종류 인자 marker**

| 마커 이름                  | marker 값 | 마커 기호 | 예제 코드                    |
| :------------------------- | :-------- | :-------- | :--------------------------- |
| 점 (Point)                 | `'.'`     | ·         | `plt.plot(x, y, marker='.')` |
| 원 (Circle)                | `'o'`     | ●         | `plt.plot(x, y, marker='o')` |
| 삼각형 하 (Triangle_down)  | `'v'`     | ▼         | `plt.plot(x, y, marker='v')` |
| 삼각형 상 (Triangle_up)    | `'^'`     | ▲         | `plt.plot(x, y, marker='^')` |
| 삼각형 우 (Triangle_right) | `'>'`     | ▶         | `plt.plot(x, y, marker='>')` |
| 삼각형 좌 (Triangle_left)  | `'<'`     | ◀         | `plt.plot(x, y, marker='<')` |
| 사각형 (Square)            | `'s'`     | ■         | `plt.plot(x, y, marker='s')` |
| 다이아몬드 (Diamond)       | `'D'`     | ◆         | `plt.plot(x, y, marker='D')` |
| 육각형 (Hexagon)           | `'h'`     | ⬣         | `plt.plot(x, y, marker='h')` |
| 별 (Star)                  | `'*'`     | ★         | `plt.plot(x, y, marker='*')` |
| 십자 (Plus)                | `'+'`     | +         | `plt.plot(x, y, marker='+')` |
| 곱하기 (X)                 | `'x'`     | x         | `plt.plot(x, y, marker='x')` |

다음은 5가지 마커를 사용한 코드이다.

```python
import matplotlib.pyplot as plt

# 5.3.2 데이터 준비
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [2, 3, 4, 5]
y3 = [2, 2, 3, 3]
y4 = [3, 1, 4, 2]
y5 = [4, 5, 6, 8]

# 5.3.2 그래프 그리기
plt.plot(x, y1, marker='o', label='Circle') # 원
plt.plot(x, y2, marker='^', label='Triangle_up') # 삼각형 위
plt.plot(x, y3, marker='s', label='Square') # 사각형
plt.plot(x, y4, marker='*', label='Star') # 별
plt.plot(x, y5, marker=',', label='Pixel') # 픽셀

# 5.3.2 그래프 제목과 축 레이블
plt.title("Marker Styles in Matplotlib")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# 5.3.2 범례 추가
plt.legend()

# 5.3.2 그래프 보여주기
plt.show()
```

다음 함수 `plot()`에서 인자 `ls=' '`, `marker='o'`는 `scatter()`와 유사한 그림을 그릴 수 있다. 인자 `ls=' '` 또는 `ls=''`로 지정하면 선이 없이 마커만 표시할 수 있다.

```python
plt.plot(range(1, 5), range(5, 9), ls=' ', marker='o')
plt.show()
```

이미 알아본 기니피그의 치아성장 세포 데이터 `ToothGrowth`에서 사용되는 비타민 C의 종류로는 오렌지 주스(OJ)와 아스코르브산(VC)이 있다. 이 자료 값은 변수 `tg.supp`에 저장된다. 다음으로 비타민 C의 종류가 각각 "VC"와 "OJ"인 행 중에서 열 `dose`와 `len`으로 구성된 데이터프레임을 추출한다.

```python
vc = tg[tg.supp == 'VC'][['len', 'dose']]
oj = tg[tg.supp == 'OJ'][['len', 'dose']]
```

위 자료에서 비타민 C의 "VC" 자료인 `vc`를 사용해 열 `dose`, `len`에 따른 산점도를 그린다. 인자 `lw`(line width)는 선의 굵기를 지정한다. 인자 `label`에 지정한 글자는 범례에 사용된다.

```python
plt.plot(vc.dose, vc.len, color='cyan', marker='o', label="아스코르브산(VC)", lw=.7)
```

위 그림 위에 비타민 C의 "OJ" 자료로 다시 산점도를 그릴 수 있다. 선과 점을 모양을 바꿔 그려보자. 다음 함수 `plt.legend()`를 사용해 범례를 그린다. 범례 위치는 자동으로 지정된다.

```python
plt.plot(vc.dose, vc.len, color='cyan', marker='o', label="아스코르브산(VC)", lw=.7)
plt.plot(oj.dose, oj.len, color='deeppink', marker='*', ls=':', label="오렌지 주스(OJ)", lw=.7, alpha=.5)

plt.title("기니피그의 비타민과 치아성장 관계")
plt.xlabel("비타민 용량")
plt.ylabel("치아성장 세포길이")
plt.legend();
```

범례 위치는 `loc=(x좌표, y좌표)`로 범례의 좌측 상단 모서리 위치를 좌표로 지정할 수 있다. 그러므로 범례 위치는 자유롭게 조정할 수 있다.

```python
plt.plot(vc.dose, vc.len, color='cyan', marker='o', label="아스코르브산(VC)", lw=.7)
plt.plot(oj.dose, oj.len, color='deeppink', marker='*', ls=':', label="오렌지 주스(OJ)", lw=.7, alpha=.5)

plt.title("기니피그의 비타민과 치아성장 관계")
plt.xlabel("비타민 용량")
plt.ylabel("치아성장 세포길이")
plt.legend(loc='lower right');
```

범례 위치를 간단히 지정하는 인자 `loc`의 값은 다음과 같다. 인자 `loc`을 지정하지 않으면 `best`와 같다.

**[표 9-3] 범례의 위치 지정 패러미터 loc 종류**

| 위치 이름    | loc 값           | 예제 코드                        |
| :----------- | :--------------- | :------------------------------- |
| Best         | `'best'`         | `plt.legend(loc='best')`         |
| Upper right  | `'upper right'`  | `plt.legend(loc='upper right')`  |
| Upper left   | `'upper left'`   | `plt.legend(loc='upper left')`   |
| Lower left   | `'lower left'`   | `plt.legend(loc='lower left')`   |
| Lower right  | `'lower right'`  | `plt.legend(loc='lower right')`  |
| Right        | `'right'`        | `plt.legend(loc='right')`        |
| Center left  | `'center left'`  | `plt.legend(loc='center left')`  |
| Center right | `'center right'` | `plt.legend(loc='center right')` |
| Lower center | `'lower center'` | `plt.legend(loc='lower center')` |
| Upper center | `'upper center'` | `plt.legend(loc='upper center')` |
| Center       | `'center'`       | `plt.legend(loc='center')`       |

#### ③ Seaborn을 활용한 선 그래프 (lineplot)

시간의 흐름에 따른 변화(시계열)를 볼 때 유용합니다. Seaborn의 `lineplot`은 같은 x값에 여러 y값이 존재하면 **자동으로 평균선과 투명한 신뢰구간(그림자)** 영역을 그려주는 매우 강력한 기능을 가지고 있습니다.

```python
import seaborn as sns

# 5.3.2 Seaborn 내장 예제 데이터
fmri = sns.load_dataset("fmri") 

# 5.3.2 hue='event': 사건별로 선 색깔 다르게, style='event': 사건별로 선 모양(실선/점선) 다르게
sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event", style="event")
plt.title("시간에 따른 fMRI 신호 변화")
plt.show()
```