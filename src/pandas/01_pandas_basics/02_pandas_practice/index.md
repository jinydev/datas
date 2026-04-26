---
layout: pandas
title: "6.1.2 판다스 설치 및 기초 실습"
---

# 6.1.2 판다스 설치 및 기초 실습

> 💾 **[실습 파일 다운로드]**
> 본 강의의 전체 실습 코드를 직접 실행해 볼 수 있는 주피터 노트북 파일입니다. 아래 링크를 클릭하여 다운로드 후 VS Code에서 열어보세요.
> - [📥 pandas_intro_practice.ipynb 파일 다운로드](./pandas_intro_practice.ipynb) (클릭 또는 마우스 우클릭 후 '다른 이름으로 링크 저장')

## 🪄 [실습 1] 파이썬 예제 코드와 필터링 동작 원리

다음은 Pandas를 사용하여 데이터를 생성하고, 조건에 맞게 필터링(조건 검색)하는 간단한 예제입니다.

```python
import pandas as pd

# 1. 딕셔너리를 활용하여 데이터프레임(DataFrame) 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 92, 78, 95]
}
df = pd.DataFrame(data)

# 2. DataFrame 출력 (원본 데이터 확인)
print("--- 원본 데이터 ---")
print(df)

# 3. 데이터 필터링: Score가 90을 초과하는 우수 학생만 추출
excellent_students = df[df['Score'] > 90]

# 4. 필터링된 결과 확인
print("\n--- 90점 초과 우수 학생 ---")
print(excellent_students)
```

아래 데이터 변환 애니메이션은 위 파이썬 코드에서 `df[df['Score'] > 90]` 구문이 어떻게 동작하여 원본 데이터프레임(왼쪽)에서 조건을 만족하는 행들만 필터링한 후 새로운 결과 데이터프레임(오른쪽)을 만들어내는지를 직관적으로 보여줍니다.

![Pandas DataFrame Filtering Animation](./img/pandas_animation.svg)

---

## [실습 2] 왜 판다스를 써야 할까요?

수백만 건의 데이터를 엑셀로 열면 프로그램이 멈출 수 있지만, 판다스는 Python, Cython, C로 최적화되어 있어 엄청난 양의 데이터를 초고속으로 읽어 들이고 조작할 수 있습니다. 

현재 판다스는 **파이썬 데이터 분석 1위의 표준 도구**로 쓰이고 있습니다.

```python
import pandas as pd
import numpy as np

# Pandas는 대량의 데이터도 무심하게 처리해줍니다
data = pd.DataFrame(np.random.rand(1000000, 3), columns=['A_Score', 'B_Score', 'C_Score'])

print("100만 건 데이터 맛보기:\n", data.head(3))
```

**[실행 결과]**
```text
100만 건 데이터 맛보기:
     A_Score   B_Score   C_Score
0   0.12345   0.67890   0.45678
1   0.23456   0.78901   0.56789
2   0.34567   0.89012   0.67890
```

![초거대 데이터프레임 초고속 생성 퍼포먼스](./img/pandas_massive_df.svg)
