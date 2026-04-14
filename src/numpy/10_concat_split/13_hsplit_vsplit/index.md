---
layout: numpy
title: "4.10.13 직관적인 분할 함수: hsplit()과 vsplit()"
---

# 4.10.13 직관적인 분할 함수: hsplit()과 vsplit()

앞서 배운 `split(axis=...)` 처럼 `axis` 숫자 번호를 외우지 않아도 되도록, 아주 직관적인 방향(수평, 수직) 이름을 가진 짝꿍 쪼개기 함수들이 있습니다. 바로 배열을 수평 방향으로 자르는 **`hsplit`**과 수직 방향으로 자르는 **`vsplit`**입니다.

---

## ① np.hsplit(ary): 샌드위치 반으로 갈라 썰기

**[비유로 이해하기: 샌드위치 반절로 자르기]**
식빵을 반으로 잘라 먹기 좋은 샌드위치를 만드는 것처럼 데이터를 **옆으로(좌우 열 단위)** 수직 칼날을 찍어 내리며 가릅니다. 
실무 데이터 분석에서는 거대한 2차원 표(엑셀 데이터)에서 가로축(수평, Horizontal)을 따라 나아갈 때 이를 통째로 갈라 **입력 문제 데이터(X)** 열(Column)들과 **정답 데이터(y)** 열(Column)을 왼쪽, 오른쪽으로 서로 분리할 때 아주 널리 사용하는 방식입니다.

![np.hsplit 샌드위치 갈라 썰기](./img/hsplit_sandwich.svg)

수평으로 가로지르며 나누는 `np.hsplit(a)`는 1차원 데이터가 아닌 다차원일 경우 이전에 배운 `np.split(a, axis=1)`과 하는 역할이 똑같습니다.

### [1단계] 1차원 배열 hsplit 하기
1차원 배열은 가로로 일렬로 늘어서 있으므로, 그냥 `np.split` 처럼 똑같이 n등분하거나 칼집 인덱스 번호로 자르면 리스트로 툭툭 조각나 떨어집니다.

![1차원 배열 hsplit](./img/hsplit_step1.svg)

```python
import numpy as np

a = np.arange(10) # [0 1 2 ... 9]

# 똑같이 반으로 2등분 하기
print("🔪 2등분 결과:\n", np.hsplit(a, 2))

# 특정 인덱스(2와 5 위치 앞)에 칼집 넣기
print("\n🔪 불균등 분할 (결괏값 3덩이):\n", np.hsplit(a, [2, 5]))
```

**[실행 결과]**
```text
🔪 2등분 결과:
 [array([0, 1, 2, 3, 4]), array([5, 6, 7, 8, 9])]

🔪 불균등 분할 (결괏값 3덩이):
 [array([0, 1]), array([2, 3, 4]), array([5, 6, 7, 8, 9])]
```

### [2단계] 2차원 배열 hsplit 하기 (열 분할)
2차원 공간의 배열이 주어지면, 이제는 배열 안의 촘촘한 세로 열(Column) 단위로 칼을 찍어 내려 좌우로 가릅니다.

![2차원 배열 hsplit](./img/hsplit_step2.svg)

```python
# 2행 12열 배열 생성
a = np.arange(24).reshape(2, 12)

# 가로로 길게 누워있는 배열을 세로로 내리쳐 전체 열을 3덩어리로 자릅니다. (4기둥씩 묶임)
result = np.hsplit(a, 3)
print("🔪 열(Column) 방향 3등분 첫 번째 덩어리:\n", result[0])
```

---

## ② np.vsplit(ary): 겹겹이 쌓인 케이크 층 떼어내기

**[비유로 이해하기: 맛있는 케이크 층 떼어내기]**
층이 겹겹이 쌓인 맛있는 케이크를 포크로 층별로 하나하나 떼어 분리하는 것과 같습니다. 데이터를 **위아래 수직(Vertical)의 층(행 단위)**으로 분리합니다. 인공지능 학습 시 수천 장의 커다란 이미지 데이터가 한 겹 한 겹 수직으로 층층이 쌓여 있을 때, 메모리 폭주의 우려 없이 한 번에 100장씩 가로 칼로 슬라이스 쳐서 모델에게 훈련용 미니 배치(Mini-Batch) 묶음으로 분할 배식할 때 이 방법이 기가 막히게 유용하게 쓰입니다.

![np.vsplit 케이크 층 떼어내기](./img/vsplit_cake.svg)

위에서부터 층별로 분리해 내는 `np.vsplit(a)`는 이전에 배운 `np.split(a, axis=0)`과 100% 동일하게 동작합니다.

### [1단계] 1차원 배열은 vsplit이 불가능하다!
기본적인 1차원 배열(벡터)은 층 자체가 가장 밑바닥 1층뿐인 단층집이므로 윗층/아래층으로 층간 분리를 할 수가 없습니다.

![1차원 배열 vsplit 에러](./img/vsplit_step1_error.svg)

```python
a = np.arange(10)
# np.vsplit(a, 2)
# ValueError: vsplit only works on arrays of 2 or more dimensions
```
> **🚨 Numpy의 단호한 거절:** "위아래로 쪼갤 최소 2층(2차원)짜리 구조물을 가져와!"

### [2단계] 2차원 배열 vsplit 하기 (행 떼어내기)
2차원 형태로 아파트가 완성되어 있다면 `vsplit`을 써서 거대한 아파트의 층수를 똑 하고 떼어낼 수 있습니다.

![2차원 배열 vsplit](./img/vsplit_step2.svg)

```python
# 6행 3열 2차원 배열 (6층 아파트)
a = np.arange(18).reshape(6, 3)

# 위아래 행 방향(Row)으로 3등분 합니다. (2층짜리 아파트 3동으로 재건축)
result = np.vsplit(a, 3)
print("🔪 위아래 층 분할 첫 번째 덩어리:\n", result[0])

# 특정 층계참(인덱스 1층 시작 전, 4층 시작 전)에서 칼집 넣기
result_uneven = np.vsplit(a, (1, 4))
print("\n🔪 불균등 분할 마지막 덩어리 (4층 아래부터 옥상까지):\n", result_uneven[-1])
```

---

## ③ [심화] 3차원 공간에서의 hsplit 과 vsplit
마치 3차원 루빅스 큐브를 자르는 것과 같습니다. 어렵게 느껴질 수 있지만 동작 원리는 2차원과 똑같습니다. 함수 이름이 어느 축 방향으로 작용하는지 외우면 가장 편합니다.

*   `np.vsplit(x)`: `axis=0` 담당입니다. 가장 커다란 박스 껍데기 포장 단위인 **덩어리/블록(Depth)**을 위아래로 반갈죽 분리합니다.
*   `np.hsplit(x)`: `axis=1` 담당입니다. 전체 블록은 유지하되, 블록 내부를 열어 그 안에 있는 **각 행(Row)**들을 상하로 반갈죽 나눕니다.

![3차원 배열의 vsplit 과 hsplit](./img/hsplit_vsplit_3d.svg)

```python
import numpy as np

# (4덩어리, 4행, 2열) 크기의 3차원 큐브
x = np.arange(32).reshape(4, 4, 2)

# V-split: 제일 바깥쪽 포장인 4개의 거대한 '덩어리' 자체를 2개씩 묶어 분리합니다. 
v_result = np.vsplit(x, 2)
print("V-split 첫 번째 잘린 조각의 형태:", v_result[0].shape) # (2, 4, 2) 가 됨

# H-split: 바깥쪽 4개 덩어리는 그대로 유지한 채, 각 덩어리 내부를 까서 4행을 2행씩 분리합니다.
h_result = np.hsplit(x, 2)
print("H-split 첫 번째 잘린 조각의 형태:", h_result[0].shape) # (4, 2, 2) 가 됨
```
