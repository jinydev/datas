---
layout: numpy
title: "4.11.3 정수형 주사위 굴리기"
description: "기계(rg)의 integers(low, high, size) 버튼은 윷놀이나 보드게임처럼 딱딱 떨어지는 정수만 필요할 때 사용합니다. low부터 high - 1 까지만 나옵니다. (파이썬의 인덱스 규칙과 동일합니다!)"
---

# 4.11.3 integers(): 정수형 주사위 굴리기

기계(`rg`)의 **`integers(low, high, size)`** 버튼은 윷놀이나 보드게임처럼 딱딱 떨어지는 **정수**만 필요할 때 사용합니다. `low`부터 `high - 1` 까지만 나옵니다. (파이썬의 인덱스 규칙과 동일합니다!)

![정수 주사위 굴리기](./img/random_step3.svg)

```python
# 앞에서 만든 기계 사용 가정: rg = np.random.default_rng(12345)

# 0부터 9 (10 미만) 사이의 정수 난수를 3개 뽑기
cube_rolls = rg.integers(low=0, high=10, size=3)
print("🎲 정수 난수 3개:", cube_rolls)

# 1부터 6 (7 미만) 사이의 주사위를 굴려 (3행 4열) 모양으로 기록하기
board_rolls = rg.integers(1, 7, size=(3, 4))
print("🎲 주사위 굴리기 결과:\n", board_rolls)
```
**[실행 결과]**
```text
🎲 정수 난수 3개: [0 2 4]
🎲 주사위 굴리기 결과:
 [[5 6 4 4]
 [2 6 4 5]
 [1 3 5 2]]
```
