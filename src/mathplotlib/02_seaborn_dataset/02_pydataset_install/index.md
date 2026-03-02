---
layout: mathplotlib
title: "5.2.2 패키지 pydataset 설치"
---

# 5.2.2 패키지 pydataset 설치

다음 패키지 설치 명령 `pip install pydataset`으로 간단하게 설치할 수 있다.

```bash
!pip install pydataset
```

### ① 전체 자료 정보

설치된 pydataset의 전체적인 정보를 얻기 위해 데이터셋 목록을 표시해 보자. 패키지 `pydataset`에서 데이터를 불러와 `data()`로 생성하면 데이터셋 ID(`dataset_id`)와 제목(`title`)이 포함된 데이터프레임을 반환받을 수 있다.

다음으로 패키지 pydataset에는 757개의 샘플 데이터가 있다는 것을 알 수 있다.

```python
from pydataset import data

all_data = data()
print(all_data)
```
**출력:**
```
    dataset_id                                              title
0   AirPassengers       Monthly Airline Passenger Numbers 1949-1960
1         BJsales           Sales Data with Leading Indicator
2             BOD                       Biochemical Oxygen Demand
3    Formaldehyde                   Determination of Formaldehyde
4    HairEyeColor       Hair and Eye Color of Statistics Students
..            ...                                             ...
752       VerbAgg            Verbal Aggression item responses
753          cake               Breakage Angle of Chocolate Cakes
754          cbpp               Contagious bovine pleuropneumonia
755   grouseticks  Data on red grouse ticks from Elston et al. 2001
756    sleepstudy         Reaction times in a sleep deprivation study

[757 rows x 2 columns]
```