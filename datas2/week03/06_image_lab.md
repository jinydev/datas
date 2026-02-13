# 3-6. [실습] 이미지 색상 반전 시키기

## 1. 이미지를 배열로 다루기
이미지(Image)는 0~255 사이의 숫자로 이루어진 행렬입니다.
(0: 검은색, 255: 흰색)

## 2. 미션: 체스판 무늬 만들기
`matplotlib`의 `imshow`를 사용하면 2차원 배열을 그림으로 보여줍니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 10x10 크기의 0(검은색) 행렬 생성
image = np.zeros((10, 10))

# 슬라이싱으로 색 채우기
# 짝수 줄의 홀수 칸은 1(흰색)로 변경
image[0::2, 1::2] = 1 
# 홀수 줄의 짝수 칸은 1(흰색)로 변경
image[1::2, 0::2] = 1

plt.imshow(image, cmap='gray') # gray: 흑백 모드
plt.show()
```

## 3. 도전 과제: 색상 반전
위에서 만든 체크무늬의 색상을 반대로 뒤집어 보세요.
(흰색 -> 검은색, 검은색 -> 흰색)

### 힌트
*   0은 1로, 1은 0으로 만들어야 합니다.
*   수학적으로 어떻게 하면 될까요? (`1 - image`를 하면?)

```python
inverted_image = 1 - image
plt.imshow(inverted_image, cmap='gray')
plt.title("Inverted Image")
plt.show()
```

## 4. 마무리
우리는 그림판 툴을 쓰지 않고 **수학(행렬)**과 **코드**만으로 이미지를 조작했습니다.
이것이 포토샵 필터의 원리이자 딥러닝 비전 처리의 기초입니다.
