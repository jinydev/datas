---
layout: pandas
title: 판다스 (Pandas)
permalink: /pandas/
---

# 판다스 (Pandas) 핵심 가이드

파이썬 기반의 강력한 데이터 분석 및 조작 라이브러리인 **Pandas(판다스)**를 학습합니다. 주요 자료구조인 Series와 DataFrame의 생성부터 데이터 선택, 수정, 연산, 파일 입출력까지 실무에 필요한 데이터 정제 기술을 5개의 논리적인 섹션으로 나누어 살펴봅니다.

![Pandas Concept Illustration](./pandas_illustration.png)

<br/>

## 🐼 Pandas란 무엇인가요?

Pandas는 파이썬에서 표 형태의 데이터(Tabular Data)를 가장 쉽고 빠르게 다룰 수 있게 해주는 라이브러리입니다. 엑셀이나 SQL과 같은 데이터베이스의 기능을 파이썬 코드 안에서 빠르고 강력하게 사용할 수 있습니다.

### 파이썬 예제 코드 살펴보기
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

<br/>

## 🪄 데이터 변환 애니메이션 (필터링 동작 원리)

아래 데이터 변환 애니메이션은 위 파이썬 코드에서 `df[df['Score'] > 90]` 구문이 어떻게 동작하여 원본 데이터프레임(왼쪽)에서 조건을 만족하는 행들만 필터링한 후 새로운 결과 데이터프레임(오른쪽)을 만들어내는지를 직관적으로 보여줍니다.

<div style="text-align: center; margin: 2rem 0;">
  <img src="./pandas_animation.svg" alt="Pandas DataFrame Filtering Animation" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
</div>

---

## 6.1 판다스 기초 {#section-01}
- [6.1.1 판다스 소개](/pandas/01_pandas_basics/01_pandas_intro/)
- [6.1.2 Series(시리즈) 개요](/pandas/01_pandas_basics/02_series_intro/)
- [6.1.3 DataFrame(데이터프레임) 개요](/pandas/01_pandas_basics/03_dataframe_intro/)

## 6.2 자료구조 생성 (Series & DataFrame) {#section-02}
- [6.2.1 Series(시리즈) 생성과 데이터 추출](/pandas/02_series_dataframe_creation/01_series_creation/)
- [6.2.2 Series(시리즈) 필수 함수와 통계 요약](/pandas/02_series_dataframe_creation/02_series_functions/)
- [6.2.3 DataFrame 생성자(Constructor) 개요](/pandas/02_series_dataframe_creation/03_dataframe_constructor/)
- [6.2.4 2차원 행렬(Matrix)로 데이터프레임 만들기](/pandas/02_series_dataframe_creation/04_df_from_matrix/)
- [6.2.5 딕셔너리(Dict)를 이용한 데이터프레임 구조화](/pandas/02_series_dataframe_creation/05_df_from_dict/)
- [6.2.6 여러 개의 Series(시리즈)를 조립해 DataFrame 만들기](/pandas/02_series_dataframe_creation/06_df_from_series/)
- [6.2.7 리스트 속 딕셔너리(List of Dicts)로 DataFrame 만들기](/pandas/02_series_dataframe_creation/07_df_from_dict_list/)
- [6.2.8 딕셔너리의 값(Value)으로 Series(시리즈) 사용하기](/pandas/02_series_dataframe_creation/08_df_from_series_dict/)
- [6.2.9 데이터프레임의 자료형 검사와 변경 (dtypes)](/pandas/02_series_dataframe_creation/09_df_dtypes/)
- [6.2.10 시계열 데이터의 꽃: date_range()로 자동 날짜 생성하기](/pandas/02_series_dataframe_creation/10_date_range/)
- [6.2.11 완전체 시계열 데이터프레임 만들기](/pandas/02_series_dataframe_creation/11_df_with_dates/)

## 6.3 데이터 참조 및 인덱싱 {#section-03}
- [6.3.1 DataFrame 열(Column) 추출의 마법](/pandas/03_data_selection/01_column_selection/)
- [6.3.2 데이터프레임 논리식 검색 (Conditional Selection)](/pandas/03_data_selection/02_conditional_selection/)
- [6.3.3 loc[이름] 속성으로 행(Row) 참조 구하기](/pandas/03_data_selection/03_row_selection_loc/)
- [6.3.4 loc[index[i]]를 활용한 우회적 행 참조](/pandas/03_data_selection/04_row_selection_loc_i/)
- [6.3.5 loc[ : , 열이름] 으로 열(Column) 참조하기](/pandas/03_data_selection/05_col_selection_loc/)
- [6.3.6 loc[:, columns[i]]를 활용한 우회적 열 참조](/pandas/03_data_selection/06_col_selection_loc_i/)
- [6.3.7 loc[행, 열] 십자선 동시 참조](/pandas/03_data_selection/07_row_col_selection/)
- [6.3.8 df.iloc[위치] 로 번호 기반 참조](/pandas/03_data_selection/08_iloc_selection/)

## 6.4 데이터프레임 정보 확인 및 수정 {#section-04}
- [6.4.1 데이터프레임 종합 건강검진](/pandas/04_data_modification/01_df_info_modify/)
- [6.4.2 축(Axis) 기준 데이터 압축 연산](/pandas/04_data_modification/02_df_extract_assign/)
- [6.4.3 파생 열(Column)과 요약 행(Row) 추가하기](/pandas/04_data_modification/03_df_modify_assign/)
- [6.4.4 데이터프레임 고급 조건 검색 (isin, contains)](/pandas/04_data_modification/04_df_conditional_search/)
- [6.4.5 데이터프레임 쌍끌이 정렬](/pandas/04_data_modification/05_df_sorting/)
- [6.4.6 데이터프레임 전처리 공방](/pandas/04_data_modification/06_df_various_modifications/)

## 6.5 데이터 입출력 및 수집 {#section-05}
- [6.5.1 CSV와 Excel 파일 입출력](/pandas/05_file_io/01_csv_excel_io/)
- [6.5.2 실전! 지저분한 공공데이터 정제하기](/pandas/05_file_io/02_internet_data/)

