---
layout: docs
title: "04. GridSpec을 사용한 맞춤형 figure 레이아웃"
---

## SECTION 02. 맞춤형 서브플롯

### 01. GridSpec을 사용한 맞춤형 figure 레이아웃

#### ① GridSpec 개요

다음은 위에서 실습한 `plt.subplots`으로 2행 2열의 레이아웃을 그린 코드와 결과이다.

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(ncols=2, nrows=2, constrained_layout=True)
```

`matplotlib.gridspec.GridSpec` 클래스는 서브플롯을 배치할 그리드의 형상을 지정하는 데 사용된다. 이를 위해서는 행과 열의 개수를 설정해야 한다. 선택적으로 서브플롯 레이아웃 매개변수 조정도 수행할 수 있다. 다음은 클래스 `matplotlib.gridspec.GridSpec`의 인자 설명이다.

`class matplotlib.gridspec.GridSpec(nrows, ncols, figure=None, left=None, bottom=None, right=None, top=None, wspace=None, hspace=None, width_ratios=None, height_ratios=None)`

- `nrows`: 그리드의 행 수를 나타내는 정수
- `ncols`: 그리드의 열 수를 나타내는 정수
- `figure`: 그림을 그리는 데 사용되는 선택적 매개변수
- `left, right, top, bottom`: 그림 너비 또는 높이의 일부로 서브플롯의 범위를 정의하는 데 사용되는 선택적 매개변수
- `wspace`: 서브플롯 사이의 너비 공간을 예약하는 데 사용되는 선택적 부동 소수점 인수
- `hspace`: 서브플롯 사이의 높이 공간을 예약하는 데 사용되는 선택적 부동 소수점 인수
- `width_ratios`: 열의 너비 비율을 나타내는 선택적 매개변수
- `height_ratios`: 행의 높이 비율을 나타내는 선택적 매개변수

위와 같은 2행 2열의 레이아웃을 `GridSpec`으로 코딩해 보자. 다음처럼 `GridSpec` 인스턴스를 별도로 만든 다음, `GridSpec` 인스턴스의 요소를 `add_subplot()` 메서드에 전달하여 서브플롯 객체를 생성해야 한다. `GridSpec`의 요소는 일반적으로 numpy 배열과 동일한 방식으로 참조된다.

다음은 2행 2열의 레이아웃을 `GridSpec`으로 만든 내용과 결과이다. 사실 이러한 2행 2열의 단순한 배치를 만들려면 `GridSpec`보다 위 방식이 더 간편하다. 여기에서는 `GridSpec`의 설명을 위해 그린 레이아웃이다.

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig2 = plt.figure(constrained_layout=True)
spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig2)

f2_ax1 = fig2.add_subplot(spec2[0, 0])
f2_ax2 = fig2.add_subplot(spec2[0, 1])
f2_ax3 = fig2.add_subplot(spec2[1, 0])
f2_ax4 = fig2.add_subplot(spec2[1, 1])
```

![2행 2열 GridSpec 레이아웃](img/page_019.png)

#### ② GridSpec을 활용한 다양한 그리드 레이아웃

`GridSpec`의 장점은 행과 열에 걸쳐 있는 하위 그림을 만들 수 있다는 점이다. 위의 `gridspec.GridSpec` 대신에 메서드 `figure.add_gridspec`를 사용할 수 있다. 다음은 3행 3열의 그리드 배치를 만드는 코드이다.

```python
fig3 = plt.figure(constrained_layout=True)
gs = fig3.add_gridspec(3, 3)
```

3행 3열의 배치에서 각 서브플롯이 차지할 그리드 사양 객체를 선택하기 위한 NumPy 슬라이싱 구문을 사용한다. 즉, `gs[0, :]`은 0행과 모든 열의 배치하는 서브플롯이 된다.

```python
f3_ax1 = fig3.add_subplot(gs[0, :])
```

다음은 `GridSpec`의 슬라이싱 방법으로 다양한 배치를 만든 코드와 결과이다.

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig3 = plt.figure(constrained_layout=True)
gs = fig3.add_gridspec(3, 3)

f3_ax1 = fig3.add_subplot(gs[0, :])
f3_ax1.set_title('gs[0, :]')

f3_ax2 = fig3.add_subplot(gs[1, :-1])
f3_ax2.set_title('gs[1, :-1]')

f3_ax3 = fig3.add_subplot(gs[1:, -1])
f3_ax3.set_title('gs[1:, -1]')

f3_ax4 = fig3.add_subplot(gs[-1, 0])
f3_ax4.set_title('gs[-1, 0]')

f3_ax5 = fig3.add_subplot(gs[-1, -2])
f3_ax5.set_title('gs[-1, -2]')
```

![GridSpec 다양한 배치](img/page_020.png)

다음 `from` 문장을 사용하면 `GridSpec`을 바로 사용할 수 있다.

```python
from matplotlib.gridspec import GridSpec
```

다음은 8행, 39열의 배치 형태의 `GridSpec`이며, `plt.subplot(gs)`으로 그림이 가능하다. 다음 서브플롯 `ax1`은 슬라이싱 배열 참조 `gs[:6, :35]`를 통해 0행에서 5행까지, 0열에서 34열까지를 통합하는 배치를 만들 수 있다. 마찬가지로 `ax2`는 6행에서 마지막 행까지, 모든 열을 통합하는 배치를 만들 수 있다.

```python
gs = GridSpec(8, 39)
ax1 = plt.subplot(gs[:6, :35])
ax2 = plt.subplot(gs[6:, :])
```

다음은 6행, 35열의 난수와 2행, 39열의 이미지를 `GridSpec`으로 레이아웃을 배치해 그린 그림이다.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

gs = GridSpec(8, 39)

ax1 = plt.subplot(gs[:6, :35])
ax2 = plt.subplot(gs[6:, :])
data1 = np.random.rand(6, 35)
data2 = np.random.rand(2, 39)

ax1.imshow(data1)
ax2.imshow(data2)

plt.show()
```

#### ③ axes.annotate()로 텍스트 추가

다음은 그리드를 그리면서 메서드 `axes.annotate`로 서브플롯 내부에 텍스트를 표시하는 코드이다.

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig4 = plt.figure(constrained_layout=True)
spec4 = fig4.add_gridspec(ncols=2, nrows=2)

anno_opts = dict(xy=(0.5, 0.5), xycoords='axes fraction',
                 va='center', ha='center')

f4_ax1 = fig4.add_subplot(spec4[0, 0])
f4_ax1.annotate('GridSpec[0, 0]', **anno_opts)

fig4.add_subplot(spec4[1, 0]).annotate('GridSpec[1, 0]', **anno_opts)
fig4.add_subplot(spec4[1, 1]).annotate('GridSpec[1, 1]', **anno_opts)
fig4.add_subplot(spec4[0, 1]).annotate('GridSpec[0, 1]', **anno_opts)
```

![axes.annotate() 예제](img/page_022.png)

#### ④ 가로와 세로 비율로 레이아웃 배치

서브플롯의 가로와 세로 길이 비율을 각각 지정하는 옵션으로 `width_ratios` 및 `height_ratios` 매개변수를 제공한다. 인자 유형은 상대 비율의 숫자 목록이다. 즉 `width_ratios=[2, 4, 8]`과 `width_ratios=[1, 2, 4]`는 같은 의미이다.

다음은 가로와 세로를 각각 `widths = [2, 3, 1.5]`와 `heights = [1, 3, 2]`로 지정해 3행 3열로 배치한 서브플롯이다. 가로와 세로가 독립적인 값이므로 가로에서 소수를 빼고 `widths = [4, 6, 3]`으로 해도 같은 결과가 나온다.

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig5 = plt.figure(constrained_layout=True)
widths = [2, 3, 1.5]
heights = [1, 3, 2]

spec5 = fig5.add_gridspec(ncols=3, nrows=3,
                          width_ratios=widths,
                          height_ratios=heights)

for row in range(3):
    for col in range(3):
        ax = fig5.add_subplot(spec5[row, col])
        label = 'Width: {}\nHeight: {}'.format(widths[col], heights[row])
        ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')
```

![가로 세로 비율 레이아웃](img/page_023.png)

#### ⑤ gridspec_kw 키워드 인자 활용

함수 `subplot()`의 키워드 인자 `gridspec_kw`에서도 속성 `width_ratios` 및 `height_ratios`를 사용할 수 있다. 구조체 `gridspec_kw`를 만들어 인자로 사용한다.

```python
widths = [4, 6, 3]
heights = [1, 3, 2]
gs_kw = dict(width_ratios=widths, height_ratios=heights)
```

다음 코드는 이전 코드와 같은 기능의 함수 `plt.subplots(ncols=3, nrows=3, constrained_layout=True, gridspec_kw=gs_kw)`를 사용한다.

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

widths = [4, 6, 3]
heights = [1, 3, 2]
gs_kw = dict(width_ratios=widths, height_ratios=heights)

fig6, f6_axes = plt.subplots(ncols=3, nrows=3, constrained_layout=True,
                             gridspec_kw=gs_kw)

for r, row in enumerate(f6_axes):
    for c, ax in enumerate(row):
        label = 'Width: {}\nHeight: {}'.format(widths[c], heights[r])
        ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')
```

![gridspec_kw 활용](img/page_024.png)

#### ⑥ 그리드 서브플롯의 추가와 삭제

`GridSpec`과 `get_gridspec` 방법은 서브플롯을 이용하여 대부분의 서브플롯을 만든 후 일부를 제거하고 결합하는 것이 편리하다. 다음 코드로 3행 3열의 그리드 배치를 만들 수 있다.

```python
fig7, f7_axs = plt.subplots(ncols=3, nrows=3)
```

다음 코드처럼 메서드 `get_gridspec()`의 결과를 `gs`에 저장해 서브플롯으로 추가할 수 있다.

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig7, f7_axs = plt.subplots(ncols=3, nrows=3)
gs = f7_axs[1, 2].get_gridspec()

print(gs)
# GridSpec(3, 3)

gs = f7_axs[0, 2].get_gridspec()
print(gs)
# GridSpec(3, 3)
```

다음은 2행 3열과 3행 3열의, 2개 서브플롯을 제거하는 문장이다.

```python
f7_axs[1, -1].remove()
f7_axs[2, -1].remove()
```

다시 다음 문장으로 두 서브플롯 영역에 하나의 서브플롯을 추가하는 코드이다.

```python
axbig = fig7.add_subplot(gs[1:, -1])
```

다음은 전체 코드와 결과이다.

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig7, f7_axs = plt.subplots(ncols=3, nrows=3)
gs = f7_axs[1, 2].get_gridspec()

# remove the underlying axes
# for ax in f7_axs[1:, -1]:
#     ax.remove()

f7_axs[1, -1].remove()
f7_axs[2, -1].remove()

axbig = fig7.add_subplot(gs[1:, -1])

axbig.annotate('Big Axes \nGridSpec[1:, -1]', (0.1, 0.5),
               xycoords='axes fraction', va='center')

fig7.tight_layout()
```

![서브플롯 추가와 삭제](img/page_026.png)

#### ⑦ GridSpec의 세부 조정

`GridSpec`을 명시적으로 사용하면 `GridSpec`을 생성하면서 하위 플롯의 레이아웃 매개변수를 조정할 수 있다. 이 옵션은 서브플롯 크기를 조정하거나 그림을 채우기 위해 `figure.tight_layout()`이나 `constrained layout`으로 호환되지 않는다.

인자 `left`는 전체 그림의 왼쪽 위치를, `right`는 오른쪽 위치를 비율로 나타낸다. 즉 왼쪽 반 정도만 사용하도록 한다.

```python
gs1 = fig8.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48,
                        hspace=0.3, wspace=0.7)
```

다음은 `fig8.add_gridspec()`으로 전체 레이아웃 조정하고 다시 `fig8.add_subplot()`으로 3개의 서브플롯을 그리는 코드와 결과이다. 다음은 `subplots_adjust`와 유사하지만 지정된 `GridSpec`에서 생성된 하위 플롯에만 영향을 미친다.

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig8 = plt.figure(constrained_layout=False)
gs1 = fig8.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48,
                        hspace=0.3, wspace=0.7)

f8_ax1 = fig8.add_subplot(gs1[:-1, :])
f8_ax2 = fig8.add_subplot(gs1[-1, :-1])
f8_ax3 = fig8.add_subplot(gs1[-1, -1])
```

![GridSpec 세부 조정](img/page_027.png)

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig9 = plt.figure(constrained_layout=False)

gs1 = fig9.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48,
                        wspace=0.05)

f9_ax1 = fig9.add_subplot(gs1[:-1, :]) # 1~2행, 모든 열에 걸친 서브플롯
f9_ax1.annotate('f9_ax1 -> gs1[:-1, :]', (0.1, 0.5), xycoords='axes fraction', va='center')

f9_ax2 = fig9.add_subplot(gs1[-1, :-1]) # 3행에 1~2열에 걸친 서브플롯
f9_ax2.annotate('f9_ax2 -> gs1[-1, :-1]', (0.1, 0.5), xycoords='axes fraction', va='center')

f9_ax3 = fig9.add_subplot(gs1[-1, -1]) # 3행 3열 서브플롯
f9_ax3.annotate('gs1[-1, -1]', (0.1, 0.5), xycoords='axes fraction', va='center')

gs2 = fig9.add_gridspec(nrows=3, ncols=3, left=0.55, right=0.98,
                        hspace=0.05)

f9_ax4 = fig9.add_subplot(gs2[:, :-1]) # 모든 행, 1~2열에 걸친 서브플롯
f9_ax4.annotate('f9_ax4 -> gs2[:, :-1]', (0.1, 0.5), xycoords='axes fraction', va='center')

f9_ax5 = fig9.add_subplot(gs2[:-1, -1]) # 1~2행과 3열에 걸친 서브플롯
f9_ax5.annotate('gs2[:-1, -1]', (0.1, 0.5), xycoords='axes fraction', va='center')

f9_ax6 = fig9.add_subplot(gs2[-1, -1]) # 3행 3열 서브플롯
f9_ax6.annotate('gs2[-1, -1]', (0.1, 0.5), xycoords='axes fraction', va='center')

plt.subplots_adjust(hspace=.5, wspace=.7)
plt.show()
```

![GridSpec 세부 조정 2](img/page_028.png)

#### ⑧ SubplotSpec을 사용하는 GridSpec

메서드 `subgridspec()`으로 `GridSpec`을 생성할 수 있으며, 이 경우 해당 레이아웃 매개변수는 지정된 `SubplotSpec`의 인자로 설정된다.

다음으로 1행 2열의 그리드를 배치할 수 있다.

```python
gs0 = fig10.add_gridspec(1, 2) # 1행 2열
```

1열 객체인 `gs0[0]`의 메서드 `subgridspec(2, 3)`의 호출로 1열 내부에 2행 3열의 서브플롯을 그릴 수 있다. 2열 객체인 `gs0[1]`의 `subgridspec(3, 2)`의 호출로 2열 내부에 3행 2열의 서브플롯을 그릴 수 있다.

```python
gs00 = gs0[0].subgridspec(2, 3) # 1열 내부에 2행 3열의 서브플롯
gs01 = gs0[1].subgridspec(3, 2) # 2열 내부에 3행 2열의 서브플롯
```

다음은 1열 내부에 2행 3열의 서브플롯, 2열 내부에 3행 2열의 서브플롯을 그리는 내용과 결과이다.

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig10 = plt.figure(constrained_layout=True)
gs0 = fig10.add_gridspec(1, 2) # 1행 2열

gs00 = gs0[0].subgridspec(2, 3) # 1열 내부에 2행 3열의 서브플롯
gs01 = gs0[1].subgridspec(3, 2) # 2열 내부에 3행 2열의 서브플롯

for a in range(2):
    for b in range(3):
        fig10.add_subplot(gs00[a, b])
        fig10.add_subplot(gs01[b, a])
```

![SubplotSpec 중첩](img/page_029.png)

#### ⑨ SubplotSpec을 사용해 중첩된 그리드 배치

다음 코드는 외부 4 x 4 그리드의 각각의 내부에 다시 내부 3 x 3 그리드를 표현한 그림이다. 각각의 그리드에는 외부와 내부의 서브플롯을 참조할 수 있는 첨자를 보이게 하고 있다. 다음이 외부 4 x 4 그리드를 만든 코드이다.

```python
outer_grid = fig11.add_gridspec(4, 4, wspace=0, hspace=0)
```

다음은 16개의 `outer_grid[a, b]`에서 `subgridspec(3, 3, ...)`으로 내부에 다시 3 x 3의 그리드를 만드는 코드이다.

```python
inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
axs = inner_grid.subplots() # Create all subplots for the inner grid.
```

`numpy`에 있는 `ndenumerate(arr)`은 배열 첨자 좌표와 해당 값의 쌍을 만드는 반복자(iterator)를 반환한다. 다음처럼 `for` 반복에서 두 개의 변수 `index`, `x`로 받아 출력하면 내용을 이해할 수 있다.

```python
>>> a = np.array([[1, 2], [3, 4]])
>>> for index, x in np.ndenumerate(a):
        print(index, x)

(0, 0) 1
(0, 1) 2
(1, 0) 3
(1, 1) 4
```

또한, 다음으로 16개의 `outer_grid[a, b]`를 순회하면서 각각 3 x 3의 모든 서브플롯에서 외부와 내부의 서브플롯을 참조할 수 있는 텍스트를 호출해 자리를 보이게 하고 있다. 또한, 모든 눈금(ticks)은 없도록 지정한다.

```python
for (c, d), ax in np.ndenumerate(axs):
    s1, s2 = f'out[{a}, {b}]', f'in[{c}, {d}]'
    ax.text(0.1, 0.3, s1, fontsize=7)
    ax.text(0.1, 0.6, s2, fontsize=7)
    ax.set(xticks=[], yticks=[]) # 눈금 없애기
```

다음이 전체 코드와 결과이다.

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

fig11 = plt.figure(figsize=(8, 8), constrained_layout=False)
outer_grid = fig11.add_gridspec(4, 4, wspace=0, hspace=0)

for a in range(4):
    for b in range(4):
        # gridspec inside gridspec
        inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
        axs = inner_grid.subplots() # Create all subplots for the inner grid.

        for (c, d), ax in np.ndenumerate(axs):
            s1, s2 = f'out[{a}, {b}]', f'in[{c}, {d}]'
            ax.text(0.1, 0.3, s1, fontsize=7)
            ax.text(0.1, 0.6, s2, fontsize=7)
            ax.set(xticks=[], yticks=[]) # 눈금 없애기

plt.show()
```

![SubplotSpec 중첩 그리드 텍스트](img/page_031.png)

#### ⑩ SubplotSpec을 사용해 중첩된 그리드 배치에 기하학적인 그래프 그리기

먼저 `sin()`과 `cos()` 함수를 사용해 다양한 그림을 그려보자. 다음에서 구현한 함수를 `squiggle_xy(1, 2, 1, 3)`로 호출해 `x`, `y`의 값을 얻어 플롯해 보면 기하학적인 그림이 그려진다. 네 개의 인자를 정수로 적정하게 바꾸면 다양한 기하학적인 문양이 만들어진다.

```python
import numpy as np
import matplotlib.pyplot as plt

def squiggle_xy(a, b, c, d, i=np.arange(0.0, 2*np.pi, 0.05)):
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)

fig = plt.figure(figsize=(4, 4))

plt.plot(*squiggle_xy(1, 2, 1, 3))
plt.show()
```

![기하학적 그래프](img/page_032.png)

다음은 16개의 `outer_grid[a, b]`에서 `subgridspec(3, 3, ...)`으로 내부에 다시 3 x 3의 그리드를 만드는 코드이다.

```python
inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
axs = inner_grid.subplots() # Create all subplots for the inner grid.
```

또한, 다음으로 16개의 `outer_grid[a, b]`를 순회하면서 각각 3 x 3의 모든 서브플롯에서 기하학적인 그림을 그리고 모든 눈금(ticks)은 없도록 지정한다.

```python
for (c, d), ax in np.ndenumerate(axs):
    ax.plot(*squiggle_xy(a + 1, b + 1, c + 1, d + 1))
    ax.set(xticks=[], yticks=[])
```

다음이 전체 코드와 결과이다.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def squiggle_xy(a, b, c, d, i=np.arange(0.0, 2*np.pi, 0.05)):
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)

fig11 = plt.figure(figsize=(8, 8), constrained_layout=False)
outer_grid = fig11.add_gridspec(4, 4, wspace=0, hspace=0)

for a in range(4):
    for b in range(4):
        # gridspec inside gridspec
        inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
        axs = inner_grid.subplots() # Create all subplots for the inner grid.

        for (c, d), ax in np.ndenumerate(axs):
            ax.plot(*squiggle_xy(a + 1, b + 1, c + 1, d + 1))
            ax.set(xticks=[], yticks=[])

        # show only the outside spines
        for ax in fig11.get_axes():
            ss = ax.get_subplotspec()
            ax.spines.top.set_visible(ss.is_first_row())
            ax.spines.bottom.set_visible(ss.is_last_row())
            ax.spines.left.set_visible(ss.is_first_col())
            ax.spines.right.set_visible(ss.is_last_col())

plt.show()
```

내부 외곽선을 보이지 않게 처리하는 부분(마지막 `for` 문장)이 없는 경우, 다음처럼 보인다.

![기하학적 중첩 그리드](img/page_034.png)
