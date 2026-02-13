# 10-4. 데이터 합치기 (Merge/Concat)

## 1. 데이터가 쪼개져 있다면?
A반 성적 파일, B반 성적 파일이 따로 있다면?
또는 학생 명부 파일과 성적 파일이 따로 있다면?
하나로 합쳐야 분석을 할 수 있습니다.

## 2. 위아래로 붙이기 (Concat)
단순히 데이터를 이어 붙이는 것입니다. (Concatenation)
`pd.concat([df1, df2])`

## 3. 옆으로 붙이기 (Merge)
공통된 열(Key)을 기준으로 정보를 합칩니다. (SQL의 Join과 유사)
`pd.merge(왼쪽, 오른쪽, on='기준열', how='inner')`

## 4. [응용 예제] 고객 정보와 구매 내역 합치기
고객 DB와 구매 DB를 합쳐서 "VIP 고객"이 누구인지 찾아봅시다.

[소스 코드 실행하기](src/04_merge_concat.py) | [Colab에서 열기](src/04_merge_concat.ipynb)
