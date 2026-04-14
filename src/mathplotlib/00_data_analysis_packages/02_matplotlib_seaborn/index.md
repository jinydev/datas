---
layout: mathplotlib
title: "5.0.2 패키지 matplotlib, seaborn, pydataset 개요"
---

## 5.0.2 Matplotlib, Seaborn, pydataset의 역할과 철학

파이썬의 시각화 세계에는 양대 산맥이 존재합니다. 하나는 그림의 모든 세부 사항을 밑바닥부터 100% 통제하는 전통적인 장인 **Matplotlib**이고, 다른 하나는 자주 쓰는 통계 그래프들을 알아서 예쁘게 그려주는 최신식 마법 템플릿 **Seaborn**입니다.

### 두 시각화 라이브러리의 철학 차이

**[전산학적/시각적 의미: Procedural vs Declarative]**
- **`matplotlib` (절차적 방식)**: 빈 도화지(Figure)를 만들고, 가로축 눈금은 무엇으로 할지, 붓 색깔은 빨간색으로 할지, 점을 어느 좌표에 하나하나 찍을지 컴퓨터에게 **명령(Procedural)**하여 그림을 완성시키는 라이브러리입니다. 세밀한 조작이 가능하지만 코드가 길어집니다.
- **`seaborn` (선언적 방식)**: `matplotlib`의 엔진을 기반으로, 그 위에 디자인 껍데기(테마)를 씌운 것입니다. 그냥 구체적인 지시 없이 "이 Pandas 데이터를 통째로 넣을 테니 막대그래프(Barplot)로 눈에 띄게 그려줘!" 라고 **선언(Declarative)**만 하면 알아서 축을 그리고 색상을 입혀줍니다.

![Matplotlib과 Seaborn의 시각화 철학 비교](img/mpl_vs_sns.svg)

수업 전반부에는 `matplotlib`의 뼈대를 배우고, 후반부에서는 `seaborn`으로 화려하고 복잡한 통계 분석 차트를 단 몇 줄로 생성하는 방법을 배우게 됩니다.

---

### 장난감 데이터 창고: `pydataset`

그래프를 그리기 위해서는 먼저 도화지에 올릴 '물감(데이터)'이 필요합니다. 매번 인터넷에서 엑셀이나 CSV 파일을 다운로드받아서 코드로 불러오는 것은 매우 번거롭습니다.

이때 구원투수로 등장하는 패키지가 바로 **`pydataset`** 입니다.

- **장난감 데이터(Toy Data)**: 데이터 분석가들이 시각화나 머신러닝 알고리즘을 연습하기 위해 표준적으로 사용하는 깨끗하고 유명한 더미(Dummy) 데이터들을 말합니다.
- `pydataset`을 설치하면 파이썬 내장 함수 1개만 호출해도 <타이타닉 승객 목록>, <붓꽃(Iris) 사이즈>, <식당 손님들의 팁(Tips)> 데이터가 Pandas의 `DataFrame` 객체 형태로 즉각 소환됩니다.

---

### 시각화 환경 패키지 불러오기 (Import)

앞서 `pip install matplotlib seaborn pydataset`을 통해 컴퓨터(아나콘다)에 도구들을 다운로드 받았다면, 이제 파이썬 스크립트(.py 파일이나 주피터 노트북) 내부로 이 도구들을 꺼내와야 합니다. 

현업 데이터 사이언티스트들이 전 세계 공통으로 사용하는 '별명(Alias)' 매핑 규칙은 다음과 같습니다.

```python
# 가장 기본이 되는 데이터 가공/수학 엔진
import pandas as pd
import numpy as np

# 전통적인 수동 시각화 장인 도구 (가장 많이 쓰는 pyplot 하위 모듈만 꺼냅니다)
import matplotlib.pyplot as plt

# 현대적인 자동 시각화 마법 템플릿 도구
import seaborn as sns

# 샘플(Toy) 데이터 장난감 창고
from pydataset import data
```

> **📌 핵심 요약**
> - 세밀한 텍스트 폰트 조각, 도화지 분할, 파일 저장은 `plt` (Matplotlib)가 담당합니다.
> - 복잡한 통계 분포나 색상 팔레트를 입힌 데이터 차트는 `sns` (Seaborn)가 담당합니다.
> - 이 둘은 적대적 관계가 아니며, 항상 **같이 사용(혼용)** 됩니다!
