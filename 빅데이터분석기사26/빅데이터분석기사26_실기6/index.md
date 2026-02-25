


**파트 소개**
이 파트에서는 Python을 활용한 통계모형을 다룹니다. 선형 회귀 분석(Linear Regression)과 로지스틱 회귀 분석(Logistic Regression)을 통해 연속형 및 범주형 데이터를 모델링하는 방법을 학습합니다.

**◇ 주요 내용**

- **선형 회귀 분석**: 회귀모델 적합, 계수 해석, 다중공선성 문제(VIF), 모델 평가($R^2$, F-검정)
- **로지스틱 회귀 분석**: 오즈비(Odds Ratio), 계수 해석, 모델 유의성 검정(Deviance 검정)



## SECTION 01 선형 회귀 분석

> **핵심 태그**: 다중 선형 회귀, 통계적 유의성, 결정 계수, AIC, BIC

**1. 상관계수(Correlation Coefficient)**
**1) 피어슨 상관계수(Pearson Correlation Coefficient, PCC)**
상관계수는 두 변수 간의 선형 관계를 측정하는 통계적 지표입니다. 상관계수는 일반적으로 피어슨 상관계수를 의미하지만, 데이터의 특징에 따라 다른 유형의 상관계수도 활용될 수 있습니다.

**피어슨 상관계수**는 두 연속형 변수 간의 선형적 관계를 측정하는 가장 일반적인 방법입니다. 계산 공식은 다음과 같습니다.
$$ r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}} = \frac{S_{xy}}{\sqrt{S_{xx} S_{yy}}} $$

- $x_i, y_i$: 개별 데이터 값
- $\bar{x}, \bar{y}$: 각 변수의 평균

피어슨 상관계수의 분모는 $x, y$ 변수의 표준편차를 곱한 값이고 분자는 두 변수의 공분산입니다. 즉 공분산을 표준화한 값이라고 볼 수 있습니다. 따라서 상관계수 $r$은 다음 범위를 가집니다.
$$ -1 \le r \le 1 $$

- **r = 1**: 두 변수는 완벽한 양의 상관 관계를 가짐 (즉, 한 변수가 증가하면 다른 변수도 비례하여 증가)
- **r = -1**: 두 변수는 완벽한 음의 상관 관계를 가짐 (즉, 한 변수가 증가하면 다른 변수는 비례하여 감소)
- **r = 0**: 두 변수 간에는 선형적 관계가 없음



피어슨 상관계수는 두 변수 간의 선형 관계를 측정하는 가장 직관적인 방법이지만, **이상치(outlier)**에 민감하다는 단점이 있습니다.

- 위 그림을 통해 보면 이상치가 존재할 경우 상관계수 값이 크게 변화하는 것을 확인할 수 있습니다.
- 데이터가 비선형 구조를 가질 경우, 피어슨 상관계수는 그 관계를 포착하지 못할 수 있습니다.

- 위 그림을 통해 보면 비선형 관계가 존재하지만, 상관계수는 0인 것을 확인할 수 있습니다.



**2) 피어슨 상관계수 검정**
피어슨 상관계수 검정은 두 연속형 변수 간 선형 관계가 존재하는지에 대해 검정하는 방법입니다.

**① 귀무가설과 대립가설**
- **귀무가설 ($H_0$)**: $\rho = 0$ (두 변수 간 상관관계가 없음)
- **대립가설 ($H_A$)**: $\rho \neq 0$ (두 변수 간 상관관계가 있음)

**② 검정통계량**
$$ t = r \sqrt{\frac{n-2}{1-r^2}} $$
- $r$은 표본 피어슨 상관계수이며, $n$은 데이터 개수입니다. 검정통계량 $t$는 자유도가 $n-2$인 t-분포를 따른다고 알려져 있습니다.

- 다음 예제를 통해 피어슨 상관계수를 계산해 보겠습니다. `scipy` 라이브러리의 `pearsonr()`를 활용하면 쉽게 피어슨 상관계수를 계산할 수 있습니다.

**한 쌍의 데이터 x, y 생성**

```python
import numpy as np
import scipy.stats as stats

# 샘플 데이터
x = np.array([10, 20, 30, 40, 50])
y = np.array([5, 15, 25, 35, 48])
```

**피어슨 상관계수와 p-value 계산**

```python
corr_coeff, p_value = stats.pearsonr(x, y)

print(f"피어슨 상관계수 (r): {corr_coeff:.4f}")
print(f"p-value: {p_value:.4f}")
```
```
피어슨 상관계수 (r): 0.9984 
p-value: 0.0001
```

- 상관계수는 0.9984로 높은 양의 상관 관계가 존재하며, 유의수준 5%에서 p-value=0.0001로 통계적 유의성 또한 존재합니다.



**(참고) 수식 기반 직접 계산**

```python
# 평균
x_mean = np.mean(x)
y_mean = np.mean(y)

# 분자: 공분산의 분자
numerator = np.sum((x - x_mean) * (y - y_mean))

# 분모: 표준편차 곱
denominator = np.sqrt(np.sum((x - x_mean) ** 2)) * np.sqrt(np.sum((y - y_mean) ** 2))

# 피어슨 상관계수
r = numerator / denominator
print(f"피어슨 상관계수 (수식 기반): {r:.4f}")
```
```
피어슨 상관계수 (수식 기반): 0.9984
```

**2. 단순 선형 회귀(Simple Linear Regression)**
**1) 모델 표현**
데이터를 나타내는 기호가 다음과 같을 때,

- 반응변수 $y_i, \quad i=1, \dots, n$
- 독립변수 $x_i, \quad i=1, \dots, n$
- 잡음변수 $\epsilon_i, \quad i=1, \dots, n$

단순 선형회귀 모델을 정의하면 다음과 같습니다.
$$ y_i = \beta_0 + \beta_1 x_i + \epsilon_i, \quad i=1, \dots, n $$

- $\beta_0$: 절편(intercept)
- $\beta_1$: 기울기(slope)

위 형태를 다음과 같이 벡터 형태로 표현할 수 있습니다.
$$ \mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon} $$

$$
\mathbf{y} = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix}, \quad
\mathbf{X} = \begin{pmatrix} 1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n \end{pmatrix}, \quad
\boldsymbol{\beta} = \begin{pmatrix} \beta_0 \\ \beta_1 \end{pmatrix}, \quad
\boldsymbol{\epsilon} = \begin{pmatrix} \epsilon_1 \\ \epsilon_2 \\ \vdots \\ \epsilon_n \end{pmatrix}
$$



**2) 모델 가정**
반응변수의 관찰값들은 다음과 같은 모델을 통해서 발생되었다고 가정합니다.
$$ y_i \sim N(\beta_0 + \beta_1 x_i, \sigma^2) $$

관찰값 $y_i$은 독립변수 $x_i$와 잡음 $\epsilon_i$의 선형결합으로 이루어져 있습니다.
$$ y_i = \beta_0 + \beta_1 x_i + \epsilon_i, \quad i=1, \dots, n $$

잡음 $\epsilon_i$들의 분포는 평균이 0이고 분산이 $\sigma^2$인 독립인 정규분포를 따른다고 가정합니다.
$$ \epsilon_i \overset{i.i.d}{\sim} N(0, \sigma^2) $$

**3) 회귀계수 추정하기**
회귀계수 추정은 관측치를 가장 잘 설명하는 직선을 찾는 것입니다. 다음 예시를 통해 확인해 보겠습니다.

- Graph 1보다는 Graph 2가 직선과 관측치 사이의 거리(잔차)가 가깝기 때문에 해당 관측치를 잘 설명하는 직선입니다.
단순 선형회귀에서 회귀계수 $\beta_0$(절편)와 $\beta_1$(기울기)는 **최소제곱법(Least Squares Method)**을 통해 추정합니다. 이는 잔차 제곱합(RSS, Residual Sum of Squares)을 최소화하는 계수를 찾는 방식입니다.

1. **잔차(residual)**
   $$ e_i = y_i - \hat{y}_i = y_i - (\hat{\beta}_0 + \hat{\beta}_1 x_i) $$

2. **잔차제곱합(RSS)**
   $$ \text{RSS} = \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2 $$

이를 최소화하는 $\beta_0, \beta_1$를 계산하면 다음과 같습니다.

3. **회귀계수의 추정값**
   $$ \hat{\beta}_1 = \frac{S_{xy}}{S_{xx}} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
   $$ \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} $$



- $\bar{x}, \bar{y}$: x, y의 평균
- $S_{xy}$: 공분산
- $S_{xx}$: x의 제곱편차합

벡터로 표현한 후 회귀계수를 유도하면 다음과 같습니다.

1. **잔차(residual)**
   $$ \mathbf{e} = \mathbf{y} - \hat{\mathbf{y}} = \mathbf{y} - \mathbf{X}\hat{\boldsymbol{\beta}} $$

2. **잔차 제곱합(RSS)**
   $$ \text{RSS} = \mathbf{e}^T \mathbf{e} = (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^T (\mathbf{y} - \mathbf{X}\boldsymbol{\beta}) $$

3. **회귀계수의 추정값 (최소제곱법)**
   $$ \hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} $$

**4) Python에서 회귀계수 계산하기**
- 넘파이 라이브러리를 활용하여 회귀계수를 직접 계산해보겠습니다.

```python
import numpy as np

x = np.array([10, 20, 30, 40, 50])
y = np.array([5, 15, 25, 35, 48])

# 평균 계산
x_mean = np.mean(x)
y_mean = np.mean(y)

# 기울기 β1 계산 (공식: Sxy / Sxx)
Sxy = np.sum((x - x_mean) * (y - y_mean))
Sxx = np.sum((x - x_mean) ** 2)
beta_1 = Sxy / Sxx

# 절편 β0 계산
beta_0 = y_mean - beta_1 * x_mean

# 결과 출력 
print(f"기울기 (beta_1): {beta_1:.4f}")
print(f"절편 (beta_0): {beta_0:.4f}")

# 예측식 
print(f"회귀직선 방정식: y = {beta_0:.4f} + {beta_1:.4f} * x")
```
```
기울기 (beta_1): 1.0600 
절편 (beta_0): -6.2000 
회귀직선 방정식: y = -6.2000 + 1.0600 * x
```

- 추정된 회귀계수를 바탕으로 회귀직선을 시각화 해보겠습니다．
```python
import matpiotiib.pypiot as pit 
import matpiotiib.font_manager as fm 
# 예측값 계산
y_pred = beta_O + beta_i * x
```
# 시각화 
pit. figure(figsize=(6, 4)) pit.scatter(x, y, 1.abel.="reai", coior= 'biue') pit.pl.ot(x, y_pred, color="red', iabei="fitted 1ine ") pit. titie("fitted ilne visuaiization") pit .xiabeiC'x") pit. yiabei("y ") pit. iegend() pit.grid(True) pit. showO fitted line visualization .

콘 병，..

- 
uueu uine

1. 
15
plt.figure(figsize=(6, 4))
plt.scatter(x, y, label="real", color='blue')
plt.plot(x, y_pred, color="red", label="fitted line")
plt.title("fitted line visualization")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
```
fitted line visualization

- $S_x$: x의 표준편차
- $S_y$: y의 표준편차
- $r$: x와 y의 피어슨 상관계수

단순 선형회귀에서 기울기 $\beta_1$는 상관계수 $r$과 다음과 같은 관계가 있습니다.
$$ \beta_1 = \frac{S_{xy}}{S_{xx}} = r \frac{S_y}{S_x} $$

즉, 상관계수가 클수록 회귀 기울기의 절댓값도 커집니다.



- 넘파이를 통해 직접 계산해보면서 최소제곱법으로 유도한 결과와 비교해보겠습니다.

```python
import numpy as np
from scipy.stats import pearsonr

x = np.array([10, 20, 30, 40, 50])
y = np.array([5, 15, 25, 35, 48])

# 평균 및 표준편차
x_mean, y_mean = np.mean(x), np.mean(y)
s_x, s_y = np.std(x, ddof=1), np.std(y, ddof=1)

# 상관계수 계산 
r, _ = pearsonr(x, y) 

# 회귀계수 계산
beta_1 = r * (s_y / s_x) 
beta_0 = y_mean - beta_1 * x_mean 

print(f"상관계수 r: {r:.4f}") 
print(f"기울기 beta_1 (r * sy/sx): {beta_1:.4f}")
```
```
상관계수 r: 0.9984 
기울기 beta_1 (r * sy/sx): 1.0600
```

- 결과가 동일한 것을 확인할 수 있습니다.

**3. 다중 선형 회귀(Multiple Linear Regression)**
**1) 모델 표현**
데이터를 나타내는 기호들이 다음과 같을 때,

- 반응변수 $y_i, \quad i=1, \dots, n$
- 독립변수 $x_{ij}, \quad i=1, \dots, n, \quad j=1, \dots, p$
- 잡음변수 $\epsilon_i, \quad i=1, \dots, n$

다중 선형회귀 모델을 정의하면 다음과 같습니다.
$$ y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_p x_{ip} + \epsilon_i, \quad i=1, \dots, n $$

위의 형태를 다음과 같이 행렬 형태로 표현할 수 있습니다.
$$ \mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon} $$

$$
\mathbf{y} = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix}, \quad
\mathbf{X} = \begin{pmatrix} 1 & x_{11} & \cdots & x_{1p} \\ 1 & x_{21} & \cdots & x_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n1} & \cdots & x_{np} \end{pmatrix}, \quad
\boldsymbol{\beta} = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \vdots \\ \beta_p \end{pmatrix}, \quad
\boldsymbol{\epsilon} = \begin{pmatrix} \epsilon_1 \\ \epsilon_2 \\ \vdots \\ \epsilon_n \end{pmatrix}
$$



**2) 모델 가정**
반응변수의 관찰값들이 다음과 같은 모델을 통해서 발생되었다고 가정합니다.
$$ \mathbf{y} \sim N(\mathbf{X}\boldsymbol{\beta}, \sigma^2 \mathbf{I}) $$

단순 선형회귀에서 정의한 것과 마찬가지로 관찰값 $y_i$은 독립변수 $x_i$와 잡음 $\epsilon_i$의 선형결합으로 이루어져 있습니다.
$$ y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_p x_{ip} + \epsilon_i $$

잡음 $\epsilon_i$들의 분포는 평균이 0이고 분산이 $\sigma^2$인 독립인 정규분포를 따른다고 가정합니다.

**3) Python에서 회귀 분석**
회귀 분석은 주로 `statsmodels` 라이브러리를 활용합니다. `statsmodels` 라이브러리는 통계적 추론에 관한 다양한 통계 테스트, 시각화 도구를 제공합니다.

> **기적의 Tip**: 이전에 공부했던 `scikit-learn` 라이브러리도 활용할 수 있지만, `scikit-learn`은 예측에 초점을 둔 라이브러리로, 통계적 추론에 관한 도구는 제공하지 않습니다.

`statsmodels` 라이브러리에서는 회귀 분석을 수행하는 두 가지 방식이 있습니다.

**iris 데이터 실습**

```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# 1. iris 데이터 로드
df_iris = load_iris()

# 2. pandas DataFrame으로 변환 
iris = pd.DataFrame(data=df_iris.data, columns=df_iris.feature_names) 
iris.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'] # 칼럼명 변경

# 3. 타겟(클래스) 추가 
iris["species"] = df_iris.target

# 4. 클래스 라벨을 실제 이름으로 변환 (0: setosa, 1: versicolor, 2: virginica) 
iris["species"] = iris["species"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
```



**① 방법 1: Formula API 활용**

- `종속변수(y) ~ 독립변수(x)` 형식으로 formula를 정의할 수 있습니다.

```python
import statsmodels.api as sm 
import statsmodels.formula.api as smf

model = smf.ols("Petal_Length ~ Petal_Width + Sepal_Length", data=iris).fit() 
print(model.summary())
```
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           Petal_Length   R-squared:                       0.949
Model:                            OLS   Adj. R-squared:                  0.948
Method:                 Least Squares   F-statistic:                     1354.
Date:                Fri, 03 Jan 2025   Prob (F-statistic):           2.01e-95
Time:                        08:46:52   Log-Likelihood:                -75.090
No. Observations:                 150   AIC:                             156.2
Df Residuals:                     147   BIC:                             165.2
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       -1.5071      0.337     -4.473      0.000      -2.173      -0.841
Petal_Width      1.7481      0.075     23.205      0.000       1.599       1.897
Sepal_Length     0.5423      0.069      7.820      0.000       0.405       0.679
==============================================================================
Omnibus:                        1.243   Durbin-Watson:                   1.339
Prob(Omnibus):                  0.537   Jarque-Bera (JB):                0.840
Skew:                          -0.058   Prob(JB):                        0.657
Kurtosis:                       3.348   Cond. No.                         64.7
==============================================================================
```

```python
model = smf.glm("Petal_Length ~ Petal_Width + Sepal_Length", family=sm.families.Gaussian(), data=iris).fit()
```
- `family=sm.families.Gaussian()`은 다중 선형회귀 모형을 의미합니다.

> **기적의 Tip**: `smf.ols`는 `smf.glm`에 비해 선형회귀에 특화된 가설 검정 결과를 제공합니다. (예: Durbin-Watson)

- 독립변수로 범주형 변수가 존재하는 경우, `C()`로 해당 범주형 변수를 명시해줍니다. 이 경우 해당 독립 변수는 더미 인코딩되어 계산됩니다.

```python
model = smf.ols("Petal_Length ~ Petal_Width + Sepal_Length + C(species)", data=iris).fit()
```



**(2) 방법 2: 행렬 활용**
- 데이터 행렬을 직접 대입합니다. y, X를 사전에 지정하며, X에 `add_constant()`를 활용하여 상수항(절편)을 추가합니다.

```python
import statsmodels.api as sm

X = iris[['Petal_Width', 'Sepal_Length']]
y = iris['Petal_Length']
X = sm.add_constant(X)

# 다중회귀 분석 모델 적합 (train 데이터 사용)
model = sm.OLS(y, X).fit()

# 회귀계수 출력 
print(model.summary())
```
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           Petal_Length   R-squared:                       0.949
Model:                            OLS   Adj. R-squared:                  0.948
Method:                 Least Squares   F-statistic:                     1354.
Date:                Fri, 03 Jan 2025   Prob (F-statistic):           2.01e-95
Time:                        09:04:53   Log-Likelihood:                -75.090
No. Observations:                 150   AIC:                             156.2
Df Residuals:                     147   BIC:                             165.2
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
const           -1.5071      0.337     -4.473      0.000      -2.173      -0.841
Petal_Width      1.7481      0.075     23.205      0.000       1.599       1.897
Sepal_Length     0.5423      0.069      7.820      0.000       0.405       0.679
==============================================================================
Omnibus:                        1.243   Durbin-Watson:                   1.339
Prob(Omnibus):                  0.537   Jarque-Bera (JB):                0.840
Skew:                          -0.058   Prob(JB):                        0.657
Kurtosis:                       3.348   Cond. No.                         64.7
==============================================================================
```



- 독립변수로 범주형 변수가 존재하는 경우, 사전에 더미인코딩을 적용해줘야 합니다.

```python
# 독립 변수 (Petal_Width, Sepal_Length) + 범주형 변수 species 추가
X = iris[['Petal_Width', 'Sepal_Length', 'species']]

# 범주형 변수 species를 더미 변수로 변환 (setosa를 기준으로 drop)
X = pd.get_dummies(X, columns=['species'], drop_first=True)
X = X.astype(float) # boolean to float conversion might be needed

y = iris['Petal_Length']
X = sm.add_constant(X)

model2 = sm.OLS(y, X).fit()
```

- 행렬을 이용한 방법보다 formula를 활용한 방법이 조금 더 간단하므로, 시험에서는 formula를 활용한 방법을 권장합니다.

> **기적의 Tip**: **상수항(절편)을 무조건 추가해야 하는가?**
> 일반적으로 회귀 분석을 수행할 때, 상수항(절편)을 포함한 모델을 사용합니다. 특수한 경우, 즉 데이터가 원점을 지난다는 정보가 주어진 상황이 아니라면 상수항을 제외하는 것은 바람직하지 않습니다.
> 시험에서는 독립변수의 개수를 묻는 문제가 출제됩니다. 절편은 독립변수가 아니므로 개수를 셀 때 제외해야 합니다.

- `summary()` 테이블에는 모델을 종합적으로 평가할 수 있는 다양한 지표가 출력됩니다.

**③ 회귀계수에 따른 모델식**

- 모델의 회귀계수는 coef를 확인하면 됩니다. coef 결과를 바탕으로 모델식을 표현해보겠습니다.
  $$ \text{Petal\_Length} = -1.5071 + 1.7481 \times \text{Petal\_Width} + 0.5423 \times \text{Sepal\_Length} $$

- `coef` 결과에 접근하여 회귀계수를 추출할 수 있습니다. 절편을 제외하고 회귀계수가 가장 큰 변수를 추출해보겠습니다.

**1. Petal_Width의 계수 ($\beta_1$)**
- $H_0: \beta_1 = 0$ (Petal_Width가 Petal_Length에 영향을 미치지 않는다)
- $H_1: \beta_1 \neq 0$ (Petal_Width가 Petal_Length에 영향을 미친다)

Petal_Width의 회귀 계수 추정치는 1.7481입니다. 유의수준 5%에서 $H_0$에 대한 $P > |t|$는 0.000로 매우 작으므로, $H_0$를 기각합니다. 따라서 Petal_Width는 Petal_Length에 통계적으로 유의미한 영향을 미칩니다.

**2. Sepal_Length의 계수 ($\beta_2$)**
- $H_0: \beta_2 = 0$ (Sepal_Length가 Petal_Length에 영향을 미치지 않는다)
- $H_1: \beta_2 \neq 0$ (Sepal_Length가 Petal_Length에 영향을 미친다)

Sepal_Length의 회귀 계수 추정치는 0.5423입니다. 유의수준 5%에서 $H_0$에 대한 $P > |t|$는 0.000로 매우 작으므로, $H_0$를 기각합니다. 이는 Sepal_Length는 Petal_Length에 통계적으로 유의미한 영향을 미칩니다.

**3. 절편 ($\beta_0$)**
- $H_0: \beta_0 = 0$ (절편이 0이다)
- $H_1: \beta_0 \neq 0$ (절편이 0이 아니다)

절편의 추정치는 -1.5071입니다. 유의수준 5%에서 $H_0$에 대한 $P > |t|$는 0.000로 매우 작으므로, $H_0$를 기각합니다. 따라서 절편이 통계적으로 유의미하게 0이 아님을 의미합니다.

**⑤ t-value, p-value 결과에 접근**

```python
t_values = model.tvalues 
print("t-values:\n", t_values)

p_values = model.pvalues 
print("p-values:\n", p_values)
```
```
t-values:
const           -4.472752
Petal_Width     23.205443
Sepal_Length     7.819907
dtype: float64

p-values:
const           1.535178e-05
Petal_Width     5.257543e-51
Sepal_Length    9.414477e-13
dtype: float64
```



**⑥ t-value 절댓값이 가장 큰 변수를 추출**

```python
print('t-value가 가장 큰 변수:', np.abs(t_values).idxmax())
```
```
t-value가 가장 큰 변수: Petal_Width
```

- `[0.025 0.975]`는 유의수준 5%에서 신뢰구간을 의미합니다. 신뢰구간을 추출해 보겠습니다.

**신뢰구간**

```python
conf_intervals = model.conf_int() 
print("Confidence intervals:\n", conf_intervals)
```
```
Confidence intervals:
                     0         1
const        -2.173050 -0.841227
Petal_Width   1.599230  1.896976
Sepal_Length  0.405218  0.679294
```

- 유의수준은 일반적으로 5%이지만 조정하고자 한다면 `alpha=` 옵션을 지정하면 됩니다.

```python
conf_intervals_90 = model.conf_int(alpha=0.10) 
# 90% 신뢰구간 
print("90% Confidence intervals:\n", conf_intervals_90)
```
```
90% Confidence intervals:
                     0         1
const        -2.064903 -0.949373
Petal_Width   1.623408  1.872798
Sepal_Length  0.427473  0.657038
```

**4) 더미 변수(Dummy Variable) 처리**
더미 인코딩은 통계학과 머신러닝에서 모두 자주 사용되나 그 목적에는 차이가 있습니다. 예측을 목표로 하는 머신러닝 모델에서는 원-핫 인코딩과 더미 인코딩 두 가지 방법을 모두 사용할 수 있지만, 통계적 추론을 목적으로 하는 다중회귀 모델에서는 원-핫 인코딩을 사용할 때 '**더미 변수 함정**' 문제가 발생할 수 있습니다.

이 문제는 모든 범주에 대해 더미 변수를 생성하고 상수항(constant)까지 포함시킬 때 발생합니다. 즉, 각 더미 변수의 합이 항상 1이 되어 완전한 다중공선성(perfect multicollinearity)이 생기는 것입니다.

따라서 이를 방지하기 위해 기준 범주(reference category) 하나를 제거한 더미 인코딩을 적용해야 합니다.



```python
import pandas as pd 
import statsmodels.api as sm

# 샘플 데이터 생성
data = {
    'color': ['red', 'blue', 'green', 'red', 'green', 'red', 'green', 'blue', 'green', 'red'], 
    'size': [1, 2, 3, 1, 3, 5, 9, 2, 9, 10], 
    'price': [10, 20, 30, 10, 30, 55, 29, 10, 25, 12]
}

df = pd.DataFrame(data)
```

- pandas의 `get_dummies()`를 활용하면 원-핫 인코딩을 적용할 수 있습니다.

```python
# 범주형 변수 더미 코딩 (drop_first=True로 기준 범주 제거)
df_dummies = pd.get_dummies(df, columns=['color'], drop_first=True) 
print(df_dummies)
```
```
   size  price  color_green  color_red
0     1     10        False       True
1     2     20        False      False
2     3     30         True      False
3     1     10        False       True
4     3     30         True      False
5     5     55        False       True
6     9     29         True      False
7     2     10        False      False
8     9     25         True      False
9    10     12        False       True
```

- 여기서 blue가 기준 범주로 제거되었고, `color_green`, `color_red`만 남게 됩니다.
- `statsmodels` 라이브러리의 `sm.OLS()`를 활용하여, 다중회귀모델을 적합시키겠습니다. 데이터는 더미 인코딩된 행렬을 활용합니다.

```python
# 종속 변수와 독립 변수 설정
X = df_dummies[['size', 'color_green', 'color_red']]
y = df_dummies['price']

X = X.astype(float)
y = y.astype(float)

# 상수항 추가
X = sm.add_constant(X)
```



```python
# 다중회귀 모델 적합
model2 = sm.OLS(y, X).fit() 
print(model2.summary())
```
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  price   R-squared:                       0.146
Model:                            OLS   Adj. R-squared:                 -0.280
Method:                 Least Squares   F-statistic:                    0.3430
Date:                Fri, 16 Aug 2024   Prob (F-statistic):              0.796
Time:                        07:26:37   Log-Likelihood:                -39.360
No. Observations:                  10   AIC:                             86.72
Df Residuals:                       6   BIC:                             87.93
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
const         14.3994     12.2989      1.171      0.286     -15.695      44.494
size           0.3003      1.679       0.179      0.864      -3.809       4.409
color_green   11.8000     15.397       0.766      0.472     -25.875      49.475
color_red    -14.4750     14.360      -1.008      0.352     -49.613      20.663
==============================================================================
Omnibus:                       13.796   Durbin-Watson:                   1.777
Prob(Omnibus):                  0.001   Jarque-Bera (JB):                6.788
Skew:                           1.679   Prob(JB):                       0.0336
Kurtosis:                       5.240   Cond. No.                         24.0
==============================================================================
```

- `color_green`과 `color_red`의 계수는 `blue` 대비 효과로 해석됩니다. 예를 들어 `color_red` 계수가 +6이라면, 같은 size일 때 red 제품은 blue 제품보다 평균적으로 6만큼 더 비싸다는 의미입니다.

- 이번에는 `smf()`를 활용하여 R formula 기반으로 다중회귀모델을 적합시키겠습니다.

```python
import statsmodels.formula.api as smf

# 회귀 분석 공식 설정
formula = 'price ~ size + C(color)'

# 회귀 모델 적합
model2 = smf.ols(formula, data=df).fit()

# 모델 요약 출력 
print(model2.summary())
```



```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  price   R-squared:                       0.146
Model:                            OLS   Adj. R-squared:                 -0.280
Method:                 Least Squares   F-statistic:                    0.3430
Date:                Fri, 16 Aug 2024   Prob (F-statistic):              0.796
Time:                        07:50:56   Log-Likelihood:                -39.360
No. Observations:                  10   AIC:                             86.72
Df Residuals:                       6   BIC:                             87.93
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
Intercept               14.3994     12.2989      1.171      0.286     -15.695      44.494
C(color)[T.green]       11.8000     15.397       0.766      0.472     -25.875      49.475
C(color)[T.red]        -14.4750     14.360      -1.008      0.352     -49.613      20.663
size                     0.3003      1.679       0.179      0.864      -3.809       4.409
==============================================================================
Omnibus:                       13.796   Durbin-Watson:                   1.777
Prob(Omnibus):                  0.001   Jarque-Bera (JB):                6.788
Skew:                           1.679   Prob(JB):                       0.0336
Kurtosis:                       5.240   Cond. No.                         24.0
==============================================================================
```

- `C(color)`로 지정하면 자동으로 더미 인코딩을 적용하고, 기준 범주를 제거해 회귀식을 적합합니다. 결과는 앞서 `drop_first=True`를 사용한 방식과 동일합니다.

**5. 모델 평가**
**1) 모델 평가 지표**
`summary()` 결과를 보면 R-squared, Adj. R-squared, F-statistic, Prob (F-statistic), AIC, BIC와 같은 지표가 요약되어 있습니다. 해당 지표의 의미와 지표 산출 방법에 대해 알아보겠습니다.

**① 결정계수 ($R^2$, R-squared)**
- 붓꽃의 꽃잎 길이에 아무런 추가 정보가 없을 경우 평균($\bar{y}$)으로 예측할 것입니다. 이렇게 반응변수 평균값($\bar{y}$)에서 각 관측치들까지의 변동성의 제곱합은 다음과 같이 분해할 수 있습니다.
  $$ SST = SSR + SSE $$

1. **관측치들의 편차제곱합(SST)**: $\sum (y_i - \bar{y})^2$
2. **예측치의 오차들의 제곱합(SSE)**: $\sum (y_i - \hat{y}_i)^2$ 


```python
교해볼 수 있습니다． 

- Adj. R-squared는 `.rsquared_adj`를 통해 접근할 수 있습니다.

```python
print('Adj. R-squared:', np.round(model.rsquared_adj, 2))
```
```
Adj. R-squared: 0.95
```

**③ F-statistic**

- F 통계량은 회귀 모델의 유의성을 평가하는 지표입니다. F 통계량에 관한 가설은 다음과 같습니다.
  - $H_0$: 모든 회귀계수들이 0이다. ($\beta_1 = \beta_2 = \cdots = \beta_p = 0$)
  - $H_1$: 0이 아닌 회귀계수가 존재한다.

  $$ F = \frac{SSR/p}{SSE/(n-p-1)} $$

- 이것은 ANOVA에서 그룹별 평균이 다르다고 결론을 내리는 논리와 동일합니다. 회귀 분석을 통해서 향상된 예측 효과(분자 부분)가 모델의 잡음보다 훨씬 크다면, 회귀 분석 모델의 효과가 통계적으로 의미가 있다고 판단합니다. 즉, 독립변수를 고려하는 것이 정말 효과가 있는지를 검정합니다. 귀무가설을 기각할 수 없다면, 모든 회귀계수가 0이므로 모델을 적합하는 의미가 없어집니다.

- F-statistic은 `.fvalue`를 통해 접근할 수 있습니다. F 통계량에 대한 p-value(Prob (F-statistic))는 `.f_pvalue`를 통해 접근할 수 있습니다.



```python
print('F-statistic:', np.round(model.fvalue, 4)) 
print('Prob (F-statistic):', np.round(model.f_pvalue, 4))
```
```
F-statistic: 1354.3397 
Prob (F-statistic): 0.0
```

- 유의수준 5% 하에서 F-value (1354.33)와 대응하는 p-value 0.0을 고려할 때, 귀무가설을 기각합니다.

**④ AIC, BIC**

- AIC, BIC는 Likelihood function 기반 모델 적합도와 모델의 복잡도를 함께 고려하여 모델의 품질을 평가하는 지표입니다.

  $$ AIC = -2\log L + 2p $$
  $$ BIC = -2\log L + p\log n $$

- 일반적으로 Likelihood 값은 높을수록 모델의 적합도가 높다고 판단할 수 있습니다. 하지만, 모델에 사용되는 변수가 늘어날수록 Likelihood 값이 높아지는 경향을 보입니다.
- 또한, 일반적으로 모델에 사용되는 변수는 적으면 적을수록 좋습니다(같은 성능이면 모델 복잡성 낮은 모델을 선호). 특정 변수가 추가되었는데 늘어나는 Likelihood 값이 미미하다면 추가하지 않는 것이 좋습니다.
- 이러한 아이디어에서 정의된 지표가 AIC, BIC입니다. AIC, BIC는 Likelihood($\log L$)값에 음수가 붙어있으므로 값이 낮을수록 좋습니다.

```python
print('AIC:', np.round(model.aic, 2)) 
print('BIC:', np.round(model.bic, 2))
```
```
AIC: 156.18 
BIC: 165.21
```

**2) 모델 비교하기 - Model 1 vs. Model 2**
선형회귀모델 간 비교를 해야하는 경우가 있습니다. 예를 들어 독립변수 2개 추가가 효용성이 있는지를 검정해보겠습니다.

- 모델 1: 독립변수 1개 - Petal_Width
- 모델 2: 독립변수 3개 - Petal_Width + Sepal_Length + Sepal_Width

**① 귀무가설과 대립가설**
- $H_0$: Reduced Model이 알맞음
- $H_1$: Full Model이 알맞음

- 같은 구조를 가지고 있는 모델 중 한 모델이 다른 모델을 포함하는 형식의 두 모델을 비교합니다.
  - **Full model**: Petal_Width + Sepal_Length + Sepal_Width
  - **Reduced model**: Petal_Width



**② F-검정**

- F-검정을 활용할 수 있습니다. 두 모델의 오차제곱합 차이를 비교합니다.

  $$ F = \frac{(SSE_{red} - SSE_{full}) / (p_{full} - p_{red})}{SSE_{full} / (n - p_{full} - 1)} $$

- $p_{full}$: Full 모델의 독립변수 개수
- $p_{red}$: Reduced 모델의 모수 개수(Intercept 포함)

```python
import statsmodels.api as sm 
from statsmodels.formula.api import ols

model1 = ols('Petal_Length ~ Petal_Width', data=iris).fit() 
model2 = ols('Petal_Length ~ Petal_Width + Sepal_Length + Sepal_Width', data=iris).fit()

# anova table
table = sm.stats.anova_lm(model1, model2) 
print(table)
```
```
   df_resid    ssr     df_diff   ss_diff         F     Pr(>F) 
0     148.0  33.844753     0.0       NaN       NaN        NaN 
1     146.0  14.852948     2.0 18.991805 93.341859 7.752746e-27
```

> **기적의 Tip**: Reduced 모델이 첫 번째, Full 모델이 두 번째로 들어가는 것에 주의하세요. 모델 순서에 따라 결과값이 달라집니다.

- 유의수준 5% 하에서 F 검정통계량과 p-value로 확인했을 때, 귀무가설을 기각할 수 있으며, Full model을 선택할 수 있습니다.
- 또한, 모델 비교 시 위에서 언급했던 AIC, BIC 지표를 활용할 수 있습니다. 선형회귀모델 간 비교 시에는 F statistic을 활용할 수 있고, 그 외 단순 모델 간 비교 시에는 AIC, BIC 지표를 활용할 수 있습니다.

**3) (Optional) 모델 가정 진단하기**
모델의 오차(잡음)에 대한 가정을 확인하기 위해 다양한 방식의 잔차 그래프와 통계 검정 방법을 활용합니다. 빅데이터분석기사 시험에서는 시각화 문제가 출제되지 않으므로, 통계 검정 방법을 알아보겠습니다.

**① 독립성 가정 체크**

- 회귀 분석에서는 독립성 가정이 존재합니다. 즉, 오차(잡음) 간에는 상관관계가 없다고 가정합니다.
- 독립성 가정이 위반되는 대표적인 케이스는 시계열 데이터입니다. 시계열 데이터의 경우 시간 순서에 따라 오차 간의 상관관계(자기상관)가 존재합니다.



- 독립성 가정을 체크하기 위한 대표적인 검정으로 **더빈-왓슨 테스트(Durbin-Watson test)**가 있습니다. 이것은 1차 자기상관이 존재하는지 검증합니다.
- 더빈-왓슨 통계량은 다음과 같습니다.
  $$ d = \frac{\sum_{t=2}^n (e_t - e_{t-1})^2}{\sum_{t=1}^n e_t^2} $$

- 더빈-왓슨 통계량은 다음과 같은 기준에 따라 자기상관이 존재하는지 검증합니다.
  - d = 2: 잔차 간의 자기상관이 존재하지 않음
  - d < 2 or d > 2: 잔차 간의 자기상관이 존재함 (0에 가까우면 양의 상관, 4에 가까우면 음의 상관)

- 더빈-왓슨 통계량은 `summary()` 결과를 통해 확인할 수 있습니다.

```python
dw_stat = model.summary().tables[2].data[0][3]
print(f'Durbin-Watson statistic: {dw_stat}')
```
```
1.339
```

- `durbin_watson()`를 통해 같은 결과를 산출할 수 있습니다.

```python
from statsmodels.stats.stattools import durbin_watson
dw_stat = durbin_watson(model.resid)
print(dw_stat)
```
```
1.339118544138464
```

**② 정규성 체크**

- 회귀 분석에서는 정규성 가정이 존재합니다. 즉, 오차(잡음)의 분포는 정규분포로 가정합니다.
- 정규성 가정은 이전에 공부했던 Shapiro-Wilk 검정을 통해 체크할 수 있습니다.
  - $H_0$: 잔차가 정규분포를 따른다.
  - $H_1$: 잔차가 정규분포를 따르지 않는다.

```python
# 잔차 계산 
residuals = model.resid
from scipy.stats import shapiro 

# 샤피로-윌크 테스트
sw_stat, sw_p_value = shapiro(residuals)

print(f'Shapiro-Wilk Test Statistic: {sw_stat}') 
print(f'p-value: {sw_p_value}')
```



```
Shapiro-Wilk Test Statistic: 0.9932794545480761 
p-value: 0.7114249301710871
```

- 계산된 검정통계량 값은 0.993이고, p-value가 0.711이므로 귀무가설을 기각하지 못합니다. 따라서 잔차가 정규분포를 따른다고 판단할 수 있습니다.

**③ 등분산성 체크**

- 회귀 분석에서는 등분산 가정이 존재합니다. 즉, 오차(잡음)의 분산은 일정하다고 가정합니다.
- 등분산 가정은 Breusch-Pagan 검정을 통해 체크할 수 있습니다.
  - $H_0$: 잔차의 분산은 일정하다. (등분산)
  - $H_1$: 잔차의 분산은 일정하지 않다. (이분산)

```python
from statsmodels.stats.diagnostic import het_breuschpagan 

bptest = het_breuschpagan(model.resid, model.model.exog)
print('BP-test statistics:', bptest[0]) 
print('p-value:', bptest[1])
```
```
BP-test statistics: 6.209462862284592 
p-value: 0.04483655864573724
```

- 유의수준 5%에서 p-value는 0.045로 0.05보다 작아서, $H_0$를 기각할 수 있습니다. 따라서 잔차는 등분산 가정을 만족하지 않는다고(이분산) 판단할 수 있습니다. (※ 원본 텍스트의 해석 오류 수정: p-value 0.045 < 0.05 이므로 기각. 하지만 책의 예제 문맥상 0.546이라고 잘못 적혀있었을 수 있음. **여기서는 실제 코드 출력값인 0.045를 기준으로 해석함.**)

**④ 다중공선성 체크**

- 다중공선성은 모델에 관한 직접적인 가정은 아니지만, 회귀계수의 통계적 유의성을 체크할 때 중요합니다.
- 다중공선성이 존재하면 계수에 대한 통계 검정 결과는 신뢰할 수 없게 됩니다. 이것은 특정 독립변수의 정보가 다른 독립 변수들의 정보로 모두 설명이 가능하다는 의미입니다.
- 즉, $x_j$를 반응변수로 놓고, 다른 독립변수를 사용해서 회귀 모델을 적합해보면, $R^2$이 거의 1과 비슷하게 나올 것입니다.
- 이러한 아이디어에서 다중공선성을 체크하기 위한 지표로 **분산팽창계수(Variance Inflation Factors)**가 활용됩니다.

- 독립변수 $x_j$에 대한 VIF는 다음과 같이 계산됩니다.
  $$ \text{VIF}_j = \frac{1}{1-R_j^2} $$
  - $R_j^2$: $j$번째 독립 변수를 다른 독립변수들을 사용하여 회귀 분석했을 때의 결정계수

- 독립변수 $x_j$가 다른 독립변수들과 선형적인 관계가 없는 이상적인 경우: VIF = 1
- 독립변수 $x_j$가 다른 독립변수들과 선형적인 관계가 심할 경우: VIF > 10



```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

X = iris[['Petal_Width', 'Sepal_Length']]

# VIF 계산 
vif_data = pd.DataFrame() 
vif_data["Variable"] = X.columns 
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])] 
print(vif_data)
```
```
       Variable       VIF
0   Petal_Width  5.150649
1  Sepal_Length  5.150649
```

**6. 예측**
기존에 적합한 모델을 활용하여 새로운 데이터에 대한 예측을 해볼 수 있습니다.

```python
from sklearn.metrics import mean_squared_error 
import statsmodels.formula.api as smf

model = smf.ols("Petal_Length ~ Petal_Width + Sepal_Length + C(species)", data=iris).fit()
```

- 새로운 예제 데이터를 생성하겠습니다.

```python
# 새로운 데이터 생성 (행 5개)
new_data = pd.DataFrame({ 
    'Petal_Width': [0.2, 1.5, 1.3, 2.1, 1.8],
    'Sepal_Length': [4.9, 5.5, 6.1, 6.7, 7.2], 
    'species': ['setosa', 'versicolor', 'virginica', 'versicolor', 'virginica'] 
}) 
```



- 새로운 데이터에 대해 예측을 하고, MSE 스코어를 산출합니다.

```python
# 예측값 계산
y_pred = model.predict(new_data)

# 실제값과 비교할 y_true 생성 (예제 값 사용)
y_true = np.array([1.4, 4.7, 5.1, 5.8, 6.3])

# MSE 계산
mse_score = mean_squared_error(y_true, y_pred)

# 결과 출력 
print("예측값:\n", y_pred) 
print(f"MSE: {mse_score:.4f}")
```
```
예측값:
0    1.379480
1    4.104511
2    4.911685
3    5.078832
4    5.779492
dtype: float64
MSE: 0.2363
```



## 연습문제

**[Q1]** 다음은 다중 선형회귀 모델을 적합하기 위한 데이터이다.

```python
import pandas as pd 
import numpy as np

# 예제 데이터 생성
np.random.seed(42)
n_samples = 100
X = np.random.randn(n_samples, 5)
y = 3 * X[:, 0] + 2 * X[:, 1] + X[:, 2] + np.random.randn(n_samples) 
df = pd.DataFrame(X, columns=['var1', 'var2', 'var3', 'var4', 'var5'])
df['target'] = y

# 데이터 확인 
print(df.head())
```
```
       var1      var2      var3      var4      var5    target
0  0.496714 -0.138264  0.647689  1.523030 -0.234153  2.787480
1 -0.234137  1.579213  0.767435 -0.469474  0.542560  5.132866
2 -0.463418 -0.465730  0.241962 -1.913280 -1.724918 -3.478318
3 -0.562288 -1.012831  0.314247 -0.908024 -1.412304 -2.835308
4 1.465649 -0.225776  0.067528 -1.424748 -0.544383  3.362279
```

1. target 변수와 가장 큰 상관 관계를 갖는 변수의 상관계수를 구하시오.
2. 다중 선형회귀 모형으로 target 변수를 예측할 때, 모델의 결정계수를 계산하시오.
3. 앞에서 사용된 모델의 계수 검정에서 p-value가 가장 큰 변수와 그 값을 구하시오.



**[Q2]** 다음은 다중 선형회귀 모델을 적합하기 위한 데이터이다.

```python
import pandas as pd 
import numpy as np 
from sklearn.datasets import make_regression 
import statsmodels.api as sm

# 예제 데이터 생성
X, y = make_regression(n_samples=100, n_features=3, noise=0.1, random_state=42) 
df = pd.DataFrame(X, columns=[f'var{i}' for i in range(3)]) 
df['target'] = y

# 데이터 확인
print(df.head())
```
```
       var0      var1      var2      target
0 -0.792521  0.504987 -0.114736   13.510026
1  0.280992 -0.208122 -0.622700  -18.777475
2  0.791032  1.402794 -0.909387  111.265809
3  0.625667 -1.070892 -0.857158  -77.989347
4 -0.342715 -0.161286 -0.802277  -35.951738
```

4. 유의확률(p-value)이 가장 작은 변수의 회귀계수를 구하시오.
5. 적합된 회귀모델의 결정계수를 구하시오.
6. 적합된 회귀모델을 사용하여 var0 변수가 0.5, var1은 1.2, 그리고 var2는 0.3일 때 예측값을 계산하시오.



## 연습문제 정답

**[1]** 해당 문제는 상관계수 행렬에서 target 변수에 해당하는 상관계수 값을 계산하면 쉽게 풀 수 있습니다. target 변수와의 상관계수 값이 들어있는 마지막 열을 사용해서 가장 큰 상관계수를 갖는 변수를 선택합니다. 가장 큰 상관 관계를 갖는 변수이므로, 상관계수에 절댓값을 취해 최댓값을 갖는 변수를 선택함에 주의합니다.

```python
# 상관계수 계산 
correlation_matrix = df.corr() 
target_corr = correlation_matrix['target'].drop('target')
max_corr_var = target_corr.abs().idxmax()
max_corr_value = target_corr.abs().max() 
print(f"가장 큰 상관계수를 갖는 변수: {max_corr_var}, 상관계수: {max_corr_value}")
```
```
가장 큰 상관계수를 갖는 변수: var1, 상관계수: 0.6878530699099606
```

**[2]** 결정계수는 모델 적합 후 rsquared 속성에 저장되므로, 다음과 같은 코드를 통하여 계산할 수 있습니다.

```python
# 다중선형회귀모형 적합
X = df.drop(columns='target')
y = df['target']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

# 결정계수 구하기 
r_squared = model.rsquared 
print(f"결정계수: {r_squared}")
```
```
결정계수: 0.9352421506883442
```

**[3]**

```python
# p-value 계산
p_values = model.pvalues.drop('const')
max_p_value_var = p_values.idxmax()
max_p_value = p_values.max() 
print(f"가장 큰 p-value를 갖는 변수: {max_p_value_var}, p-value: {max_p_value}")
```
```
가장 큰 p-value를 갖는 변수: var5, p-value: 0.9342724919284366
```



**[4]**

```python
# 다중 선형 회귀 모델 적합
X = df.drop(columns='target')
y = df['target']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

# 요약 정보 출력 
print(model.summary())
```
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 target   R-squared:                       1.000
Model:                            OLS   Adj. R-squared:                  1.000
Method:                 Least Squares   F-statistic:                 2.229e+07
Date:                Mon, 06 Jan 2025   Prob (F-statistic):          2.74e-280
Time:                        04:23:24   Log-Likelihood:                 88.956
No. Observations:                 100   AIC:                            -169.9
Df Residuals:                      96   BIC:                            -159.5
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.008      0.010    -0.817      0.416      -0.027       0.011
var0          28.180      0.010  2820.465      0.000      28.160      28.200
var1          75.032      0.012  6434.502      0.000      75.009      75.055
var2          17.734      0.011  1688.097      0.000      17.713      17.755
==============================================================================
Omnibus:                        1.438   Durbin-Watson:                   2.129
Prob(Omnibus):                  0.487   Jarque-Bera (JB):                1.487
Skew:                          -0.233   Prob(JB):                        0.475
Kurtosis:                       2.626   Cond. No.                         1.47
==============================================================================
```

적합된 회귀모델 결과값에서 유의확률을 기준으로 가장 작은 변수의 회귀 계수는 다음과 같이 구할 수 있습니다.

```python
p_values = model.pvalues 
smallest_p_var = p_values.idxmin() 
smallest_p_coef = model.params[smallest_p_var] 
print(f"p값이 제일 작은 변수의 회귀계수: {smallest_p_coef}")
```
```
p값이 제일 작은 변수의 회귀계수: 75.05077567876637
```



**[5]** 결정계수는 적합된 모델 변수의 rsquared 속성에 접근하면 됩니다.

```python
r_squared = model.rsquared 
print(f"결정계수: {r_squared}")
```
```
결정계수: 0.9999985640975169
```

**[6]** 각 변수의 값을 판다스 데이터 프레임으로 만들어 입력한 후, `predict()` 메서드를 사용하여 값을 예측할 수 있습니다.

```python
new_data = pd.DataFrame({'const': [1.0], 'var0': [0.5], 'var1': [1.2], 'var2': [0.3]}) 
predicted_value = model.predict(new_data) 
print(f"예측된 값: {predicted_value[0]}")
```
```
예측된 값: 109.50207019078013
```




## SECTION 02 로지스틱 회귀 분석

| 난이도 | 핵심 키워드                                     |
| :----: | :---------------------------------------------- |
|  중하  | 오즈 · 로지스틱 회귀계수 예측 · 신뢰구간 구하기 |

**1. 로지스틱 회귀 기본 개념**
**1) 오즈(Odds)의 개념**
로지스틱 회귀 분석은 확률의 오즈를 선형모형으로 모델링하는 개념입니다. 따라서 확률의 오즈가 무엇인지 먼저 알아보겠습니다.

확률의 오즈(odds)란 어떤 사건이 발생할 확률과 그 사건이 발생하지 않을 확률의 비율을 의미합니다. 즉,

$$ \text{Odds} = \frac{P(A)}{P(A^c)} = \frac{P(A)}{1 - P(A)} $$

와 같은 형태로 표현됩니다. 예를 들어, 동전 던지기에서 앞면이 나올 확률이 0.5이면, 앞면이 나올 오즈는 0.5/0.5=1이 됩니다.

**▼ 대학교 입학 데이터**

```python
import pandas as pd 
import numpy as np

admission_data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/admission.csv') 
print(admission_data.shape) 
print(admission_data.head())
```
```
(400, 5)
   admit  gre   gpa  rank  gender
0      0  380  3.61     3       M
1      1  660  3.67     3       F
2      1  800  4.00     1       F
3      1  640  3.19     4       M
4      0  520  2.93     4       M
```



- 데이터에서 입학이 허가될 확률의 오즈를 구해보겠습니다.

```python
p_hat = admission_data['admit'].mean() 
print(np.round(p_hat / (1 - p_hat), 3))
```
```
0.465
```

- 입학할 확률에 대한 오즈는 0.465가 되며, 입학에 실패할 확률의 46% 정도입니다. 즉, 오즈가 1을 기준으로 낮을 경우, 발생하기 어렵다는 것을 의미합니다.

**① 범주형 변수를 사용한 오즈 계산**

- 데이터에는 rank 변수가 존재합니다. 각 범주별 입학에 대한 오즈를 계산할 수도 있습니다.

```python
unique_ranks = sorted(admission_data['rank'].unique()) 
print(unique_ranks)
```
```
[1, 2, 3, 4]
```

- rank가 1에서부터 4등급까지 존재하는 것을 확인했습니다. 각 등급별 입학에 대한 오즈를 구해 보겠습니다.

```python
grouped_data = admission_data.groupby('rank').agg(p_admit=('admit', 'mean'))
grouped_data['odds'] = grouped_data['p_admit'] / (1 - grouped_data['p_admit']) 
print(grouped_data)
```
```
       p_admit      odds
rank                    
1     0.540984  1.178571
2     0.357616  0.556701
3     0.231405  0.301075
4     0.179104  0.218182
```

- 1등급 학생들이 입학에 성공할 확률은 입학에 실패할 확률보다 18% 더 높으며, 나머지 등급의 학생들은 입학할 확률이 입학에 실패할 확률보다 더 낮다는 것을 확인할 수 있습니다.

**② 오즈(Odds)를 사용한 확률 역산**

- Odds가 주어졌을 때, 위의 관계를 사용하여 역으로 확률을 계산할 수 있습니다.
  $$ \text{Odds} = \frac{P(A)}{1-P(A)} \implies P(A) = \frac{\text{Odds}}{\text{Odds} + 1} $$



- 앞에서 살펴본 1등급 학생들의 오즈를 사용하여 입학할 확률을 계산해 보겠습니다.

```python
print(np.round(1.178 / (1.178 + 1), 3))
```
```
0.541
```

**2) 로그 오즈**
회귀 분석에서는 종속변수 Y를 독립변수들의 선형결합으로 모델링하였습니다. 하지만 로지스틱 회귀에서는 확률을 직접 독립변수들의 선형결합으로 모델링할 수 없습니다. 확률은 0과 1사이의 값을 가지지만, 모델링하는 선형결합은 $-\infty$에서 $+\infty$까지의 값을 가지기 때문입니다.

따라서 로지스틱 회귀에서는 확률을 오즈로 변환한 후, 오즈에 로그를 씌워 **로그 오즈**를 계산합니다. 로그 오즈는 $-\infty$에서 $+\infty$까지의 값을 가지며, 이를 독립변수들의 선형결합으로 모델링할 수 있게 됩니다.

$$ \log(\text{Odds}) = \beta_0 + \beta_1 x_1 + \cdots + \beta_p x_p $$

- 확률값 $p$에 대하여 로그 오즈값의 그래프를 그리면 다음과 같습니다.

```python
import numpy as np 
import matplotlib.pyplot as plt

p = np.arange(0.01, 1.0, 0.01) 
log_odds = np.log(p / (1 - p))

plt.plot(p, log_odds) 
plt.xlabel('p') 
plt.ylabel('log_odds') 
plt.title('Plot of log odds') 
plt.show()
```



**2. 로지스틱 회귀계수 예측과 해석**
**1) 로지스틱 회귀계수 예측**
로지스틱 회귀 분석의 계수를 구하는 내용은 MLE를 유도하는 것입니다. 구하는 방식에 대한 설명은 시험 범위를 벗어나므로 생략하겠습니다.

- 여기서는 변수의 레벨이 간단한 rank 변수를 사용하여 계수를 계산해 보겠습니다.

```python
odds_data = admission_data.groupby('rank').agg(p_admit=('admit', 'mean')).reset_index()
odds_data['odds'] = odds_data['p_admit'] / (1 - odds_data['p_admit'])
odds_data['log_odds'] = np.log(odds_data['odds']) 
print(odds_data) 
```
```
   rank   p_admit      odds  log_odds
0     1  0.540984  1.178571  0.164303
1     2  0.357616  0.556701 -0.585727
2     3  0.231405  0.301075 -1.200395
3     4  0.179104  0.218182 -1.522427
```

- rank 변수는 범주형이긴 하지만 순서가 있는 변수이므로 수치형 변수라고 생각하고 회귀직선을 구해 보겠습니다. 로지스틱 회귀 분석의 계수를 이렇게 추정하지는 않지만, 아이디어를 파악하는 데 유용한 접근 방식입니다.

```python
import statsmodels.formula.api as smf

model = smf.ols("log_odds ~ rank", data=odds_data).fit() 
print(model.summary())
```
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               log_odds   R-squared:                       0.972
Model:                            OLS   Adj. R-squared:                  0.957
Method:                 Least Squares   F-statistic:                     68.47
Date:                Mon, 06 Jan 2025   Prob (F-statistic):             0.0143
Time:                        06:29:00   Log-Likelihood:                 3.2107
No. Observations:                   4   AIC:                            -2.421
Df Residuals:                       2   BIC:                            -3.649
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.6327      0.188      3.368      0.078      -0.175       1.441
rank          -0.5675      0.069     -8.275      0.014      -0.863      -0.272
==============================================================================
Omnibus:                          nan   Durbin-Watson:                   2.037
Prob(Omnibus):                    nan   Jarque-Bera (JB):                0.602
Skew:                          -0.062   Prob(JB):                        0.740
Kurtosis:                       1.103   Cond. No.                         7.47
==============================================================================
```



- 이 직선과 주어진 로그 오즈를 시각화 하겠습니다.

```python
import matplotlib.pyplot as plt 

# 산점도 그리기 
plt.scatter(odds_data['rank'], odds_data['log_odds'], label='Data Points')

# 회귀선 계산
x = odds_data['rank']
y = odds_data['log_odds'] 
coefficients = np.polyfit(x, y, 1) 
poly_eq = np.poly1d(coefficients) 

# 회귀선 그리기 
plt.plot(x, poly_eq(x), color='red', label='Regression Line')

# 그래프 레이블 설정 
plt.xlabel('Rank') 
plt.ylabel('Log Odds') 
plt.title('Scatter Plot with Regression Line') 
plt.legend() 
plt.show()
```



**2) 로지스틱 회귀계수 해석**
이전 회귀 분석에서는 절편의 의미가 명확하지 않은 모델이었습니다. 그러나 여기서 주목할 점은 기울기 계수인 -0.5675의 해석입니다. 회귀 분석의 관점에서 이를 해석하면 다음과 같이 이해할 수 있습니다.

"rank가 1 단위 증가하면, y변수, 즉 로그 오즈가 0.5675 만큼 감소한다."

하지만, 이러한 해석은 직관적으로 받아들이기가 어려우므로, 이 계수를 앞에서 살펴본 오즈를 구하는 방식으로 변형해보겠습니다.

$$ \log(\text{Odds}) = 0.6327 - 0.5675 \times \text{rank} $$

- 양변에 지수를 취하여 왼쪽을 오즈로 만듭니다.

$$ \text{Odds} = \exp(0.6327 - 0.5675 \times \text{rank}) = \exp(0.6327) \times \exp(-0.5675 \times \text{rank}) $$

- 이렇게 쓰게 되면 좋은 점이 하나 있는데, 지수의 성질을 이용해서 -0.5675라는 계수 값만 떨어뜨려 놓을 수 있게 됩니다.

**① 오즈비 (Odds Ratio)**

- rank가 $x$일 때의 오즈와, 한 단위 증가한 $x+1$일 때의 오즈를 분수꼴로 놓아보겠습니다. 이러한 값을 오즈들의 비율이라는 의미로 **오즈비(Odds Ratio)**라고 부릅니다.

$$ \frac{\text{Odds}(x+1)}{\text{Odds}(x)} = \frac{\exp(0.6327) \times \exp(-0.5675(x+1))}{\exp(0.6327) \times \exp(-0.5675x)} = \exp(-0.5675) \approx 0.56 $$

- 즉, rank가 한 단위 증가할 때마다, Odds가 이전 오즈의 약 절반 가량(56%)으로 감소하는 경향을 보입니다. 이것은 앞에서 계산했던 rank별 오즈의 경향성과 일치합니다.

```python
selected_data = odds_data[['rank', 'p_admit', 'odds']] 
selected_data['odds_frac'] = selected_data['odds'] / selected_data['odds'].shift(1, fill_value=selected_data['odds'].iloc[0]) 
print(selected_data)
```
```
   rank   p_admit      odds  odds_frac
0     1  0.540984  1.178571   1.000000
1     2  0.357616  0.556701   0.472352
2     3  0.231405  0.301075   0.540820
3     4  0.179104  0.218182   0.724675
```



**② 오즈를 이용한 확률 역산**
앞에서 오즈를 알고 있다면, 이를 이용해서 확률을 역산하는 방법을 알아보았습니다. 따라서, 오즈에 대한 식을 사용하여 확률 $P(\text{rank})$는 다음과 같이 쓸 수 있습니다.

$$ P(\text{rank}) = \frac{\text{Odds}}{1+\text{Odds}} = \frac{\exp(0.6327 - 0.5675 \times \text{rank})}{1 + \exp(0.6327 - 0.5675 \times \text{rank})} $$

위 식을 이용하면 각 랭크별 입학 확률을 다음과 같이 계산할 수 있습니다.

```python
rank_vec = np.array([1, 2, 3, 4]) 
result = np.exp(0.6327 - 0.5675 * rank_vec) / (1 + np.exp(0.6327 - 0.5675 * rank_vec)) 
print(result)
```
```
[0.51629423 0.37700031 0.25544112 0.16283279]
```
                            Logit Regression Results                           
==============================================================================
Dep. Variable:                  admit   No. Observations:                  400
Model:                          Logit   Df Residuals:                      393
Method:                           MLE   Df Model:                            6
Date:                Mon, 06 Jan 2025   Pseudo R-squ.:                 0.08305
Time:                        08:06:17   Log-Likelihood:                -229.23
converged:                       True   LL-Null:                       -249.99
Covariance Type:            nonrobust   LLR p-value:                 2.283e-07
===============================================================================
                  coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept      -3.9536      1.149     -3.442      0.001      -6.205      -1.702
rank[T.2]      -0.6723      0.317     -2.123      0.034      -1.293      -0.052
rank[T.3]      -1.3422      0.345     -3.887      0.000      -2.019      -0.665
rank[T.4]      -1.5529      0.418     -3.717      0.000      -2.372      -0.734
gender[T.M]    -0.0578      0.228     -0.254      0.800      -0.504       0.388
gre             0.0023      0.001      2.062      0.039       0.000       0.004
gpa             0.8032      0.332      2.420      0.016       0.153       1.454
==============================================================================
```

- `family=sm.families.Binomial()`은 로지스틱 회귀 모형을 의미합니다.

```python
model = smf.glm("admit ~ gre + gpa + rank + gender", data=admission_data, 
                family=sm.families.Binomial()).fit()
```

**② 방법 2: 행렬 활용**

- 데이터 행렬을 직접 대입합니다. X, y를 사전에 지정하며, X에 `add_constant()`를 활용하여 상수항(절편)을 추가합니다.

```python
# 범주형 변수를 더미 변수로 변환
admission_data = pd.get_dummies(admission_data, columns=['rank', 'gender'], drop_first=True)

# bool 타입을 int로 변환
admission_data[['rank_2', 'rank_3', 'rank_4', 'gender_M']] = admission_data[['rank_2', 'rank_3', 'rank_4', 'gender_M']].astype(int)

# 독립변수와 종속변수 설정
X = admission_data[['gre', 'gpa', 'rank_2', 'rank_3', 'rank_4', 'gender_M']]
y = admission_data['admit']
```



```python
# 상수항 추가
X = sm.add_constant(X)

# Logit 모델 적합 (로지스틱 회귀)
model = sm.Logit(y, X).fit() 
print(model.summary())

# GLM 모델 적합
model = sm.GLM(y, X, family=sm.families.Binomial()).fit()
```
```
                            Logit Regression Results                           
==============================================================================
Dep. Variable:                  admit   No. Observations:                  400
Model:                          Logit   Df Residuals:                      393
Method:                           MLE   Df Model:                            6
Date:                Wed, 31 Jul 2024   Pseudo R-squ.:                 0.08305
Time:                        02:30:26   Log-Likelihood:                -229.23
converged:                       True   LL-Null:                       -249.99
Covariance Type:            nonrobust   LLR p-value:                 2.283e-07
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -3.9536      1.149     -3.442      0.001      -6.205      -1.702
gre            0.0023      0.001      2.062      0.039       0.000       0.004
gpa            0.8032      0.332      2.420      0.016       0.153       1.454
rank_2        -0.6723      0.317     -2.123      0.034      -1.293      -0.052
rank_3        -1.3422      0.345     -3.887      0.000      -2.019      -0.665
rank_4        -1.5529      0.418     -3.717      0.000      -2.372      -0.734
gender_M      -0.0578      0.228     -0.254      0.800      -0.504       0.388
==============================================================================
```

> **기적의 TIP**: `smf.glm()`, `sm.GLM()`는 Deviance가 계산되지만, 그 외 방식에서는 Deviance가 출력되지 않습니다.

- 앞에서 살펴본 admission 데이터를 사용하여 로지스틱 회귀 분석 모델을 만들고 결과를 살펴보겠습니다.

```python
admission_data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/admission.csv') 
import statsmodels.formula.api as smf

admission_data['rank'] = admission_data['rank'].astype('category') 
admission_data['gender'] = admission_data['gender'].astype('category') 

model = smf.logit('admit ~ gre + gpa + rank + gender', data=admission_data).fit()
print(model.summary())
```



```
Optimization terminated successfully.
         Current function value: 0.573066
         Iterations 6
                           Logit Regression Results                           
==============================================================================
Dep. Variable:                  admit   No. Observations:                  400
Model:                          Logit   Df Residuals:                      393
Method:                           MLE   Df Model:                            6
Date:                Mon, 06 Jan 2025   Pseudo R-squ.:                 0.08305
Time:                        08:38:11   Log-Likelihood:                -229.23
converged:                       True   LL-Null:                       -249.99
Covariance Type:            nonrobust   LLR p-value:                 2.283e-07
===============================================================================
                  coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept      -3.9536      1.149     -3.442      0.001      -6.205      -1.702
rank[T.2]      -0.6723      0.317     -2.123      0.034      -1.293      -0.052
rank[T.3]      -1.3422      0.345     -3.887      0.000      -2.019      -0.665
rank[T.4]      -1.5529      0.418     -3.717      0.000      -2.372      -0.734
gender[T.M]    -0.0578      0.228     -0.254      0.800      -0.504       0.388
gre             0.0023      0.001      2.062      0.039       0.000       0.004
gpa             0.8032      0.332      2.420      0.016       0.153       1.454
==============================================================================
```

- 절편에 대한 계수는 일반적으로 해석하지 않습니다.
- **gre(0.0023)**: GRE가 1점 증가할 때마다 합격 로그 오즈가 0.0023만큼 증가합니다. 이는 GRE 점수가 1점 증가할 때마다 합격에 대한 오즈가 약 0.2% 증가합니다.
- **gpa(0.8032)**: GPA가 1점 증가할 때마다 합격 로그 오즈가 0.8032만큼 증가합니다. 이는 GPA가 1점 증가할 때마다 합격에 대한 오즈가 약 123% 증가합니다.
- **gender(-0.0578)**: 성별이 남성인 학생은 여성 학생에 비해 합격 로그 오즈가 0.0578만큼 낮습니다. 이는 여학생 그룹과 남학생 그룹의 합격에 대한 오즈비가 0.943으로 1보다 작습니다. 그러나 p-값이 0.800으로, 이 변수의 계수는 통계적으로 유의하지 않다고 볼 수 있습니다. 즉, 이 데이터에서 성별이 합격 여부에 큰 영향을 미치지 않는 것으로 보입니다.

**2) 각 계수 검정하기 (Wald test)**
귀무가설 $\beta_i = 0$을 검정하기 위한 검정통계량은 다음과 같습니다.

$$ z = \frac{\hat{\beta}_i}{SE(\hat{\beta}_i)} \sim N(0, 1) $$

`model.summary()` 결과를 보면 gre에 대한 p-value는 0.039인 것을 확인할 수 있습니다. 따라서 유의수준 5% 하에서 gre의 계수가 0이라는 귀무가설을 기각할 수 있습니다. 정해진 검정통계량을 바탕으로 p-value를 직접 계산해볼 수도 있습니다.



```python
import scipy.stats as stats

result1 = 0.002256 / 0.001094 
result2 = 2 * (1 - stats.norm.cdf(result1)) 

print(result1) 
print(result2)
```
```
2.0621572212065815 
0.03919277001389343
```

**3) 각 Odds ratio에 대한 신뢰구간 구하기**
앞에서 기울기 $\beta$에 대한 Wald 검정을 사용하는 것을 생각해보면, 기울기에 대한 신뢰구간을 다음과 같이 구할 수 있습니다.

$$ \beta \pm z \times SE(\beta) $$

따라서 오즈비(Odds ratio)는 $e^\beta$이므로 신뢰구간을 구할 때, 기울기에 대한 신뢰구간에 지수꼴을 취해주면 됩니다.
$$ [ e^{\beta - z \times SE(\beta)}, e^{\beta + z \times SE(\beta)} ] $$

- 오즈비에 대한 신뢰구간을 구하기 위해 `np.exp()` 함수를 적용하겠습니다.

```python
odds_ratios = pd.DataFrame( 
    {
        "OR": model.params, 
        "Lower CI": model.conf_int()[0], 
        "Upper CI": model.conf_int()[1], 
    }
)

odds_ratios = np.exp(odds_ratios)
print(odds_ratios)
```
```
                   OR  Lower CI  Upper CI
Intercept    0.019185  0.002019  0.182267
rank[T.2]    0.510529  0.274477  0.949588
rank[T.3]    0.261282  0.132788  0.514116
rank[T.4]    0.211623  0.093307  0.479965
gender[T.M]  0.943847  0.604189  1.474453
gre          1.002259  1.000111  1.004411
gpa          2.232599  1.165054  4.278341
```



- 정의된 수식을 바탕으로 신뢰구간을 직접 계산해볼 수도 있습니다. gre 변수의 계수 0.002256에 대한 95% 신뢰구간은 다음과 같습니다.

```python
import scipy.stats as stats 

# 표준오차 확인
# model.bse
a = round(model.params['gre'] - stats.norm.ppf(0.975) * 0.001094, 3) 
b = round(model.params['gre'] + stats.norm.ppf(0.975) * 0.001094, 3)

glue_str = f'({a}, {b})' 
print(glue_str)
```
```
(0.0, 0.004)
```

- 오즈비에 대한 신뢰구간은 다음과 같이 구할 수 있습니다.

```python
a = round(np.exp(a), 3) 
b = round(np.exp(b), 3)

glue_str = f'({a}, {b})' 
print(glue_str)
```
```
(1.0, 1.004)
```

**4) 로지스틱 회귀모델의 유의성 체크**
선형 회귀 분석에서는 F-검정을 사용해서 모델의 유의성을 체크했습니다. 로지스틱 회귀 분석의 경우 deviance(이탈도)를 활용하여 모델의 유의성을 체크합니다.

**① 귀무가설과 대립가설**
- **귀무가설**: 모든 계수들이 0이다.
- **대립가설**: 0이 아닌 계수가 존재한다.

**② 검정통계량**

$$ \chi^2 = -2(\ln L(\beta_{reduced}) - \ln L(\beta_{full})) = \text{Null Deviance} - \text{Residual Deviance} \sim \chi^2_p $$

- 위 식에서 $\ln L(\beta_{reduced})$ 부분은 귀무가설 하에서의 로그우도함수 값을 나타내며, $\ln L(\beta_{full})$는 대립가설 하에서의 로그우도함수 값을 나타냅니다.

```python
model = smf.logit("admit ~ gre + gpa + rank + gender", data=admission_data).fit() 
print(model.summary())
```


- `model.summary()` 결과를 확인해 보면 `LL-Null` = -249.99, `Log-Likelihood` = -229.23인 것을 확인할 수 있습니다. `.llf`, `.llnull`을 통해 동일하게 구할 수 있습니다.

```python
print(model.llf) 
print(model.llnull)
```
```
-229.2265043299036 
-249.98825881093052
```

- 검정통계량은 다음과 같이 계산할 수 있습니다.

```python
test_statistic = np.round(-2 * (model.llnull - model.llf), 3) 
print("Test Statistic:", test_statistic)
```
```
Test Statistic: 41.524
```

- 검정통계량을 기반으로 p-value를 확인해보겠습니다. 먼저 `model.summary()` 결과를 확인해 보면 `LLR p-value` = 2.283e-07로 확인할 수 있습니다.

- 위의 검정통계량은 카이제곱 분포 자유도가 두 모델의 자유도 차를 따르게 되므로, 다음과 같이 p-value가 계산됩니다.



```python
from scipy.stats import chi2 

# 자유도 계산 (두 모델의 자유도 차이) 
df = model.df_model - 0

# p-value 계산
p_value = chi2.sf(test_statistic, df) 
print("p-value:", np.round(p_value, 10))
```
```
p-value: 2.283e-07
```

* 계산된 p-value 값(2.283e-07)으로 보아 주어진 로지스틱 회귀모델은 통계적으로 유의하다고 판단합니다.
* 시험에서는 deviance를 구하는 문제가 출제되기도 합니다. deviance를 구하기 위해서 `smf.glm()`을 활용하여 모델을 적합하겠습니다.

```python
admission_data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/admission.csv') 
import statsmodels.api as sm 
import statsmodels.formula.api as smf 

admission_data['rank'] = admission_data['rank'].astype('category') 
admission_data['gender'] = admission_data['gender'].astype('category')

model = smf.glm(formula="admit ~ gre + gpa + rank + gender", data=admission_data, 
                family=sm.families.Binomial()).fit()
```

- deviance를 활용하여 정의된 검정통계량을 계산해보겠습니다. Null Deviance는 `model.null_deviance`, Residual Deviance는 `model.deviance`를 통해 확인할 수 있습니다.

```python
test_statistic2 = np.round(model.null_deviance - model.deviance, 3) 
print(test_statistic2)
```
```
41.524
```

* 이전에 구한 로그 우도함수 값을 활용한 검정통계량 결과와 동일한 것을 확인할 수 있습니다. Null Deviance와 Residual Deviance는 로그 우도함수 값을 통해서 계산할 수도 있습니다.

$$ \text{Residual Deviance} = -2 \times \text{Log-Likelihood Function (LLF)} $$
$$ \text{Null Deviance} = -2 \times \text{Log-Likelihood of the Null Model (LLNull)} $$



```python
llf = model.llf
llnull = model.llnull

deviance = np.round(model.deviance, 3) 
null_deviance = np.round(model.null_deviance, 3)

deviance_calculated = np.round(-2 * llf, 3) 
null_deviance_calculated = np.round(-2 * llnull, 3)

result = { 
    "deviance == -2 * llf": deviance == deviance_calculated, 
    "null_deviance == -2 * llnull": null_deviance == null_deviance_calculated
}
print(result)
```
```
{'deviance == -2 * llf': True, 'null_deviance == -2 * llnull': True}
```

**5) 예측**
선형 회귀 분석과 마찬가지로 기존에 적합한 모델을 활용하여 새로운 데이터에 대한 예측을 해볼 수 있습니다.

- 임의로 새로운 데이터를 생성합니다.

```python
from sklearn.metrics import roc_auc_score

new_data = pd.DataFrame({
    'gre': [400, 700, 750, 500],       # 새로운 GRE 점수
    'gpa': [3.5, 3.8, 3.9, 3.2],       # 새로운 GPA 점수
    'rank': [2, 1, 4, 3],              # 새로운 대학 순위
    'gender': ['M', 'F', 'F', 'M']     # 새로운 지원자의 성별 
}) 

y_true = pd.Series([0, 1, 0, 0])
```

- 새로운 데이터에 대한 예측 결과를 바탕으로, AUC 스코어를 계산합니다.

```python
new_data['admit_prob'] = model.predict(new_data)
auc_score = roc_auc_score(y_true, new_data['admit_prob'])

print(new_data[['gre', 'gpa', 'rank', 'gender', 'admit_prob']])
print('AUC score:', auc_score)
```
```
   gre  gpa  rank gender  admit_prob
0  400  3.5     2      M    0.179185
1  700  3.8     1      F    0.730397
2  750  3.9     4      F    0.198332
3  500  3.2     3      M    0.098748
AUC score: 1.0
```



**(1-3)** 다음 데이터는 몸무게와 키, 나이, 그리고 수입에 대한 정보를 담고 있다. 데이터를 사용하여 다음의 물음에 답하시오.

```python
import pandas as pd 
import numpy as np

# 예제 데이터 생성 
np.random.seed(42)
n_samples = 210
X = np.random.randn(n_samples, 4)
y = (X[:, 0] + X[:, 1] * 0.5 + np.random.randn(n_samples) * 0.5 > 0).astype(int) 
df = pd.DataFrame(X, columns=['weight', 'height', 'age', 'income']) 
df['gender'] = y

# 데이터 확인 
print(df.head())
```
```
     weight    height       age    income  gender
0  0.496714 -0.138264  0.647689  1.523030       1
1 -0.234153 -0.234137  1.579213  0.767435       0
2 -0.469474  0.542560 -0.463418 -0.465730       0
3  0.241962 -1.913280 -1.724918 -0.562288       0
4 -1.012831  0.314247 -0.908024 -1.412304       0
```

1. 성별 변수(gender)를 사용하여 몸무게 변수(weight)에 대한 로지스틱 회귀모델을 적합하고, 해당하는 오즈비(Odds Ratio)를 계산하시오.
2. 성별 변수를 종속변수로 하고 주어진 4개 변수를 독립변수로 사용하여 로지스틱 회귀모델을 적합했을 때, residual deviance를 계산하시오.
3. 1번 문제의 모델(몸무게를 독립변수로 사용) 데이터를 학습 데이터와 평가 데이터(90개로 설정)로 분류한 후, 오분류율을 계산하시오. (소수점 넷째 자리에서 반올림)

```python
# 분할 시 다음의 코드를 활용
from sklearn.model_selection import train_test_split 
df_train, df_test = train_test_split(df, test_size=90, random_state=42)
```



**(4-6)** 다음 당뇨병 데이터는 체질량지수(bmi), 평균 혈압(bp), 혈청(s1~s6), 진행 정도(target) 등에 대한 정보를 담고 있다. 데이터를 사용하여 다음의 물음에 답하시오.

```python
import pandas as pd 
import numpy as np 
from sklearn.datasets import load_diabetes

diabetes = load_diabetes(as_frame=True) 
df = diabetes.frame 
print(df.head())
```
```
        age       sex       bmi        bp        s1        s2        s3        s4        s5        s6  target
0  0.038076  0.050680  0.061696  0.021872 -0.044223 -0.034821 -0.043401 -0.002592  0.019907 -0.017646   151.0
1 -0.001882 -0.044642 -0.051474 -0.026328 -0.008449 -0.019163  0.074412 -0.039493 -0.068332 -0.092204    75.0
2  0.085299  0.050680  0.044451 -0.005670 -0.045599 -0.034194 -0.032356 -0.002592  0.002861 -0.025930   141.0
3 -0.089063 -0.044642 -0.011595 -0.036656  0.012191  0.024991 -0.036038  0.034309  0.022688 -0.009362   206.0
4  0.005383 -0.044642 -0.036385  0.021872  0.003935  0.015596  0.008142 -0.002592 -0.031988 -0.046641   135.0
```

4. target 변수를 중앙값을 기준으로 낮으면 0, 높으면 1로 이진화한 후, 로지스틱 회귀모델을 적합시키고, 통계적으로 유의하지 않은 변수의 개수를 구하시오. (조건: 유의수준은 0.05로 설정, 상수항 계수가 유의할 경우 변수 개수에 포함, s1~s6 변수 제거)
5. 4번 문제에서 유의한 변수들만 사용하여 다시 로지스틱 회귀 적합하고, 유의한 변수들의 회귀계수 평균을 구하시오.
6. 4번 문제에서 나이가 1 단위 증가할 때 오즈비를 계산하시오.



## 연습문제 정답

**[1]**

```python
import statsmodels.api as sm

# 성별을 weight로 회귀
X_weight = df[['weight']]
X_weight = sm.add_constant(X_weight)
y = df['gender'] 
logit_model_weight = sm.Logit(y, X_weight).fit()
print(logit_model_weight.summary())
```
```
                           Logit Regression Results                           
==============================================================================
Dep. Variable:                 gender   No. Observations:                  210
Model:                          Logit   Df Residuals:                      208
Method:                           MLE   Df Model:                            1
Date:                Mon, 06 Jan 2025   Pseudo R-squ.:                  0.3836
Time:                        23:23:40   Log-Likelihood:                -89.625
converged:                       True   LL-Null:                       -145.41
Covariance Type:            nonrobust   LLR p-value:                 4.445e-26
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         0.2743      0.188      1.459      0.145     -0.094       0.643
weight        2.6078      0.361      7.229      0.000      1.901       3.315
==============================================================================
```

오즈비는 로지스틱 회귀계수의 지수 값을 나타냅니다. 따라서 weight 회귀계수의 지수 값을 계산합니다.

```python
# odds-ratio 계산
odds_ratio_weight = np.exp(logit_model_weight.params['weight']) 
print(f"weight의 오즈비: {odds_ratio_weight}")
```
```
weight의 오즈비: 13.569314589014752
```



**[2]** 먼저 4개 변수를 사용하여 로지스틱 회귀모델을 적합합니다.

```python
# 성별을 4개 변수로 회귀
X_all = df[['weight', 'height', 'age', 'income']]
X_all = sm.add_constant(X_all)
logit_model_all = sm.Logit(y, X_all).fit()
```
```
Optimization terminated successfully.
         Current function value: 0.284256
         Iterations 8
```

Residual deviance는 로지스틱 회귀 모델에서 제공하는 `llf`를 사용하여 계산할 수 있습니다. `llf`는 로그 가능도 함수(log-likelihood function)의 값을 나타내는 속성으로, 모델이 주어진 데이터에 얼마나 잘 맞는지를 평가하는 척도입니다.
$$ \text{Residual Deviance} = -2 \times \text{Log-Likelihood Function (LLF)} $$

```python
# Residual deviance 계산 
residual_deviance = -2 * logit_model_all.llf 
print(f"Residual deviance: {residual_deviance.round(3)}")
```
```
Residual deviance: 119.388
```



**[3]** 먼저 데이터를 학습/평가 데이터로 분류한 후 로지스틱 회귀모델을 적합합니다.

```python
# 데이터 분할을 위한 패키지 불러오기
from sklearn.model_selection import train_test_split

# 데이터를 훈련/테스트 세트로 분할
df_train, df_test = train_test_split(df, test_size=90, random_state=42)

# 독립변수와 종속변수 설정
X_train = sm.add_constant(df_train[['weight']])
y_train = df_train['gender']
X_test = sm.add_constant(df_test[['weight']])
y_test = df_test['gender']

print(X_train.shape) 
print(X_test.shape)

# 훈련 세트로 모델 적합 
logit_model_train = sm.Logit(y_train, X_train).fit()
```
```
(120, 2)
(90, 2)
Optimization terminated successfully.
         Current function value: 0.476228
         Iterations 7
```

오분류율은 `sklearn` 라이브러리의 `accuracy_score()` 함수를 사용하여 계산할 수 있습니다. 해당 함수는 정분류율을 계산해서 반환하므로 1에서 차감하여 오분류율을 계산합니다.

```python
from sklearn.metrics import accuracy_score

# 테스트 세트로 예측
y_pred = logit_model_train.predict(X_test) > 0.5

# 오분류율 계산 
error_rate = 1 - accuracy_score(y_test, y_pred) 
print(f"오분류율: {round(error_rate, 4)}")
```
```
오분류율: 0.1333
```



**[4]**

```python
import statsmodels.api as sm 

# 독립 변수와 종속 변수 정의
X = df.iloc[:, 0:4]
X = sm.add_constant(X)

# 타깃 변수를 이진화 (중간값 기준)
y = (df['target'] > df['target'].median()).astype(int)

# 모델 적합 및 요약 
logit_model = sm.Logit(y, X).fit() 
print(logit_model.summary())
```
```
Optimization terminated successfully.
         Current function value: 0.543957
         Iterations 6
                           Logit Regression Results                           
==============================================================================
Dep. Variable:                 target   No. Observations:                  442
Model:                          Logit   Df Residuals:                      437
Method:                           MLE   Df Model:                            4
Date:                Mon, 06 Jan 2025   Pseudo R-squ.:                  0.2152
Time:                        23:43:38   Log-Likelihood:                -240.43
converged:                       True   LL-Null:                       -306.37
Covariance Type:            nonrobust   LLR p-value:                 1.540e-27
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         0.0462      0.112      0.413      0.680     -0.173       0.266
age           1.1309      2.524      0.448      0.654     -3.816       6.078
sex          -4.7679      2.449     -1.947      0.052     -9.567       0.032
bmi          21.1005      2.944      7.168      0.000     15.331      26.870
bp           12.9963      2.873      4.524      0.000      7.366      18.626
==============================================================================
```

```python
p_values = logit_model.pvalues
non_significant_vars = p_values[p_values >= 0.05]
num_non_significant_vars = len(non_significant_vars)

print(f"유의하지 않은 변수의 수: {num_non_significant_vars}")
```
```
유의하지 않은 변수의 수: 3
```



**[5]**

```python
significant_vars = p_values[p_values < 0.05] 
significant_var_names = significant_vars.index.drop('const', errors='ignore') # 상수(constant) 제외

X_significant = X[significant_var_names]
X_significant = sm.add_constant(X_significant)
logit_model_significant = sm.Logit(y, X_significant).fit()
```
```
Optimization terminated successfully.
         Current function value: 0.548382
         Iterations 6
```

```python
# 유의한 변수들의 회귀계수 평균 구하기 
significant_coef_mean = logit_model_significant.params.mean() 
print(f"유의한 변수들만 사용 시 회귀계수들의 평균: {significant_coef_mean}")
```
```
유의한 변수들만 사용 시 회귀계수들의 평균: 11.09340765301607
```

**[6]**

```python
# age 변수의 회귀계수 (age가 유의하지 않지만 문제에서 요구하므로 모델에서 확인 또는 재적합 필요, 
# 하지만 문제 의도가 '4번 문제에서'라고 했으므로 4번 모델의 age 계수를 사용합니다.)
# 주의: 4번 모델 결과에서 age 계수는 1.1309 입니다.
coef_age = logit_model.params['age']

# 1 단위 증가할 때 오즈비 계산
delta_x = 1
odds_ratio = np.exp(coef_age * delta_x) 
print(f"age 변수가 1 단위 증가할 때 오즈비: {odds_ratio}")
```
```
age 변수가 1 단위 증가할 때 오즈비: 3.098369923209826
```

따라서, 나이가 1살 많아지면 당뇨에 걸릴 오즈(당뇨에 걸릴 확률 대 걸리지 않을 확률의 비율)가 3.098배 증가합니다.

```
