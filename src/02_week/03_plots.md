---
layout: default
title: "2주차 2강: 기본 그래프 그리기 (Basic Plots)"
---

# 2주차 2강: 기본 그래프 그리기 (Basic Plots)

> **학습목표**: Matplotlib을 사용하여 선 그래프, 막대그래프, 산점도 등 기본적인 시각화 차트를 그리는 코드를 실습하고 데이터 패턴을 확인합니다.

## 2.2.0. 준비하기 (Preparation)

### 2.2.0.1. 한글 폰트 설정 및 버전 확인
그래프에 한글을 표시하기 위한 설정과 현재 설치된 Matplotlib의 버전을 확인합니다.

```python
import matplotlib.pyplot as plt
import matplotlib

# 1. 버전 확인
print(f"Matplotlib Version: {matplotlib.__version__}")

# 2. 한글 폰트 설정 (Mac: AppleGothic, Windows: Malgun Gothic)
# 이 코드는 그래프를 그리기 전에 한 번만 실행하면 됩니다.
import platform
if platform.system() == 'Darwin': # Mac
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows': # Windows
    plt.rc('font', family='Malgun Gothic')
    
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
```

## 2.2.1. 선 그래프 (Line Plot): 마법사의 마나 변화

> **선 그래프**: 시간에 따른 **변화의 추세(Trend)**를 볼 때 가장 좋습니다.

### 2.2.1.1. [단계 1] 간단한 선 차트 그리기
아무런 꾸밈없이 데이터만으로 그래프를 그려봅니다.

```python
# 데이터 준비 (시간, 현재 MP)
time = [0, 1, 2, 3, 4, 5]
mp = [100, 80, 60, 40, 20, 0]

# 기본 그래프 그리기
plt.figure() # 새로운 도화지 생성
plt.plot(time, mp)
plt.show()
```

### 2.2.1.2. [단계 2] 그래프 속성 변형하여 꾸미기
다양한 속성(제목, 색상, 마커, 선 스타일)을 추가하여 정보를 명확하게 전달합니다.

```python
plt.figure(figsize=(8, 5)) # 그래프 크기 설정 (가로 8, 세로 5)

# 속성 추가: 색상(color), 마커(marker), 선 스타일(linestyle), 라벨(label)
plt.plot(time, mp, color='purple', marker='o', linestyle='--', label='Mana Point')

# 제목 및 축 레이블 설정 (fontsize로 글자 크기 조절)
plt.title("Time vs Mana (Battle)", fontsize=15)
plt.xlabel("Time (sec)", fontsize=12)
plt.ylabel("Mana Point", fontsize=12)

plt.grid(True)  # 격자 표시
plt.legend()    # 범례 표시

plt.show()
```

- **해석**: 보라색 점선으로 표현하니 마법의 신비로움(?)이 더 잘 느껴지나요? 시간이 갈수록 MP가 0을 향해 일정하게 감소하는 것을 볼 수 있습니다.

## 2.2.2. 막대그래프 (Bar Plot): 직업별 공격력 비교

> **막대그래프**: 여러 그룹 간의 **크기 비교(Comparison)**에 적합합니다.

### 2.2.2.1. 시나리오: 전사, 마법사, 도적의 공격력 비교
우리 파티원들의 공격력을 비교해 봅시다. 누가 딜러인지 확인해 볼까요?

```python
# 데이터 준비
jobs = ['Warrior', 'Mage', 'Rogue']
damage = [150, 200, 120]

# 그래프 그리기
plt.bar(jobs, damage)
plt.show()
```

- **해석**: Mage(마법사)의 공격력이 가장 높고, Rogue(도적)가 가장 낮음을 바로 알 수 있습니다.

## 2.2.3. 산점도 (Scatter Plot): 명중률과 데미지의 관계

> **산점도**: 두 변수 간의 **상관관계(Correlation)**를 파악할 때 유용합니다. 점을 흩뿌려 놓은 모양입니다.

### 2.2.3.1. 시나리오: 무기의 무게와 공격력의 관계
무기가 무거우면 공격력이 높을까요? 10개의 무기를 조사해 봤습니다.

```python
# 데이터 준비
weight = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # 무게
power =  [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]  # 공격력

```python
# 그래프 크기 설정 (화면 크기 조절)
plt.figure(figsize=(10, 6)) # 가로 10인치, 세로 6인치

# 산점도 그리기 (alpha: 투명도 0~1)
plt.scatter(weight, power, c='red', alpha=0.5)

plt.title("Weapon Weight vs Power")
plt.xlabel("Weight (kg)")
plt.ylabel("Power")
plt.show()
```

- **Tip**: `alpha` 값을 낮추면 점이 겹쳐도 밀도를 파악하기 좋습니다. `figsize`는 그래프의 전체 크기를 조절합니다.

- **해석**: 점들이 오른쪽 위로 올라가는 모양입니다. 즉, **"무게가 무거울수록 공격력도 강해진다"**는 양의 상관관계를 발견했습니다!
