# 11-5. 세상은 종 모양이다 (정규분포)

## 1. 정규분포(Normal Distribution)란?
평균 근처에 데이터가 가장 많고, 멀어질수록 적어지는 **종 모양(Bell Curve)**의 분포입니다.
*   사람들의 키
*   시험 점수
*   공장에서 만든 과자의 무게

## 2. Numpy로 정규분포 만들기
`np.random.normal(평균, 표준편차, 개수)`
*   `loc`: 평균 (Center)
*   `scale`: 표준편차 (Width)

## 3. [응용 예제] 우리 학교 키 분포 시뮬레이션
평균 키 170cm, 표준편차 5cm인 학생 1000명의 키를 생성하고 히스토그램으로 그려봅시다.

[소스 코드 실행하기](src/05_normal_dist.py) | [Colab에서 열기](src/05_normal_dist.ipynb)
