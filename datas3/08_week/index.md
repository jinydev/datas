# 8주차: Pandas 개요 및 기초

## 학습 목표 (Learning Objectives)
1.  **Pandas의 이해**: 엑셀(Excel)과 비교하여 Pandas가 왜 강력한 데이터 분석 도구인지 이해합니다.
2.  **Series와 DataFrame**: Pandas의 핵심 자료구조인 시리즈(1차원)와 데이터프레임(2차원)을 다룹니다.
3.  **데이터프레임 생성**: 딕셔너리나 리스트를 이용하여 직접 데이터 표를 만들어 봅니다.

## 강의 내용 (Course Content)

### [01. 엑셀보다 강력한 도구 (Intro to Pandas)](./01_theory.md)
- Pandas란? (Python Data Analysis Library).
- 엑셀 vs Pandas: 대용량 데이터 처리와 자동화.
- Series(1줄) vs DataFrame(여러 줄).

### [02. 데이터프레임 만들기 (Creation)](./02_practice.md)
- 딕셔너리로 만들기 (Key=Column, Value=Data).
- 리스트로 만들기 (Row by Row).
- 외부 파일 읽기 맛보기 (`read_csv`).

### [03. 데이터 정찰하기 (Inspection)](./03_advanced.md)
- `head()`, `tail()`: 앞뒤 데이터 확인.
- `info()`, `describe()`: 데이터의 요약 정보와 기초 통계량 확인.
