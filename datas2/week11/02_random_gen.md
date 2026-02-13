# 11-2. 무작위 수 생성하기 (Random)

## 1. Numpy의 Random 기능
파이썬 기본 `random`보다 훨씬 빠르고 강력합니다.
*   `np.random.rand()`: 0~1 사이 균일 분포
*   `np.random.randn()`: 표준 정규 분포 (평균 0)
*   `np.random.randint()`: 정수 뽑기
*   `np.random.choice()`: 제비 뽑기

## 2. 시드(Seed) 설정
컴퓨터의 랜덤은 사실 치밀한 계산식입니다.
`np.random.seed(42)`처럼 씨앗 번호를 고정하면, 언제 실행해도 똑같은 랜덤 값이 나옵니다. (재현 가능성)

## 3. [응용 예제] 점심 메뉴 추천기
리스트에 메뉴를 넣어두고, 오늘 점심을 랜덤으로 골라주는 프로그램을 만들어봅시다.

[소스 코드 실행하기](src/02_random_gen.py) | [Colab에서 열기](src/02_random_gen.ipynb)
