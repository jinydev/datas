# 7-2. 전반기 핵심 요약 2 (Numpy & Pandas)

## 1. 데이터 다루기 핵심 (Numpy)
*   리스트보다 빠르다.
*   **Vectorization**: 반복문 없이 계산한다. ( `arr * 2`)
*   **Slicing**: 데이터를 자른다. (`arr[0:3]`)

## 2. 표 다루기 핵심 (Pandas)
*   **DataFrame**: 데이터를 엑셀 표처럼 다룬다.
*   **Read**: `read_csv`
*   **Select**: `['열이름']` 또는 `loc/iloc`
*   **Filter**: `df[ df['점수'] > 80 ]`
*   **Group**: `df.groupby('반')['점수'].mean()`

## 3. [응용 예제] 가상의 쇼핑몰 매출 데이터 분석
날짜별, 상품별 매출 데이터가 있을 때 가장 많이 팔린 상품을 찾아봅시다.

[소스 코드 실행하기](src/02_review_2.py) | [Colab에서 열기](src/02_review_2.ipynb)
