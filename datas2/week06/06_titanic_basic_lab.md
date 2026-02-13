# 6-6. [실습] 타이타닉 생존자 분석 기초

## 1. 전설의 예제: 타이타닉(Titanic)
데이터 분석계의 "Hello World"입니다.
승객 명단을 보고, 누가 살았고 누가 죽었는지, 어떤 특징(성별, 객실등급)이 생존에 영향을 줬는지 분석합니다.

## 2. 데이터 불러오기
```python
import pandas as pd
import seaborn as sns # 데이터셋 로드용

# 인터넷에서 바로 가져오기
titanic = sns.load_dataset('titanic')

# 데이터 확인
print(titanic.head())
print(titanic.info())
```

## 3. 미션 1: 결측치 확인
*   어디에 빈 값이 가장 많은가요? (deck 열일 것입니다.)
*   `isnull().sum()`을 써보세요.

## 4. 미션 2: 생존율 계산 (Groupby)
*   성별(sex)에 따른 생존율(survived) 평균을 구해보세요.
    *   survived 열은 0(사망), 1(생존)로 되어 있습니다. 평균을 구하면 그게 곧 생존율입니다.

```python
print(titanic.groupby('sex')['survived'].mean())
```

*   객실등급(class)에 따른 생존율은?

## 5. 미션 3: 시각화
*   성별 생존율을 막대 그래프로 그려보세요.

```python
result = titanic.groupby('sex')['survived'].mean()
plt.bar(result.index, result.values)
plt.title("Survival Rate by Sex")
plt.show()
```

## 6. 결론
여자가 남자보다 많이 살았나요? 1등석 사람이 3등석보다 많이 살았나요?
데이터는 거짓말을 하지 않습니다.
