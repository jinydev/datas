# 10-5. 피벗 테이블 (Pivot Table)

## 1. 데이터를 요약해서 보고 싶을 때
엑셀의 **Pivot Table**과 완전히 똑같습니다.
복잡하게 나열된 데이터를 "행, 열, 값" 기준으로 재배치하여 요약합니다.

## 2. 사용법
`df.pivot_table(index='행', columns='열', values='값', aggfunc='함수')`

## 3. [응용 예제] 매장별, 품목별 매출 현황판
여러 매장(Store)에서 여러 품목(Item)이 팔렸을 때, 한 눈에 들어오도록 표를 재구성해봅시다.

[소스 코드 실행하기](src/05_pivot.py) | [Colab에서 열기](src/05_pivot.ipynb)
