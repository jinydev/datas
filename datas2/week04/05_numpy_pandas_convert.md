# 4-5. 넘파이와 판다스 왔다갔다 하기 (Integration)

## 1. 판다스는 넘파이의 옷을 입은 것
판다스 데이터프레임에서 알맹이만 쏙 빼면 넘파이 배열이 나옵니다.

```python
# .values 속성을 쓰면 됩니다.
numpy_array = df.values

print(type(numpy_array)) 
# 결과: <class 'numpy.ndarray'>
```

## 2. 언제 넘파이로 바꾸나요?
*   판다스 기능으로 해결 안 되는 복잡한 수학 계산을 할 때
*   AI 모델(TensorFlow, PyTorch)에 데이터를 넣을 때

## 3. 넘파이 배열을 판다스로 만들기
반대로 계산된 넘파이 배열을 다시 보기 좋게 표로 만들 수도 있습니다.

```python
import numpy as np
import pandas as pd

arr = np.array([[1, 2], [3, 4]])
df_new = pd.DataFrame(arr, columns=['A', 'B'])

print(df_new)
```

## 4. 핵심 정리
*   `df.values`: 데이터프레임을 넘파이 배열로 변환.
*   두 라이브러리는 **형제** 지간이라 데이터 호환이 아주 자유롭습니다.
