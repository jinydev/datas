# 9주차: Pandas 데이터프레임 조작

## 학습 목표 (Learning Objectives)
1.  **데이터 입출력 (I/O)**: CSV, Excel 같은 외부 파일을 읽어오고(`read`), 분석 결과를 다시 파일로 저장하는(`to`) 방법을 익힙니다.
2.  **데이터 선택 (Selection)**: 원하는 열(Column)이나 행(Row)을 선택하여 분석 대상을 좁히는 법을 배웁니다.
3.  **인덱서 활용 (loc, iloc)**: 이름으로 찾기(`loc`)와 위치로 찾기(`iloc`)의 차이점을 명확히 이해합니다.

## 강의 내용 (Course Content)

### [01. 데이터 불러오기/저장하기 (I/O)](./01_theory.md)
- `read_csv`: CSV 파일 읽어오기 (가장 기본).
- `to_csv`: 분석 결과를 파일로 내보내기.
- Colab에서 파일 업로드/다운로드 방법.

### [02. 열과 행 선택하기 (Selection)](./02_practice.md)
- 열 선택: 시리즈 추출 `df['Name']`.
- 행 선택: 범위 지정 `df[0:3]`.
- 조건 선택: `df[df['Level'] >= 10]`.

### [03. 정밀 타격: loc와 iloc (Indexing)](./03_advanced.md)
- `loc[행이름, 열이름]`: 명찰(Label) 기반 검색.
- `iloc[행번호, 열번호]`: 좌표(Position) 기반 검색.
- 둘의 차이점 완벽 정리.
