# 6-5. 여러 그래프 한번에 그리기 (Subplots)

## 1. 화면 분할의 마법
지금까지는 그래프를 하나 그리고 `show`, 또 하나 그리고 `show` 했습니다.
한 화면에 여러 개를 바둑판처럼 배치하고 싶다면 **Subplot**을 씁니다.

## 2. plt.subplot(행, 열, 순서)
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 5)) # 전체 도화지 크기 설정

# 1행 2열 중 첫 번째
plt.subplot(1, 2, 1)
plt.plot(x, np.sin(x))
plt.title("Sin")

# 1행 2열 중 두 번째
plt.subplot(1, 2, 2)
plt.plot(x, np.cos(x), color='red')
plt.title("Cos")

plt.show()
```

## 3. plt.subplots() (추천 방식)
객체 지향 방식이라고 부르는데, 더 많이 씁니다.

```python
# fig는 도화지, ax는 각 그래프 칸들
fig, ax = plt.subplots(2, 2) # 2x2 = 4개

ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x**2)
ax[1, 0].plot(x, x**3)
# 네 번째는 비워둘 수도 있음

plt.tight_layout() # 간격 자동 조절 (꿀팁!)
plt.show()
```

## 4. 핵심 정리
*   `subplot`: 화면을 나누어 여러 정보를 비교할 때 사용.
*   `tight_layout()`: 그래프끼리 겹치지 않게 해주는 필수 명령어.
