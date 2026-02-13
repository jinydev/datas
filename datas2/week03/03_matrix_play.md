# 3-3. 0과 1의 행렬 놀이 (Zeros, Ones)

## 1. 초기화 (Initialization)
데이터 분석을 할 때, 일단 0으로 가득 찬 판을 만들거나 1로 가득 찬 리스트가 필요할 때가 많습니다.

## 2. 0으로 채우기 (zeros) / 1로 채우기 (ones)
```python
import numpy as np

# 0이 5개 들어있는 배열
print(np.zeros(5)) 

# 1이 10개 들어있는 배열
print(np.ones(10))
```

## 3. 2차원 배열 (행렬, Matrix)
지금까지는 한 줄(1차원)이었습니다. 이제 가로세로가 있는 **표(2차원)**를 만들어봅시다.

```python
# 2행 3열짜리 0 행렬
# (세로, 가로) 순서입니다!
zero_matrix = np.zeros((2, 3)) 

print(zero_matrix)
```

## 4. 모양 확인하기 (Shape)
데이터의 크기(모양)가 궁금할 땐 `.shape`를 물어봅니다.

```python
print(zero_matrix.shape)
# 결과: (2, 3) -> 세로 2줄, 가로 3칸이군요.
```

## 5. 핵심 정리
*   `np.zeros((행, 열))`: 0으로 채운 행렬 생성.
*   `np.ones((행, 열))`: 1로 채운 행렬 생성.
*   `.shape`: 배열의 크기를 알려주는 속성.
