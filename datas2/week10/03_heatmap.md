# 10-3. 히트맵 그리기 (Heatmap)

## 1. 숫자만 보면 머리 아프다
`df.corr()` 결과는 숫자가 가득한 표입니다. 한 눈에 들어오지 않습니다.
색깔로 숫자의 크기를 표현하는 **히트맵(Heatmap)**을 쓰면 직관적입니다.

## 2. Seaborn Heatmap
```python
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
```
*   `annot=True`: 칸 안에 숫자를 써준다.
*   `cmap='coolwarm'`: 빨강(양수) ~ 파랑(음수) 색상 테마.

## 3. [응용 예제] 성적 데이터 히트맵
앞서 만든 성적 데이터의 상관관계를 히트맵으로 그려봅시다.

[소스 코드 실행하기](src/03_heatmap.py) | [Colab에서 열기](src/03_heatmap.ipynb)
