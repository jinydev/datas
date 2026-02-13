# 5-5. 데이터 분포 확인하기 (Histogram with Matplotlib)

## 1. 점수만 봐서는 모른다
우리 반 평균이 50점이라고 칩시다.
*   모두가 50점일 수도 있고
*   0점 반, 100점 반일 수도 있습니다.

데이터가 어떻게 퍼져있는지(분포)를 눈으로 확인하는 가장 좋은 방법이 **히스토그램(Histogram)**입니다.

## 2. 히스토그램 그리기
판다스 데이터로 바로 그림을 그릴 수 있습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 가짜 점수 1000개 생성 (평균 70, 표준편차 10)
scores = np.random.normal(70, 10, 1000)

plt.hist(scores, bins=20, color='skyblue', edgecolor='black')
plt.title("Score Distribution")
plt.show()
```

## 3. 해석하기
*   가운데가 불룩 솟아있나요? (정규분포)
*   어느 한쪽으로 쏠려있나요?
*   산봉우리가 두 개인가요?

## 4. 핵심 정리
*   `plt.hist(데이터)`: 히스토그램 그리기.
*   `bins`: 막대 개수 (구간을 얼마나 잘게 쪼갤지).
*   데이터의 **모양(Shape)**을 파악하는 첫 단계입니다.
