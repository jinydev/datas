---
layout: docs
title: "03. figure와 서브플롯"
---

## 03. figure와 서브플롯

#### ① figure와 axes 개요

`matplotlib`에서 `figure`와 `axes`는 그래프를 생성하고 구성하는 데 중요한 역할을 하는 요소이다. 이 두 가지 개념을 자세히 알아보자.

전체 그림인 `Figure`는 그래프를 담는 캔버스나 종이 시트와 같이 생각할 수 있다. `Figure`는 그래프의 전체적인 레이아웃과 스타일을 관리한다. 하나의 `Figure` 객체에는 하나 이상의 `Axes` 객체가 포함될 수 있다. `Axes`는 `Figure` 내부에서 실제 그래프가 그려지는 영역을 나타낸다. `Axes`에는 x 축(axis)과 y 축(axis)이 있으며, 그래프의 데이터를 시각화하는 데 사용된다. 하나의 `Figure` 안에 여러 개의 `Axes`를 배치하여 서브플롯을 만들 수 있다. 정리해 보면 `figure`와 `axes` 구성 요소는 계층적 구조이다.

- **Figure 객체**: 전체 그림
- **Axes 객체(axes)**: Figure 객체에 속하며 시각화할 데이터를 추가하는 공간
- **Axis 객체**: Axes 객체에 속하는 축을 말하며, Axis는 다시 X Axis, Y Axis로 분류

다음 그림은 세 객체 `figure`와 `axes`, 그리고 `axis` 간의 계층적 관계를 보여준다.

![전체 종이인 figure와 부분 그림인 axes](img/page_012.png)

#### ② 서브플롯과 방법

`matplotlib`에서 서브플롯이란 하나의 `Figure`에 여러 개의 그래프를 동시에 그리는 레이아웃을 말한다. 여기에서는 서브플롯과 부분플롯이란 용어를 혼용해서 쓸 예정이다. `matplotlib`을 사용하면서 부분플롯을 만들어야 하는 상황이 생길 수 있다. 부분플롯을 그리는 방법으로 `plt.subplot()`과 `plt.subplots()`, 그리고 `fig.add_subplot()`이 주로 사용된다. 세 가지 방법으로 부분플롯을 그리는 간단한 코드와 결과를 확인해 보도록 하자.

- `plt.subplot()`
- `plt.subplots()`
- `fig.add_subplot()`

#### ③ 서브플롯 plt.subplot() 개요

다음은 `plt.subplot(m, n, index)`로 부분플롯을 그린 그림이다. `m`은 행의 수, `n`은 열의 수이며, `index`는 1부터 시작하는 부분플롯의 번호를 말한다.

다음은 2행, 2열의 부분플롯과 `index`를 보여주고 있다. `index`는 행이 우선으로 1부터 4까지이다.

![2행 2열의 서브플롯과 index 참조](img/page_013.png)

다음은 2행 3열의 부분플롯을 `plt.subplot(m, n, index)`로 그린 결과이다. `index`를 1, 5, 6만 그리기 때문에 중간 2, 3, 4 부분이 비어 있는 것을 볼 수 있다.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 4))

plt.subplot(2, 3, 1)
plt.subplot(2, 3, 5)
plt.subplot(2, 3, 6)

plt.plot()
plt.show()
```

#### ④ 서브플롯 plt.subplots() 개요

다음은 `plt.subplots(m, n)`으로 부분플롯을 그린 그림이다. 부분플롯에서 `m`은 행의 수, `n`은 열의 수이다. 다음은 `plt.subplots(2, 2)`로 2행, 2열의 부분플롯을 사용한 결과 그림이다. 부분플롯인 `axes[m, n]`으로 행이 `m`, 열이 `n`인 부분플롯에 원하는 그래프를 그릴 수 있다.

![2행 2열의 서브플롯과 axes 참조](img/page_014.png)

다음은 2행 4열의 부분플롯을 `plt.subplots(2, 4)`로 그린 결과이다.

```python
import matplotlib.pyplot as plt
plt.figure(figsize=(9, 4))

plt.subplots(2, 4) # 2행 4열의 서브플롯

plt.show()
```

#### ⑤ 서브플롯 fig.add_subplot() 개요

다음은 `fig.add_subplot(m, n, index)`으로 부분플롯을 그린 그림이다. 부분플롯에서 `m`은 행의 수, `n`은 열의 수이며, `index`는 1부터 시작하는 부분플롯의 번호이다.

다음은 3행, 2열의 부분플롯과 `index`를 보여주고 있다. `index`는 행이 우선으로 1부터 6까지이다. 다음 그림에서 `(3, 2, 1)`은 `(321)`로 쓰는 것이 가능하다. 다만 `(321)`로 사용하는 경우, 단 단위 자리만 가능하므로 1에서 9까지만 가능하다.

```python
import matplotlib.pyplot as plt

# define figure
fig = plt.figure()

# add subplots
fig.add_subplot(321).set_title('321')
fig.add_subplot(322).set_title('322')
fig.add_subplot(323).set_title('323')
fig.add_subplot(324).set_title('324')
fig.add_subplot(325).set_title('325')
fig.add_subplot(326).set_title('326')

# adjust spaces
fig.subplots_adjust(wspace=.2, hspace=.7)

plt.show()
```

다음은 2행 2열의 부분플롯을 `plt.add_subplot(m, n, index)`으로 그린 결과이다. `index`를 2, 3, 4만 그리기 때문에 중간에 1만 비어 있는 것을 볼 수 있다.

```python
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7, 5))
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
```
