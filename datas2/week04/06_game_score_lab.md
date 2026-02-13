# 4-6. [실습] 나만의 게임 전적표 만들기

## 1. 미션: 게임 캐릭터 데이터 만들기
여러분이 좋아하는 게임(롤, 발로란트, 오버워치 등)의 캐릭터나 선수 데이터를 직접 데이터프레임으로 만들어보세요.

## 2. 코드 가이드

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. 데이터 준비 (딕셔너리)
game_data = {
    'Character': ['Jett', 'Omen', 'Sova', 'Sage', 'Phoenix'],
    'Role': ['Duelist', 'Controller', 'Initiator', 'Sentinel', 'Duelist'],
    'PickRate': [50, 30, 45, 20, 15], # 픽률 (%)
    'WinRate': [55, 48, 52, 60, 45]   # 승률 (%)
}

# 2. 데이터프레임 생성
df = pd.DataFrame(game_data)

# 3. 데이터 확인
print(df)
print("----------------")
print(df.info())

# 4. 간단한 시각화 (판다스랑 맷플롯립 같이 쓰기!)
# 캐릭터 이름(Character)을 x축으로, 승률(WinRate)을 막대 그래프로
plt.bar(df['Character'], df['WinRate'], color='skyblue')
plt.title("Valorant Character Win Rates")
plt.xlabel("Character")
plt.ylabel("Win Rate (%)")
plt.ylim(0, 100) # 0~100% 범위
plt.show()
```

## 3. 도전 과제
*   자신이 만든 데이터에서 승률이 50% 이상인 캐릭터만 눈으로 찾아보세요.
*   (힌트) 다음 주에는 이것을 코드로 1초 만에 찾는 법을 배울 것입니다!
