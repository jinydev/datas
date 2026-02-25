# PART 07
# 최신 기출문제 정답 & 해설

**시험 시간**: 180분 | **풀이 시간**: - | **합격 점수**: 60점 | **내점수**: -

## 기출문제 제10회 (2025-06-21 시행)

데이터셋 경로: `https://raw.githubusercontent.com/YoungjinBD/data/main/exam/`

### 작업형 제1유형

**1.** 소주제별 정답률 계산

```python
import pandas as pd
import numpy as np 
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/10_1_1.csv') 
print(df.head())
```
*Output:*
```
   학생ID  문제ID 대주제 소주제  정답여부
0  1001     1   과학   동물     0
1  1001     2   사회   정치     1
2  1001     3   과학   지구     0
3  1001     4   과학   식물     0
4  1001     5   수학   측정     1
```

- 소주제별 정답률을 계산합니다.
```python
numer = df.groupby(["소주제"])["정답여부"].sum()
denom = df.groupby(["소주제"])["정답여부"].count()
ratio = np.round((numer / denom), 2)
```


- (방법1) 정답률을 내림차순으로 정렬한 후 세 번째로 높은 정답률인 소주제를 확인합니다.
```python
print(ratio.sort_values(ascending=False).head())
```
*Output:*
```
소주제
독해    0.74
듣기    0.70
문법    0.70
경제    0.68
지구    0.66
Name: 정답여부, dtype: float64
```

- (방법2) 정답률 중복 제거 후 내림차순으로 정렬하여, 세 번째로 높은 정답률을 계산합니다. 또한, 세 번째로 높은 정답률에 대응되는 소주제를 확인합니다.

```python
unique_ratios = sorted(ratio.unique(), reverse=True) 
third = unique_ratios[2]
third_subs = ratio[ratio == third].index.tolist()
print(f"\n3번째로 높은 정답률: {third}") 
print("소주제:", third_subs)
```
*Output:*
```
3번째로 높은 정답률: 0.68
소주제: ['경제']
```

**2.** 두 번째로 큰 매출액과 조건에 맞는 카테고리별 합계

```python
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/10_1_2.csv') 
print(df.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 250 entries, 0 to 249
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   date          250 non-null    object
 1   category      250 non-null    object
 2   item          250 non-null    object
 3   price         250 non-null    int64 
dtypes: int64(1), object(3)
memory usage: 7.9+ KB
None
```

- date 칼럼이 object형이므로, 전처리 편의를 위해 날짜형으로 변환합니다.
```python
df["date"] = pd.to_datetime(df["date"])
```

- date 칼럼에서 년, 월 칼럼을 새롭게 생성합니다.
```python
df["year"] = df["date"].dt.year 
df["month"] = df["date"].dt.month
```

- 년-월별 price의 합계를 계산하고, 두 번째로 큰 매출액(합계)을 계산합니다.
```python
monthly_sales = ( 
    df.groupby(["year", "month"])["price"].sum().sort_values(ascending=False)
)
print('두 번째로 큰 price(합계):', monthly_sales.iloc[1])
```
*Output:*
```
두 번째로 큰 price(합계): 1777389
```

- 네 번째로 큰 price 합계에 해당하는 년-월을 찾습니다.
- 해당 년-월에서 카테고리별 price 합계를 구한 다음 가장 높은 값을 출력합니다.


```python
year, month = monthly_sales.reset_index().iloc[3][["year", "month"]]
df_sub = df.loc[(df['year'] == year) & (df['month'] == month), :] 
print('price 합계:', df_sub.groupby('category')['price'].sum().max())
```
*Output:*
```
price 합계: 1012500
```

**3.** 스팸/햄 메시지 단어 수 평균 차이

```python
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/10_1_3.csv') 
print(df.head())
```
*Output:*
```
                                             message label
0  You have won a free vacation to Hawaii! Reply ...  spam
1  Your account will be locked in 24 hours. Act now.  spam
2           Hey, are you coming to the meeting later?   ham
3  Don't forget to pick up milk on your way home.     ham
4  Special discount! 50% off on all shoes today a...  spam
```

- `str.split()` 메서드를 사용하여 각 문장을 공백 기준으로 나눈 뒤, 나눠진 단어의 개수를 계산하여 새로운 칼럼에 저장합니다.
```python
df['word_count'] = df["message"].str.split(' ').apply(len)
```

- 'spam', 'ham' 각각의 평균 단어 수를 계산합니다.
```python
mean_word_count = df.groupby('label')['word_count'].mean() 
print(mean_word_count)
```
*Output:*
```
label
ham     6.232143
spam    6.531915
Name: word_count, dtype: float64
```


- 'spam', 'ham'의 평균 차이를 계산합니다.
```python
result = np.round(abs(mean_word_count["spam"] - mean_word_count["ham"]), 3) 
print(result)
```
*Output:*
```
0.3
```

### 작업형 제2유형

**가스 소비량 예측 모델**

```python
import pandas as pd 
import numpy as np 
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/10_2_train.csv') 
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/10_2_test.csv')
```


**1. 데이터 탐색**

- 모델을 적합하기 전 데이터에 결측치가 있는지 확인해야 합니다. 결측치가 존재할 경우 모델 적합 시 에러가 발생할 수 있습니다.

```python
print(train.info()) 
print(test.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 160 entries, 0 to 159
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   biz_type        160 non-null    object
 1   area            160 non-null    float64
 2   age             160 non-null    int64  
 3   num_households  160 non-null    int64  
 4   gas_totl        160 non-null    int64  
dtypes: float64(1), int64(3), object(1)
memory usage: 6.4+ KB
None
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 40 entries, 0 to 39
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   biz_type        40 non-null     object
 1   area            40 non-null     float64
 2   age             40 non-null     int64  
 3   num_households  40 non-null     int64  
 4   gas_totl        0 non-null      float64
dtypes: float64(2), int64(2), object(1)
memory usage: 1.7+ KB
None
```
- `gas_totl`이 0인 경우는 전체 12.5%에 해당합니다. `gas_totl`이 0인 경우는 삭제합니다.

```python
train = train.loc[train['gas_totl'] != 0, :] 
train_X = train.drop(["gas_totl"], axis=1) 
train_y = train["gas_totl"]
test_X = test.drop(["gas_totl"], axis=1) 
test_y = test["gas_totl"]
```


**2. 데이터 분할**

- 모델 성능 확인을 위해 훈련 데이터의 일부를 검증 데이터로 나눕니다.
```python
from sklearn.model_selection import train_test_split 
train_X, valid_X, train_y, valid_y = train_test_split( 
    train_X, train_y, test_size=0.3, random_state=1
)
```

**3. 데이터 전처리**

- 범주형 변수에 대해서 원-핫 인코딩을 수행하겠습니다. 범주형 변수와 수치형 변수의 각 칼럼명을 저장합니다.

```python
cat_columns = train_X.select_dtypes('object').columns
num_columns = train_X.select_dtypes('number').columns
```
- one-hot 인코딩을 위한 메서드를 불러옵니다.
```python
from sklearn.preprocessing import OneHotEncoder 
onehotencoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore").set_output(transform="pandas")
```

- 훈련 데이터와 검증 데이터, 테스트 데이터에 대해 전처리를 진행합니다. 전처리 결과는 `set_output(transform='pandas')`로 설정했으므로, `pandas.DataFrame`으로 출력됩니다.

```python
train_X_cat_preprocessed = onehotencoder.fit_transform(train_X[cat_columns])
valid_X_cat_preprocessed = onehotencoder.transform(valid_X[cat_columns]) 
test_X_cat_preprocessed = onehotencoder.transform(test_X[cat_columns]) 
train_X_preprocessed = pd.concat( 
    [train_X_cat_preprocessed, train_X[num_columns]], axis=1
)
valid_X_preprocessed = pd.concat(
    [valid_X_cat_preprocessed, valid_X[num_columns]], axis=1
)
test_X_preprocessed = pd.concat(
    [test_X_cat_preprocessed, test_X[num_columns]], axis=1
)
```


**4. 모델 적합**

- 랜덤 포레스트 모델을 적합합니다.
```python
from sklearn.ensemble import RandomForestRegressor 
rf = RandomForestRegressor(random_state=1) 
rf.fit(train_X_preprocessed, train_y)
```

- 검증 데이터를 활용하여 모형 성능을 확인해보겠습니다.
```python
from sklearn.metrics import root_mean_squared_error 
pred_val = rf.predict(valid_X_preprocessed) 
print('valid RMSE:', root_mean_squared_error(valid_y, pred_val))
```
*Output:*
```
valid RMSE: 75.47488439083246
```

- 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred = rf.predict(test_X_preprocessed) 
test_pred = pd.DataFrame(test_pred, columns=['pred']) 
print(test_pred.head())
```
*Output:*
```
       pred
0   484.92
1  1038.76
2   352.11
3  1329.99
4   207.37
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False)
```

### 작업형 제3유형

**문제 1. 이직 여부 예측 (로지스틱 회귀)**


```python
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/10_3_1.csv') 
print(df.head())
```
*Output:*
```
   attrition  age  income  overtime
0          0   51    9270         0
1          0   23    9603         1
2          1   49    2860         2
3          0   56    7390         1
4          0   42    7226         2
```

- `smf.logit()`을 통해 로지스틱 회귀 모형을 적합합니다.
```python
import statsmodels.formula.api as smf
model = smf.logit("attrition ~ age + income + C(overtime)", data=df).fit()
pvalues = model.pvalues[1:]
params = model.params[1:] 
print(pvalues)
```
*Output:*
```
Optimization terminated successfully.
         Current function value: 0.048045
         Iterations: 35
C(overtime)[T.1]    0.997790
C(overtime)[T.2]    0.997772
age                 0.121215
income              0.009629
dtype: float64
```


- 유의수준 0.05에서 `income` 변수의 p-value가 0.009629 < 0.05이므로, 유의한 변수입니다. `income` 변수의 회귀계수를 확인합니다.
```python
# 유의확률 0.05 미만, 절편(Intercept) 제외 
sig_vars = params[pvalues < 0.05]
rounded_coefs = np.round(sig_vars, 3) 
print(rounded_coefs)
```
*Output:*
```
income   -0.005
dtype: float64
```

- 로지스틱 회귀모형에서 회귀계수는 로그 오즈비를 의미합니다. 오즈비를 계산하기 위해서 회귀계수에 지수 함수를 적용하여 로그를 소거합니다.

```python
age_coef = model.params["age"] 
# 오즈비(odds ratio) 계산
odds_ratio_age = np.exp(age_coef) 
odds_ratio_age_rounded = round(odds_ratio_age, 3) 
print('age 오즈비:', odds_ratio_age_rounded)
```
*Output:*
```
age 오즈비: 0.894
```

- `age=20`, `income=3000`, `overtime=2`인 새로운 데이터에 대해서 이직확률을 예측합니다.
```python
# 예측할 데이터 생성 
test_df = pd.DataFrame({
    "age": [20],
    "income": [3000],
    "overtime": [2]
})

# 예측 확률 산출
pred_prob = model.predict(test_df)
# 소수점 셋째 자리까지 반올림
pred_prob_rounded = np.round(pred_prob, 3) 
print("예측 이직확률:", pred_prob_rounded)
```
*Output:*
```
예측 이직확률: 0.48
```

**문제 2. 주택 가격 예측 (다중선형회귀)**


```python
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/10_3_2.csv') 
print(df.head())
```
*Output:*
```
        price       area    height  wall
0  317.312359  89.934283  10.715575     0
1  273.821798  77.234714  11.121569     0
2  319.961122  92.953771  12.166102     0
3  364.561162  110.460597  12.107604     1
4  254.338664  75.316933   7.244661     1
```

- `smf.ols()`를 통해 다중선형회귀모형을 적합합니다. 절편을 제외한 유의미한 회귀계수의 합을 계산합니다.
```python
import statsmodels.formula.api as smf
# 다중선형회귀 적합
model = smf.ols("price ~ area + height + wall", data=df).fit()

# 각 변수의 계수, p-value
params = model.params[1:]
pvalues = model.pvalues[1:]

# 유의한 변수(유의확률 0.05 미만, 절편 제외)
sig_vars = params[pvalues < 0.05]

coef_sum = sig_vars.sum()
coef_sum_rounded = np.round(coef_sum, 3) 
print(coef_sum_rounded)
```
*Output:*
```
10.289
```


- 유의한 변수인 `area`, `height`를 뽑아서 다중선형회귀모형을 적합합니다. 해당 모형의 결정계수를 계산합니다.
```python
sig_var_names = sig_vars.index.tolist()
# formula 문자열 만들기
formula = 'price ~ ' + ' + '.join(sig_var_names) 
# 새 모델 적합
model2 = smf.ols(formula, data=df).fit()
r2_rounded = np.round(model2.rsquared, 3) 
print(r2_rounded)
```
*Output:*
```
0.859
```

- `area=100`, `height=10`, `wall=1`인 새로운 데이터에 대해 예측값을 산출합니다.
```python
# 예측용 입력 생성 (딕셔너리 리터럴 사용)
test_df = pd.DataFrame({"area": [100], "height": [10], "wall": [1]}) 
# 유의한 변수만 추출 
test_X = test_df[sig_var_names] 
# 예측
pred_price = model2.predict(test_X)
pred_price_rounded = np.round(pred_price, 3) 
print(pred_price_rounded)
```
*Output:*
```
0    329.036
dtype: float64
```

df. drop(colunins = [ " 평균근속연수 " 〕， iriplace = True)

- 결측치가 처리된 결과를 확인합니다．
df.isnaQ.sumO 부서 0 등급 0 평균만족도 0 근속연수 0 교육참가횟수 0 조건에 따른 평균 계산 ③ A : 부서가 ' HR ' 이고 등급이 ' A ' 인 사람들의 평균 근속연수를 계산하시오． ④ B : 부서가 ' Sales ' 이고 등급이 ' B ' 인 ㅅ남들의 펑균 교육참가횟수를 계산하시오．

# ;
⑤ A와 B를 더한 값을 구하시오．

- 부서가 ' HR ' 이고 등급이 ' A ' 인 사람들의 평균 근속연수를 계산합니다．
```python
A = df. 1.oc[(df[ " 부서 " ] - 
"HR") & (df[ " 등급 " 〕 == "A"), " 근속연수 " ].mean()
- 부서가 'Sales'이고 등급이 'B'인 사람들의 평균 교육참가횟수를 계산합니다.
```python
B = df.loc[(df["부서"] == "Sales") & (df["등급"] == "B"), "교육참가횟수"].mean()
```


- 두 조건의 합을 계산합니다.
```python
result = A + B 
print("A (평균 근속연수):", A) 
print("B (평균 교육참가횟수):", B) 
print("A + B:", result)
```
*Output:*
```
A (평균 근속연수): 17.625
B (평균 교육참가횟수): 7.6
A + B: 25.225
```

### 작업형 제2유형

**농업 유형 예측 모델 (다중 분류)**

```python
import pandas as pd 
import numpy as np
# 데이터 로드 
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/9_2_train.csv') 
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/9_2_test.csv')
```


**1. 데이터 탐색**

- 모델을 적합하기 전 데이터에 결측치가 있는지 확인해야 합니다. 결측치가 존재할 경우 모델 적합 시 에러가 발생할 수 있습니다.

```python
print(train.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1680 entries, 0 to 1679
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   ID      1680 non-null   int64 
 1   지역      1680 non-null   object
 2   등급      1680 non-null   object
 3   농업면적    1680 non-null   int64 
 4   연도      1680 non-null   int64 
 5   라벨      1680 non-null   int64 
dtypes: int64(4), object(2)
memory usage: 78.9+ KB
None
```
- 결측치 없음

```python
print(test.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 720 entries, 0 to 719
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   ID      720 non-null    int64 
 1   지역      720 non-null    object
 2   등급      720 non-null    object
 3   농업면적    720 non-null    int64 
 4   연도      720 non-null    int64 
 5   라벨      720 non-null    int64 
dtypes: int64(4), object(2)
memory usage: 33.9+ KB
None
```
- 결측치 없음


- 테스트 데이터를 활용한 최종 결과를 제출하기 위해 ID 칼럼을 따로 저장합니다.
```python
test_id = test['ID'] 
train_X = train.drop(['라벨'], axis=1) 
train_y = train['라벨'] 
test_X = test.drop(['라벨'], axis=1) 
test_y = test['라벨']
```

**2. 데이터 분할**

- 모델 성능 확인을 위해 훈련 데이터의 일부를 검증 데이터로 나누겠습니다.
```python
from sklearn.model_selection import train_test_split 
# 데이터 분할 
train_X, valid_X, train_y, valid_y = train_test_split(train_X, train_y, test_size=0.3, random_state=1)
```

**3. 데이터 전처리**

- 범주형 변수에 대해서 원-핫 인코딩을 수행하겠습니다. 범주형 변수와 수치형 변수의 각 칼럼명을 저장합니다.

```python
cat_columns = train_X.select_dtypes('object').columns
num_columns = train_X.select_dtypes('number').columns
```

- 원-핫 인코딩을 위한 메서드를 불러옵니다.
```python
from sklearn.preprocessing import OneHotEncoder 
onehotencoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform='pandas')
```

- 훈련 데이터와 검증 데이터, 테스트 데이터에 대해 전처리를 진행합니다. 전처리 결과는 `set_output(transform='pandas')`로 설정했으므로, `pandas.DataFrame`으로 출력됩니다.

```python
train_X_cat_preprocessed = onehotencoder.fit_transform(train_X[cat_columns]) 
valid_X_cat_preprocessed = onehotencoder.transform(valid_X[cat_columns]) 
test_X_cat_preprocessed = onehotencoder.transform(test_X[cat_columns]) 
train_X_preprocessed = pd.concat([train_X_cat_preprocessed, train_X[num_columns]], axis=1)
valid_X_preprocessed = pd.concat([valid_X_cat_preprocessed, valid_X[num_columns]], axis=1)
test_X_preprocessed = pd.concat([test_X_cat_preprocessed, test_X[num_columns]], axis=1)
```


**4. 모델 적합**

- 랜덤 포레스트 모델을 적합하겠습니다.
```python
from sklearn.ensemble import RandomForestClassifier 
rf = RandomForestClassifier(random_state=1) 
rf.fit(train_X_preprocessed, train_y)
```

- 검증 데이터를 활용하여 모형 성능을 확인합니다.
```python
from sklearn.metrics import f1_score 
pred_val = rf.predict(valid_X_preprocessed) 
print('valid f1-macro:', f1_score(valid_y, pred_val, average='macro'))
```
*Output:*
```
valid f1-macro: 0.3099787685774947
```

- 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred = rf.predict(test_X_preprocessed) 
test_pred = pd.DataFrame(test_pred, columns=['pred'])
```

- ID, pred 칼럼만 존재하는 결과 파일을 생성합니다.
```python
result = pd.concat([test_id, test_pred], axis=1) 
print(result.head(2))
```
*Output:*
```
     ID  pred
0  1094     0
1  1341     0
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) # 시험에서 제시되는 파일명 작성할 것
```

- 만약 모델 성능이 낮다고 판단되면, 교차검증을 활용한 하이퍼파라미터 튜닝을 진행해볼 수 있습니다. 홀드 아웃 방법이 아닌 k-폴드 교차검증을 진행할 것이기 때문에 기존에 분할했던 학습 데이터와 검증 데이터를 합치겠습니다.

```python
train_X_full = np.concatenate([train_X_preprocessed, valid_X_preprocessed], axis=0) 
train_y_full = np.concatenate([train_y, valid_y], axis=0)
```


- GridSearchCV를 통해 하이퍼파라미터 튜닝을 진행하겠습니다.
```python
from sklearn.model_selection import GridSearchCV
param_grid = { 
    'max_depth': [10, 20, 30], 
    'min_samples_split': [2, 5, 10]
}
rf = RandomForestClassifier(random_state=1) 
rf_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=3, 
    scoring='f1_macro'
)
rf_search.fit(train_X_full, train_y_full) 
print('valid f1-macro:', rf_search.best_score_)
```
*Output:*
```
valid f1-macro: 0.3111111111111111
```

> [!TIP]
> 파라미터 값의 범위가 넓어지면 모델 학습 시 많은 시간이 소요될 수 있으므로 주의가 필요합니다.

- 하이퍼파라미터 튜닝 결과를 바탕으로 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred2 = rf_search.predict(test_X_preprocessed) 
test_pred2 = pd.DataFrame(test_pred2, columns=['pred'])
```

**5. 테스트 데이터로 예측**

- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰줍니다.
```python
result = pd.concat([test_id, test_pred2], axis=1)
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) 
# 시험에서 제시되는 파일명 작성할 것
```

**ColumnTransformer와 Pipeline을 활용한 방법**

```python
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/9_2_train.csv')
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/9_2_test.csv') 
test_id = test['ID']
train_X = train.drop(['라벨'], axis=1) 
train_y = train['라벨']
test_X = test.drop(['라벨'], axis=1) 
test_y = test['라벨'] 
```


- ColumnTransformer를 활용하면 연속형 변수와 수치형 변수 각각에 대해서 한 번에 전처리를 진행할 수 있습니다.

```python
from sklearn.preprocessing import OneHotEncoder 
from sklearn.compose import ColumnTransformer

onehotencoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
cat_columns = train_X.select_dtypes('object').columns 
# num_columns = train_X.select_dtypes('number').columns

# ColumnTransformer를 활용한 데이터 전처리
c_transformer = ColumnTransformer( 
    transformers=[ 
        ('cat', onehotencoder, cat_columns),
        # ('num', imputer, num_columns) 
    ], 
    remainder='passthrough'
)
```

- ColumnTransformer로 데이터 전처리를 진행한 후 Pipeline을 활용해서 모델을 정의하겠습니다.

```python
from sklearn.pipeline import Pipeline 
from sklearn.model_selection import GridSearchCV 
from sklearn.ensemble import RandomForestClassifier

pipe_rf = Pipeline([ 
    ("preprocess", c_transformer), 
    ("classifier", RandomForestClassifier(random_state=1)) 
])
```

- Pipeline을 활용해서 모델링을 정의한 후 GridSearchCV를 활용하여 교차검증을 통한 파라미터 튜닝을 진행하겠습니다.

```python
param_grid = {
    'classifier__max_depth': [10, 20, 30], 
    'classifier__min_samples_split': [2, 5, 10]
}
rf_search_pipe = GridSearchCV(
    estimator=pipe_rf,
    param_grid=param_grid, 
    cv=3, 
    scoring='f1_macro'
) 
rf_search_pipe.fit(train_X, train_y)
```


- 교차검증 `f1_macro` score를 확인합니다.
```python
print('교차검증 f1-macro:', rf_search_pipe.best_score_)
```
*Output:*
```
교차검증 f1-macro: 0.3111111111111111
```

- 파라미터 튜닝 결과를 바탕으로 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred3 = rf_search_pipe.predict(test_X) 
test_pred3 = pd.DataFrame(test_pred3, columns=['pred'])
```

- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰줍니다.
```python
result = pd.concat([test_id, test_pred3], axis=1) 
print(result.head(2))
```
*Output:*
```
     ID  pred
0  1094     0
1  1341     0
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) 
# 시험에서 제시되는 파일명 작성할 것
```

### 작업형 제3유형

**문제 1. 생산성 요인 분석 (다중회귀)**


```python
import pandas as pd 
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/9_3_1.csv') 
train = df[df['id'] <= 140] 
test = df[df['id'] > 140]
```

- 다중회귀모델을 적합합니다.
```python
from statsmodels.formula.api import ols 
formula = "design ~ tenure + f2 + f3 + f4 + f5" 
model = ols(formula, data=train).fit()
```

- 각 칼럼의 p-value를 확인합니다.
```python
p_values = model.pvalues
```

- 유의하지 않은 칼럼 개수를 계산합니다.
```python
non_significant_vars = (p_values[1:] >= 0.05).sum() 
print("유의하지 않은 설명변수의 개수:", non_significant_vars)
```
*Output:*
```
유의하지 않은 설명변수의 개수: 2
```

> [!TIP]
> 절편은 칼럼 개수에 포함되지 않으므로 칼럼 개수를 셀 때 주의가 필요합니다.


- scipy를 활용하여 피어슨 상관계수를 구할 수 있습니다.
```python
y_pred = model.predict(train)
y_real = train['design']
from scipy.stats import pearsonr 
correlation, _ = pearsonr(y_pred, y_real) 
print("상관계수:", correlation)
```
*Output:*
```
상관계수: 0.914750154303963
```

- 다른 방법으로는 pandas의 `.corr` 메서드를 활용하여 구할 수 있습니다.
```python
y_pred_series = pd.Series(y_pred)
y_real_series = pd.Series(y_real)
correlation = y_pred_series.corr(y_real_series) 
print("상관계수:", correlation)
```
*Output:*
```
상관계수: 0.9147501543039637
```

- 테스트 데이터에서의 RMSE를 구합니다.
```python
y_pred_test = model.predict(test)
from sklearn.metrics import root_mean_squared_error
rmse = root_mean_squared_error(test['design'], y_pred_test) 
print("RMSE:", rmse)
```
*Output:*
```
RMSE: 4.396152958589427
```

**문제 2. 고객 이탈 요인 분석 (로지스틱 회귀)**


```python
import numpy as np 
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/9_3_2.csv')
```

- 로지스틱 회귀 모델을 적합합니다.
```python
from statsmodels.formula.api import logit 
formula = "churn ~ col1 + col2 + Phone_Service + Tech_Insurance"
model = logit(formula, data=df).fit()
```
*Output:*
```
Optimization terminated successfully.
         Current function value: 0.640721
         Iterations 5
```

- `col1`의 p-value를 계산합니다.
```python
col1_pvalue = round(model.pvalues['col1'], 3) 
print("col1의 p-value:", col1_pvalue)
```
*Output:*
```
col1의 p-value: 0.0
```

- 이탈 확률 오즈비를 계산합니다.
```python
odds_ratio_phone_service = round(np.exp(model.params['Phone_Service']), 3) 
print("Phone_Service의 오즈비:", odds_ratio_phone_service)
```
*Output:*
```
Phone_Service의 오즈비: 1.867
```

- 적합된 모델의 예측 확률을 계산한 후 0.3 이상인 고객의 수를 계산합니다.
```python
predicted_probs = model.predict(df) # 예측 확률 계산
num_customers_above_03 = sum(predicted_probs > 0.3) # 확률 0.3 초과 고객 수 
print("확률 0.3 이상 고객 수:", num_customers_above_03)
```
*Output:*
```
확률 0.3 이상 고객 수: 450
```


**시험 시간**: 180분 | **풀이 시간**: 30분 | **합격 점수**: 60점 | **내점수**: -

## 기출문제 제8회 (2024-06-22 시행)

데이터셋 경로: `https://raw.githubusercontent.com/YoungjinBD/data/main/exam/`

### 작업형 제1유형

**1.** 대륙별 맥주 소비량 분석

```python
import pandas as pd 
import numpy as np
pd.set_option('display.max_columns', None) 
# 모든 칼럼이 출력되게 조절
dat = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_1_1.csv') 
print(dat.head())
```
*Output:*
```
   대륙          국가  맥주소비량
0  AS  Afghanistan       0
...
```

- `.groupby`를 통해 대륙별 평균 맥주소비량을 구한 후 가장 맥주소비량이 많은 대륙을 구합니다.

```python
result = dat.groupby('대륙')['맥주소비량'].mean().idxmax() 
print('대륙:', result)
```
*Output:*
```
대륙: SA
```


- 맥주소비량이 가장 많은 대륙 데이터를 필터링하고 5번째로 맥주소비량이 많은 나라를 계산합니다.

```python
sub_dat = dat.loc[dat['대륙'] == result]
result2 = sub_dat.groupby('국가')['맥주소비량'].sum().sort_values(ascending=False).index[4] 
print('국가:', result2)
```
*Output:*
```
국가: Venezuela
```
- 5번째로 맥주소비량이 많은 나라의 평균 맥주소비량을 계산합니다.

```python
result3 = dat.loc[dat['국가'] == result2, '맥주소비량'].mean().round() 
print('평균 맥주소비량:', result3)
```
*Output:*
```
평균 맥주소비량: 253.0
```

**2. 국가별 방문객 유형 분석**

```python
dat = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_1_2.csv')
print(dat.head())
```

```python
print('국가 수 =', len(dat['국가'].unique())) 
print('전체 행 수 =', len(dat))
```
*Output:*
```
국가 수 = 48
전체 행 수 = 100
```


- 국가별로 복수의 행이 존재합니다. 따라서 국가별 '관광', '사무', '공무', '유학', '기타'의 합계를 계산합니다.

```python
dat_sub = dat.groupby('국가', as_index=False)[['관광', '사무', '공무', '유학', '기타']].sum() 
print('전체 행 수 =', len(dat_sub))
```
*Output:*
```
전체 행 수 = 48
```

- 문제에 정의된 기준에 맞춰서 합계 칼럼을 생성합니다. axis=1은 행 방향, axis=0은 열 방향 합계를 계산하는 옵션입니다.
```python
dat_sub['합계'] = dat_sub.loc[:, ['관광', '사무', '공무', '유학', '기타']].sum(axis=1)
```

- 문제에 정의된 기준에 맞춰서 관광객비율 칼럼을 생성합니다.
```python
dat_sub['관광객비율'] = np.round(dat_sub['관광'] / dat_sub['합계'], 3)
```

- 관광객 비율이 두 번째로 높은 나라의 관광 수를 계산합니다. 제시된 두 가지 방법을 참고하세요.

```python
# 방법1 
result1 = (dat_sub.sort_values(by='관광객비율', ascending=False).iloc[1, 1]) 
print('관광 수 =', result1)
```
*Output:*
```
관광 수 = 9039
```

```python
# 방법2
result2 = (dat_sub.sort_values(by='관광객비율', ascending=False).reset_index(drop=True).loc[1, '관광']) 
print('관광 수 :', result2)
```
*Output:*
```
관광 수 : 9039
```

> [!TIP]
> `.sort_values`를 활용하여 데이터 정렬 후 `.loc`를 적용할 경우에는 `.reset_index()`를 통해 인덱스를 재설정하고 적용해야 합니다.


- 관광 수가 두 번째로 높은 나라를 찾습니다.
```python
second_country = dat_sub.sort_values(by='관광', ascending=False).iloc[1, 0] 
print('국가:', second_country)
```
*Output:*
```
국가: 이스라엘
```

- 관광 수가 두 번째로 높은 나라의 공무 수 평균을 계산합니다.
```python
result3 = dat.loc[dat['국가'] == second_country, '공무'].mean().round() 
print('공무 수 평균 :', result3)
```
*Output:*
```
공무 수 평균 : 494.0
```

- 관광 수와 공무 수의 합계를 계산합니다.
```python
print('관광 + 공무 :', result1 + result3)
```
*Output:*
```
관광 + 공무 : 9533.0
```

**3. Min-Max 스케일링**

```python
dat = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_1_3.csv') 
print(dat.head())
```


- Min-Max 스케일러를 임포트합니다.
```python
from sklearn.preprocessing import MinMaxScaler 
scaler = MinMaxScaler()
```
- Min-Max 스케일링을 `CO(GT)`, `NMHC(GT)` 칼럼에 적용합니다.
```python
dat = dat.loc[:, ['CO(GT)', 'NMHC(GT)']] 
scaled_data = scaler.fit_transform(dat)
```
- 스케일링된 칼럼의 표준편차를 계산합니다.
```python
co_std = scaled_data[:, 0].std().round(2)
nmhc_std = scaled_data[:, 1].std().round(2)
print("CO(GT) std:", co_std)
print("NMHC(GT) std:", nmhc_std)
```
*Output:*
```
CO(GT) 표준편차 : 0.37 
NMHC(GT) 표준편차 : 0.15
```

### 작업형 제2유형

**자전거 총 대여 건수 예측 모델 (회귀)**

제공된 학습용 데이터(`8_2_train.csv`)는 자전거 대여와 관련된 날짜별 정보와 해당 날짜의 총 대여 건수 (`count`)를 포함하고 있다. 학습용 데이터를 활용하여 자전거 총 대여 건수(`count`)를 예측하는 회귀 모델을 개발하고, 성능이 가장 우수한 모델을 평가용 데이터(`8_2_test.csv`)에 적용하여 예측 결과를 제출하시오.

- **모델 성능 지표**: MAE (Mean Absolute Error)
- **타깃(라벨)**: `count` (자전거 총 대여 건수)

**Data description**
- `ID`: 고유 식별자
- `holiday`: 공휴일 여부
- `workingday`: 평일 여부
- `weather`: 날씨 상황
- `temp`: 실제 기온
- `atemp`: 체감 온도
- `humidity`: 습도
- `windspeed`: 풍속
- `count`: 자전거 총 대여 건수


**제출 형식**
- 파일명: `result.csv` (디렉토리/폴더명 제외)
- 제출 칼럼: `ID`, `pred` (총 2개 칼럼)
- `pred`: 예측된 자전거 대여 건수 (정수 또는 소수 가능)
- 행 수: 테스트 데이터(`8_2_test.csv`)의 `ID` 수와 동일

```python
import pandas as pd 
import numpy as np 
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_2_train.csv') 
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_2_test.csv')
```

**1. 데이터 탐색**

- 모델을 적합하기 전 데이터에 결측치가 있는지 확인해야 합니다. 결측치가 존재할 경우 모델 적합 시 에러가 발생할 수 있습니다.

```python
print(train.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 378 entries, 0 to 377
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   ID          378 non-null    int64  
 1   holiday     378 non-null    object 
 2   workingday  378 non-null    object 
 3   weather     378 non-null    object 
 4   temp        378 non-null    float64
 5   atemp       378 non-null    float64
 6   humidity    378 non-null    int64  
 7   windspeed   378 non-null    float64
 8   count       378 non-null    int64  
dtypes: float64(3), int64(3), object(3)
memory usage: 26.7+ KB
None
```
- 결측치 없음 

```python
print(test.info())
```


*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 166 entries, 0 to 165
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   ID          166 non-null    int64  
 1   holiday     166 non-null    object 
 2   workingday  166 non-null    object 
 3   weather     166 non-null    object 
 4   temp        166 non-null    float64
 5   atemp       166 non-null    float64
 6   humidity    166 non-null    int64  
 7   windspeed   166 non-null    float64
 8   count       0 non-null      float64
dtypes: float64(4), int64(2), object(3)
memory usage: 11.8+ KB
None
```
- 결측치 확인

- 테스트 데이터를 활용한 최종 결과를 제출하기 위해 ID 칼럼을 따로 저장합니다.
```python
test_id = test['ID']
```

**2. 데이터 분할**

- 모델 성능 확인을 위해 훈련 데이터의 일부를 검증 데이터로 나누겠습니다.
```python
train_X = train.drop(['count'], axis=1) 
train_y = train['count']
test_X = test.drop(['count'], axis=1) 
test_y = test['count']

from sklearn.model_selection import train_test_split 
train_X, valid_X, train_y, valid_y = train_test_split(train_X, train_y, test_size=0.3, random_state=1) 
print(train_X.shape, train_y.shape, valid_X.shape, valid_y.shape)
```
*Output:*
```
(264, 8) (264,) (114, 8) (114,)
```


**3. 데이터 전처리**

- 범주형 변수에 대해서 원-핫 인코딩을 수행하겠습니다. 범주형 변수와 수치형 변수의 각 칼럼명을 저장합니다.
```python
cat_columns = train_X.select_dtypes('object').columns
num_columns = train_X.select_dtypes('number').columns
```

- 원-핫 인코딩을 위한 메서드를 불러옵니다.
```python
from sklearn.preprocessing import OneHotEncoder 
onehotencoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform='pandas')
```

- 훈련 데이터, 검증 데이터, 테스트 데이터에 대해 데이터 전처리를 진행합니다.
- 전처리 결과는 `set_output(transform='pandas')`로 설정했으므로, `pandas.DataFrame`으로 출력됩니다.

```python
train_X_cat_preprocessed = onehotencoder.fit_transform(train_X[cat_columns]) 
valid_X_cat_preprocessed = onehotencoder.transform(valid_X[cat_columns]) 
test_X_cat_preprocessed = onehotencoder.transform(test_X[cat_columns]) 

train_X_preprocessed = pd.concat([train_X_cat_preprocessed, train_X[num_columns]], axis=1)
valid_X_preprocessed = pd.concat([valid_X_cat_preprocessed, valid_X[num_columns]], axis=1)
test_X_preprocessed = pd.concat([test_X_cat_preprocessed, test_X[num_columns]], axis=1)
```

**4. 모델 적합**

- 랜덤 포레스트 모델을 적합해 보겠습니다.
```python
from sklearn.ensemble import RandomForestRegressor 
rf = RandomForestRegressor(random_state=1) 
rf.fit(train_X_preprocessed, train_y)
```

- 검증 데이터를 활용하여 모형 성능을 확인해 보겠습니다.
```python
from sklearn.metrics import mean_absolute_error 
pred_val = rf.predict(valid_X_preprocessed) 
print('valid MAE:', mean_absolute_error(valid_y, pred_val))
```
*Output:*
```
valid MAE: 140.09640785564048
```

- 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred = rf.predict(test_X_preprocessed) 
test_pred = pd.DataFrame(test_pred, columns=['pred'])
```


- ID, pred 칼럼만 존재하는 결과 파일을 생성합니다.
```python
result = pd.concat([test_id, test_pred], axis=1) 
print(result.head(2))
```
*Output:*
```
      ID        pred
0   4775  207.473806
1  10539  210.002005
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) # 시험에서 제시되는 파일명 작성할 것
```

- 만약 모델 성능이 낮다고 판단되면, 교차검증을 활용한 하이퍼파라미터 튜닝을 진행해볼 수 있습니다. 홀드 아웃 방법이 아닌 k-폴드 교차검증을 진행할 것이기 때문에 기존에 분할했던 학습 데이터와 검증 데이터를 합치겠습니다.

```python
train_X_full = np.concatenate([train_X_preprocessed, valid_X_preprocessed], axis=0) 
train_y_full = np.concatenate([train_y, valid_y], axis=0)
```

- GridSearchCV를 통해 하이퍼파라미터 튜닝을 진행하겠습니다.

```python
from sklearn.model_selection import GridSearchCV
param_grid = {
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10]
} 
rf = RandomForestRegressor(random_state=1) 
rf_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=3, 
    scoring='neg_mean_absolute_error'
) 
rf_search.fit(train_X_full, train_y_full) 
print('교차검증 MAE-score:', -rf_search.best_score_)
```
*Output:*
```
교차검증 MAE-score: 133.16357727632837
```

> [!TIP]
> 파라미터 값의 범위가 넓어지면 모델 학습 시 많은 시간이 소요될 수 있으므로 주의가 필요합니다.

- 하이퍼파라미터 튜닝 결과를 바탕으로 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred2 = rf_search.predict(test_X_preprocessed)
test_pred2 = pd.DataFrame(test_pred2, columns=['pred'])
```


**5. 테스트 데이터로 예측**

- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰줍니다.
```python
result = pd.concat([test_id, test_pred2], axis=1)
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) 
# 시험에서 제시되는 파일명 작성할 것
```

**ColumnTransformer와 Pipeline을 활용한 방법**

```python
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_2_train.csv') 
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_2_test.csv') 
test_id = test['ID']
train_X = train.drop(['count'], axis=1) 
train_y = train['count']
test_X = test.drop(['count'], axis=1) 
test_y = test['count']
```

- ColumnTransformer를 활용하면 연속형 변수와 수치형 변수 각각에 대해서 한 번에 전처리를 진행할 수 있습니다.

```python
from sklearn.preprocessing import OneHotEncoder 
onehotencoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
```

- ColumnTransformer를 활용하여 데이터 전처리 방식을 정의하겠습니다.
```python
cat_columns = train_X.select_dtypes('object').columns
# num_columns = train_X.select_dtypes('number').columns.to_list()

# ColumnTransformer를 활용한 전처리
from sklearn.compose import ColumnTransformer
c_transformer = ColumnTransformer( 
    transformers=[ 
        ('cat', onehotencoder, cat_columns),
        # ('num', imputer, num_columns) 
    ], 
    remainder='passthrough'
)
```


- ColumnTransformer로 데이터 전처리를 진행한 후 Pipeline을 활용해서 모델을 정의하겠습니다.

```python
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

pipe_rf = Pipeline([
    ("preprocess", c_transformer), 
    ("regressor", RandomForestRegressor(random_state=1)) 
])
```

- Pipeline을 활용해서 모델링을 정의한 후 GridSearchCV를 활용하여 교차검증을 통한 파라미터 튜닝을 진행하겠습니다.

```python
param_grid = {
    'regressor__max_depth': [10, 20, 30], 
    'regressor__min_samples_split': [2, 5, 10]
} 
rf_search_pipe = GridSearchCV(
    estimator=pipe_rf,
    param_grid=param_grid,
    cv=3, 
    scoring='neg_mean_absolute_error'
) 
rf_search_pipe.fit(train_X, train_y)
```

- 교차검증 MAE score는 다음과 같습니다.
```python
print('교차검증 MAE-score:', -rf_search_pipe.best_score_)
```
*Output:*
```
교차검증 MAE-score: 169.1781961265393
```

- 파라미터 튜닝 결과를 바탕으로 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred3 = rf_search_pipe.predict(test_X) 
test_pred3 = pd.DataFrame(test_pred3, columns=['pred'])
```

- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰줍니다.
```python
result = pd.concat([test_id, test_pred3], axis=1) 
print(result.head(2))
```
*Output:*
```
      ID        pred
0   4775   98.204045
1  10539  365.312833
```


- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) 
# 시험에서 제시되는 파일명 작성할 것
```

### 작업형 제3유형

**문제 1. 업무 효율성 분석 (대응표본 t-검정 / 부호 순위 검정)**

어느 회사에서 직원들의 업무 효율성을 높이기 위한 새로운 소프트웨어를 도입하였다. 도입 전과 도입 후의 업무 처리 시간을 각각 측정하여 새로운 소프트웨어의 효과를 검증하고자 한다.

- **데이터**: `exam8_3_1.csv`
- **①** 도입 전과 도입 후의 업무처리 시간의 평균과 표준편차를 구하시오. (소수점 둘째 자리까지 반올림)
- **②** 도입 전후의 업무처리 시간 차이가 유의미한지 **부호 순위 검정**을 실시하고, 검정통계량을 계산하시오. (소수점 둘째 자리까지 반올림)
- **③** p-value를 바탕으로 유의수준 5%에서 귀무가설의 기각/채택 여부를 결정하시오. (p-value는 소수점 셋째 자리까지 반올림)

```python
import pandas as pd 
data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_3_1.csv')
```

- 도입 전과 도입 후의 업무 처리 시간의 평균과 표준편차를 계산하고 소수점 셋째 자리에서 반올림하여 출력합니다.

```python
# 도입 전 평균과 표준편차 계산
mean_before = data['before'].mean() 
std_before = data['before'].std()
# 도입 후 평균과 표준편차 계산
mean_after = data['after'].mean() 
std_after = data['after'].std()

print('도입 전 업무 처리 시간 평균:', round(mean_before, 2)) 
print('도입 전 업무 처리 시간 표준편차:', round(std_before, 2)) 
print('도입 후 업무 처리 시간 평균:', round(mean_after, 2)) 
print('도입 후 업무 처리 시간 표준편차:', round(std_after, 2))
```
*Output:*
```
도입 전 업무 처리 시간 평균: 8.21
도입 전 업무 처리 시간 표준편차: 1.71
도입 후 업무 처리 시간 평균: 7.23
도입 후 업무 처리 시간 표준편차: 1.96
```


- 부호 검정은 `wilcoxon()`를 통해 수행할 수 있습니다.
```python
from scipy.stats import wilcoxon 
# 부호 순위 검정 수행 
statistic, p_value = wilcoxon(data['before'], data['after']) 
print('검정통계량:', statistic.round(2))
```
*Output:*
```
검정통계량: 72.0
```

- 유의수준 5% 하에서 p-value가 0.05보다 작은지 확인하여 귀무가설의 기각과 채택을 결정합니다.

```python
p_value = round(p_value, 3) 
# 결과 해석 
if p_value < 0.05: 
    result = "기각" 
else: 
    result = "채택" 
print(result)
```
*Output:*
```
기각
```

**문제 2. 생산성 영향 요인 분석 (다중회귀)**

어느 회사에서 직원들의 생산성에 영향을 미치는 요인이 무엇인지 확인하고자 한다. 100명의 직원들을 대상으로 생산성 점수, 근무 시간, 연령, 그리고 경력을 조사하였다.

- **데이터**: `8_3_2_train.csv`, `8_3_2_test.csv`
- **①** 훈련 데이터를 기준으로 생산성 점수(`productivity`)를 종속변수로 하고 근무 시간, 연령, 그리고 경력을 독립변수로 하는 다중회귀 분석을 수행한 후, 회귀계수가 가장 높은 변수를 구하시오. (다중회귀모형 적합 시 절편 포함)
- **②** 유의수준 5% 하에서 각 독립변수가 생산성에 미치는 영향이 통계적으로 유의미한지 판단하고, 유의미한 변수 개수를 구하시오. (p-value는 소수점 넷째 자리까지 반올림)
- **③** 테스트 데이터로 모델의 성능을 평가하시오. (R2 산출)

```python
import pandas as pd 
train_data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_3_2_train.csv')
test_data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_3_2_test.csv')
```


- 상수항을 추가하여 모델을 적합합니다.
```python
import statsmodels.api as sm
# 독립 변수와 종속 변수 설정 (train 데이터 사용)
X_train = train_data[['hours', 'age', 'experience']]
y_train = train_data['productivity']
X_train = sm.add_constant(X_train) 
# 상수항 추가
model = sm.OLS(y_train, X_train).fit() 
# 다중회귀 분석 모델 적합 (train 데이터 사용) 
print(model.summary()) 
# 회귀계수 출력
```
*Output:*
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           productivity   R-squared:                       0.732
Model:                            OLS   Adj. R-squared:                  0.721
Method:                 Least Squares   F-statistic:                     69.03
Date:                Fri, 17 Jan 2025   Prob (F-statistic):           1.20e-21
Time:                        04:14:29   Log-Likelihood:                -297.10
No. Observations:                  80   AIC:                             602.2
Df Residuals:                      76   BIC:                             611.7
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         67.2310      6.059     11.097      0.000      55.165      79.297
hours          3.1220      1.618      1.929      0.057      -0.100       6.345
age            0.2110      0.431      0.489      0.626      -0.648       1.070
experience     3.3720      1.532      2.200      0.031       0.320       6.424
==============================================================================
Omnibus:                        2.381   Durbin-Watson:                   1.692
Prob(Omnibus):                  0.304   Jarque-Bera (JB):                1.779
Skew:                           0.210   Prob(JB):                        0.411
Kurtosis:                       3.618   Cond. No.                        611.
==============================================================================
```

- 회귀계수가 가장 큰 변수를 출력합니다.
```python
# 회귀계수 추출 
coefficients = model.params[1:] 
print('회귀계수가 가장 큰 변수:', coefficients.idxmax())
```
*Output:*
```
회귀계수가 가장 큰 변수: experience
```


- 유의수준 5% 하에서 p-value를 확인하고, 유의미한 변수의 개수를 계산합니다.
```python
p_values = model.pvalues[1:].round(4) 
significant_vars = p_values[p_values < 0.05]
num_significant_vars = len(significant_vars)
print('유의미한 변수 개수:', num_significant_vars) 
print(significant_vars)
```
*Output:*
```
유의미한 변수 개수: 1
experience    0.0000
dtype: float64
```
> [!NOTE]
> `hours`는 p-value가 0.057로 0.05보다 크므로 유의하지 않습니다. `age` 역시 0.626으로 유의하지 않습니다.

- R2는 `sklearn.metrics` 모듈의 `r2_score()` 함수를 사용하여 계산할 수 있습니다.
```python
from sklearn.metrics import r2_score
# 독립 변수와 종속 변수 설정 (test 데이터 사용)
X_test = test_data[['hours', 'age', 'experience']]
y_test = test_data['productivity']
X_test = sm.add_constant(X_test) 
# 상수항 추가
y_pred = model.predict(X_test) 
# 예측 수행
r2 = r2_score(y_test, y_pred) 
# R2 계산 
print('테스트 데이터 Squared:', round(r2, 3))
```
*Output:*
```
테스트 데이터 Squared: 0.804
```

- 적합된 회귀모델이 학생들 성적 데이터의 전체 변동성 중 80.4%를 설명하고 있다고 볼 수 있습니다.


**시험 시간**: 180분 | **풀이 시간**: 60분 | **합격 점수**: 60점 | **내점수**: -

## 기출문제 제7회 (2023-12-02 시행)

데이터셋 경로: `https://raw.githubusercontent.com/YoungjinBD/data/main/exam/`

### 작업형 제1유형

**1. 제품보고서 처리 시간 분석**

각 제품보고서별 처리 시간(처리시각과 신고시각의 차이) 칼럼(초단위)을 생성 후 공장별 처리 시간의 평균을 산출하시오. 산출된 결과를 바탕으로 평균 처리 시간이 3번째로 적은 공장명을 구하시오.

- **데이터**: `7_1_1.csv`

```python
import pandas as pd 
import numpy as np 
pd.set_option('display.max_columns', None) 
# 모든 칼럼이 출력되게 조절
from sklearn import set_config 
set_config(display="diagram") 
# scikit-learn 파이프라인 시각화
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/7_1_1.csv') 
print(df.head())
```
*Output:*
```
     제품보고서번호 공장명  결함유형    신고일자  신고시각         처리일시
0  202200000001M25795  공장B  기계 결함  20220722  205914  2022-10-27 18:47
1  202200000002M10860  공장B  풍질 문제  20220622   31050  2022-11-09 13:27
2  202200000007M47194  공장C  기계 결함  20220211  132628  2022-05-16 23:23
3  202200000011M26023  공장E  기계 결함  20220120   14812  2022-05-17 12:04
4  202200000031M75725  공장A  전기 결함  20220601  171835  2022-09-08 10:31
```


```python
print(df.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 135 entries, 0 to 134
Data columns (total 11 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   제품보고서번호  135 non-null    object
 1   공장명      135 non-null    object
 2   결함유형     135 non-null    object
 3   신고일자     135 non-null    int64 
 4   신고시각     135 non-null    int64 
 5   처리일자     135 non-null    int64 
 6   처리시각     135 non-null    int64 
 7   작업자직업명   135 non-null    object
 8   사고발생장소   135 non-null    object
 9   신고일시     135 non-null    object
 10  처리일시     135 non-null    object
dtypes: int64(4), object(7)
memory usage: 11.7+ KB
None
```

**1. 처리 시간 칼럼 생성**

- 처리 시간 칼럼을 만들기 위해서는 신고일자, 신고시각, 처리일자, 처리시각 칼럼을 년-월-일-시간-분-초 형태로 만들어야 합니다. 신고일자, 신고시각, 처리일자, 처리시각 칼럼을 str 형식으로 변환합니다.
```python
df.loc[:, ['신고일자', '신고시각', '처리일자', '처리시각']] = \
    df.loc[:, ['신고일자', '신고시각', '처리일자', '처리시각']].astype(str)
```

- 날짜형으로 변환 전 문자열의 길이가 모두 동일한지 확인합니다.
```python
print(df["신고일자"].str.len().unique()) 
print(df["신고시각"].str.len().unique())
```
*Output:*
```
[8]
[6 5 4 3]
```


- 신고일자는 8자리(YYYYMMDD)로 일정하지만, 신고시각은 6자리(HHMMSS), 5자리(HMMSS), 4자리(MMSS), 3자리(MSS) 등 다양한 길이로 되어 있습니다.

```python
print(df.loc[df["신고시각"].str.len() == 5, "신고시각"].head(1)) 
print(df.loc[df["신고시각"].str.len() == 4, "신고시각"].head(1)) 
print(df.loc[df["신고시각"].str.len() == 3, "신고시각"].head(1))
```
*Output:*
```
1    31050
Name: 신고시각, dtype: object
49    3502
Name: 신고시각, dtype: object
124    303
Name: 신고시각, dtype: object
```

- 날짜 패턴에 맞게 0을 적절히 채워넣어야 합니다. `.str.pad()`를 활용하여 문자열 왼쪽에 0을 채워넣습니다.
```python
df["신고시각"] = df["신고시각"].apply(lambda x: x.rjust(6, "0"))
```

- 처리시각 칼럼도 이전과 마찬가지로, 날짜 형식에 맞게 0을 채워넣습니다.
```python
print(df["처리일자"].str.len().unique()) 
print(df["처리시각"].str.len().unique()) 
print(df.loc[df["처리시각"].str.len() == 2, "처리시각"].head(1))
```
*Output:*
```
[8]
[6 5 4 3 2]
42    14
Name: 처리시각, dtype: object
```
```python
df["처리시각"] = df["처리시각"].apply(lambda x: x.rjust(6, "0"))
```

- 신고시각, 처리시각 칼럼을 시간-분-초 형태(6자리)로 변환해줬으므로, 신고일자, 처리일자 칼럼과 합쳐서 datetime 형식으로 변환합니다.
```python
df["신고일시"] = pd.to_datetime(df["신고일자"] + df["신고시각"], format="%Y%m%d%H%M%S") 
df["처리일시"] = pd.to_datetime(df["처리일자"] + df["처리시각"], format="%Y%m%d%H%M%S")
```


- 처리 시간 칼럼(초단위)을 생성합니다.
```python
df['처리시간'] = (df['처리일시'] - df['신고일시']).dt.total_seconds()
```

**2. 공장명별 처리 시간의 평균 계산**

- 공장명별로 데이터를 그룹화하여 처리시간의 평균을 계산합니다.
```python
mean_response_time = df.groupby('공장명')['처리시간'].mean().reset_index() 
print(mean_response_time)
```
*Output:*
```
   공장명          처리시간
0  공장A  9.021685e+05
1  공장B -1.647024e+06
2  공장C -1.598311e+06
3  공장D  3.107579e+05
4  공장E  9.247514e+05
```

> [!TIP]
> `reset_index()`는 `groupby()`를 사용하여 설정되는 인덱스를 일반적인 데이터 프레임 형태로 변환합니다.

**3. 데이터 정렬 후 출력**

- 산출된 결과를 바탕으로 3번째로 처리 시간이 적은 공장명을 출력합니다.
```python
print('공장명:', mean_response_time.sort_values(by='처리시간').iloc[2, 0])
```
*Output:*
```
공장명: 공장D
```

**2. 서울시 자전거 대여소 정보 분석**

`STATION_ADDR1` 변수에서 구 정보만 추출한 후, 마포구, 성동구의 평균 이동 거리를 구하시오. (소수점 셋째 자리에서 반올림)

- **데이터**: `7_1_2.csv`

```python
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/7_1_2.csv') 
print(df.head())
```
*Output:*
```
          rent_date rent_place  using_time  dist bill_type  STATION_LONGITUDE  \
0  2019-03-19 0:42      51-920           6  1660     BIL002         126.858254   
1  2019-02-14 10:53       ST-148          27  4530     BIL004         126.987793   
2  2019-02-22 17:31        ST-1B          28  4240     BIL002         126.918617   
3  2019-01-07 18:39       ST-366          41  9930     BIL005         127.017662   
4  2019-01-19 16:02       ST-248          11  1080     BIL014         127.029213   

   STATION_LATITUDE STATION_ADDR1  
0         37.549290    서울특별시 양천구 목동 923  
1         37.561840    서울특별시 중구 을지로2가 101-1  
2         37.555069    서울특별시 마포구 신정동 300-1  
3         37.508999    서울특별시 강남구 삼성동 147-2  
4         37.528320    서울특별시 강남구 삼성동 159-1
```


- `+`: 바로 앞의 패턴이 하나 이상 반복됨을 의미
- `구`: '구'라는 문자 찾기 
- `()`: 그룹을 나타내며, 일치한 부분 문자열 캡처

- 한글 음절이 하나 이상 반복되는 문자열에서 마지막이 '구'로 끝나는 문자를 찾는 것이므로:
`df['STATION_ADDR1'].str.extract(r'([가-힣]+구)')`

> [!TIP]
> `str.extract`를 사용할 때는 반드시 소괄호를 사용하여 캡처 그룹을 정의해야 합니다.

- 구 정보를 추출하여 변수를 생성합니다.
```python
df = df.assign(gu=df['STATION_ADDR1'].str.extract(r'([가-힣]+구)')[0])
```

**2. 성동구, 마포구만 추출한 후 평균 이동 거리 계산**

- `.isin`을 활용하여 성동구, 마포구를 필터링한 후 각 구별 평균 거리를 계산합니다.
```python
print(df.loc[df['gu'].isin(['성동구', '마포구']), :].groupby('gu')['dist'].mean().round(2))
```
*Output:*
```
gu
마포구    3045.88
성동구    3202.31
Name: dist, dtype: float64
```


**3. 분기별 총 판매량 분석**

3분기별 총 판매량(제품A~E 합계)의 월평균을 구하고, 월평균이 최대인 연도와 분기를 구하시오.

- **데이터**: `7_1_3.csv`

**1. 분기별 총 판매량 계산**

- 총 판매량을 계산하기 위해 제품A-E의 합계를 계산합니다.
```python
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/7_1_3.csv') 
df['총판매량'] = df[['제품A', '제품B', '제품C', '제품D', '제품E']].sum(axis=1)
```

**2-1. 분기 칼럼 생성 (방법1)**

```python
df1 = df.copy()
```

- 분기를 구하기 위해 기간 칼럼에서 연도와 월을 분리한 새로운 칼럼을 생성합니다.
```python
df1[['연도', '월']] = df1['기간'].str.split('_', expand=True) 
print(df1[['연도', '월']].head())
```
*Output:*
```
     연도   월
0  2018년  1월
1  2018년  2월
2  2018년  3월
3  2018년  4월
4  2018년  5월
```

- 월을 숫자로 처리하기 위해 '월' 문자를 제거합니다.
```python
df1['월'] = df1['월'].str.replace('월', '').astype(int)
```

- `pd.cut()`을 활용하여 분기에 해당하는 구간을 나눈 후 분기 칼럼을 생성합니다.
```python
df1['분기'] = pd.cut(df1['월'], bins=[0, 3, 6, 9, 12], labels=[1, 2, 3, 4], right=True) 
print(df1.head())
```


**2-2. 분기 칼럼 생성 (방법2)**

```python
df2 = df.copy()
```

- 분기를 구하기 위해 정규표현식을 활용하여 기간 칼럼에서 연도와 월을 분리한 새로운 칼럼을 생성합니다.
```python
df2[['연도', '월']] = df2['기간'].str.extract(r'(\d+)년_(\d+)월')
print(df2[['연도', '월']].head())
```
*Output:*
```
     연도  월
0  2018  1
1  2018  2
2  2018  3
3  2018  4
4  2018  5
```

- 연도와 월을 합친 새로운 칼럼을 생성한 후 datetime 형식으로 변환합니다. 또한, datetime 형식으로 변환한 날짜를 분기 형식(`period[Q]`)으로 변환합니다.

```python
df2['연월'] = df2['연도'] + df2['월'] 
df2['분기'] = pd.to_datetime(df2['연월'], format='%Y%m').dt.to_period('Q')
print(df2.head())
```

**3. 분기별 총판매량의 월평균 계산**

```python
quarterly_avg = df1.groupby(['연도', '분기'])['총판매량'].mean().reset_index() # df2도 같은 결과
```

**4. 최댓값을 가지는 연도, 분기 계산**

```python
print(quarterly_avg.loc[quarterly_avg['총판매량'].idxmax()])
```
*Output:*
```
연도     2018년
분기         3
총판매량 3226.666667
Name: 2, dtype: object
```


### 작업형 제2유형

**학업 성과 예측 모델 (다중 분류)**

제공된 학습용 데이터(`7_2_train.csv`)는 학생들의 개인 정보 및 학업 관련 정보(혼인 여부, 지원 방식, 부모의 학력 및 직업, 성별 등)와 해당 학생의 학업 성과(`Target`)를 포함하고 있다. 학습용 데이터를 활용하여 학생의 학업 성과(`Target`)를 예측하는 분류 모델을 개발하고, 가장 우수한 모델을 평가용 데이터(`7_2_test.csv`)에 적용하여 예측 결과를 제출하시오.

- **모델 성능 지표**: Macro F1 Score
- **타깃(라벨)**: `Target` (학업 결과 - 분류 대상 변수)

**Data description**
- `ID`: 고유 식별자
- `Marital Status`: 혼인 여부
- `Application mode`: 지원 방식
- `Course`: 지원한 학과
- `Daytime/evening attendance`: 주간/야간 수업 구분
- `Previous qualification`: 이전 학력
- `Nacionality`: 국적
- `Mother's qualification`: 어머니의 학력
- `Father's qualification`: 아버지의 학력
- `Mother's occupation`: 어머니의 직업
- `Father's occupation`: 아버지의 직업
- `Educational special needs`: 교육적 특수 요구 여부
- `Gender`: 성별
- `Curricular units 1st sem (credited)`: 1학기 인정 학점 수
- `Curricular units 1st sem (enrolled)`: 1학기 수강 과목 수
- `Curricular units 1st sem (evaluations)`: 1학기 평가 횟수
- `Curricular units 1st sem (approved)`: 1학기 통과 과목 수
- `Target`: 학업 결과 (분류 대상 변수)

**제출 형식**
- 파일명: `result.csv` (디렉토리/폴더명 제외)
- 제출 칼럼: `ID`, `pred` (총 2개 칼럼)
- `pred`: 예측된 학업 결과 클래스 (문자열 또는 정수 가능)
- 행 수: 테스트 데이터(`7_2_test.csv`)의 `ID` 수와 동일

```python
import pandas as pd
import numpy as np 
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/7_2_train.csv') 
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/7_2_test.csv')
```

**1. 데이터 탐색**

- 모델을 적합하기 전 데이터에 결측치가 있는지 확인해야 합니다. 결측치가 존재할 경우 모델 적합 시 에러가 발생할 수 있습니다.


```python
print(train.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 309 entries, 0 to 308
Data columns (total 19 columns):
...
dtypes: int64(6), object(13)
memory usage: 46.0+ KB
None
```
- 결측치 없음

```python
print(test.info())
```


- 결측치 없음

- 테스트 데이터를 활용한 최종 결과를 제출하기 위해 ID 칼럼을 따로 저장합니다.
```python
test_id = test['ID']
```
- `level_0`, `ID` 칼럼은 정보가 없는 칼럼이므로 삭제합니다.
```python
train = train.drop(['level_0', 'ID'], axis=1) 
test = test.drop(['level_0', 'ID'], axis=1)
```


**2. 데이터 분할**

- 모델 성능 확인을 위해 훈련 데이터의 일부를 검증 데이터로 나눠주겠습니다.
```python
train_X = train.drop(['Target'], axis=1) 
train_y = train['Target'] 
test_X = test.drop(['Target'], axis=1) # Target variable is dropped from test if it exists
test_y = test['Target'] # Assuming Target exists in test for evaluation in this example
```

```python
from sklearn.model_selection import train_test_split 
train_X, valid_X, train_y, valid_y = train_test_split(train_X, train_y, test_size=0.3, random_state=1) 
print(train_X.shape, train_y.shape, valid_X.shape, valid_y.shape)
```
*Output:*
```
(216, 16) (216,) (93, 16) (93,)
```

**3. 데이터 전처리**

- 범주형 변수에 대해서 라벨 인코딩을 수행하고, 수치형 변수에 대해서 표준화를 수행하겠습니다.

> [!TIP]
> 독립변수에 범주형 변수가 매우 많으므로 원-핫 인코딩을 수행할 경우 데이터의 차원이 급격히 증가하여, 모델 적합시 계산 비용이 커지는 문제가 있습니다. 따라서 라벨 인코딩을 선택합니다.

- 먼저 범주형 변수와 수치형 변수의 각 칼럼명을 저장합니다.
```python
cat_columns = train_X.select_dtypes('object').columns
num_columns = train_X.select_dtypes('number').columns
```

- 라벨 인코딩과 표준화를 위한 메서드를 불러옵니다.
```python
from sklearn.preprocessing import OrdinalEncoder 
from sklearn.preprocessing import StandardScaler
ordinalencoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1) 
stdscaler = StandardScaler()
```

- 훈련 데이터, 검증 데이터, 테스트 데이터 각각에 데이터 전처리를 진행합니다. 전처리 결과는 `numpy.array`로 출력됩니다. 모델 적합시 전처리 완료된 데이터를 `pandas.DataFrame`으로 변경하지 않아도 무방합니다.


```python
train_X_numeric_scaled = stdscaler.fit_transform(train_X[num_columns]) 
valid_X_numeric_scaled = stdscaler.transform(valid_X[num_columns]) 
test_X_numeric_scaled = stdscaler.transform(test_X[num_columns])

train_X_categorical_encoded = ordinalencoder.fit_transform(train_X[cat_columns]) 
valid_X_categorical_encoded = ordinalencoder.transform(valid_X[cat_columns]) 
test_X_categorical_encoded = ordinalencoder.transform(test_X[cat_columns])

train_X_preprocessed = np.concatenate([train_X_numeric_scaled, train_X_categorical_encoded], axis=1) 
valid_X_preprocessed = np.concatenate([valid_X_numeric_scaled, valid_X_categorical_encoded], axis=1) 
test_X_preprocessed = np.concatenate([test_X_numeric_scaled, test_X_categorical_encoded], axis=1)
```

**4. 모델 적합**

- 랜덤 포레스트 모델을 적합해 보겠습니다.
```python
from sklearn.ensemble import RandomForestClassifier 
rf = RandomForestClassifier(random_state=1) 
rf.fit(train_X_preprocessed, train_y)
```

- 검증 데이터를 활용하여 모형 성능을 확인해 보겠습니다.
```python
from sklearn.metrics import f1_score
pred_val = rf.predict(valid_X_preprocessed) 
print('valid f1-score:', f1_score(valid_y, pred_val, average='macro'))
```
*Output:*
```
valid f1-score: 0.5574074074074074
```

**5. 테스트 데이터로 예측**

- 테스트 데이터를 활용하여 최종 예측을 수행합니다. `.predict`를 통해 예측값을 계산합니다.
```python
test_pred = rf.predict(test_X_preprocessed) 
test_pred = pd.DataFrame(test_pred, columns=['pred'])
```

- ID, pred 칼럼만 존재하는 결과 파일을 생성합니다.
```python
result = pd.concat([test_id, test_pred], axis=1) 
print(result.head(2))
```
*Output:*
```
   ID      pred
0  1903  Graduate
1   796  Graduate
```


- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) 
# 시험에서 제시되는 파일명 작성할 것
```

- 만약 모델 성능이 낮다고 판단되면, 교차검증을 활용한 하이퍼파라미터 튜닝을 진행해볼 수 있습니다. 홀드 아웃 방법이 아닌 k-폴드 교차검증을 진행할 것이기 때문에 기존에 분할했던 학습 데이터와 검증 데이터를 합치겠습니다.

```python
train_X_full = np.concatenate([train_X_preprocessed, valid_X_preprocessed], axis=0) 
train_y_full = np.concatenate([train_y, valid_y], axis=0)
```

- GridSearchCV를 통해 하이퍼파라미터 튜닝을 진행하겠습니다.
```python
from sklearn.model_selection import GridSearchCV
param_grid = {
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10]
} 
rf = RandomForestClassifier(random_state=1) 
rf_search = GridSearchCV(
### 작업형 제3유형

**문제 1. 학습 프로그램 효과 분석 (대응표본 t-검정)**

어느 학교에서 50명의 학생들을 대상으로 새로운 학습 프로그램의 효과를 검증하고자 한다. 각 학생에 대해 학습 전과 학습 후의 시험 점수를 측정하였다.

- **데이터**: `7_3_1.csv`
- **①** 학습 전과 학습 후의 시험 점수의 평균과 표준편차를 구하시오. (소수점 둘째 자리까지 반올림)
- **②** 학습 전후의 점수 차이가 유의미한지 검정하기 위해 대응표본 t-검정을 수행하고, 검정통계량을 계산하시오. (소수점 둘째 자리까지 반올림)
- **③** p-value를 바탕으로 유의수준 5%에서 귀무가설의 기각/채택 여부를 결정하시오. (p-value는 소수점 셋째 자리까지 반올림)

```python
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/7_3_1.csv')
```


- 학습 전과 학습 후의 시험 점수의 평균과 표준편차를 계산하고 소수점 둘째 자리까지 반올림하여 출력합니다.

```python
# 학습 전 평균과 표준편차 계산
mean_before = data['before'].mean() 
std_before = data['before'].std()
# 학습 후 평균과 표준편차 계산
mean_after = data['after'].mean() 
std_after = data['after'].std()

print('학습 전 점수 평균:', round(mean_before, 2)) 
print('학습 전 점수 표준편차:', round(std_before, 2)) 
print('학습 후 점수 평균:', round(mean_after, 2)) 
print('학습 후 점수 표준편차:', round(std_after, 2))
```
*Output:*
```
학습 전 점수 평균: 71.41
학습 전 점수 표준편차: 11.37
학습 후 점수 평균: 76.3
학습 후 점수 표준편차: 11.94
```

- 대응표본 t-검정은 `ttest_rel()`를 통해 수행할 수 있습니다.
```python
from scipy.stats import ttest_rel 
# 대응 표본 t-검정 수행 
t_statistic, p_value = ttest_rel(data['before'], data['after']) 
print('t-통계량:', t_statistic.round(2))
```
*Output:*
```
t-통계량: -7.9
```

- 유의수준 5% 하에서 p-value가 0.05보다 작은지 확인하여 귀무가설의 기각과 채택을 결정합니다.

```python
p_value = round(p_value, 3)
# 결과 해석 
if p_value < 0.05: 
    result = "기각" 
else: 
    result = "채택" 
print(result)
```
*Output:*
```
기각
```


**문제 2. 고객 제품 구매 예측 (로지스틱 회귀)**

어느 회사가 조사한 고객 데이터는 100개의 샘플로 이루어져 있으며, 각 샘플에는 고객의 나이, 소득, 가족 수, 그리고 제품 구매 여부가 포함되어 있다. 로지스틱 회귀 분석을 통해 고객의 제품 구매 여부를 예측하고자 한다. (임곗값 0.5 기준)

- **데이터**: `7_3_2_train.csv`, `7_3_2_test.csv`
- **①** 로지스틱 회귀 분석을 수행하고, 소득 변수의 오즈비를 계산하시오.
- **②** train 데이터 기준의 잔차 이탈도(Residual Deviance)를 계산하시오.
- **③** test 데이터로 오분류율을 계산하시오.

```python
import pandas as pd 
train_data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/7_3_2_train.csv') 
test_data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/7_3_2_test.csv')
```

- 상수항을 포함하여 로지스틱 회귀모델을 적합합니다.
```python
import statsmodels.api as sm
# 독립 변수와 종속 변수 설정 (train 데이터 사용)
X_train = train_data[['age', 'income', 'family_members']]
y_train = train_data['purchase']
# 상수항 추가 
X_train = sm.add_constant(X_train) 
# 로지스틱 회귀 분석 모델 적합 
logit_model = sm.Logit(y_train, X_train).fit() 
# 모델 요약 출력
print(logit_model.summary())
```
*Output:*
```
                           Logit Regression Results                           
==============================================================================
Dep. Variable:               purchase   No. Observations:                  100
Model:                          Logit   Df Residuals:                       96
Method:                           MLE   Df Model:                            3
Date:                Thu, 13 Feb 2025   Pseudo R-squ.:                 0.02405
Time:                        07:07:40   Log-Likelihood:                -54.094
converged:                       True   LL-Null:                       -55.427
Covariance Type:            nonrobust   LLR p-value:                    0.4461
==================================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
----------------------------------------------------------------------------------
const             -0.9261      1.127     -0.821      0.411      -3.136       1.284
age               -0.0066      0.014     -0.459      0.646      -0.035       0.022
income          1.521e-05   1.65e-05      0.919      0.358   -1.72e-05    4.76e-05
family_members     0.2042      0.202      1.008      0.313      -0.193       0.601
==================================================================================
```


- 오즈비를 계산하기 위해 `np.exp()`를 적용합니다. 소수점 셋째 자리까지 반올림한 결과를 출력합니다.

```python
import numpy as np
# 특정 변수 'income'의 오즈비 계산
odds_ratios = np.exp(logit_model.params) 
print('소득(income)의 오즈비:', odds_ratios['income'].round(3))
```
*Output:*
```
소득(income)의 오즈비: 1.0
```

- `.llf`를 활용하여 잔차 이탈도를 계산합니다. (Residual Deviance = -2 * Log-Likelihood Function(LLF))

```python
# 잔차 이탈도 계산
residual_deviance = -2 * logit_model.llf 
print('잔차 이탈도:', residual_deviance)
```
*Output:*
```
잔차 이탈도: 108.18783555703051
```

- 훈련 데이터로 학습한 모델을 활용하여 테스트 데이터에 대한 예측을 수행합니다.
```python
# 독립 변수와 종속 변수 설정 (test 데이터 사용)
X_test = test_data[['age', 'income', 'family_members']]
y_test = test_data['purchase']
# 상수항 추가
X_test = sm.add_constant(X_test)
# 예측 수행
y_pred_prob = logit_model.predict(X_test)
y_pred = (y_pred_prob >= 0.5).astype(int)
```

- 테스트 데이터에 대한 오분류율을 계산합니다.
```python
# 오류율 계산 
error_rate = np.mean(y_pred != y_test) 
print('오류율:', error_rate)
```
*Output:*
```
오류율: 0.35
```


**시험시간**: 180분 | **풀이시간**: - | **합격점수**: - | **내점수**: -

## 기출문제 제6회 (2023-06-24 시행)

데이터셋 경로: `https://raw.githubusercontent.com/YoungjinBD/data/main/exam/`

### 작업형 제1유형

**1. 제품 가격 차이 분석**

다음 데이터에서 `ProductA` 가격과 `ProductB` 가격이 모두 0원이 아닌 데이터를 필터링하고, `ProductA`와 `ProductB`의 가격 차이를 정의하시오. 각 도시별 가격 차이의 평균 중 가장 큰 값을 구하시오. (소수점 첫째 자리에서 반올림)

- **데이터**: `6_1_1.csv`

```python
import pandas as pd 
import numpy as np 
pd.set_option('display.max_columns', None) 
# 모든 칼럼이 출력되게 조절
from sklearn import set_config 
set_config(display="diagram") 
# scikit-learn 파이프라인 시각화
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/6_1_1.csv') 
print(df.head())
```
*Output:*
```
  도시명  ProductA가격  ProductB가격
0  울산         25000         10000
1  인천         30000             0
2  광주         15000          8000
3  울산             0         10000
4  대구         25000          6000
```

- AND 연산자를 사용하여 `ProductA` 가격과 `ProductB` 가격 모두 0원이 아닌 행만 포함하는 데이터프레임을 생성합니다.

```python
filtered_df = df.loc[(df['ProductA가격'] != 0) & (df['ProductB가격'] != 0), :]
```

- `ProductA` 가격과 `ProductB` 가격의 차이를 연산하여 변수로 정의합니다.
```python
filtered_df.loc[:, '차이'] = np.abs(filtered_df['ProductA가격'] - filtered_df['ProductB가격'])
```


- 도시별 가격 차이의 평균을 `mean()`으로 계산합니다.
```python
mean_difference_by_city = filtered_df.groupby('도시명')['차이'].mean()
```

- `max()`로 해당 데이터에서 최댓값을 가져옵니다. `round()` 함수를 사용해 소수점 첫째 자리까지 반올림합니다.

```python
max_mean_difference = round(mean_difference_by_city.max(), 1) 
print("도시별 가격 차이의 평균 중 가장 큰 값:", max_mean_difference)
```
*Output:*
```
도시별 가격 차이의 평균 중 가장 큰 값: 16333.3
```

**2. BMI 체중 분류 분석**

100명의 키와 몸무게를 조사하여 적정 체중인지 판단할 수 있는 BMI를 산출하려 한다. 아래 표를 참고하여 BMI를 기준으로 저체중, 정상, 과체중, 비만을 구분하고, 저체중인 사람과 비만인 사람의 총 합을 구하시오.

- **데이터**: `6_1_2.csv`
- **BMI 구분**:
    - 저체중: 18.5 미만
    - 정상: 18.5 이상 23 미만
    - 과체중: 23 이상 25 미만
    - 비만: 25 이상

```python
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/6_1_2.csv') 
print(df.head())
```
*Output:*
```
   Height_cm   Weight_kg
0  165.021320   66.131592
1  183.219470   82.164648
2  140.006862  110.875368
3  158.139954   68.581581
4  148.805353  112.682812
```

**1. BMI 계산**
- `Height_cm`의 경우 cm를 100으로 나누어 m 기준으로 변환한 후 BMI 공식을 적용하여 파생변수를 생성합니다.
```python
df['Height_m'] = df['Height_cm'] / 100
df['BMI'] = np.round(df['Weight_kg'] / (df['Height_m'] ** 2), 1)
```

**2-1. 저체중, 정상, 과체중, 비만 구분 (방법1)**


- `.loc`를 이용해서 각 조건에 맞는 값을 직접 할당합니다.
```python
df1 = df.copy() 
df1['Category'] = 'Unknown' 
df1.loc[df['BMI'] >= 25, 'Category'] = 'Severely Obese' 
df1.loc[(df['BMI'] < 25) & (df['BMI'] >= 23), 'Category'] = 'Obese' 
df1.loc[(df['BMI'] < 23) & (df['BMI'] >= 18.5), 'Category'] = 'Normal' 
df1.loc[df['BMI'] < 18.5, 'Category'] = 'Underweight'

print(df1['Category'].value_counts())
```
*Output:*
```
Category
Severely Obese    52
Underweight       22
Normal            16
Obese             10
Name: count, dtype: int64
```

**2-2. 저체중, 정상, 과체중, 비만 구분 (방법2)**

- `pd.cut()`을 활용하여 각 조건에 맞는 값을 할당합니다. `pd.cut()` 기본 옵션은 `right=True`로 오른쪽 경계값을 포함시킵니다(18.5 초과 23 이하). 따라서 `right=False`로 변경해줘야 왼쪽 경계값을 포함시키며, BMI 표와 같은 조건을 설정할 수 있습니다(18.5 이상 23 미만).

```python
df2 = df.copy() 
bins = [-float('inf'), 18.5, 23, 25, float('inf')] 
labels = ['Underweight', 'Normal', 'Obese', 'Severely Obese'] 
df2['Category'] = pd.cut(df2['BMI'], bins=bins, labels=labels, right=False)
print(df2['Category'].value_counts())
```
*Output:*
```
Category
Severely Obese    52
Underweight       22
Normal            16
Obese             10
Name: count, dtype: int64
```


**3. 비만과 저체중인 인원 수 계산**

- `.shape`는 (행 개수, 열 개수) 형태의 튜플을 반환하며 `.shape[0]`을 사용하면 행 개수, 즉 인원 수를 가져옵니다.

```python
severely_obese_count = df2[df2['Category'] == 'Severely Obese'].shape[0]
underweight_count = df2[df2['Category'] == 'Underweight'].shape[0] 
total_count = severely_obese_count + underweight_count

print(f"비만 인원: {severely_obese_count}") 
print(f"저체중 인원: {underweight_count}") 
print(f"비만과 저체중 총 인원: {total_count}")
```
*Output:*
```
비만 인원: 52
저체중 인원: 22
비만과 저체중 총 인원: 74
```

**3. 공장 순생산량 분석**

다음 데이터에서 연도별로 가장 큰 순생산량(생산된 제품 수 - 판매된 제품 수)을 가진 공장을 찾고, 순생산량의 합을 계산하시오.

- **데이터**: `6_1_3.csv`
- `products_made_domestic`: 국내 생산된 제품 수
- `products_made_international`: 해외 생산된 제품 수
- `products_sold_domestic`: 국내 판매된 제품 수
- `products_sold_international`: 해외 판매된 제품 수

```python
df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/6_1_3.csv') 
print(df.head())
```
*Output:*
```
     factory  products_made_domestic  products_made_international  ...  year
0  Factory B                    1428                          814  ...  2020
1  Factory C                    1752                          369  ...  2023
2  Factory E                    1263                          657  ...  2021
3  Factory D                     621                          856  ...  2020
4  Factory E                    1850                          622  ...  2023
```

- 순생산량(생산된 제품 수 - 판매된 제품 수) 칼럼을 생성합니다.
```python
df['net_production'] = ((df['products_made_domestic'] + df['products_made_international']) - 
                        (df['products_sold_domestic'] + df['products_sold_international']))
```


- 연도, 공장별로 `net_production` 값의 총합(net_sum)을 계산합니다.
```python
result = df.loc[:, ['year', 'factory', 'net_production']].groupby(['year', 'factory']).agg(net_sum=('net_production', 'sum')).reset_index()
```

- `net_sum`이 최대인 연도, 공장 결과를 저장합니다.
```python
max_production_per_year = result.loc[result.groupby('year')['net_sum'].idxmax()]
```

- 전체 기간의 `net_sum`의 합을 계산합니다.
```python
total_max_production_sum = max_production_per_year['net_sum'].sum() 
print(f"전체 기간의 해당 순생산량들의 합: {total_max_production_sum}")
```
*Output:*
```
전체 기간의 해당 순생산량들의 합: 9130
```


작업형제2유형 제공된 학습용 데이터（6_2_train.csv）는 환자의 나이 , 성별 , 체질량지수（BMI) , 혈당 및 콜레스테롤 수치 등의 정보를 포함하고 있으며 , 이로부터 이완기 혈압（DBP）을 예측하고자 한다 . 학습용 데이터를 활용하여 환자의 이완기 혈압（DBP）을 예측하는 회귀 모델을 개발하고 , 성능이 가장 우수한 모델을 평가용 데이터 (6_2_test.csv）에 적용하여 예측 결과를 제출하시오， ※ 모델 성능 지표 : RMSE(Root Mean Squared Error) ※leveL0 칼럼은 인덱스 초기화 과정에서 생성된 것으로 분석 시 제외 Data description ㄸ〕 : 고유 식별자 Age : 나이 Gender : 성별（범주형： Male/FemaLe 등） BMI ; 체질량지수 ALT : 간 기능 수치 FPG ; 공복혈당 ChoL '. 총 콜레스테롤 Tn : 중성지방 HOL: 고밀도지단백 콜레스테롤 LD L : 저밀도지단백 콜레스테롤 DBP : 이완기 혈압 560 PART 07 . 최신 기출문저

제출 형식 파일명 : resutt.csv （디렉토리／폴더명 제외） 제출 칼럼 : ID. pred （총 2개 칼럼） pred : 예측된 이완기 혈압（DBP) 값 （실수형 가능） 행 수 : 테스트 데이터（6_2_test.csv）의 ＂〕 수와 동일

```python
import pandas as pd 
import numpy as np 
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/6_2_trajn.csv ') 
test = pd.read_csv( 'https://raw.githubusercontent.com/YoungjinBD/data/main/exam/6_2_test.csv')
```
1 . 데이터 탐색

- 모델을 적합하기 전 데이타에 결측치가 있는지 확인해야 합니다 . 결측치가 존재할 경우 모델 
적합 시 에러가 발생할 수 있습니다．

```python
print(train.info 0)
```
<class 'pandas. core. frame. DataFrame 5 Rangelndex: 301 entries, 0 to 300 Data columns (total 12 columns):

# 
Column Non-Null Count Dtype 0 level 0 301 non-null int64 1 ID 301 non-null int64

## 2 
Age 301 non-null int64 3 Gender 290 non-null object H결측치존재 4 BMI 301 non-null f1oat64 5 DBP 301 non-null int64 6 FPG 301 non-null f1oat64 7 Chol 301 non-null f1oat64 8 Tn 301 non-null f1oat64 9 HDL 301 non-null f1oat64 10 LDL 301 non-null f1oat64 11 ALT 301 non-null f1oat64 dtypes: f10at64(7), int64(4), object(1) memory usage: 28.3+ KB pnint(test.infoQ) 기출문제 저］6회 정답 & 해설 561

<class 'pandas. core. frame. DataFrame '> Rangelndex: 129 entries, 0 to 128 Data columns (total 12 columns):

# 
Column Non-Null Count Dtype 0 level_0 129 non-null int64 1 ID 129 non-null int64 2 Age 129 non-null int64

## 3 
Gender 122 non-null object H결측치존재 4 BMI 129 non-null fl.0at64 5 DBPC 129 non-null int64 6 FPG 129 non-null f1oat64 7 Chol 129 non-null f1oat64 ,:8" Tni 129 non-null f1oat64 9 HDL 129 non-null f1oat64 10 LDL 129 non-null f1oat64 11 ALT 129 non-null f1oat64 dtypes: f1oat64(7), 1nt64(4), object(1) memory usage: 12.2+ KB None

- 테스트 데이터를 활용한 최종 결과를 제출하기 위해 II) 칼럼을 따로 저장합니다．
```python
test_id = test[ 'ID ']
```
- level 0, ID 칼럼은 정보가 없는 칼럼이므로 삭제합니다．
```python
train = train.drop(['level_O', 'ID '] , axis = 1)
test = test.drop(['level_0', 'ID'] , axis = 1)
```
562 PART 07· 최신기출문제

2 . 데이터 분할 ' 모델 성능 확인을 위해 훈런 데이터의 일부를 검증 데이터로 나누겠습니다．

```python
train-X = train.drop([ 'DBP'] , axis = 1) 
train_y = train[ 'DBP'] 
test_X = test.drop([ 'DBP'], axis = 1) 
test-y = test[ 'DBP']
```
9rom sklearn.model_sel.ection import train_test_spi.it " train_X, valid_X, train_y, valid_y = train_test_spl.it (train_X, train_y, test_size = 0.3,

```python
긋' 
random_state = 1) 
print(train_X.shape, train_y.shape, valid_X.shape, valid_y.shape)
```
(210, 9) (210,) (91, 9) (91,) 3 . 데이터 전처리

- 범주형 변수에 대해서 원－핫 인코딩을 수행하고 , 결측치가 존재하는 Gender 칼럼에 대해 
결측치 대치 방법을 수행하겠습니다．

- 먼저 범주형 변수와 수치형 변수의 각 칼럼명을 저장합니다．
```python
cat_columns = train_X.select_dtypes('object').columns 
num_columns = train_X.select_dtypes('number').col.umns
```
- 원－핫 인코딩과 최빈값 대치법을 위한 메서드를 불러옵니다．
```python
from sklearn.preprocessing import OneHotEncoder 
from sklearn.impute import Simplelmputer
onehotencoder = OneHotEncoder(sparse_output = False , handle_unknown = 'ignore') 
imputer = Simple工mputer(strategy = 'most_frequent')
```
' 훈런 데이터， 검증 데이터 , 데스트 데이터 각각에 데이터 전처리를 진행합니다 . 전처리 결과 는 numpy. array로 출력됩니다 . 모델 적합시 전처리 완료된 데이터를 pandas. DataFrame 으로 변경하지 않아도 무방합니다．

```python
train_X_categorical_imputed = imputer. fit_transform(train_X[cat_columns]) 
valid_X_categorical_imputed = imputer.transform(val.id_X[cat_colunins]) 
test_X_categorical_imputed 볍 imputer. transform(test_X[cat_columns])
train_X_categoricaL_encoded = onehotencoder. fit_transform(train_x_categorical_imputed) 
valid_X_categorical._encoded = onehotencoder. transform(valid_X_categorical_imputed) 
test_X_categoricaL_encoded = onehotencoder. transforin(test_X_categorical_imputed)
```
기출문제제6회정답＆해설 563

```python
train_X_preprocessed = up . concatenate([train_X[num_col.umns], train_X_categorical_encoded], axis =
```
D D D

```python
valid_X_preprocessed = np. concatenate([valid_X{num_colurnns], vaLid_X_categorical_encoded], axis =
test_X_preprocessed = np. concatenate({test_X[num_columns], test_X_categorical_ericoded], axis =
```
4 . 모델 적합

- 랜덤 포레스트 모델을 적합해 보겠습니다．
```python
from skLearn.ensembLe import RandomForestRegressor 
rf = RandomForestRegressor(random_state = 1) 
rf. fit (train_X_preprocessed, train_y)
```
- 검증 데이터를 활용하여 모형 성능을 확인해 보겠습니다．
```python
from sklearn.metrics import mean_squared_error
pred_val = rf.predict(valid_X)
mse = mean_squared_error(valid_y, pred_val)
rmse = np.sqrt(mse) 
print('valid RMSE:', rmse)
```
*Output:*
```
valid RMSE: 12.521506027104452
```

**5. 테스트 데이터로 예측**

- 테스트 데이터를 활용하여 최종 예측을 수행합니다. `.predict`를 통해 예측값을 계산합니다.
```python
test_pred = rf.predict(test_X_preprocessed) 
test_pred = pd.DataFrame(test_pred, columns=['pred'])
```

- ID, pred 칼럼만 존재하는 결과 파일을 생성합니다.
```python
result = pd.concat([test_id, test_pred], axis=1) 
print(result.head(2))
```
*Output:*
```
     ID   pred
0  2856  73.72
1  3116  80.13
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) # 시험에서 제시되는 파일명 작성할 것
```


- 만약 모델 성능이 낮다고 판단되면, 교차검증을 활용한 하이퍼파라미터 튜닝을 진행해볼 수 있습니다. 홀드 아웃 방법이 아닌 k-폴드 교차검증을 진행할 것이기 때문에 기존에 분할했던 학습 데이터와 검증 데이터를 합치겠습니다.

```python
train_X_full = np.concatenate([train_X_preprocessed, valid_X_preprocessed], axis=0) 
train_y_full = np.concatenate([train_y, valid_y], axis=0)
```

- GridSearchCV를 통해 하이퍼파라미터 튜닝을 진행하겠습니다.
```python
from sklearn.model_selection import GridSearchCV
param_grid = {
    'max_depth': [10, 20, 30], 
    'min_samples_split': [2, 5, 10]
} 
rf = RandomForestRegressor(random_state=1) 
rf_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=3,
    scoring='neg_root_mean_squared_error'
) 
rf_search.fit(train_X_full, train_y_full) 
print('교차검증 RMSE-score:', -rf_search.best_score_)
```
*Output:*
```
교차검증 RMSE-score: 11.113614481372197
```

> [!TIP]
> 파라미터 값의 범위가 넓어지면 모델 학습 시 많은 시간이 소요될 수 있으므로 주의가 필요합니다.

- 하이퍼파라미터 튜닝 결과를 바탕으로 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred2 = rf_search.predict(test_X_preprocessed) 
test_pred2 = pd.DataFrame(test_pred2, columns=['pred'])
```

- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰줍니다.
```python
result = pd.concat([test_id, test_pred2], axis=1)
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) 
# 시험에서 제시되는 파일명 작성할 것
```


**ColumnTransformer와 Pipeline을 활용한 방법**

```python
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/6_2_train.csv') 
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/6_2_test.csv') 
test_id = test['ID']

train = train.drop(['level_0', 'ID'], axis=1) 
test = test.drop(['level_0', 'ID'], axis=1)

train_X = train.drop(['DBP'], axis=1) 
train_y = train['DBP']
test_X = test.drop(['DBP'], axis=1) 
test_y = test['DBP']
```

- ColumnTransformer를 활용하면 연속형 변수와 수치형 변수 각각에 대해서 한 번에 전처리를 진행할 수 있습니다.

```python
from sklearn.preprocessing import OneHotEncoder 
from sklearn.impute import SimpleImputer
onehotencoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore') 
imputer = SimpleImputer(strategy='most_frequent')
```

- ColumnTransformer를 활용하여 데이터 전처리 방식을 정의하겠습니다.
```python
cat_columns = train_X.select_dtypes('object').columns
num_columns = train_X.select_dtypes('number').columns

from sklearn.compose import ColumnTransformer
c_transformer = ColumnTransformer( 
    transformers=[ 
        ('cat', onehotencoder, cat_columns), 
        ('num', imputer, num_columns) 
    ], 
    remainder='passthrough' 
)
```


- ColumnTransformer로 데이터 전처리를 진행한 후 Pipeline을 활용해서 모델을 정의하겠습니다.

```python
from sklearn.pipeline import Pipeline 
from sklearn.model_selection import GridSearchCV 
from sklearn.ensemble import RandomForestRegressor

pipe_rf = Pipeline([
    ("preprocess", c_transformer), 
    ("regressor", RandomForestRegressor(random_state=1)) 
])
```

- Pipeline을 활용해서 모델링을 정의한 후 GridSearchCV를 활용하여 교차검증을 통한 파라미터 튜닝을 진행하겠습니다.

```python
param_grid = {
    'regressor__max_depth': [10, 20, 30], 
    'regressor__min_samples_split': [2, 5, 10]
} 
rf_search_pipe = GridSearchCV(
    estimator=pipe_rf,
    param_grid=param_grid, 
    cv=5, 
    scoring='neg_root_mean_squared_error'
) 
rf_search_pipe.fit(train_X, train_y)
```

- 교차검증 RMSE-score는 다음과 같습니다.
```python
print('교차검증 RMSE-score:', -rf_search_pipe.best_score_)
```
*Output:*
```
교차검증 RMSE-score: 11.411497349635692
```

- 파라미터 튜닝 결과를 바탕으로 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred3 = rf_search_pipe.predict(test_X) 
test_pred3 = pd.DataFrame(test_pred3, columns=['pred'])
```

- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰줍니다.
```python
result = pd.concat([test_id, test_pred3], axis=1) 
print(result.head(2))
```
*Output:*
```
     ID       pred
0  2856  74.134712 
1  3116  84.494603
```


- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) # 시험에서 제시되는 파일명 작성할 것
```

### 작업형 제3유형

**문제 1. 업무 수행 시간 분석 (K-S 검정)**

어느 회사에서 100명의 직원들을 대상으로 하루 업무 수행 시간을 조사하였다. K-S 검정을 통해 업무 수행 시간이 정규분포를 따르는지 검정하고자 한다.

- **데이터**: `6_3_1.csv`
- **①** 직원들의 업무 수행 시간의 평균과 표준편차를 구하시오. (소수점 셋째 자리까지 반올림)
- **②** 직원들의 업무 수행 시간이 정규분포를 따르는지 K-S 검정을 실시하고, 검정통계량을 계산하시오. (소수점 셋째 자리까지 반올림)
- **③** p-value를 바탕으로 유의수준 5%에서 귀무가설의 기각/채택 여부를 결정하시오. (p-value는 소수점 셋째 자리까지 반올림)

```python
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/6_3_1.csv')
```

- 직원들의 하루 업무 수행 시간의 평균과 표준편차를 계산하고 소수점 셋째 자리까지 반올림하여 출력합니다.

```python
# 업무 수행 시간 평균과 표준편차 계산
mean_work_hours = data['work_hours'].mean()
std_work_hours = data['work_hours'].std()
print('업무 수행 시간 평균:', round(mean_work_hours, 3)) 
print('업무 수행 시간 표준편차:', round(std_work_hours, 3))
```
*Output:*
```
업무 수행 시간 평균: 8.09
업무 수행 시간 표준편차: 1.519
```


- K-S 검정은 `kstest()`를 통해 수행할 수 있습니다.
```python
from scipy.stats import kstest, norm
# 정규분포의 평균과 표준편차를 사용하여 K-S 검정 수행 
statistic, p_value = kstest(data['work_hours'], 'norm', args=(mean_work_hours, std_work_hours))
print('K-S 검정통계량:', round(statistic, 3)) 
print('p-value:', round(p_value, 3))
```
*Output:*
```
K-S 검정통계량: 0.064
p-value: 0.778
```

- 유의수준 5% 하에서 p-value가 0.05보다 작은지 확인하여 귀무가설의 기각과 채택을 결정합니다.

```python
p_value = round(p_value, 3) 
# 결과 해석 
if p_value < 0.05: 
    result = "기각" 
else: 
    result = "채택" 
print(result)
```
*Output:*
```
채택
```

**문제 2. 주택 가격 회귀 분석**

다음의 데이터는 주택들의 가격(price), 면적(area), 방의 개수(rooms), 연식(age)을 조사하여 기록한 것이다.

- **데이터**: `6_3_2.csv`
- **①** 주택 가격을 종속변수로 하고, 면적, 방의 개수, 연식을 독립변수로 하는 다중회귀 분석을 수행하여. 회귀계수가 가장 높은 변수를 구하시오. (다중회귀모형 적합 시 절편 포함)
- **②** 유의수준 5% 하에서 각 독립변수가 주택 가격에 미치는 영향이 통계적으로 유의미한지 판단하고 유의미한 변수 개수를 구하시오.

```python
import pandas as pd 
data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/6_3_2.csv')
```


- 절편(상수항)을 추가한 후, 모델을 적합시킵니다.
```python
import statsmodels.api as sm
# 독립 변수와 종속 변수 설정
X = data[['area', 'rooms', 'age']]
y = data['price']
# 상수항 추가
X = sm.add_constant(X)
# 다중회귀 분석 모델 적합
model = sm.OLS(y, X).fit()
```

- 회귀계수가 가장 높은 변수를 확인합니다.
```python
import numpy as np
# 회귀계수 추출 
coefficients = model.params[1:] 
print('회귀계수가 가장 큰 변수:', coefficients.idxmax())
```
*Output:*
```
회귀계수가 가장 큰 변수: rooms
```

- 각 독립변수가 주택 가격에 미치는 영향이 통계적으로 유의미한지 판단하기 위해 p-value를 확인하고, 유의미한 변수의 개수를 계산합니다.

```python
p_values = model.pvalues[1:] 
print('유의미한 변수 개수:', np.sum(p_values < 0.05))
```
*Output:*
```
유의미한 변수 개수: 3
```


**시험시간**: 180분 | **풀이시간**: - | **합격점수**: 60점 | **내점수**: -

## 기출문제 제5회 (2022-12-03 시행)

데이터셋 경로: `https://raw.githubusercontent.com/YoungjinBD/data/main/exam/`

### 작업형 제1유형

**1. 특수문자 제거 및 IQR 계산**

다음 데이터에서 `conventional` 칼럼의 특수문자를 제거하고, IQR(3분위수 - 1분위수)를 구하시오. (소수점 첫째 자리에서 반올림)

- **데이터**: `5_1_1.csv`

```python
import pandas as pd 
import numpy as np 
pd.set_option('display.max_columns', None)
# 모든 칼럼이 출력되게 조절
from sklearn import set_config 
set_config(display="diagram")
# scikit-learn 파이프라인 시각화
dat = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/5_1_1.csv') 
print(dat.head())
```
*Output:*
```
  minority  crime  poverty  language  highschool        date  conventional
0     26.1     49     18.9       0.2        43.5  2023-01-01         26.1
1      5.7     62     10.7       1.7        17.5  2023-01-02         5.7
2     18.9     81     13.2       3.2        27.6  2023-01-03         18.9
3     16.9     38     19.0       0.2        44.5  2023-01-04         16.9
4     24.3     73     10.4       5.0        26.0  2023-01-05         24.3
```

**1. 특수문자 삭제**

- 칼럼 내에 특수 문자를 제거하기 위해 정규 표현식을 활용합니다.
    - `a-z`: 소문자 알파벳에 해당하는 모든 문자
    - `A-Z`: 대문자 알파벳에 해당하는 모든 문자
    - `0-9`: 0~9까지의 모든 문자
    - `가-힣`: 가~힣까지의 모든 한국어 문자
    - `a-zA-Z0-9가-힣`: 영어, 한국어, 숫자 선택
    - `^`: 부정(not)을 의미
    - `[]`: 대괄호 안에 있는 문자 중 하나를 의미

- 영어, 숫자, 한국어를 제외한 모든 문자를 제거합니다.
```python
dat.loc[:, 'conventional'] = dat.loc[:, 'conventional'].str.replace(r'[^a-zA-Z0-9가-힣]', '', regex=True)
```


**2. IQR(3분위수 - 1분위수) 계산**

- 정규표현식으로 특수문자 제거 후 IQR을 계산하기 위해 float형으로 변환합니다. 변환하기 전에 공백은 Nan으로 처리해주어야 합니다.

```python
dat.loc[:, 'conventional'] = dat.loc[:, 'conventional'].replace('', np.nan)
dat.loc[:, 'conventional'] = dat.loc[:, 'conventional'].astype(float)
```

- IQR을 계산합니다.
```python
Q1 = dat['conventional'].quantile(0.25)
Q3 = dat['conventional'].quantile(0.75)
IQR = Q3 - Q1 
print('IQR:', np.round(IQR))
```
*Output:*
```
IQR: 9.0
```

**2. 조건부 범죄율 평균 계산**

위 데이터에서 흑인 또는 히스패닉 비율(`minority`) + 빈곤율(`poverty`) > 2이며, 도시 유형(`city`)이 state인 도시의 범죄율(`crime`) 평균을 구하시오. (소수점 첫째 자리에서 반올림)

- 문제의 조건에 해당하는 행을 필터링합니다.
```python
# (dat['minority'] + dat['poverty'] > 2) & (dat['city'] == 'state')
```

- 조건을 사용하여 범죄율(`crime`) 칼럼을 선택해 별도로 저장합니다.
```python
sub_dat = dat.loc[(dat['minority'] + dat['poverty'] > 2) & (dat['city'] == 'state'), 'crime']
```

- 범죄율(`crime`) 평균을 계산한 후 소수점 첫째 자리에서 반올림하여 결과를 산출합니다.
```python
print(sub_dat.mean().round(1))
```
*Output:*
```
61.0
```


**3. 특정 기간 이후 온도 평균**

다음 데이터에서 2016년 9월 이후, 온도(`actual`)의 평균을 구하시오. (소수점 첫째 자리에서 반올림)

- **데이터**: `5_1_2.csv`

```python
dat = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/5_1_2.csv') 
print(dat.head())
```
*Output:*
```
   year  month  day  week  temp_2  temp_1  average  actual  friend
0  2016      1    1   Fri      45      45     45.6      45      29
1  2016      1    2   Sat      44      45     45.7      44      61
2  2016      1    3   Sun      45      44     45.8      41      56
3  2016      1    4   Mon      44      41     45.9      40      53
4  2016      1    5  Tues      41      40     46.0      44      41
```

- year, month, day 칼럼을 활용하여 년-월-일 형식의 날짜 칼럼을 생성합니다.
```python
dat['date'] = pd.to_datetime(dat[['year', 'month', 'day']])
```

- 생성된 date 칼럼을 index에 할당합니다.
```python
dat.set_index('date', inplace=True)
```

- 2016-09-01 이후 온도(`actual`)의 평균을 계산합니다.
```python
print('actual 평균:', dat.loc['2016-09-01':, 'actual'].mean().round(1))
```
*Output:*
```
actual 평균: 58.0
```

> [!TIP]
> **기적의 Tip**
> 데이터의 index를 DatetimeIndex로 변경하면 시간 기반 인덱싱을 수행하기 용이해집니다.


### 작업형 제2유형

제공된 학습용 데이터(`5_2_train.csv`)는 유방암 종양의 다양한 특성(반지름, 둘레, 면적, 질감 등)에 대한 정량적 지표와 악성/양성 여부(`target`)를 포함하고 있다. 학습용 데이터를 활용하여 종양이 악성일 확률(`target=1`)을 예측하는 이진 분류 확률 예측 모델을 개발하고, 가장 우수한 모델을 평가용 데이터(`5_2_test.csv`)에 적용하여 예측 결과를 제출하시오.

- **모델 성능 지표**: AUC(Area Under the Curve)
- `level_0` 칼럼은 인덱스 초기화로 생긴 값으로 분석에 사용하지 않음

**Data description**
종양의 크기, 질감 등 특징을 나타내는 데이터입니다.
- `ID`: 고유 식별자
- `mean radius`: 반지름 평균
- `mean texture`: 질감 평균
- `mean_perimeter`: 둘레 평균
- `mean area`: 면적 평균
- `mean_smoothness`: 매끄러움 평균
- `mean_compactness`: 조밀도 평균
- `mean_concavity`: 오목함 평균
- `mean_concave_points`: 오목한 점 평균
- `mean_symmetry`: 대칭성 평균
- `mean_fractal_dimension`: 프랙탈 차원 평균
- `radius_error`: 반지름 오차
- ... : 기타 유사한 통계 지표들
- `target`: 악성 종양 여부 (0: 양성, 1: 악성)

**제출 형식**
- 파일명: `result.csv` (디렉토리/폴더명 제외)
- 제출 칼럼: `ID`, `pred` (총 2개 칼럼)
    - `prob`: 예측된 악성 확률 (0 이상 1 이하의 실수)
- 행 수: 테스트 데이터(`5_2_test.csv`)의 ID 수와 동일

```python
import pandas as pd 
import numpy as np 
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/5_2_train.csv') 
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/5_2_test.csv')
```

**1. 데이터 탐색**

- 모델을 적합하기 전 데이터에 결측치가 있는지 확인해야 합니다. 결측치가 존재할 경우 모델 적합 시 에러가 발생할 수 있습니다.



```python
print(train.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 398 entries, 0 to 397
Data columns (total 33 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   level_0                  398 non-null    int64  
 1   ID                       398 non-null    int64  
 2   mean radius              398 non-null    float64
 3   mean texture             398 non-null    float64
 4   mean_perimeter           398 non-null    float64
 ...
 21  fractal dimension error  378 non-null    float64  # 결측치 존재
 32  target                   398 non-null    int64  
dtypes: float64(30), int64(3)
memory usage: 182.7 KB
```

```python
print(test.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 171 entries, 0 to 170
Data columns (total 33 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   level_0                  171 non-null    int64  
 1   ID                       171 non-null    int64  
 2   mean radius              171 non-null    float64
 3   mean texture             171 non-null    float64
 4   mean_perimeter           171 non-null    float64
 ...
 21  fractal dimension error  160 non-null    float64  # 결측치 존재
 32  target                   171 non-null    int64  
dtypes: float64(30), int64(3)
memory usage: 44.2 KB
```

- 테스트 데이터를 활용한 최종 결과를 제출하기 위해 ID 칼럼을 따로 저장합니다.
```python
test_id = test['ID']
```


- `level_0`, `ID` 칼럼은 정보가 없는 칼럼이므로 삭제합니다.
```python
train = train.drop(['level_0', 'ID'], axis=1) 
test = test.drop(['level_0', 'ID'], axis=1)
```

**2. 데이터 분할**

- 모델 성능 확인을 위해 훈련 데이터의 일부를 검증 데이터로 나누겠습니다.
```python
train_X = train.drop(['target'], axis=1) 
train_y = train['target'] 
test_X = test.drop(['target'], axis=1) 
test_y = test['target']

from sklearn.model_selection import train_test_split 
train_X, valid_X, train_y, valid_y = train_test_split(train_X, train_y, test_size=0.3, random_state=1) 
print(train_X.shape, train_y.shape, valid_X.shape, valid_y.shape)
```
*Output:*
```
(278, 30) (278,) (120, 30) (120,)
```

**3. 데이터 전처리**

- 결측치가 존재하는 칼럼에 대해 결측치 대치 방법을 수행하겠습니다.
```python
from sklearn.impute import SimpleImputer 
imputer = SimpleImputer(strategy='mean')
```

- 훈련 데이터, 검증 데이터, 테스트 데이터 각각에 데이터 전처리를 진행합니다.
- 전처리 결과는 `numpy.array`로 출력됩니다. 모델 적합시 전처리 완료된 데이터를 `pandas.DataFrame`으로 변경하지 않아도 됩니다.

```python
train_X_preprocessed = imputer.fit_transform(train_X) 
valid_X_preprocessed = imputer.transform(valid_X) 
test_X_preprocessed = imputer.transform(test_X)
```

**4. 모델 적합**

- 랜덤 포레스트 모델을 적합해 보겠습니다.
```python
from sklearn.ensemble import RandomForestClassifier 
rf = RandomForestClassifier(random_state=1) 
rf.fit(train_X_preprocessed, train_y)
```


- 검증 데이터를 활용하여 모델 성능을 확인합니다.
```python
from sklearn.metrics import roc_auc_score 
pred_val = rf.predict_proba(valid_X_preprocessed)[:, 1] 
print('valid AUC:', roc_auc_score(valid_y, pred_val))
```
*Output:*
```
valid AUC: 0.9915433403805497
```

**5. 테스트 데이터로 예측**

- 테스트 데이터를 활용하여 최종 예측을 수행합니다. `.predict_proba`를 통해 예측값을 계산합니다.
```python
test_pred = rf.predict_proba(test_X_preprocessed)[:, 1] 
test_pred = pd.DataFrame(test_pred, columns=['prob'])
```

- ID, prob 칼럼만 존재하는 결과 파일을 생성합니다.
```python
result = pd.concat([test_id, test_pred], axis=1) 
print(result.head(2))
```
*Output:*
```
    ID  prob
0  421  0.38
1   47  0.31
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) # 시험에서 제시되는 파일명 작성할 것
```

- 만약 모델 성능이 낮다고 판단되면, 교차검증을 활용한 하이퍼파라미터 튜닝을 진행해볼 수 있습니다. 홀드 아웃 방법이 아닌 k-폴드 교차검증을 진행할 것이기 때문에 기존에 분할했던 학습 데이터와 검증 데이터를 합치겠습니다.

```python
train_X_full = np.concatenate([train_X_preprocessed, valid_X_preprocessed], axis=0) 
train_y_full = np.concatenate([train_y, valid_y], axis=0)
```


- GridSearchCV를 통해 하이퍼파라미터 튜닝을 진행하겠습니다.
```python
from sklearn.model_selection import GridSearchCV
param_grid = {
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10]
} 
rf = RandomForestClassifier(random_state=1) 
rf_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=3, 
    scoring='roc_auc'
) 
rf_search.fit(train_X_full, train_y_full) 
print('교차검증 AUC-score:', rf_search.best_score_)
```
*Output:*
```
교차검증 AUC-score: 0.9942283419391852
```

> [!TIP]
> 파라미터 값의 범위가 넓어지면 모델 학습 시 많은 시간이 소요될 수 있으므로 주의가 필요합니다.

- 하이퍼파라미터 튜닝 결과를 바탕으로 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred2 = rf_search.predict_proba(test_X_preprocessed)[:, 1] 
test_pred2 = pd.DataFrame(test_pred2, columns=['prob'])
```

- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰줍니다.
```python
result = pd.concat([test_id, test_pred2], axis=1)
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) 
# 시험에서 제시되는 파일명 작성할 것
```


**ColumnTransformer와 Pipeline을 활용한 방법**

```python
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/5_2_train.csv') 
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/5_2_test.csv') 
test_id = test['ID']

train = train.drop(['level_0', 'ID'], axis=1) 
test = test.drop(['level_0', 'ID'], axis=1) 

- 피어슨 상관계수는 `pearsonr()`을 통해 계산할 수 있습니다.
```python
from scipy.stats import pearsonr
# 피어슨 상관계수 계산 
corr, p_value = pearsonr(data['study_hours'], data['exam_scores']) 
print('공부 시간과 시험 점수 간의 피어슨 상관계수:', round(corr, 3))
```
*Output:*
```
공부 시간과 시험 점수 간의 피어슨 상관계수: 0.923
```


- 유의수준 5% 하에서 p-value가 0.05보다 작은지 확인하여 귀무가설의 기각과 채택을 결정합니다.

```python
p_value = round(p_value, 3)
# 결과 해석 
if p_value < 0.05: 
    result = "기각" 
else: 
    result = "채택" 
print(result)
```
*Output:*
```
기각
```

**문제 2. ANOVA 검정**

어느 마케팅 회사에서 세 가지 마케팅 캠페인(A, B, C)의 효과가 유의미하게 다른지를 조사하고자 한다. 각 캠페인에 대해 각각 50명의 고객을 랜덤으로 추출하여 만족도를 조사하였다.

- **데이터**: `5_3_2.csv`
- **①** 각 캠페인의 만족도 점수의 평균, 표준편차를 구하시오. (소수점 둘째 자리까지 반올림)
- **②** 세 캠페인의 평균 만족도 점수가 유의미하게 다른지 검정하기 위해 ANOVA 검정을 수행하고, 검정통계량을 계산하시오. (소수점 셋째 자리까지 반올림)
- **③** p-value를 바탕으로 유의수준 5%에서 귀무가설의 기각/채택 여부를 결정하시오. (p-value는 소수점 셋째 자리까지 반올림)

```python
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/5_3_2.csv')
```

- 각 캠페인의 만족도 점수 평균과 표준편차를 계산하고 소수점 셋째 자리에서 반올림하여 출력합니다.

```python
# 각 캠페인의 평균과 표준편차 계산
mean_A = data[data['campaign'] == 'A']['satisfaction_score'].mean()
std_A = data[data['campaign'] == 'A']['satisfaction_score'].std()

mean_B = data[data['campaign'] == 'B']['satisfaction_score'].mean()
std_B = data[data['campaign'] == 'B']['satisfaction_score'].std()

mean_C = data[data['campaign'] == 'C']['satisfaction_score'].mean()
std_C = data[data['campaign'] == 'C']['satisfaction_score'].std()
```


```python
print('A 캠페인 만족도 점수 평균:', round(mean_A, 2)) 
print('B 캠페인 만족도 점수 평균:', round(mean_B, 2)) 
print('C 캠페인 만족도 점수 평균:', round(mean_C, 2)) 
print('A 캠페인 만족도 점수 표준편차:', round(std_A, 2)) 
print('B 캠페인 만족도 점수 표준편차:', round(std_B, 2)) 
print('C 캠페인 만족도 점수 표준편차:', round(std_C, 2))
```
*Output:*
```
A 캠페인 만족도 점수 평균: 69.17
B 캠페인 만족도 점수 평균: 68.31
C 캠페인 만족도 점수 평균: 74.52
A 캠페인 만족도 점수 표준편차: 8.87
B 캠페인 만족도 점수 표준편차: 9.94
C 캠페인 만족도 점수 표준편차: 10.64
```

- ANOVA 검정은 `f_oneway()`를 통해 수행할 수 있습니다.
```python
from scipy.stats import f_oneway 
# ANOVA 검정 수행 
f_statistic, p_value = f_oneway( 
    data[data['campaign'] == 'A']['satisfaction_score'], 
    data[data['campaign'] == 'B']['satisfaction_score'], 
    data[data['campaign'] == 'C']['satisfaction_score']
)
print('검정통계량:', round(f_statistic, 3))
```
*Output:*
```
검정통계량: 5.617
```

- 유의수준 5% 하에서 p-value가 0.05보다 작은 지 확인하여 귀무가설의 기각과 채택을 결정합니다.

```python
p_value = round(p_value, 3)
# 결과 해석 
if p_value < 0.05: 
    result = "기각" 
else: 
    result = "채택" 
print(result)
```
*Output:*
```
기각
```


**시험시간**: 180분 | **풀이시간**: - | **합격점수**: 60점 | **내점수**: -

## 기출문제 제4회 (2022-06-25 시행)

데이터셋 경로: `https://raw.githubusercontent.com/YoungjinBD/data/main/exam/`

### 작업형 제1유형

**1. 결측치 처리 및 데이터 추출**

다음 데이터에서 결측치가 존재하는 행을 모두 삭제하시오. 인덱스 기준 데이터의 상위 70%에 해당하는 데이터를 추출하고, `PTRATIO` 칼럼의 1분위수를 구하시오. (소수점 첫째 자리까지 반올림)

- **데이터**: `4_1_1.csv`

```python
import pandas as pd 
import numpy as np
pd.set_option('display.max_columns', None) 
# 모든 칼럼이 출력되게 조절
from sklearn import set_config
set_config(display="diagram") 
# scikit-learn 파이프라인 시각화
dat = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/4_1_1.csv') 
print(dat.head())
```
*Output:*
```
      CRIM  ZN  INDUS  CHAS    NOX     RM  PRICE
0  0.00632  18   2.31     0  0.538  6.575   24.0
1  0.02731   0   7.07     0  0.469  6.421   21.6
2  0.02729   0   7.07     0  0.469  7.185   34.7
3  0.03237   0   2.18     0  0.458  6.998   33.4
4  0.06905   0   2.18     0  0.458  7.147   36.2
```

- 결측치가 존재하는 칼럼을 확인합니다.
```python
print(dat.isna().sum())
# PTRATIO    11  -> 결측치 존재
```


- 결측치가 존재하는 행을 모두 삭제하고 `reset_index()`를 통해 인덱스를 초기화합니다.
```python
dat.dropna(inplace=True)
dat.reset_index(inplace=True, drop=True)
```

- 데이터의 상위 70%를 추출합니다.
```python
sub_dat = dat.loc[:int(len(dat)*0.7), :]
```

> [!TIP]
> **기적의 Tip**
> `loc[]`를 활용하여 데이터를 필터링할 경우 `reset_index()`로 인덱스 초기화를 진행해야 합니다. `loc[]`는 인덱스 위치가 아닌 라벨을 기준으로 동작하므로, 인덱스가 [0, 1, 3, 4, 6]이라면 `loc[:3]`은 라벨이 0~3인 행만 반환합니다. 이 경우 실제 행 개수나 위치와 다를 수 있어 혼동될 수 있습니다. 정확한 위치 기준 필터링이 필요하다면 `iloc[]`을 사용하거나 인덱스를 초기화해야 합니다.

- `PTRATIO` 칼럼의 1분위수를 계산합니다.
```python
result = sub_dat.loc[:, 'PTRATIO'].quantile(0.25) 
print(np.round(result, 1))
```
*Output:*
```
16.4
```

**2. 건축연도 및 학교등급 조건 필터링**

건축연도(`yearBuilt`)가 1991~2000년이면서 평균 학교등급(`avgSchoolRating`)이 평균 이하인 주택 id(`uid`)와, 건축연도 2001~2010년에 평균 학교등급이 평균 이상인 주택 id의 수를 구하시오.

- **데이터**: `4_1_2.csv`

```python
dat = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/4_1_2.csv') 
print(dat.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'> 
RangeIndex: 500 entries, 0 to 499 
Data columns (total 15 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   uid                         500 non-null    int64  
 1   city                        500 non-null    object 
 ...
```


- 건축연도가 1991~2000년도인 주택과, 건축연도가 2001~2010년도인 주택을 필터링합니다.
```python
sub_dat1 = dat.loc[(dat['yearBuilt'] >= 1991) & (dat['yearBuilt'] <= 2000), :] 
sub_dat2 = dat.loc[(dat['yearBuilt'] >= 2001) & (dat['yearBuilt'] <= 2010), :]
```

- 건축연도 기준으로 필터링된 데이터를 활용하여 학교 등급이 평균 이상, 평균 이하인 주택 id를 구합니다.
```python
uid1 = sub_dat1.loc[sub_dat1['avgSchoolRating'] <= dat['avgSchoolRating'].mean(), 'uid'] 
uid2 = sub_dat2.loc[sub_dat2['avgSchoolRating'] >= dat['avgSchoolRating'].mean(), 'uid']
```

- 주택 id 값에 중복이 있을 수 있으므로, unique 값을 구합니다.
```python
result = pd.concat([uid1, uid2], axis=0) 
print(len(result.unique()))
```
*Output:*
```
83
```


**3. 결측치 최빈 칼럼 확인**

위 2번 데이터의 각 칼럼 중 결측치가 가장 많은 칼럼을 출력하시오.

- 각 칼럼에서 결측치의 개수를 합산하여 확인할 수 있습니다.
```python
result = dat.isna().sum() 
print(result)
```
*Output:*
```
uid                             0
latitude                       11
longitude                      21
numOfPatioAndPorchFeatures     31
...
dtype: int64
```

- 아래와 같이 `idxmax()`를 이용하여 구할 수도 있습니다.
```python
print('결측치가 가장 많은 칼럼:', result.idxmax())
```
*Output:*
```
결측치가 가장 많은 칼럼: numOfPatioAndPorchFeatures
```

- 다른 방법으로는 결측치 개수 기준으로 데이터를 내림차순 정렬하고, 결측치가 가장 많은 인덱스(칼럼명)를 구해볼 수도 있습니다.

```python
print('결측치가 가장 많은 칼럼:', result.sort_values(ascending=False).index[0])
```
*Output:*
```
결측치가 가장 많은 칼럼: numOfPatioAndPorchFeatures
```


### 작업형 제2유형

제공된 학습용 데이터(`4_2_train.csv`)는 고객의 카드 사용 정보와 이탈 여부를 포함하고 있다. 학습용 데이터를 활용하여 고객 이탈 여부를 예측하는 이진 분류 모델을 개발하고, 가장 우수한 모델을 평가용 데이터(`4_2_test.csv`)에 적용하여 예측 결과를 제출하시오.

- **모델 성능 지표**: F1 Score
- **타깃**: 이탈 여부 (`Attrition_Flag`)

**Data description**
- `ID`: 고유 식별자
- `Attrition_Flag`: 이탈 여부 (0: 잔류 고객, 1: 이탈 고객)
- `Gender`: 성별
- `Customer_Age`: 고객 나이
- `Income_Category`: 소득 구간
- `Card_Category`: 카드 종류
- `Credit_Limit`: 신용 한도
- `Total_Revolving_Bal`: 순환 잔액
- `Avg_Utilization_Ratio`: 평균 사용률
- `Avg_Open_To_Buy`: 평균 구매 가능 금액
- `Months_Inactive_12_mon`: 최근 12개월 비활성 월 수

**제출 형식**
- 파일명: `result.csv` (디렉토리/폴더명 제외)
- 제출 칼럼: `ID`, `pred` (총 2개 칼럼)
    - `pred`: 예측된 이탈 여부 (정수형 0 또는 1)
- 제출 개수: 평가용 데이터와 예측 결과의 행 개수가 일치해야 함

```python
import pandas as pd 
import numpy as np 
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/4_2_train.csv') 
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/4_2_test.csv')
```

**1. 데이터 탐색**

- 모델을 적합하기 전 데이터에 결측치가 있는지 확인해야 합니다. 결측치가 존재할 경우 모델 적합 시 에러가 발생할 수 있습니다.

```python
print(train.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 354 entries, 0 to 353
Data columns (total 11 columns):
```


```
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   ID                        354 non-null    int64  
 1   Attrition_Flag            354 non-null    object 
 2   Gender                    354 non-null    object 
 ...
 10  Months_Inactive_12_mon    354 non-null    int64  
dtypes: float64(3), int64(4), object(4)
memory usage: 30.6+ KB
```

```python
print(test.info())
```

**2. 전처리 및 인코딩**

- 범주형 변수의 unique 값을 확인합니다.
```python
print(train['Attrition_Flag'].unique())
```
*Output:*
```
['Existing Customer' 'Attrited Customer']
```

- 기준 범주(관심 대상)인 'Attrited Customer'를 1로 설정합니다.
```python
train['Attrition_Flag'] = train['Attrition_Flag'].map({'Existing Customer': 0, 'Attrited Customer': 1}) 
# test['Attrition_Flag'] = test['Attrition_Flag'].map({'Existing Customer': 0, 'Attrited Customer': 1}) # test에는 타겟 없음
```

- 테스트 데이터를 활용한 최종 결과를 제출하기 위해 ID 칼럼을 따로 저장합니다.
```python
test_id = test['ID']
```

- ID 칼럼은 정보가 없는 칼럼이므로 삭제합니다.
```python
train = train.drop(['ID'], axis=1) 
test = test.drop(['ID'], axis=1)
```

**2. 데이터 분할**

- 모델 성능 확인을 위해 훈련 데이터의 일부를 검증 데이터로 나누겠습니다.
```python
train_X = train.drop(['Attrition_Flag'], axis=1) 
train_y = train['Attrition_Flag'] 
# test_X = test.drop(['Attrition_Flag'], axis=1) # test에는 타겟 없음
test_X = test.copy()
# test_y = test['Attrition_Flag'] # 없음

from sklearn.model_selection import train_test_split 
train_X, valid_X, train_y, valid_y = train_test_split(train_X, train_y, test_size=0.3, random_state=1) 
print(train_X.shape, train_y.shape, valid_X.shape, valid_y.shape)
```
*Output:*
```
(247, 9) (247,) (107, 9) (107,)
```


**3. 데이터 전처리**

- 범주형 변수에 대해서 원-핫 인코딩을 수행하고, 수치형 변수에는 표준화를 진행합니다. 범주형 변수에 대한 인코딩은 모델 적합 시 필수적이며, 그 외 전처리는 선택 사항입니다.

- 먼저 범주형 변수와 수치형 변수의 각 칼럼명을 저장합니다.
```python
- 원-핫 인코딩과 표준화 전처리 메서드를 불러옵니다.
```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder
onehotencoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore') 
stdscaler = StandardScaler()
```

- 훈련 데이터, 검증 데이터, 테스트 데이터 각각에 데이터 전처리를 진행합니다. 전처리 결과는 `numpy.array`로 출력됩니다. 모델 적합 시 전처리 완료된 데이터를 `pandas.DataFrame`으로 변경하지 않아도 무방합니다.

```python
train_X_numeric_scaled = stdscaler.fit_transform(train_X[num_columns]) 
valid_X_numeric_scaled = stdscaler.transform(valid_X[num_columns]) 
test_X_numeric_scaled = stdscaler.transform(test_X[num_columns])

train_X_categorical_encoded = onehotencoder.fit_transform(train_X[cat_columns]) 
valid_X_categorical_encoded = onehotencoder.transform(valid_X[cat_columns]) 
test_X_categorical_encoded = onehotencoder.transform(test_X[cat_columns])

train_X_preprocessed = np.concatenate([train_X_numeric_scaled, train_X_categorical_encoded], axis=1) 
valid_X_preprocessed = np.concatenate([valid_X_numeric_scaled, valid_X_categorical_encoded], axis=1) 
test_X_preprocessed = np.concatenate([test_X_numeric_scaled, test_X_categorical_encoded], axis=1)
```

**4. 모델 적합**

- 랜덤 포레스트 모델을 적합해 보겠습니다.
```python
from sklearn.ensemble import RandomForestClassifier 
rf = RandomForestClassifier(random_state=1) 
rf.fit(train_X_preprocessed, train_y)
```


- 검증 데이터를 활용하여 모형 성능을 확인해 보겠습니다.
```python
from sklearn.metrics import roc_auc_score 
pred_val = rf.predict_proba(valid_X_preprocessed)[:, 1] 
print('valid AUC:', roc_auc_score(valid_y, pred_val))
```
*Output:*
```
valid AUC: 0.7599587912087913
```

**5. 테스트 데이터로 예측**

- 테스트 데이터를 활용하여 최종 예측을 수행합니다. `predict_proba`를 통해 예측값을 계산합니다.
```python
test_pred = rf.predict_proba(test_X_preprocessed)[:, 1] 
test_pred = pd.DataFrame(test_pred, columns=['prob'])
```

- ID, prob 칼럼만 존재하는 결과 파일을 생성합니다.
```python
result = pd.concat([test_id, test_pred], axis=1)
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) # 시험에서 제시되는 파일명 작성할 것
```

> [!TIP]
> **기적의 Tip**
> 예측 결과를 제출해야 하는 경우, 문제에서 요구하는 제출 형식(수치형 또는 문자형)을 확인하여, 인코딩 된 타깃 변수를 다시 문자형으로 변환해야 할 수도 있습니다.

```python
test_pred_label = rf.predict(test_X_preprocessed) 
label = {0: 'Existing Customer', 1: 'Attrited Customer'} 
test_pred_label = pd.Series(test_pred_label).map(label) 
test_pred_df = pd.DataFrame(test_pred_label, columns=['pred'])
```

- 만약 모델 성능이 낮다고 판단되면, 교차검증을 활용한 하이퍼파라미터 튜닝을 진행해볼 수 있습니다. 홀드 아웃 방법이 아닌 k-폴드 교차검증을 진행할 것이기 때문에 기존에 분할했던 학습 데이터와 검증 데이터를 합치겠습니다.

```python
train_X_full = np.concatenate([train_X_preprocessed, valid_X_preprocessed], axis=0) 
train_y_full = np.concatenate([train_y, valid_y], axis=0)
```


- GridSearchCV를 통해 하이퍼파라미터 튜닝을 진행하겠습니다.
```python
from sklearn.model_selection import GridSearchCV
param_grid = {
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10]
} 
rf = RandomForestClassifier(random_state=1) 
rf_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5, 
    scoring='roc_auc'
) 
rf_search.fit(train_X_full, train_y_full)
print('교차검증 AUC-score:', rf_search.best_score_)
```
*Output:*
```
교차검증 AUC-score: 0.8873852752805681
```

> [!TIP]
> **기적의 Tip**
> 파라미터 값의 범위가 넓어지면 모델 학습 시 많은 시간이 소요될 수 있으므로 주의가 필요합니다.

- 하이퍼파라미터 튜닝 결과를 바탕으로 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred2 = rf_search.predict_proba(test_X_preprocessed)[:, 1] 
test_pred2 = pd.DataFrame(test_pred2, columns=['prob'])
```

- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰줍니다.
```python
result = pd.concat([test_id, test_pred2], axis=1)
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) 
# 시험에서 제시되는 파일명 작성할 것
```


**ColumnTransformer와 Pipeline을 활용한 방법**

```python
train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/4_2_train.csv') 
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/4_2_test.csv') 
test_id = test['ID']
train = train.drop(['ID'], axis=1) 
test = test.drop(['ID'], axis=1)

train['Attrition_Flag'] = train['Attrition_Flag'].map({'Existing Customer': 0, 'Attrited Customer': 1})
train_X = train.drop(['Attrition_Flag'], axis=1) 
train_y = train['Attrition_Flag']
test_X = test.copy()
```

- ColumnTransformer를 활용하면 연속형 변수와 수치형 변수 각각에 대해서 한 번에 전처리를 진행할 수 있습니다.

```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder
onehotencoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore') 
stdscaler = StandardScaler()
```

- ColumnTransformer를 활용하여 데이터 전처리 방식을 정의하겠습니다.
```python
cat_columns = train_X.select_dtypes('object').columns
num_columns = train_X.select_dtypes('number').columns
from sklearn.compose import ColumnTransformer
c_transformer = ColumnTransformer( 
    transformers=[ 
        ('cat', onehotencoder, cat_columns), 
        ('num', stdscaler, num_columns) 
    ], 
    remainder='passthrough'
)
```


- ColumnTransformer로 데이터 전처리를 진행한 후 Pipeline을 활용해서 모델을 정의하겠습니다.

```python
from sklearn.pipeline import Pipeline 
from sklearn.model_selection import GridSearchCV 
from sklearn.ensemble import RandomForestClassifier

pipe_rf = Pipeline([
    ("preprocess", c_transformer), 
    ("classifier", RandomForestClassifier(random_state=1))
])
```

- Pipeline을 활용해서 모델링을 정의한 후 GridSearchCV를 활용하여 교차검증을 통한 파라미터 튜닝을 진행하겠습니다.

```python
param_grid = { 
    'classifier__max_depth': [10, 20, 30], 
    'classifier__min_samples_split': [2, 5, 10]
}
rf_search_pipe = GridSearchCV(
    estimator=pipe_rf,
    param_grid=param_grid, 
    cv=5, 
    scoring='roc_auc'
) 
rf_search_pipe.fit(train_X, train_y)
```

- 교차검증 AUC-score는 다음과 같습니다.

```python
print('교차검증 AUC-score:', rf_search_pipe.best_score_)
```
*Output:*
```
교차검증 AUC-score: 0.8870243845114284
```

- 파라미터 튜닝 결과를 바탕으로 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
test_pred3 = rf_search_pipe.predict_proba(test_X)[:, 1] 
test_pred3 = pd.DataFrame(test_pred3, columns=['prob'])
```


- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰줍니다.
```python
result = pd.concat([test_id, test_pred3], axis=1) 
print(result.head(2))
```
*Output:*
```
     ID      prob
0  6086  0.933479 
1  6630  0.623602
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) # 시험에서 제시되는 파일명 작성할 것
```

> [!TIP]
> **기적의 Tip**
> ColumnTransformer와 Pipeline을 활용하면 간결한 코드로 데이터 전처리와 모델링을 한 번에 진행할 수 있습니다.

### 작업형 제3유형

**문제 1. T-검정 (Two-sample T-test)**

어느 회사에서 두 부서(A와 B) 직원들의 주간 근무 시간 평균이 유의미하게 다른지를 조사하고자 한다. 각 부서에서 각각 30명의 직원을 랜덤으로 추출하여 주간 근무 시간을 조사하였다.

- **데이터**: `4_3_1.csv`
- **①** 두 부서의 평균과 표준편차를 구하시오. (소수점 둘째 자리까지 반올림)
- **②** 두 부서의 평균 근무 시간 차이를 검정하기 위해 등분산을 가정한 독립 2표본 t-검정을 수행하고, 검정통계량을 구하시오. (소수점 둘째 자리까지 반올림)
- **③** p-value를 바탕으로 유의수준 5%에서 귀무가설의 기각/채택 여부를 결정하시오. (p-value는 소수점 둘째 자리까지 반올림)

```python
import pandas as pd 
data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/4_3_1.csv')
```


- A, B 부서의 주간 근무 시간 평균과 표준편차를 계산하고 소수점 둘째 자리까지 반올림하여 출력합니다.

```python
# 각 부서의 평균과 표준편차 계산
mean_A = data[data['department'] == 'A']['hours_worked'].mean()
std_A = data[data['department'] == 'A']['hours_worked'].std()

mean_B = data[data['department'] == 'B']['hours_worked'].mean()
std_B = data[data['department'] == 'B']['hours_worked'].std()

print('A 부서 근무시간 평균:', round(mean_A, 2)) 
print('B 부서 근무시간 평균:', round(mean_B, 2)) 
print('A 부서 근무시간 표준편차:', round(std_A, 2)) 
print('B 부서 근무시간 표준편차:', round(std_B, 2))
```
*Output:*
```
A 부서 근무시간 평균: 42.21
B 부서 근무시간 평균: 43.55
A 부서 근무시간 표준편차: 5.5
B 부서 근무시간 표준편차: 4.57
```

- 2표본(독립 표본) t-검정은 `ttest_ind()`를 통해 수행할 수 있습니다.
```python
from scipy.stats import ttest_ind 
# 2표본 t-검정 수행 
t_statistic, p_value = ttest_ind(
    data[data['department'] == 'A']['hours_worked'], 
    data[data['department'] == 'B']['hours_worked'],
    equal_var=True
)
print('검정통계량:', round(t_statistic, 2))
```
*Output:*
```
검정통계량: -1.02
```

- 유의수준 5% 하에서 p-value가 0.05보다 작은 지 확인하여 귀무가설의 기각과 채택을 결정합니다.

```python
p_value = round(p_value, 2)
# 결과 해석 
if p_value < 0.05: 
    result = "기각" 
else: 
    result = "채택" 
print(result)
```
*Output:*
```
채택
```


**문제 2. 크루스칼-왈리스 검정 (Kruskal-Wallis Test)**

어느 제조업체에서 세 공장(A, B, C)에서 생산된 제품의 품질 점수가 유의미하게 다른지를 조사하고자 한다. 각 공장에서 각각 30개의 제품을 랜덤으로 추출하여 품질 점수를 조사하였다.

- **데이터**: `4_3_2.csv`
- **①** 세 공장 품질 점수의 평균과 표준편차를 구하시오. (소수점 둘째 자리까지 반올림)
- **②** 세 공장의 품질 점수가 유의미하게 다른지 검정하기 위해 크루스칼-왈리스 검정을 수행하고, 검정통계량을 계산하시오. (소수점 둘째 자리까지 반올림)
- **③** p-value를 바탕으로 유의수준 5%에서 귀무가설의 기각/채택 여부를 결정하시오. (p-value는 소수점 둘째 자리까지 반올림)

```python
import pandas as pd 
data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/4_3_2.csv')
```

- 각 공장의 품질 점수 평균과 표준편차를 계산하고 소수점 둘째 자리까지 반올림하여 출력합니다.

```python
# 각 공장의 평균과 표준편차 계산
mean_A = data[data['factory'] == 'A']['quality_score'].mean()
std_A = data[data['factory'] == 'A']['quality_score'].std()

mean_B = data[data['factory'] == 'B']['quality_score'].mean()
std_B = data[data['factory'] == 'B']['quality_score'].std()

mean_C = data[data['factory'] == 'C']['quality_score'].mean()
std_C = data[data['factory'] == 'C']['quality_score'].std()

print('A 공장 품질 점수 평균:', round(mean_A, 2)) 
print('B 공장 품질 점수 평균:', round(mean_B, 2)) 
print('C 공장 품질 점수 평균:', round(mean_C, 2)) 
print('A 공장 품질 점수 표준편차:', round(std_A, 2)) 
print('B 공장 품질 점수 표준편차:', round(std_B, 2)) 
print('C 공장 품질 점수 표준편차:', round(std_C, 2))
```
*Output:*
```
A 공장 품질 점수 평균: 74.45
B 공장 품질 점수 평균: 72.1
C 공장 품질 점수 평균: 78.66
A 공장 품질 점수 표준편차: 11.0
B 공장 품질 점수 표준편차: 9.14
C 공장 품질 점수 표준편차: 9.65
```


- 크루스칼-왈리스 검정은 `kruskal()`을 통해 수행할 수 있습니다.
```python
from scipy.stats import kruskal 
# 크루스칼 왈리스 검정 수행 
statistic, p_value = kruskal( 
    data[data['factory'] == 'A']['quality_score'], 
    data[data['factory'] == 'B']['quality_score'], 
    data[data['factory'] == 'C']['quality_score']
)
print('검정통계량:', round(statistic, 2))
```
*Output:*
```
검정통계량: 5.93
```

- 유의수준 5% 하에서 p-value가 0.05보다 작은 지 확인하여 귀무가설의 기각과 채택을 결정합니다.

```python
p_value = round(p_value, 2)
# 결과 해석 
if p_value < 0.05: 
    result = "기각" 
else: 
    result = "채택" 
print(result)
```
*Output:*
```
채택
```
 기출문제제4회정답＆해설 599

이 시간 합격 점수 내점수

## 기출문제 제3회 (2021-12-04시햄）
https://raw.githubusercontent.com/YoungjinBD/data/main/exam/ .

FOl -,형제1유형 30첨 다음 데이터에서 IotSizeSqFt《기 큰 top 10을 구하고 , top 10 값 중 가장 작은 값으로 해당 값을 대치 하시오 . 또한 , 건축 연도（yearBuilt）가 2000년도 이상인 IotSizeSqFt의 평균값을 구하시오 . （소수점 첫째 자리에서 반올림 , 대치된 IotSizeSqFt 기준） 데이터 : 3 Lcsv

```python
import pandas as pd
import numpy as np 
pd.set_option( 'display.max_columns' , None) 
# 모든 칼럼이 출력되게 조절
from sklearn import set_config
set_config(display = "diagram ") 
# scikit-learn 파이프라인 시각화
dat = pd.read_csv( 'https://raw.githubusercontent.com/YoungjinBD/data/main/exam/3_1.csv ') 
print(dat.head() )
```
city homeType latitude longitude garageSpaces hasSpa yearBuilt ...

priceRange 0 austin Single Family 30.19764709 -97.81681061 2 FALSE 1981 ... 350000-450000 1 austin Single Family 30.32918739 -97.75273132 2 FALSE 1951 ...

**시험시간**: 180분 | **풀이시간**: - | **합격점수**: 60점 | **내점수**: -

## 기출문제 제3회 (2021-12-04 시행)

데이터셋 경로: `https://raw.githubusercontent.com/YoungjinBD/data/main/exam/`

### 작업형 제1유형

**1. 결측치 대치 및 평균 계산**

다음 데이터에서 `lotSizeSqFt`이 큰 top 10을 구하고, top 10 값 중 가장 작은 값으로 해당 값을 대치 하시오. 또한, 건축 연도(`yearBuilt`)가 2000년도 이상인 `lotSizeSqFt`의 평균값을 구하시오. (소수점 첫째 자리에서 반올림, 대치된 `lotSizeSqFt` 기준)

- **데이터**: `3_1.csv`

```python
import pandas as pd
import numpy as np 
pd.set_option('display.max_columns', None) 
# 모든 칼럼이 출력되게 조절
from sklearn import set_config
set_config(display="diagram") 
# scikit-learn 파이프라인 시각화
dat = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/3_1.csv') 
print(dat.head())
```
*Output:*
```
     city         homeType     latitude    longitude  garageSpaces  hasSpa  yearBuilt  ...
0  austin    Single Family  30.19764709 -97.81681061             2   FALSE       1981  ...
1  austin    Single Family  30.32918739 -97.75273132             2   FALSE       1951  ...
2  austin    Single Family  30.3133049  -97.69966888             0   FALSE       1954  ...
3  austin    Single Family  30.15632057 -97.74829102             2   FALSE       2008  ...
4  austin        Townhouse  30.36699486 -97.75354767             2   FALSE       1984  ...
```

- `lotSizeSqFt` 변수를 내림차순으로 정렬합니다. 정렬 후에 인덱스 초기화를 진행합니다.
```python
sub_dat = dat.sort_values(by='lotSizeSqFt', ascending=False)
# lotSizeSqFt 변수 내림차순 정렬
# index 초기화
sub_dat = sub_dat.reset_index(drop=False)
```

> [!TIP]
> **기적의 Tip**
> `.sort_values`를 활용하여 데이터 정렬 후 `.loc`를 적용할 경우, `reset_index`를 통해 인덱스를 재설정한 후 적용해야 합니다.


- 내림차순으로 정렬된 값 중 0~9행까지의 값을 필터링하고, 최솟값을 구합니다.

```python
min_value = sub_dat.loc[:9, 'lotSizeSqFt'].min() 
print('최솟값:', min_value)
```
*Output:*
```
최솟값: 71438.4
```

- 최솟값으로 `lotSizeSqFt`이 큰 top10 값들을 대치합니다.
```python
sub_dat.loc[:9, 'lotSizeSqFt'] = min_value
# top10중 가장 작은 값으로 대치 
print(sub_dat.loc[:9, 'lotSizeSqFt'])
```
*Output:*
```
0    71438.4
1    71438.4
2    71438.4
...
9    71438.4
Name: lotSizeSqFt, dtype: float64
```

- 건축 연도가 2000년도 이상인 값을 필터링 한 후, `lotSizeSqFt` 변수의 평균을 계산합니다.
```python
result = sub_dat.loc[sub_dat['yearBuilt'] >= 2000, 'lotSizeSqFt'].mean() 
print(result)
```
*Output:*
```
12954.924719101124
```

- 소수점 첫째 자리에서 반올림한 정수값을 최종 결과로 산출합니다.
```python
print(np.round(result, 0))
```
*Output:*
```
12955.0
```

**2. 결측치 중앙값 대치 및 표준편차 비교**

칼럼별 결측치 존재 여부를 확인하고, 결측치가 존재하는 경우 해당 칼럼의 중앙값으로 결측치를 대치하시오. 결측치 대치 전과 후 표준편차 차이의 절댓값을 구하시오. (소수점 둘째 자리까지 반올림)

**2-1. 결측치 확인**

- `.isna()`는 dat의 각 값이 NaN인지 여부를 확인하며, 여기에 `.sum()`을 적용하면 칼럼별 결측치의 개수를 합산하여 반환합니다.

```python
print(dat.isna().sum())
```
*Output:*
```
city                           0
homeType                       0
latitude                       0
longitude                      0
garageSpaces                   0
hasSpa                         0
yearBuilt                      0
numOfPatioAndPorchFeatures     0
lotSizeSqFt                    0
avgSchoolRating                0
MedianStudentsPerTeacher       0
numOfBathrooms                11 # 결측치 존재
numOfBedrooms                  0
priceRange                     0
dtype: int64
```

**2-2. 결측치를 중앙값으로 대치 (방법1)**

```python
imp_dat1 = dat.copy()
```

- `numOfBathrooms` 변수의 중앙값을 계산합니다.
```python
median_value = imp_dat1.loc[:, 'numOfBathrooms'].median() # 중앙값 계산
```

- `.fillna()`를 활용하여 결측치를 중앙값으로 대치합니다.
```python
imp_dat1['numOfBathrooms'] = imp_dat1['numOfBathrooms'].fillna(median_value)
```


- 결측치가 잘 대치되었는지 확인합니다.
```python
print(imp_dat1.isna().sum())
# numOfBathrooms                 0 # 결측치 없음
```

**2-2. 결측치를 중앙값으로 대치 (방법2)**

```python
imp_dat2 = dat.copy()
```

- scikit-learn에 내장된 `SimpleImputer`를 `strategy='median'` 로 설정하여 중앙값 대치법을 불러옵니다.

```python
from sklearn.impute import SimpleImputer
# 결측치 대치 모듈 불러오기
imputer = SimpleImputer(strategy='median')
# 중앙값 대치법으로 설정
```

- `.fit_transform()`을 통해 결측치를 중앙값으로 대치합니다.
```python
imp_dat2['numOfBathrooms'] = imputer.fit_transform(imp_dat2[['numOfBathrooms']])
```


- 결측치가 잘 대치되었는지 확인합니다.
```python
print(imp_dat2.isna().sum())
# numOfBathrooms                 0 # 결측치 없음
```

**3. 결측치 대치 전후 표준편차 차이 계산**

- 결측치 대치 전의 표준편차와 대치 후의 표준편차를 계산합니다.
```python
before_std = dat['numOfBathrooms'].std() 
# 결측치 대치 전 표준편차 계산 
after_std = imp_dat1['numOfBathrooms'].std() 
# 결측치 대치 후 표준편차 계산
```

- 표준편차 차이를 계산합니다.
```python
std_diff = abs(round(before_std - after_std, 2))
# 차이 계산, 소수점 셋째 자리에서 반올림 
print('표준편차 차이:', std_diff)
```
*Output:*
```
표준편차 차이: 0.01
```


**3. 이상치 (IQR Method)**

평균으로부터 1.5 표준편차만큼 벗어나는 경우를 이상치로 판단할 때, `MedianStudentsPerTeacher`의 이상치를 구하고, 이상치의 개수를 구하시오.

- 문제에 명시된 대로 이상치 구분의 기준이 되는 상한값과 하한값을 구합니다.

```python
mean_value = dat['MedianStudentsPerTeacher'].mean()
std_value = dat['MedianStudentsPerTeacher'].std()

ucl = mean_value + (1.5 * std_value)
lcl = mean_value - (1.5 * std_value)
```

- 상한값과 하한값 밖에 있는 값을 이상치로 정의하고, 이상치 개수를 산출합니다.
```python
num_rows = dat.loc[(dat['MedianStudentsPerTeacher'] > ucl) | (dat['MedianStudentsPerTeacher'] < lcl), :].shape[0]
print('행 개수:', num_rows)
```
*Output:*
```
행 개수: 65
```

### 작업형 제2유형

제공된 학습용 데이터(`3_2_train_X.csv`, `3_2_train_y.csv`)는 개인의 건강 정보와 당뇨병 여부를 포함하고 있다. 학습용 데이터를 활용하여 당뇨병 여부를 예측하는 이진 분류 모델을 개발하고, 가장 우수한 모델을 평가용 데이터(`3_2_test_X.csv`)에 적용하여 예측 결과를 제출하시오.

- **모델 성능 지표**: F1 Score
- **타깃(라벨)**: 당뇨병 여부 (`Outcome`)

**Data description**
- `Pregnancies`: 임신 횟수
- `Glucose`: 혈당 수치
- `BloodPressure`: 혈압 (mm Hg)
- `SkinThickness`: 피부 두께 (mm)
- `Insulin`: 혈중 인슐린 농도
- `BMI`: 체질량 지수
- `DiabetesPedigreeFunction`: 당뇨 유전적 소인 지수
- `Age`: 나이
- `Outcome`: 당뇨병 여부 (0: 비당뇨, 1: 당뇨)


**제출 형식**
- 파일명: `result.csv` (디렉토리/폴더명 제외)
- 제출 칼럼: `pred` (총 1개 칼럼)
    - `pred`: 예측된 당뇨병 여부 (정수형 0 또는 1)
- 제출 개수: 평가용 데이터와 예측 결과의 행 개수가 일치해야 함

```python
import pandas as pd 
import numpy as np 
train_X = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/3_2_train_x.csv') 
train_y = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/3_2_train_y.csv')
test_X = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/3_2_test_x.csv')
```

**1. 데이터 탐색**

- 모델을 적합하기 전 데이터에 결측치가 있는지 확인해야 합니다. 결측치가 존재할 경우 모델 적합 시 에러가 발생할 수 있습니다.

```python
print(train_X.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 537 entries, 0 to 536
Data columns (total 8 columns):
```

```
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   Pregnancies               537 non-null    int64  
 1   Glucose                   537 non-null    int64  
 ...
 7   Age                       537 non-null    int64  
dtypes: float64(2), int64(6)
memory usage: 33.7 KB
```
- 결측치 없음


```python
print(test_X.info())
```
- 결측치 없음

```python
print(train_y.info())
```
*Output:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 537 entries, 0 to 536
Data columns (total 1 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   Outcome  537 non-null    int64
dtypes: int64(1)
memory usage: 4.3 KB
```

**2. 데이터 분할**

- 모델 성능 확인을 위해 훈련 데이터의 일부를 검증 데이터로 나눠주겠습니다.
```python
from sklearn.model_selection import train_test_split 
train_X, valid_X, train_y, valid_y = train_test_split(train_X, train_y, test_size=0.3, random_state=1) 
print(train_X.shape, train_y.shape, valid_X.shape, valid_y.shape)
```
*Output:*
```
(375, 8) (375, 1) (162, 8) (162, 1)
```


**3. 데이터 전처리**

- 모든 변수가 수치형 변수이고, 결측치가 존재하지 않으므로 추가적인 전처리는 진행하지 않겠습니다.

**4. 모델 적합**

- 랜덤 포레스트 모델을 적합해 보겠습니다.
```python
from sklearn.ensemble import RandomForestClassifier 
rf = RandomForestClassifier(random_state=1) 
rf.fit(train_X, train_y)
```

> [!TIP]
> **기적의 Tip**
> 랜덤 포레스트 모형을 선택한 이유는 범주형 변수 인코딩 외에 추가 전처리를 진행하지 않아도 기본 모델 성능이 어느 정도 보장되기 때문입니다.

- 검증 데이터를 활용하여 모형 성능을 확인해 보겠습니다.
```python
from sklearn.metrics import f1_score 
pred_val = rf.predict(valid_X) 
print(f1_score(valid_y, pred_val, average='macro'))
```
*Output:*
```
0.7563909774436091
```

**5. 테스트 데이터로 예측**

- 테스트 데이터를 활용하여 최종 예측을 수행합니다. `.predict`를 통해 예측값을 계산합니다.
```python
pred = rf.predict(test_X)
```

- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰주겠습니다.
```python
result = pd.DataFrame({'pred': pred}) 
print(result.head(2))
```
*Output:*
```
   pred
0     1
1     0
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) 
# 시험에서 제시되는 파일명 작성할 것
```


- 만약 모델 성능이 낮다고 판단되면, 교차검증을 활용한 하이퍼파라미터 튜닝을 진행해볼 수 있습니다. 홀드 아웃 방법이 아닌 k-폴드 교차검증을 진행할 것이기 때문에 기존에 분할했던 학습 데이터와 검증 데이터를 합치겠습니다.
```python
train_X_full = np.concatenate([train_X, valid_X], axis=0) 
train_y_full = np.concatenate([train_y, valid_y], axis=0)
```

- GridSearchCV를 통해 하이퍼파라미터 튜닝을 진행하겠습니다.
```python
from sklearn.model_selection import GridSearchCV
param_grid = { 
    'max_depth': [5, 10, 20], 
    'min_samples_split': [2, 5, 10]
} 
rf = RandomForestClassifier(random_state=1) 
rf_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5, 
    scoring='f1_macro'
) 
rf_search.fit(train_X_full, train_y_full)
print('교차검증 f1-score:', rf_search.best_score_)
```
*Output:*
```
교차검증 f1-score: 0.7444900195127694
```

> [!TIP]
> **기적의 Tip**
> 파라미터 값의 범위가 넓어지면 모델 학습 시 많은 시간이 소요될 수 있으므로 주의가 필요합니다.

- 하이퍼파라미터 튜닝 결과를 바탕으로 테스트 데이터를 활용하여 최종 예측을 수행합니다.
```python
pred_test = rf_search.predict(test_X)
```

- 테스트 데이터로 예측한 결과를 주어진 제출 양식에 맞춰줍니다.
```python
result = pd.DataFrame({'pred': pred_test})
```

- 최종 결과를 저장합니다.
```python
# result.to_csv('result.csv', index=False) 
# 시험에서 제시되는 파일명 작성할 것
```


### 작업형 제3유형

**문제 1. 단일 표본 T-검정**

어느 고등학교의 수학 교사는 학생들의 시험 점수가 평균 75점 이상이라고 주장한다. 이를 검증하기 위해 랜덤으로 100명의 학생을 추출하여 시험 점수를 조사하였다.

- **데이터**: `3_3_1.csv`
- **①** 학생 성적의 평균과 표준편차를 구하시오. (소수점 둘째 자리까지 반올림)
- **②** 모평균 75를 기준으로 단일 표본 t-검정을 수행하고, 검정통계량을 계산하시오. (소수점 둘째 자리까지 반올림)
- **③** p-value를 바탕으로 유의수준 5%에서 귀무가설의 기각/채택 여부를 결정하시오. (p-value는 소수점 둘째 자리까지 반올림)

```python
import pandas as pd 
data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/3_3_1.csv')
```

- 평균과 표준편차를 계산하고, 문제에 명시된 소수점 자리수에 맞게 반올림합니다.
```python
mean_score = data['score'].mean() 
std_dev_score = data['score'].std()
print('평균:', round(mean_score, 2)) 
print('표준편차:', round(std_dev_score, 2))
```
*Output:*
```
평균: 75.6
표준편차: 10.13
```

- 주어진 모평균에 대한 단일 표본 t-검정은 `stats.ttest_1samp()`를 통해 수행할 수 있습니다.
```python
from scipy import stats
# 모집단 평균 가설값 설정 
population_mean = 75
# 단일 표본 t-검정 수행 
t_statistic, p_value = stats.ttest_1samp(data['score'], population_mean, alternative='greater')
print('검정통계량:', round(t_statistic, 2))
```
*Output:*
```
검정통계량: 0.59
```


- 유의수준 5% 하에서 p-value가 0.05보다 작은 지 확인하여 귀무가설의 기각과 채택을 결정합니다.

```python
p_value = round(p_value, 2) 
# 결과 해석 
if p_value < 0.05: 
    result = "기각" 
else: 
    result = "채택" 
print(result)
```
*Output:*
```
채택
```

**문제 2. 카이제곱 독립성 검정**

어느 고등학교에서 학생들의 성별과 동아리 가입 여부 간의 연관성을 조사하고자 한다. 이를 위해 200명의 학생을 대상으로 조사를 실시하였다.

- **데이터**: `3_3_2.csv`
- **①** 성별과 동아리 가입 여부 간의 독립성을 검정하기 위해 카이제곱 독립성 검정을 수행하고, 검정통계량을 소수점 둘째 자리까지 반올림하여 구하시오. (단, 연속성 수정은 적용하지 않음)
- **②** p-value를 바탕으로 유의수준 5%에서 귀무가설의 기각/채택 여부를 결정하시오. (p-value는 소수점 둘째 자리까지 반올림)

```python
import pandas as pd 
data = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/exam/3_3_2.csv')
```

- 성별과 동아리 가입 여부 간의 빈도수를 교차표로 생성합니다.
```python
cross_tab = pd.crosstab(data['gender'], data['club_membership']) 
print(cross_tab)
```
*Output:*
```
club_membership  No  Yes
gender                  
Female           68   38
Male             66   28
```


- 두 범주형 변수 간의 독립성을 테스트하기 위해 주어진 교차표를 바탕으로 카이제곱 검정을 수행합니다. 검정통계량을 소수점 둘째 자리까지 반올림하여 출력합니다.

```python
from scipy.stats import chi2_contingency 
# 카이제곱 검정 수행 
chi2, p, dof, expected = chi2_contingency(cross_tab, correction=False) 
print('검정통계량:', round(chi2, 2))
```
*Output:*
```
검정통계량: 0.83
```

- 유의수준 5% 하에서 p-value가 0.05보다 작은지 확인하여 귀무가설의 기각과 채택을 결정합니다.

```python
if p < 0.05: 
    result = "기각" 
else: 
    result = "채택" 
print(result)
```
*Output:*
```
채택
```

