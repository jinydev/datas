# 6-4. 데이터 그룹 짓기 (Groupby)

## 1. 끼리끼리 뭉치자
"1반 평균은?", "남자 평균과 여자 평균은?"
데이터를 그룹별로 나누어서 계산하고 싶을 때 `groupby`를 씁니다.
판다스에서 **가장 강력한 기능** 중 하나입니다.

## 2. 사용법 (Split-Apply-Combine)

```python
import pandas as pd

data = {
    '반': ['A', 'A', 'B', 'B', 'C'],
    '점수': [80, 90, 70, 85, 95]
}
df = pd.DataFrame(data)

# '반' 별로 묶어서, '점수'의 '평균'을 구하라
print(df.groupby('반')['점수'].mean())
```

## 3. 다양한 통계 한번에
```python
# 반별로 합계, 평균, 개수를 다 보고 싶다
print(df.groupby('반')['점수'].agg(['sum', 'mean', 'count']))
```

## 4. 핵심 정리
*   `df.groupby('기준열')[계산열].함수()` 패턴을 외우세요.
*   엑셀의 피벗테이블과 같은 역할입니다.
