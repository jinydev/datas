---
layout: mathplotlib
title: "5.4.2 히스토그램"
---

# 5.4.2 히스토그램

### ① 함수 hist()를 활용한 히스토그램

파이썬에서 히스토그램은 함수 `hist()`를 사용해 그린다.

다음은 자동차 데이터 `mtcars`에서 연비 데이터 변수인 `mtc.mpg`를 그린 도수분포표 결과이다. 특별히 막대 구간을 지정하지 않으면 자동으로 최소부터 최대까지 10개의 구간을 정해 알아서 그린다. 결과에서 그림이 그려지기 전에 그림에 사용한 빈도수와 구간이 표시된다.

```python
plt.hist(mtc.mpg) # 10개의 구간의 빈도수이다
```

**히스토그램(Histogram)**은 연속된 데이터를 일정한 구간(**Bin**, 통)으로 나누고, 각 구간에 속한 데이터의 개수(**Frequency**, 도수)를 막대 높이로 표현한 그래프입니다. 막대그래프가 범주(Category) 간 크기를 비교한다면, 히스토그램은 구간에 따른 데이터의 **분포(Distribution)**를 파악하는 데 특화되어 있습니다.

함수 `hist`에서 `edgecolor`에 색상을 지정하면 구간 구분이 명확해진다. 또한, 문장 마지막에 세미콜론(;)을 넣으면 출력 글자는 표시되지 않는다.

```python
plt.hist(mtc.mpg, edgecolor='black');
```

다음은 자동차 무게 변수인 `mtc.wt`를 그린 히스토그램 결과이다.

```python
plt.hist(mtc.wt, edgecolor='white')
```

구간 간격 인자인 `bins`를 설정하면 분포 구간을 다르게 설정해 그릴 수 있다. 점 인자 `bins=5`를 사용하면 5개의 구간으로 나누어 그리는 것을 알 수 있다.

```python
plt.hist(mtc.wt, bins=5, edgecolor='white')
```

다음처럼 인자 구간을 `bins = np.arange(1.5, 5.6, 0.5)`로 등분하는 구간을 직접 지정할 수 있다. 따라서, `np.arange(1.5, 5.6, 0.5)`는 1.5에서 시작하여 5.6보다 작은 값까지 0.5씩 증가하는 숫자 배열을 생성한다. 그러므로 구간 값 `bins`는 `array([1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5])`가 된다.

```python
plt.hist(mtc.wt, bins=np.arange(1.5, 5.6, 0.5), edgecolor='white')
```

구간 간격을 `bins = [1.5, 2.5, 4.5, 5.5]`로 직접 지정한다면 간격이 일정하지 않게도 할 수 있다.

```python
plt.hist(mtc.wt, bins = [1.5, 2.5, 4.5, 5.5], edgecolor='white')
```

인자 `density=True`를 사용하면 확률 밀도로 표시된다. 즉 막대의 길이가 확률이 되며 막대의 모든 면적을 합하면 1이 된다.

```python
plt.hist(mtc.wt, bins = [1.5, 2.5, 4.5, 5.5], density=True, edgecolor='white')
```

### ② 함수 hist()의 bins, edgecolor 등 다양한 패러미터

다음은 유명한 붓꽃 데이터 `iris`를 가져와 정보를 출력한 결과이다. 붓꽃 데이터 `iris`는 5개의 변수와 150개의 관측 값으로 구성된 데이터프레임이다.

```python
from pydataset import data
iris = data('iris')
iris.info()
```

변수 `Species`는 문자열 객체(object)로 표시되는 범주형으로 붓꽃의 종류 `setosa`, `versicolor`, `virginica` 중의 한 값을 갖는다. 다음 코드 `iris.Species.unique()`로 확인 가능하다.

```python
iris.Species.unique()
```

다음은 데이터 `iris`에서 꽃받침 길이 변수 `iris['Sepal.Length']`의 도수분포표 결과이다. 인자 `color='yellowgreen'`으로 막대의 색상을 일괄적으로 지정할 수 있다.

```python
plt.hist(iris['Sepal.Length'], color='yellowgreen', edgecolor='white')
```

다음처럼 인자 `bins=20`으로도 구간의 수를 지정할 수 있다. 또한, 함수 `hist()`가 반환하는 3개의 반환 값을 각각 `n`, `bins`, `patches`에 대입해 출력해 보자. `n`은 구간의 빈도수이며, `bins`는 구간의 경계 값 배열이다. 또한, `patches`는 막대컨테이너(BarContainer) 객체이다.

```python
n, bins, patches = plt.hist(iris['Sepal.Length'], bins=20, color='yellowgreen', edgecolor='white')

print(n)
print(bins)
print(patches)
```

막대컨테이너(BarContainer) 객체인 변수 `patches`의 `patches[i].set_facecolor()`로 각 막대의 색상을 지정하면 막대마다 서로 다른 색상을 지정할 수 있다. 색상을 `plt.cm.viridis(n[i]/max(n))`로 지정하면 여러 색상을 갖고 있는 색상맵 `cm.viridis`에서 값 빈도수 `n[i]`에 따라 `viridis`로 다른 색상을 반환 받을 수 있다. 다음 코드로 색상을 빈도수에 따라 색상맵 `cm.viridis`를 달리 지정해 `hist()`를 그릴 수 있다. 빈도 수가 작은 값은 보라색으로 큰 값은 노란색이 되는 것을 알 수 있다.

```python
n, bins, patches = plt.hist(iris['Sepal.Length'], bins=20, color='yellowgreen', edgecolor='white')
for i in range(len(patches)):
    patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
plt.show()
```

### ③ 커널 밀도 추정(kernel density estimation) 곡선 그리기

변수 `iris['Sepal.Width']`의 커널 밀도 추정 값을 그래프로 그리려면 메소드 `iris['Sepal.Width'].plot.density()`를 사용할 수 있다. 다음 함수로 그려진 하부 면적을 모두 합하면 1이 된다.

```python
iris['Sepal.Width'].plot.density();
```

함수 `kde()`를 사용한 메소드 `iris['Sepal.Width'].plot.kde()`도 가능하다.

```python
iris['Sepal.Width'].plot.kde();
```

### ④ 패키지 seaborn의 함수 sns.histplot()과 sns.rugplot()

다음 코드로는 꽃받침 너비 변수 `iris['Sepal.Width']`의 도수분포표와 함께 x축에 해당 자료의 눈금을 표시한다. `sns.rugplot()` 함수를 이용하면 데이터의 위치를 눈금으로 표시해 준다.

```python
import seaborn as sns
sns.histplot(data=iris, x=iris['Sepal.Width'], color='white')
sns.rugplot(data=iris, x=iris['Sepal.Width']);
```

함수 `sns.rugplot()`에 인자 `hue='Species'`를 사용하면 붓꽃의 품종에 따라 색상이 다른 눈금을 그릴 수 있다.

```python
import seaborn as sns
sns.histplot(data=iris, x=iris['Sepal.Width'], color='white')
sns.rugplot(data=iris, x=iris['Sepal.Width'], hue='Species');
```

함수 `sns.displot()`에 인자 `kde=True`, `rug=True`를 사용하면 도수분포표와 자료 값의 위치인 러그(rug)와 함께 커널 밀도 추정 그래프를 그릴 수 있다.

```python
import seaborn as sns
sns.displot(data=iris, x=iris['Sepal.Width'], kde=True, rug=True);
```

다음 코드처럼 인자 `col="Species"`의 사용으로 붓꽃이 품종에 따라 가로로 세 개의 도수분포표가 그려진다.

```python
import seaborn as sns
sns.displot(data=iris, x=iris['Sepal.Width'], col="Species", kde=True, rug=True);
```