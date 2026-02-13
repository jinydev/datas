# 5-3. 누가 1등인가? 정렬과 순위 (Sort, Rank)

## 1. 줄 세우기 (Sorting)
데이터 분석에서 가장 많이 하는 것 중 하나가 "누가 제일 잘했어?" 또는 "누가 제일 못했어?"를 찾는 것입니다.

## 2. 오름차순 vs 내림차순
*   **오름차순 (Ascending)**: 1, 2, 3... (작은 것부터)
*   **내림차순 (Descending)**: 3, 2, 1... (큰 것부터) -> **성적순**

```python
import pandas as pd

data = {'이름': ['철수', '영희', '민수'], '점수': [80, 95, 70]}
df = pd.DataFrame(data)

# 점수가 높은 순서대로 (내림차순) 정렬
# ascending=False가 중요합니다!
sorted_df = df.sort_values(by='점수', ascending=False)

print(sorted_df)
```

## 3. 순위 매기기 (Rank)
등수를 매겨서 새로운 열로 만들 수도 있습니다.

```python
# method='min'은 동점자 처리 방식 중 하나
df['등수'] = df['점수'].rank(method='min', ascending=False)
print(df)
```

## 4. 핵심 정리
*   `sort_values(by='기준열')`: 정렬하기.
*   `ascending=False`: 내림차순 (큰 수가 위로).
*   이것만 알면 "우리 학교 전교 1등" 데이터를 바로 찾을 수 있습니다.
