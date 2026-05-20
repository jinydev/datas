import os

base_dir = "/Users/hojin9/dev/jinysite/datas/src/practice"
os.makedirs(base_dir, exist_ok=True)

groups = {
    "분류 및 범주형 데이터 (Classification)": ["titanic", "iris", "penguins"],
    "회귀 및 연속형 데이터 (Regression)": ["tips", "diamonds", "mpg", "car_crashes"],
    "시계열 데이터 (Time Series)": ["flights", "fmri", "dowjones", "healthexp"],
    "기타 (Others)": ["planets", "brain_networks", "anagrams", "anscombe", "attention", "dots", "exercise", "geyser", "glue", "seaice", "taxis"]
}

top_10 = [
    ("titanic", "타이타닉 생존자 예측 실습"),
    ("iris", "붓꽃 품종 분류 실습"),
    ("tips", "레스토랑 팁 분석 실습"),
    ("penguins", "펭귄 데이터 분석 실습"),
    ("flights", "항공기 탑승객 시계열 분석 실습"),
    ("diamonds", "다이아몬드 가격 예측 실습"),
    ("mpg", "자동차 연비 분석 실습"),
    ("car_crashes", "자동차 사고 데이터 분석 실습"),
    ("planets", "외계 행성 탐색 데이터 실습"),
    ("fmri", "fMRI 뇌 활동 데이터 분석 실습")
]

# Generate index.md
index_content = """---
layout: default
title: "데이터 실습 (PyData)"
permalink: /practice/
---

# PyData 실습

Pandas와 Seaborn을 활용하여 인기 있는 데이터 셋을 직접 분석하고 시각화하는 실습 공간입니다.
기본으로 제공되는 여러 데이터 셋을 그룹별로 살펴보고, 상위 10개의 인기 데이터 셋에 대한 실습을 진행해 봅니다.

## 데이터 셋 그룹별 목록

"""

for group, datasets in groups.items():
    index_content += f"### {group}\n"
    for ds in datasets:
        # Check if it's in top 10 to provide a link
        top_10_match = next((item for item in top_10 if item[0] == ds), None)
        if top_10_match:
            idx = top_10.index(top_10_match) + 1
            index_content += f"- **[{ds}](/practice/{idx:02d}_{ds}/)**: {top_10_match[1]}\n"
        else:
            index_content += f"- {ds}\n"
    index_content += "\n"

with open(os.path.join(base_dir, "index.md"), "w", encoding="utf-8") as f:
    f.write(index_content)

# Generate 10 practice files
for idx, (ds, title) in enumerate(top_10, 1):
    ds_content = f"""---
layout: default
title: "{idx:02d}. {title}"
permalink: /practice/{idx:02d}_{ds}/
---

# {title} (`{ds}`)

이 실습에서는 `{ds}` 데이터 셋을 활용하여 데이터 전처리와 시각화를 진행합니다.

## 1. 데이터 불러오기

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 불러오기
df = sns.load_dataset('{ds}')
display(df.head())
```

## 2. 데이터 탐색 (EDA)

데이터의 기본 정보를 파악하고 결측치 등을 확인합니다.

```python
# 데이터 정보 확인
df.info()

# 기초 통계량 확인
display(df.describe())
```

## 3. 데이터 시각화

데이터의 특징을 파악할 수 있는 시각화를 수행합니다.

```python
# 예시: 산점도 또는 카운트 플롯 등
# sns.pairplot(df)
# plt.show()
```

## 4. 실습 과제

1. 주요 변수들의 분포를 시각화 해보세요.
2. 변수들 간의 상관관계를 분석하고 특징을 서술해 보세요.
3. 데이터에 결측치가 있다면 적절히 처리해 보세요.

"""
    with open(os.path.join(base_dir, f"{idx:02d}_{ds}.md"), "w", encoding="utf-8") as f:
        f.write(ds_content)

print("Generated practice files successfully.")
