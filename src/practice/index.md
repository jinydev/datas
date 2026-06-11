---
layout: practice
title: "데이터 분석 실습 (PyData)"
permalink: /practice/
---

# PyData 실전 데이터 분석 커리큘럼

Pandas와 Seaborn을 활용하여 200개의 인기 있는 데이터 셋을 직접 분석하고 시각화하는 실무 중심의 실습 공간입니다. 
데이터 사이언스 역량은 **코드(Pandas)**, **시각화(Seaborn)**, 그리고 **통계적 직관(Statistics)**이라는 3가지 축이 맞물려야 완성됩니다. 아래의 커리큘럼 목록을 통해 단계별 학습 목표를 확인하세요.

---

## 🗺️ 파이데이터 200개 모듈 커리큘럼 리스트

### 00. [파이데이터(PyData) 분석 개요](/practice/00_pydata_intro/)
본격적인 데이터 분석 실습에 들어가기에 앞서, 우리가 다루게 될 **파이데이터(PyData) 생태계**와 **데이터셋의 유형**, 그리고 앞으로 모든 실습을 관통하게 될 **4단계 데이터 분석 프레임워크**에 대해 자세히 알아보겠습니다.

### 01. [타이타닉 생존자 예측](/practice/01_titanic/)
이 실습은 데이터 분석 및 머신러닝 분야에서 가장 유명한 **"Hello World"**와도 같은 타이타닉(Titanic) 데이터셋을 다룹니다. 1912년 발생한 타이타닉호 침몰 사고의 실제 승객 명부를 바탕으로, **"어떤 특징(성별, 나이, 객실 등급 등)을 가진 승객이 더 많이 살아남았을까?"**라는 질문에 대한 해답을 데이터를 통해 추적해 봅니다.

### 02. [붓꽃 품종 분류](/practice/02_iris/)
이 실습은 통계학과 머신러닝의 역사에서 가장 널리 인용되는 **'피셔의 붓꽃(Fisher's Iris)'** 데이터셋을 다룹니다. 1936년에 만들어진 이 전설적인 데이터셋은 단 4가지의 단순한 형태학적 측정값(길이와 너비)만으로 식물의 종(Species)을 완벽에 가깝게 분류해 낼 수 있음을 보여줍니다.

### 03. [레스토랑 팁 분석](/practice/03_tips/)
미국의 레스토랑 식문화에서는 결제 금액의 일정 비율(보통 15~20%)을 웨이터에게 '팁(Tip)'으로 지불하는 관행이 있습니다. 이 데이터셋은 한 웨이터가 수개월 동안 자신이 서빙한 손님들의 성별, 흡연 여부, 방문 요일과 시간, 그리고 총결제 금액과 자신이 받은 팁을 꼼꼼하게 기록한 실제 영업 데이터입니다.

### 04. [펭귄 데이터 분석](/practice/04_penguins/)
이 실습은 기존의 식상한 '붓꽃(Iris)' 데이터셋을 대체하기 위해 최근 데이터 과학계에서 널리 사랑받고 있는 **팔머 펭귄(Palmer Penguins)** 데이터셋을 다룹니다. 남극 팔머 연구소에서 관측한 3가지 품종의 펭귄 신체 데이터를 분석하며, 결측치를 안전하게 삭제하는 방법과 통계학의 유명한 함정인 **'심슨의 역설(Simpson's Paradox)'**을 시각화를 통해 파훼하는 법을 배웁니다.

### 05. [항공기 탑승객 시계열 데이터](/practice/05_flights/)
우리가 지금까지 다룬 타이타닉, 붓꽃, 팁 데이터는 '특정 시점'의 스냅샷 데이터였습니다. 하지만 주식 시장, 날씨, 매출액과 같이 **시간의 흐름(Time Series)**에 따라 변하는 데이터는 완전히 다른 분석 접근법이 필요합니다.

### 06. [다이아몬드 가격 예측](/practice/06_diamonds/)
이 실습에서는 약 54,000개의 다이아몬드 거래 데이터셋을 다룹니다. 흔히 다이아몬드는 무거울수록(Carat) 비싸다고 생각하지만, 실제 가격은 세공(Cut), 색상(Color), 투명도(Clarity)라는 '4C'의 복합적인 상호작용에 의해 결정됩니다.

### 07. [자동차 연비 데이터](/practice/07_mpg/)
1970년대 후반에서 1980년대 초반, 전 세계 자동차 산업은 큰 격변기를 겪었습니다. 이 시기에 미국, 유럽, 일본에서 생산된 자동차들의 제원 데이터를 담고 있는 **MPG (Miles Per Gallon, 갤런당 마일)** 데이터셋을 통해, 차량의 스펙(무게, 마력, 기통 수)이 연비에 미치는 영향을 분석해 봅니다.

### 08. [앤스콤 콰르텟과 시각화의 중요성](/practice/08_anscombe/)
"평균과 분산 같은 숫자로 요약된 데이터만 믿으면 큰 코 다친다."

### 09. [뇌 신경망 상관관계](/practice/09_brain_networks/)
우리 뇌는 수많은 영역(Node)이 서로 복잡하게 연결된 거대한 네트워크입니다. 이 실습에서는 뇌의 특정 영역들이 피를 얼마나 함께 소모하는지(즉, 얼마나 동시에 활성화되는지) 측정한 기능적 뇌 영상 데이터를 분석합니다.

### 10. [fMRI 뇌파 시계열 분석](/practice/10_fmri/)
우리가 병원에서 흔히 보는 MRI(자기공명영상)가 뇌의 정적인 '구조'를 찍는 사진이라면, **fMRI(기능적 자기공명영상)**는 피가 뇌의 어느 부위로 쏠리는지를 실시간 동영상처럼 촬영하여 뇌의 '기능'을 측정하는 기술입니다.

### 11. [뉴욕 택시 데이터 분석](/practice/11_taxis/)
뉴욕시(NYC)를 누비는 옐로우 캡(Yellow Cab)과 그린 캡(Green Cab)의 실제 탑승 기록 데이터를 분석합니다. 단순한 숫자를 넘어 "뉴욕 시민들은 몇 시에 택시를 가장 많이 탈까?" 혹은 "결제 수단에 따라 팁(Tip)을 주는 비율이 다를까?"와 같은 실생활의 비즈니스 인사이트를 도출해 냅니다.

### 12. [간헐천(Geyser) 데이터](/practice/12_geyser/)
미국 옐로스톤 국립공원에는 세계에서 가장 유명한 간헐천인 '올드 페이스풀(Old Faithful)'이 있습니다. 이 간헐천은 주기적으로 뜨거운 물기둥을 하늘로 뿜어냅니다.

### 13. [미국 교통사고 데이터](/practice/13_car_crashes/)
미국 50개 주(States)와 워싱턴 D.C.에서 발생한 교통사고 통계 데이터를 분석합니다. 주마다 과속 비율, 음주운전 비율, 그리고 자동차 보험료가 다릅니다. 이 요소들이 전체 교통사고 사망자 수(Total)에 어떤 영향을 미치는지 데이터로 증명해 봅니다.

### 14. [국가별 의료비 지출과 기대수명 분석](/practice/14_healthexp/)
"국가가 국민의 건강을 위해 돈(의료비)을 많이 쓰면 쓸수록, 국민들은 더 오래 살까?" 이 근원적인 질문에 답하기 위해 1970년부터 2020년까지 주요 선진국들의 의료비 지출(Spending)과 기대수명(Life Expectancy)의 변화 추이를 추적합니다.

### 15. [운동과 식단에 따른 심박수 변화](/practice/15_exercise/)
우리가 운동을 하면 심장 박동(Pulse)이 빨라집니다. 그렇다면 걷기(Walk)와 달리기(Run)의 심박수 상승폭은 얼마나 다를까요? 혹시 운동 전에 먹은 식단(지방 섭취 여부)이 심장에 미치는 무리(부하)를 다르게 만들지는 않을까요?

### 16. [다우존스 주가지수 시계열 분석](/practice/16_dowjones/)
미국 주식 시장의 전체적인 흐름을 보여주는 가장 대표적인 지표, '다우존스 산업평균지수(Dow Jones Industrial Average)'의 100년 치 역사적 데이터를 분석합니다. 주식 차트 분석에서 가장 기본이 되는 시계열 데이터 처리와 이동 평균선 기법을 배웁니다.

### 17. [인지 심리학(Attention) 데이터 분석](/practice/17_attention/)
"음악을 들으면서, 스마트폰 메신저를 확인하며, 수학 문제를 풀면 성적이 떨어질까?" 누구나 한 번쯤 가져보았을 이 궁금증을 인지 심리학자들의 실제 통제 실험(Controlled Experiment) 데이터를 통해 증명해 봅니다.

### 18. [외계 행성(Planets) 발견 데이터 분석](/practice/18_planets/)
우리가 살고 있는 태양계 밖에는 얼마나 많은 외계 행성(Exoplanets)들이 있을까요? NASA에서 제공하는 1,000개가 넘는 외계 행성 발견 데이터를 통해 우주 탐사의 역사와 스케일을 분석해 봅니다.

### 19. [언어 모델 벤치마크(GLUE) 히트맵 분석](/practice/19_glue/)
우리가 흔히 쓰는 ChatGPT 같은 인공지능은 사람의 언어를 얼마나 잘 이해할까요? 이를 평가하기 위해 고안된 종합 국어 수능 시험이 바로 **GLUE (General Language Understanding Evaluation)** 벤치마크입니다. 2018년과 2019년에 쏟아져 나온 다양한 인공지능 모델들의 성적표를 분석해 봅니다.

### 20. [북극 해빙 면적 시계열 분석](/practice/20_seaice/)
"지구 온난화는 거짓말이다. 북극의 얼음은 겨울이 되면 다시 꽁꽁 얼어붙는다." 기후 변화 회의론자들의 이런 주장에 대해 데이터 분석가는 어떻게 반박해야 할까요? 1980년부터 2019년까지 40년간 매일 측정된 북극 해빙(Sea Ice) 면적 데이터를 통해, 그들의 주장에 숨겨진 통계적 함정을 파헤쳐 봅니다.

### 21. [와인 품질 데이터 코릴레이션(상관관계) 분석](/practice/21_wine/)
지금까지는 Seaborn에 내장된 연습용 데이터(Toy Dataset)들을 활용했습니다. 이제부터는 실무 환경과 동일하게 **로컬 폴더에 저장된 실제 CSV 파일**을 불러와서 분석하는 방법을 배웁니다.

### 22. [자전거 대여량 시계열 수요 예측 분석](/practice/22_bike/)
우버(Uber)나 따릉이 같은 모빌리티 서비스에서 가장 중요한 것은 무엇일까요? 바로 "내일 몇 대의 자전거가 필요할까?"를 예측하는 것입니다. 날씨, 온도, 계절, 그리고 요일 등 수많은 외부 환경 요인이 사람들의 이동 수요에 어떤 영향을 미치는지 데이터로 증명해 봅니다.

### 23. [캘리포니아 집값 분석과 지리적 산점도](/practice/23_housing/)
머신러닝 부동산 예측 모델의 교과서라 불리는 **캘리포니아 주택 가격(California Housing)** 데이터 셋입니다. 이 데이터에는 데이터 수집 과정의 한계로 인해 발생한 끔찍한 이상치(Outlier)가 숨어 있습니다. 이를 찾아내어 제거하고, 지리적 위경도 데이터를 활용해 캘리포니아 지도를 데이터만으로 복원해 내는 화려한 4차원 시각화를 경험해 봅니다.

### 24. [유방암 진단 분류 데이터 시각화](/practice/24_cancer/)
의료 인공지능(Medical AI) 분야에서 가장 널리 쓰이는 표준 데이터인 **유방암 진단(Breast Cancer)** 데이터입니다. 세포 핵의 크기와 모양을 수치화한 데이터를 바탕으로, 이것이 단순한 혹(양성)인지 치명적인 암(악성)인지 판별하는 머신러닝 분류(Classification)의 기초를 다집니다.

### 25. [학생 성적 예측 데이터 시각화 분석](/practice/25_student/)
교육부나 학교 현장에서 자주 다루는 **학생 학업 성취도(Student Performance)** 데이터 셋입니다. 포르투갈 학생들의 과거 수학 성적, 공부 시간, 결석 횟수, 심지어 부모님의 직업까지 방대한 특성(Feature)이 담겨 있습니다. 이 실무 데이터를 통해 우리는 최종 기말고사 성적에 절대적인 영향을 미치는 요인들을 수학적으로 찾아내고 눈으로 증명해 봅니다.

### 26. [심장 질환 예측과 연속형 변수 범주화](/practice/26_heart/)
의료 데이터 분석의 대표적인 사례인 **심장 질환(Heart Disease)** 예측 데이터입니다. 환자의 나이, 혈압, 콜레스테롤, 최대 심박수 등 다양한 신체 수치를 바탕으로 이 환자가 심장병 발병 고위험군인지 아닌지를 분류(Classification)하는 법을 배웁니다.

### 27. [인구조사 소득 예측 데이터 시각화 분석](/practice/27_adult/)
머신러닝 교과서에 반드시 등장하는 **성인 인구조사(Adult Census Income)** 데이터입니다. 나이, 직업, 학력, 결혼 상태, 근로 시간 등의 인적 사항을 바탕으로, 이 사람의 연 소득이 미국 평균 중산층 기준인 5만 달러(약 6~7천만 원)를 넘는지 못 넘는지 분류(Classification)하는 법을 탐구합니다.

### 28. [은행 마케팅 캠페인 시각화 분석](/practice/28_marketing/)
포르투갈 은행 기관의 실제 **텔레마케팅 캠페인(Bank Marketing)** 데이터입니다. 고객의 직업, 나이, 결혼 여부, 대출 유무 등 프로필 데이터를 바탕으로 이 고객에게 전화를 걸었을 때 정기 예금(Term Deposit)에 가입할지 말지를 예측하는 것이 목표입니다.

### 29. [이커머스 매출 트렌드 시계열 분석](/practice/29_ecommerce/)
온라인 쇼핑몰(이커머스)에서 하루에도 수만 건씩 쏟아지는 **실제 고객 결제 로그(Transaction Log)** 데이터입니다. 원시 데이터(Raw Data) 상태에서는 누가 언제 무엇을 샀다는 정보만 텍스트로 적혀 있을 뿐, 쇼핑몰의 전체적인 매출 현황을 알 수 없습니다.

### 30. [마트 수익 분석](/practice/30_superstore/)
글로벌 대형 마트(Superstore)의 방대한 **매출(Sales) 및 순이익(Profit)**이 담긴 결제 데이터셋입니다. 수만 건의 파편화된 영수증 데이터를 모아서, 회사의 운명을 결정짓는 핵심 KPI(핵심 성과 지표) 인사이트를 뽑아내는 훈련을 합니다.

### 31. [넷플릭스 콘텐츠 분석](/practice/31_netflix/)
세계 최대의 OTT 서비스인 넷플릭스(Netflix)의 영화 및 TV 프로그램 등록 데이터셋입니다. 영화와 TV 프로그램의 비율 분포를 확인하고, 연도별 등급의 다차원 스택 분석을 통해 글로벌 스트리밍 서비스의 콘텐츠 제작 트렌드를 추적해 봅니다.

### 32. [스포티파이 음원 분석](/practice/32_spotify/)
글로벌 1위 음원 스트리밍 서비스인 스포티파이(Spotify)의 인기 트랙 데이터셋입니다. 곡의 '댄스성(Danceability)', '에너지(Energy)', '템포(Tempo)' 등 청각적 속성을 활용하여, 어떤 특성이 대중적 '인기도(Popularity)'를 결정하는지 상관관계를 분석합니다.

### 33. [에어비앤비 숙소 가격 분석](/practice/33_airbnb/)
글로벌 공유 숙박 플랫폼 에어비앤비(Airbnb)의 숙소 등록 정보와 1박 요금 데이터셋입니다. 일반적인 숙박 가격 분포를 넘어서는 초고가 '이상치(Outlier)' 객실들을 식별해 내고, 객실 타입(공간 전체, 개인실, 다인실)에 따른 가격 차이를 박스플롯을 통해 심층 분석합니다.

### 34. [쇼핑몰 고객 세그먼트 분석](/practice/34_customer_segmentation/)
쇼핑몰 멤버십 회원들의 기본 인적 사항과 연간 소득, 소비 행동을 점수화한 가상 데이터셋입니다. 타겟 정답지 없이 데이터 내부의 유사성을 기반으로 나누는 비지도 학습(Clustering)의 원리를 이해하고, 소득 vs 소비 두 축의 교차점을 시각화하여 5개 고객 세그먼트를 발굴합니다.

### 35. [소매점 매출 분석](/practice/35_retail_sales/)
대형 소매점에서 1년 동안 발생한 실시간 거래 로그(Transaction Log) 데이터셋입니다. 판다스 시계열 변환 함수를 이용해 문자열 날짜 정보에서 월(Month) 정보를 추출하는 파생 변수 엔지니어링을 수행하고, 상품 카테고리별 총매출과 월별 매출 변동 트렌드를 시각화 보고서로 도출합니다.

### 36. [FIFA 월드컵 역사 분석](/practice/36_fifa_world_cup/)
1930년 초대 우루과이 대회부터 2022년 카타르 대회까지 역대 월드컵 본선 결승전의 공식 통계 기록 데이터셋입니다. 100년에 가까운 시간 동안 개최국, 우승 횟수 순위를 정제하고, 세계대전으로 인한 공백 및 관중 동원력의 시대적 확장세를 시각적으로 추적합니다.

### 37. [코로나19 트렌드 분석](/practice/37_covid19/)
코로나19 팬데믹 기간의 국가별 일일 신규 확진자 및 백신 누적 접종 실적 데이터셋입니다. 시계열 전파 속도를 분석하고, 백신 접종이 대규모로 확산함에 따라 일일 신규 확진자가 어떻게 비례하여 억제되었는지 두 변수 간의 역상관 관계를 추적합니다.

### 38. [직원 퇴사 요인 분석](/practice/38_employee_attrition/)
가상 기업의 인사 관리(HR) 본부에서 집계한 직원 재직/이탈 현황 데이터셋입니다. 우수한 인재들이 회사를 그만두는 핵심 원인을 규명하기 위해 직무 만족도, 연봉 수준, 그리고 근속 연수가 '퇴사 여부(Attrition - Yes/No)'에 미치는 영향력을 통계적으로 추적합니다.

### 39. [배달 앱 주문 분석](/practice/39_food_delivery/)
음식 배달 앱 플랫폼에서 기록된 가상의 1000건 주문 로그 데이터셋입니다. 배달 서비스의 핵심 품질 지표인 '배달 소요 시간(Delivery Time)'과 고객이 남긴 '별점 평점(Rating)' 간의 상관성을 분석하여, 고객 만족도를 훼손하지 않는 배달 제한 데드라인 시간을 도출합니다.

### 40. [포켓몬 능력치 분석](/practice/40_pokemon/)
게임 및 데이터 교육용으로 널리 사용되는 포켓몬스터(Pokemon) 캐릭터의 상세 능력치 통계 데이터셋입니다. 포켓몬의 주 속성(Type 1)별 개체 수 분포를 확인하고, 공격력(Attack)과 방어력(Defense)의 산점도 관계를 통해 일반 등급과 '전설의 포켓몬(Legendary)' 등급 간의 밸런스 인플레이션 경계를 파악합니다.

### 41. [유튜브 인기 동영상 분석](/practice/41_youtube/)
글로벌 최대 비디오 플랫폼인 유튜브(YouTube)의 인기 급상승 동영상 데이터셋입니다. 각 비디오의 카테고리별 누적 조회수 분포를 비교하고, 조회수(Views) 대비 좋아요(Likes)와 댓글 수(Comment Count)의 반응성을 산점도 시각화 및 상관분석을 통해 다각도로 이해합니다.

### 42. [연간 날씨 및 기온 분석](/practice/42_weather/)
2023년 한 해 동안의 일별 날씨 관측 정보가 포함된 데이터셋입니다. 판다스 시계열 변환을 사용하여 연간 기온(Temperature)의 흐름을 월 단위로 가공하고, 대기 중 습도(Humidity)의 분포 현황과 기상 형태(Condition)에 따른 기온 편차를 시각적으로 추적해 봅니다.

### 43. [차량 공유 서비스 가격 분석](/practice/43_rideshare/)
차량 공유 서비스 시장의 양대 산맥인 우버(Uber)와 리프트(Lyft)의 거래 건별 이용 요금 데이터셋입니다. 이동 거리(Distance)와 날씨 변동 할증(Weather Factor)이 요금(Price) 결정에 미치는 영향을 상관 분석과 시각화를 통해 규명하고 브랜드별 마진 책정 공식을 비교합니다.

### 44. [와인 리뷰 감성 및 평점 분석](/practice/44_wine_reviews/)
전 세계 주요 와이너리 제품들의 소믈리에 평가 점수와 1병당 시장 판매가를 추적한 데이터셋입니다. 고품질 와인일수록 판매 가격이 비선형적으로 급증하는 경제학적 패턴을 분석하고, 결측치가 존재하는 가격 변수를 국가별 대표값을 활용해 신뢰성 있게 대치하는 고급 전처리를 학습합니다.

### 45. [비디오 게임 판매 내역 분석](/practice/45_game_sales/)
글로벌 비디오 게임 업계의 1995년부터 2020년까지의 플랫폼(Console) 및 장르별 판매 로그 데이터셋입니다. 북미(NA), 유럽(EU), 일본(JP)의 대륙별 소비 선호도의 뚜렷한 국가적 격차를 비교 요약하고, 시대 변화에 따른 총 게임 시장의 전 세계 총매출 트렌드를 분석합니다.

### 46. [개발자 설문조사 분석](/practice/46_stackoverflow/)
글로벌 최대 개발자 지식 커뮤니티인 스택 오버플로우(Stack Overflow)의 설문조사 로그 데이터셋입니다. 개발자의 코딩 연차(YearsCode)와 주 사용 프로그래밍 언어(Primary Language)가 실제 시장에서 지급되는 연봉(Salary)에 어떤 가중 효과를 발휘하는지 통계적으로 비교하고 시각화합니다.

### 47. [건강 스마트워치 데이터 분석](/practice/47_health_tracker/)
스마트워치 기기에서 365일간 연속 자동 수집된 일일 건강 지표 로그 데이터셋입니다. 일별 걸음 수(Steps)와 고강도 활동 시간(ActiveMinutes)의 분포를 관찰하고, 수면 시간(SleepHours)의 증가가 실제 설문으로 표기된 수면 만족도 품질(SleepQuality) 점수에 미치는 물리적 영향 관계를 추적합니다.

### 48. [에임스 주택 가격 예측 분석](/practice/48_ames_housing/)
캐글(Kaggle) 부동산 가격 예측 입문으로 가장 대중적인 에임스 주택(Ames Housing) 데이터셋의 핵심 변수 축소 버전입니다. 지상 주거 공간 면적(GrLivArea)과 건물의 전반적 마감 품질(OverallQual)이 주택 실거래가(SalePrice)에 미치는 기여 효과를 산점도 및 다변수 분석으로 이해합니다.

### 49. [신용카드 연체 여부 예측](/practice/49_credit_default/)
금융기관의 대출 및 신용카드 심사 평가를 돕기 위한 신용 위험 데이터셋입니다. 고객의 카드 한도액(LimitBal), 학력(Education), 연령(Age)을 기반으로 다음 달 결제 대금을 갚지 못해 부도 위험에 직면하는 고객 비율(Default)을 탐색하고, 클래스 불균형이 심한 이진 분류 데이터셋의 통계 처리 요령을 학습합니다.

### 50. [통신사 고객 이탈 요인 분석](/practice/50_customer_churn/)
통신사 가입 고객들의 유지 계약 형태와 가입 연수, 그리고 매달 내는 이용 요금 데이터셋입니다. 서비스 이탈 여부(Churn = Yes/No)를 종속 변수로 삼아, 월간 요금 부담 강도와 가입 기간의 상호작용이 구독 해지 행동에 어떤 통계적 인과 패턴으로 작용하는지 정교하게 시각화합니다.

### 51. [미국 인구 통계학 분석](/practice/51_us_census/)
미국 연방 인구 조사국(US Census)의 주(State)별 핵심 인구 데이터셋입니다. 각 주의 교육 수지(대학 학위 소지 비율)가 가구 소득 중위값에 미치는 영향력을 상관분석과 다차원 산점도로 규명하고, 빈곤율의 국가적 격차를 가로 막대로 시각화합니다.

### 52. [온라인 식료품 주문 패턴 분석](/practice/52_grocery_orders/)
대형 식료품 이커머스 쇼핑몰의 일일 주문 상세 내역입니다. 하루 중 주문이 집중되는 피크 시간대를 커널 밀도 추정과 히스토그램으로 포착하고, 멤버십 우수 가입자와 일반 가입자의 평균 결제액(객단가) 격차를 상자그림으로 대조 진단합니다.

### 53. [자동차 보험 청구 및 이상 탐지](/practice/53_auto_insurance/)
자동차 손해보험사의 사고 청구 건별 관측 데이터셋입니다. 스포츠카, SUV, 승용차 등 차종에 따른 청구 가치 분포를 상자 그림으로 대조 분석하고, 운전자 나이와 청구 금액의 결합 산점도상에서 정상 범주를 이탈한 사기 의심(Fraud) 건의 경계를 도출합니다.

### 54. [영화 평점 시계열 변동](/practice/54_movie_ratings/)
영화 정보 메타데이터셋의 미니 버전입니다. 영화의 전체 상영시간(Runtime)이 정규분포를 그리는지 히스토그램으로 확인하고, 1980년부터 2023년까지 개봉된 영화들의 평균 관객 평점이 시대 흐름에 따라 어떻게 변화했는지 꺾은선 시계열 그래프로 추적합니다.

### 55. [이커머스 제품 리뷰 분석](/practice/55_product_reviews/)
이커머스 몰의 제품 카테고리별 리뷰와 평점 정보입니다. 각 카테고리의 긍정 추천 비율을 카운트 플롯의 중첩 막대로 분석하고, 불만이 높은 부정 고객(1~2점)일수록 장문의 피드백을 남기는 텍스트 글자수 분포의 특징을 상자그림으로 증명합니다.

### 56. [대기 질 오염도 요인 분석](/practice/56_air_quality/)
주요 도시의 대기 오염 정보와 교통 지수를 수집한 환경 과학 데이터셋입니다. 도시 및 계절에 따른 초미세먼지 농도의 평균차를 막대 차트로 다차원 비교하고, 도로 교통량(Traffic Index)의 증가와 미세먼지 수치 간의 양의 선형 인과관계를 산점도로 규명합니다.

### 57. [구독 서비스 이탈 요인 분석](/practice/57_sub_churn/)
구독형 멤버십 서비스 가입 고객들의 신체 활동 요약과 해지 로그 데이터셋입니다. 전체 고객 대비 이번 달 해지(Yes) 비율을 카운트 차트로 점검하고, 고객의 가입 기간과 주간 센터 이용 빈도가 이탈 해지 여부와 갖는 통계적 관계를 오버레이 산점도로 분석합니다.

### 58. [중고차 가격 감가 요인 분석](/practice/58_car_price/)
다양한 연료 타입과 기계적 제원을 지닌 중고차 거래 매물 정보입니다. 가솔린, 디젤, 하이브리드, 전기차 등 연료 형태별 평균 시세를 상자 그림으로 대조하고, 차량의 누적 주행거리(Mileage)의 증가가 가격 하락에 기여하는 감가상각 궤적을 산점도로 추적합니다.

### 59. [항공 지연 및 관제 운영 분석](/practice/59_flight_delays/)
국내선 공항의 항공편 운항 관제 로그 데이터셋입니다. 각 항공사의 정시성 효율 격차를 평균 지연 막대 그래프로 한 눈에 비교하고, 운항 예정 시각(Scheduled Time)의 흐름과 기상 악화(Weather Severity) 강도가 최종 연계 지연 분수(Delay Minutes)에 미치는 누적 효과를 분석합니다.

### 60. [운동 트래커 칼로리 소모 분석](/practice/60_fitness_tracker/)
스마트 피트니스 트래커가 측정한 운동 세션 로그 데이터셋입니다. 러닝, 수영, 사이클, 요가, 웨이트 등 각 종목별 평균 심박수(Avg Heart Rate)의 부하 분포를 상자 그림으로 비교 대조하고, 실제 운동 시간(Duration)의 증가에 따른 칼로리 소모량의 상관성을 종목별 선형 기울기로 시각화합니다.

### 61. [심장 질환 위험 인자 분석](/practice/61_heart_disease_risk/)
심장 질환 환자들의 임상 기록 데이터셋입니다. 환자들의 나이, 성별, 콜레스테롤 수치, 혈압 등이 최종 심장 질환 발생 여부(Target)에 어떻게 기여하는지 분석하고, 위험군과 일반군 간의 건강 지표 분포 차이를 시각화합니다.

### 62. [학생 공부 시간과 성적 상관성 분석](/practice/62_student_performance/)
학생들의 자기주도 학습 패턴 및 부모의 학업 관심도를 모은 학업 성취도 데이터셋입니다. 학생들의 공부 시간 분포를 파악하고, 학습 투입량과 성적(FinalGrade) 간의 인과적 트렌드를 부모 지원(ParentalSupport) 환경별로 다각도 분산 분석합니다.

### 63. [호텔 예약 취소 및 노쇼 분석](/practice/63_hotel_bookings/)
호텔 예약 트랜잭션 기록 데이터셋입니다. 예약 선행일(Lead Time)과 예약 채널, 보증금 조건(DepositType)을 바탕으로 실제 노쇼 및 취소(IsCanceled)가 빈번히 터지는 조건을 교차 빈도로 추적합니다.

### 64. [웹 트래픽 및 구매 전환율 분석](/practice/64_web_conversion/)
이커머스 쇼핑몰의 세션 로그 데이터셋입니다. 사용자의 세션 체류 시간(SessionDuration) 분포와 이탈률, 페이지 뷰가 최종 상품 구매 전환(Converted)에 미치는 기여 효과를 규명합니다.

### 65. [온라인 강좌 만족도 및 추천 분석](/practice/65_course_reviews/)
온라인 강의 플랫폼의 수강평 및 강의 만족 피드백 로그입니다. 수강생들의 만족도 별점 분포를 요약하고, 강의 추천 여부(Recommend)에 따라 남긴 후기의 본문 텍스트 단어수 편차를 상자그림으로 규명합니다.

### 66. [도심 범죄율 요인 분석](/practice/66_city_crimes/)
도심 치안 센터의 순찰관 배치 수와 인구 밀도 대비 지구별 범죄 수준 지수(CrimeRateIndex) 분석용 데이터셋입니다. 순찰 인력의 배치가 실제 거동 예방과 상관관계가 있는지 분석합니다.

### 67. [사내 교육 연수 효율성 분석](/practice/67_hr_training/)
임직원의 사내 직무 역량 강화 교육 연수 이력 데이터셋입니다. 교육 투입 시간과 교육 전후의 역량 평가 점수 도약, 그리고 최종 인사고과(PerformanceRating) 간의 시너지 관계를 규명합니다.

### 68. [부동산 월세 임대 시세 분석](/practice/68_rental_prices/)
주택 월세 임대 정보 데이터셋입니다. 방 개수(Bedrooms), 면적(SquareFootage), 도심 접근성(CityDistance_KM)이 최종 월 임대료(RentalPrice) 가격 형성에 미치는 영향력과 반려동물(PetFriendly) 혜택의 프리미엄을 다각도로 요약합니다.

### 69. [매장 유입도 및 일 매출 상관분석](/practice/69_store_traffic/)
오프라인 대형 리테일 샵의 일일 방문자 유입 및 매출 기록 데이터셋입니다. 당일 기상 조건(Weather)과 파격 세일 행사 여부(DiscountEvent)가 방문객 볼륨 및 최종 일 매출에 미치는 효과를 시각화합니다.

### 70. [신용 평가 및 연체 예측 분석](/practice/70_credit_scores/)
금융 대출 가입자들의 신용 기록 데이터셋입니다. 신청자의 개인 신용 평가 점수 분포를 진단하고, 총부채 상환 부담율(DTI)의 증가가 실제 대출금 부도 연체 이력(DefaultHistory)으로 번지는 통계 경계를 상자그림으로 도출합니다.

### 71. [전기차 배터리 효율 분석](/practice/71_ev_battery/)
전기차 주행 구동 테스트 로그입니다. 배터리 팩 용량, 구동 속도, 외기 온도 및 공조 히터/에어컨 가동 조건이 실 주행 마일리지(Range_km)에 미치는 효율성 하락 폭을 분석합니다.

### 72. [배달 배송 물류 시간 분석](/practice/72_delivery_logistics/)
배달 대행 플랫폼의 주문 물류 로그입니다. 상점 조리 소요시간 및 고객지까지의 편도 이동 거리가 라이더 총 배송시간(DeliveryTime_Mins)과 만족도 별점(Rating)에 주는 임계치 여파를 분석합니다.

### 73. [건축물 에너지 소비량 요인 분석](/practice/73_energy_consumption/)
도심 오피스, 아파트, 공장 등의 전기 사용량 및 에너지 제원 기록입니다. 건물의 평면 면적 크기, 냉난방 공조 연한(HVAC_Age)이 실제 연간 전력 소비 효율(EnergyConsumption_kWh)과 품질 등급에 미치는 시너지 효과를 분석합니다.

### 74. [매장 재고 손실 및 도난 방지 분석](/practice/74_inventory_shrinkage/)
대형 소매 유통 마트의 연간 재고 실사 기록 데이터셋입니다. 각 매장 코너별 적재된 재고량 대비 실제 분실, 훼손, 도난으로 분류된 손실 수량(LostUnits)을 파악하고 물리 보안 수준(SecurityLevel)의 실질 예방력을 검증합니다.

### 75. [스트리밍 플랫폼 이탈 요인 분석](/practice/75_stream_activity/)
온라인 스트리밍 플랫폼 가입자의 구독 패턴 데이터셋입니다. 매주 플랫폼에서 동영상을 시청한 시간(HoursWatched_Weekly) 및 가입 플랜 유형에 따라 가입자가 구독 해지(Churned) 탈퇴로 귀결되는 확률을 다변수로 추적합니다.

### 76. [커피전문점 단골 고객 브랜드 로열티](/practice/76_coffee_loyalty/)
대형 프랜차이즈 커피 전문점의 모바일 앱 회원 거래 데이터셋입니다. 단골 고객들의 월 방문 횟수, 선호 음료 및 1회 결제액(AvgSpend)이 주관적인 모바일 로열티 만족 등급(LoyaltyScore)에 미치는 시너지 효과를 분석합니다.

### 77. [채용 정보 연봉 수준 예측](/practice/77_job_salaries/)
채용 사이트의 구인 포스팅 원본 정보입니다. 신규 채용 직원의 연차 경력(ExpYears) 요구조건 및 직무 분류(RoleCategory)에 따라 책정된 제안 연봉(Salary)의 편차를 재택근무(IsRemote) 조건별로 대조 분석합니다.

### 78. [지구 대기 이산화탄소와 온난화 분석](/practice/78_co2_temp/)
환경 과학 대기 관측 데이터셋입니다. 연도별 대기 중 이산화탄소 농도와 석탄 에너지 소비량 변동이 전 지구 온도 아노말리(Temp_Anomaly) 및 해양 열량 지수에 미치는 기후 인과 지도를 규명합니다.

### 79. [모바일 게임 플레이 몰입도 분석](/practice/79_gaming_sessions/)
모바일 캐주얼/아케이드 게임 가입자의 접속 세션 로그 데이터셋입니다. 사용자의 게임 플레이 시간, 게임 모드 분류가 실제 인앱 결제 매출(IAP_Amount) 및 광고 시청 만족도에 미치는 기여를 규명합니다.

### 80. [현대인 정신 건강 및 스트레스](/practice/80_mental_health/)
직장인 스트레스 자가 진단 설문 조사 결과입니다. 매주 일하는 직무 근무 시간(WorkHours_Weekly), 수면(SleepHours), 신체활동(ActivityMinutes) 및 명상 습관(MeditationPractice)이 주관적 스트레스 수치(StressLevel_Index)에 미치는 통계 격차를 판독합니다.

### 81. [사내 직원 업무 몰입도 분석](/practice/81_employee_engagement/)
사내 임직원들을 대상으로 수집한 업무 몰입도 설문 데이터셋입니다. 직원의 근속 연수, 소속 팀 규모, 업무 만족도 및 매니저 평점이 종합 업무 몰입도 점수(EngagementScore)에 미치는 기여 효과를 진단하고 시각화합니다.

### 82. [SaaS 요금제 및 제품 가격 정책 분석](/practice/82_product_pricing/)
기업용 SaaS(Software-as-a-Service) 제품의 요금제 가입 및 계약 데이터셋입니다. 사용 계정 수(UserSeats), 주요 기능 활용률(FeaturesUsed), 할인 조건이 최종 연간 계약 가치(ContractValue)에 미치는 영향을 판정하고 시각화합니다.

### 83. [종합병원 진료 부서별 환자 대기 시간 분석](/practice/83_patient_waiting/)
종합병원 응급 및 외래 진료소의 실시간 환자 대기 이력 데이터셋입니다. 각 진료 부서(Department)와 대기 시간(WaitTime_Mins), 당직 의사 유무가 환자의 주관적 서비스 만족도 평점(SatisfactionRating)에 어떤 한계 하강 작용을 하는지 분석하고 시각화합니다.

### 84. [부동산 리모델링 공사 비용 및 ROI 분석](/practice/84_house_remodel/)
주택 리모델링 공사 매뉴얼 및 비용 산출 데이터셋입니다. 욕실, 주방, 외관 리모델링 등 공사 유형(RemodelType)과 투입된 자재 비용(MaterialsCost), 인력 공수(LaborHours)가 자산 시장에서의 최종 가치 회수율(ROI_Percent)에 미치는 통계 상관성을 탐색합니다.

### 85. [고객 센터 문의 처리 속도 및 만족도 분석](/practice/85_customer_support/)
고객 지원 헬프 데스크의 실시간 티켓 상담 로그 데이터셋입니다. 반품, 환불, 로그인 장애 등 티켓 유형(TicketType)과 상담 채널(Channel), 상담사 연차(AgentExp_Months)가 최종 해결 소요 시간(ResolutionTime_Hours) 및 고객 만족 점수(CSAT_Score)에 미치는 기여를 규명합니다.

### 86. [항공사 우수 고객 등급 및 이탈 분석](/practice/86_airline_loyalty/)
항공사의 Frequent Flyer 우수 마일리지 회원 데이터셋입니다. 회원의 가입 등급(MembershipClass)별 연간 탑승 비행 횟수(YearlyFlights), 누적 마일리지 포인트(PointsAccumulated), 마일리지 소진율(RedemptionRate)이 최종 해지 및 이탈 여부(Churned)에 미치는 기여 상관성을 추적합니다.

### 87. [건강 보험 납입료 결정 요인 분석](/practice/87_insurance_premiums/)
생명 및 건강 보험 가입자의 임상 계약 데이터셋입니다. 가입자의 나이, 흡연 상태(SmokerStatus), 부양가족 수, 체질량 지수(BMI)가 최종 산출되는 연간 총 보험료(AnnualPremium)에 미치는 가격 책정 영향력을 판독하고 시각화합니다.

### 88. [태양광 발전소 발전 효율 및 기후 분석](/practice/88_solar_energy/)
신재생 에너지 태양광 발전소의 일일 기상 및 전력 생산 기록 데이터셋입니다. 대기 일사량(SolarRadiation), 발전 패널의 표면 온도(PanelTemp), 구름량 등 자연환경 요인이 일일 최종 전력 생산량(DailyPower_kWh)에 미치는 효율 시너지를 시각화하고 진단합니다.

### 89. [스마트 그리드 정전 지속 시간 분석](/practice/89_electric_grid/)
도시 스마트 그리드(Smart Electric Grid) 전력망의 고장정비 송전 정전 이력 데이터셋입니다. 각 관리 섹터(GridSector)의 기상 악화(WeatherAnomalyIndex), 설비 점검 예방 주기(MaintenanceCycle_Months)가 실제 정전 복구 시간(OutageDuration_Hours) 및 피해 가구 수(CustomersAffected)에 미치는 위험 요인을 진단하고 시각화합니다.

### 90. [모바일 앱 신규 가입 유저 리텐션 분석](/practice/90_mobile_app_retention/)
신규 설치된 모바일 애플리케이션 유저들의 서비스 활동 로그 데이터셋입니다. 설치 유입 소스(InstallSource), 앱 내 핵심 경험인 온보딩 튜토리얼 완료 유무(OnboardingCompleted), 푸시 알림 활성화 여부가 최종 가입 7일 차 잔존 잔류(Day7_Retained)율에 미치는 활성화 가치를 판독합니다.

### 91. [이동통신 기지국 통신 품질 및 Latency 분석](/practice/91_telecom_network/)
이동통신 기지국 장비들의 무선망 통신 모니터링 로그 데이터셋입니다. 무선 커버리지 신호 세기 감도(SignalStrength_dBm), 기지국 동시 접속 트래픽 부하(TrafficLoad_Percent), 패킷 유실률이 최종 스마트폰 무선 전송 반응 지연 속도(Latency_ms)에 미치는 병목 현상을 진단합니다.

### 92. [이러닝 영상 학습 집중도 및 완강률 분석](/practice/92_elearning_engagement/)
비대면 이러닝(E-Learning) 교육 동영상 플랫폼의 수강 학습 로그 데이터셋입니다. 강의 영상 분량(VideoDuration_Mins), 학습 중 일시 정지 멈춤 빈도(PauseCount), 학습 배속(SpeedMultiplier), 단원 평가 퀴즈 점수가 최종 이러닝 비디오 완강 비율(CompletionRate)에 미치는 시너지 효과를 분석하고 시각화합니다.

### 93. [은행 가계 대출 심사 승인 여부 분석](/practice/93_bank_loan_approval/)
시중 금융 은행의 가계 대출 신청 기록 데이터셋입니다. 대출 신청자의 월 소득(ApplicantIncome), 신용 평가 점수(CreditHistoryScore), 희망 대출 청구액(LoanAmount)과 공동 보증인 유무가 최종 은행 여신 심사 승인 여부(Approved)에 미치는 정책 기여도를 규명하고 가시화합니다.

### 94. [중고 가전 및 전자기기 리셀 가격 감가 분석](/practice/94_used_electronics/)
중고 정보통신 스마트폰 및 전자기기 거래 플랫폼의 리셀 거래 데이터셋입니다. 기기의 브랜드 제조사(Brand), 사용 개월 수(DeviceAge_Months), 기기 외관 검수 점수가 최종 책정 중고 시세(ResalePrice)에 미치는 가격 감가상각 추이를 탐색합니다.

### 95. [웹 사이트 로딩 속도 및 성능 분석](/practice/95_website_performance/)
글로벌 웹 애플리케이션의 웹 트래픽 리소스로더 로그 데이터셋입니다. 페이지 전송 용량(PageSize_MB), 동시 접속 요청 수(RequestCount), CDN 캐시 히트 상태(CacheStatus)가 최종 사용자의 모바일 렌더링 로딩 지연 속도(LoadTime_ms)에 미치는 병목 유발 인자를 분석하고 시각화합니다.

### 96. [호출 택시 매칭 및 수요 요금 분석](/practice/96_ride_hailing_demand/)
실시간 온디맨드 차량 호출(Ride-hailing) 서비스의 배차 트랜잭션 데이터셋입니다. 관할 행정구역(Neighborhood), 눈/비 등 기상 조건(WeatherCondition), 활동 라이더 공급 수(DriverSupply)가 실시간 호출 수요 강도 및 탄력 요금 가산율(SurgeMultiplier)에 미치는 기여 요인을 규명합니다.

### 97. [의류 커머스 반품 요인 및 환불 분석](/practice/97_retail_returns/)
패션 패션 리테일 쇼핑몰의 고객 구매 트랜잭션 및 반품/환불 이력 데이터셋입니다. 구매한 의류 카테고리(ProductCategory), 적용 할인 혜택, 사이즈 실측 일치 여부(SizeMatch), 온/오프라인 구매 채널이 최종 상품 환불 반품 여부(Returned)에 미치는 행동 패턴을 규명합니다.

### 98. [스마트 팜 토양 수분 및 농작물 수확량 분석](/practice/98_crop_yield/)
스마트 정밀 농업(AgTech) 실험 경작지의 일일 센서 수집 데이터셋입니다. 흙의 토양 수분량(SoilMoisture), 경작지에 투입한 영양 비료 유형(FertilizerType), 재배 온도(Temperature), 강수량(Rainfall_mm)이 최종 재배 농산물의 단위 면적당 수확 생산량(CropYield_kg)에 미치는 복합 조절 상관을 규명합니다.

### 99. [피트니스 클럽 회원 연장 및 Churn 이탈 분석](/practice/99_fitness_club_churn/)
스포츠 피트니스 헬스 클럽 회원의 결제 계약 유지 로그 데이터셋입니다. 회원의 월평균 헬스장 방문 빈도(MonthlyVisits), 가입 유지 기간(MembershipDuration_Months), 단체 요가/스피닝 수업 이수 여부(ClassParticipation)가 최종 회원권 만기 시 재등록 연장(Renewed)에 미치는 잔존 가치를 판독합니다.

### 100. [가계 금융 포트폴리오 자산 건전성 분석](/practice/100_personal_finance/)
가구 금융 조사 통계를 기반으로 한 개인 자산 관리 포트폴리오 데이터셋입니다. 가구의 월평균 고정 소득(MonthlyIncome), 저축율(SavingsRate), 주거 월세(HousingExpenses), 품위 유지 외식비(DiningExpenses)가 신용 종합 평가 금융 건전지수(FinancialHealthScore)에 미치는 기여 구조를 탐색하고 최종 시각화합니다.

### 101. [개인간 (P2P) 대출 연체 요인](/practice/101_p2p_loan_defaults/)
P2P 대출 가입자들의 신용 등급 및 상환 정보를 담은 데이터셋입니다. 신용 점수(CreditScore), 부채비율(DebtToIncome), 연간 소득(AnnualIncome) 등이 대출 연체 및 부도 여부(Defaulted)에 미치는 기여 상관성을 판독합니다.

### 102. [비트코인 등 가상자산 변동성](/practice/102_crypto_volatility/)
가상자산 시장의 가격 변동 및 투자자 심리 데이터를 분석합니다. 일일 수익률, 거래량(TradingVolume_M) 및 소셜 미디어 언급 지표(SocialMentions)를 기반으로 변동성(PriceVolatility)의 상관관계를 탐색합니다.

### 103. [주식 시장 소셜 미디어 감성 지수](/practice/103_stock_sentiment/)
금융 뉴스 및 소셜 미디어 여론 데이터셋입니다. 감성 극성 점수(PolarityScore)와 기관 투자자 비중(Institutional_Ratio)이 시장 영향 점수(MarketImpactScore)에 미치는 파급 효과를 분석합니다.

### 104. [은행 ATM 기기 현금 출금 수요 예측](/practice/104_atm_cash_demand/)
은행 ATM 지점들의 일일 운영 물류 데이터셋입니다. 거래 횟수, 주변 이벤트 및 휴일 지수가 특정 ATM의 일일 현금 출금 수요(DailyWithdrawal_K)와 잔액 소진 위험에 미치는 영향을 판독합니다.

### 105. [은행 지점 고객 대기 및 업무 시간](/practice/105_bank_branch_service/)
오프라인 은행 창구의 서비스 지표 데이터셋입니다. 근무 직원 수(StaffCount)와 방문 피크 시간대(PeakHours)가 고객의 실 대기 시간(WaitTime_Mins) 및 업무 만족도에 미치는 상관성을 규명합니다.

### 106. [마이크로파이낸스 소액 대출 상환성](/practice/106_microfinance_repayment/)
개발도상국 서민 금융 공동체 보증 소액 대출 데이터셋입니다. 대출 소모 그룹 규모(GroupSize)와 차입자의 주간 소득이 대출 최종 상환율 및 연체율(Defaulted)에 미치는 영향을 검증합니다.

### 107. [신용카드 이용 한도 최적화 모델](/practice/107_credit_limit_optimization/)
카드 가입자의 한도 소진율 및 리스크 최적화 데이터셋입니다. 월지출액(MonthlySpend_K)과 연체 횟수(DelinquencyCount)를 분석하여 최종 부도 시 손실(LossGivenDefault)을 관리하기 위한 이상적인 한도 가이드를 탐구합니다.

### 108. [자동차 사고 보험 청구 허위 사기 적발](/practice/108_car_insurance_fraud/)
손해보험사의 FDS(이상 거래 탐지)용 사고 청구 데이터셋입니다. 블랙박스 유무(DashcamExists), 사고 피해 규모(DamageScore) 및 청구액 대비 최종 사기 의심 건(IsFraud)을 판독하는 규칙을 도출합니다.

### 109. [스타트업 벤처캐피탈(VC) 투자 라운드](/practice/109_startup_funding/)
스타트업 투자 유치 및 성장성 지표 데이터셋입니다. 창업자의 실무 경력 연차(FounderExpYears), 보유 특허 수 및 투자 라운드가 최종 투자 유치금(FundingAmount_M)과 투자 회수 성공(ExitSuccess)에 주는 영향을 분석합니다.

### 110. [부동산 투자 신탁 (REITs) 배당 수익률](/practice/110_reits_dividend_yield/)
상업용 부동산 REITs 포트폴리오 데이터셋입니다. 평균 임대료 수준(AverageRent_K)과 자산 가치(AssetValue_M) 대비 공실률(VacancyRate_Percent)과 최종 배당 수익률(DividendYield_Percent)의 상관관계를 탐색합니다.

### 111. [B2B SaaS 고객 평생 가치 (CLV)](/practice/111_b2b_saas_clv/)
구독형 기업 소프트웨어 비즈니스의 리텐션 데이터셋입니다. 가입 계정 수(UserSeats)와 월 구독료(MonthlyFee), 추가 확장 매출(ExpansionRevenue)이 고객 생애 가치(CLV)에 기여하는 상관관계를 판독합니다.

### 112. [쇼핑몰 장바구니 결제 포기 요인](/practice/112_cart_abandonment/)
이커머스 장바구니 전환 퍼널 데이터셋입니다. 상품 개수(TotalItems)와 배송비 비율(ShippingCostRatio), 간편 결제 이용 유무(EasyPaymentUsed)가 결제 포기(CartAbandoned) 행동에 미치는 영향력을 진단합니다.

### 113. [하이브리드 협업 필터링 추천 시스템](/practice/113_recommendation_clicks/)
개인화 상품 추천의 매칭 점수 데이터셋입니다. 알고리즘 추천 적합도(MatchingScore), 상품 가격 수준 및 사용자 나이가 실제 추천 상품 클릭률(RecommendClicked)에 미치는 전환율을 분석합니다.

### 114. [디지털 마케팅 채널 기여도 (Attribution)](/practice/114_marketing_attribution/)
다채널 마케팅 기획 및 광고지출액(AdSpend_K) 효과 데이터셋입니다. 검색 노출, 소셜 미디어 유입, 직접 방문 채널들이 최종 신규 매출액(ConversionRevenue)에 기여하는 비중을 다중 회귀 분석합니다.

### 115. [시즌 의류 품목 가격 탄력성](/practice/115_retail_price_elasticity/)
리테일 의류 시세 및 주간 판매량 데이터셋입니다. 할인율(DiscountRate_Percent)과 경쟁사 가격(CompetitorPrice_K) 변동이 주간 판매 수량(SalesQty_Weekly)과 수요 탄력성에 미치는 민감도를 진단합니다.

### 116. [쇼핑몰 핫딜/선착순 재고 품절 시간](/practice/116_flash_sale_stockout/)
선착순 타임 세일 이벤트의 트래픽 데이터셋입니다. 이벤트 시작 시점의 실시간 활성 사용자 수(ActiveUsers)와 준비 수량(StockQty) 대비 품절 시간(StockoutTime_Secs)의 상관관계를 분석합니다.

### 117. [구매 상품 고객 리뷰 텍스트 토픽 모델링](/practice/117_customer_reviews_topics/)
고객 리뷰의 비정형 만족도 평가 데이터셋입니다. 텍스트 길이, 평점(RatingScore) 및 불만 지수(ComplaintScore)를 결합하여 환불 요청(RefundRequested)과의 선형 연계성을 탐색합니다.

### 118. [멤버십 포인트 적립 및 소진 행동](/practice/118_loyalty_points_redemption/)
충성 마케팅 포인트 락인 가치 회계 데이터셋입니다. 고객의 누적 적립 포인트(PointsAccumulated), 포인트 소진 주기(RedemptionIntervalMonths) 및 등급이 실제 포인트 소진(Redeemed)에 미치는 기여를 요약합니다.

### 119. [구독 박스 서비스 정기 배송 해지 진단](/practice/119_subscription_box_churn/)
정기 배송 구독 박스 가입자의 피드백 데이터셋입니다. 큐레이션 만족도(FeedbackRating), 맞춤 설정 적용 유무(BoxCustomizations) 및 배송 지연 횟수가 최종 이탈률(Churned)에 주는 부정적 여파를 분석합니다.

### 120. [해외 직구 물류 통관 대기 소요 시간](/practice/120_crossborder_shipping_delay/)
글로벌 직구 물류 세관 전수 검사 데이터셋입니다. 화물 무게(PackageWeight_Kg) 및 세관 신고 가액(DeclaredValue_USD)이 실제 통관 대기 일수(CustomsDelayDays)에 미치는 지체 인과성을 규명합니다.

### 121. [만성 당뇨 환자 병원 재입원 위험성](/practice/121_diabetes_readmission/)
당뇨 환자의 자가 건강 관리 및 퇴원 후 리스크 데이터셋입니다. 환자 연령, 당화혈색소 수치(HbA1c_Level) 및 복약 순응도가 병원 재입원(Readmitted) 여부에 미치는 영향을 분석합니다.

### 122. [수면 스마트 밴드 무호흡 로그 진단](/practice/122_sleep_apnea_tracker/)
스마트 기기가 계측한 수면 생체 로그 데이터셋입니다. 수면 시간(SleepHours), 산소 포화도 강하 빈도(OxygenDropEvents)가 수면 무호흡증 심각도 위험 수준(ApneaIndex)에 주는 기여 상관성을 규명합니다.

### 123. [웨어러블 심박 변동성 (HRV)과 스트레스](/practice/123_hrv_stress_index/)
모바일 헬스케어 자율신경계 반응 데이터셋입니다. 심박 변동성(HRV_ms), 평균 맥박 및 일일 걸음 수가 스트레스 점수(StressScore) 및 수면 만족도에 미치는 수치를 대조 분석합니다.

### 124. [만성 질환 의약품 복용 순응도](/practice/124_drug_adherence/)
복약 지도 및 알람 기능 유효성 실증 데이터셋입니다. 복용 주기, 미복용 일수(MissedDays) 및 복약 알람 사용 여부에 따른 최종 의약품 복용 순응 수준(AdherenceLevel)을 비교 요약합니다.

### 125. [유전자 변이(SNP) 발현 및 질환 매핑](/practice/125_genomic_variants_disease/)
유전적 감수성과 환경 기저 요인의 상관관계 데이터셋입니다. 변이 대립유전자 수(MutatedAllelesCount)와 유전자 발현량(GeneExpressionLevel)이 질환 발병 시기(DiseaseOnset)에 미치는 영향을 탐구합니다.

### 126. [의료 영상 인공지능 오탐 검진 판독](/practice/126_medical_ai_accuracy/)
의료 영상 AI 판독 진단 성능 평가 데이터셋입니다. AI의 신뢰 점수(ConfidenceScore_Percent), 병변 크기(LesionSize_mm) 및 의료진 합의도가 최종 확진율(DiagnosisConfirmed)에 주는 영향을 진단합니다.

### 127. [물리치료 재활 운동 관절 가동 범위](/practice/127_rehab_joint_rom/)
물리치료 재활 관절 각도 회복 데이터셋입니다. 주간 세션 수(WeeklySessions), 사전 통증 등급(PainScaleBefore) 및 물리치료사 연차가 관절 가동 각도(JointAngle_ROM)와 성공율에 주는 인과성을 분석합니다.

### 128. [칼로리 식단 기록 및 체지방 변동](/practice/128_diet_caloric_balance/)
식이 행동 및 기초 대사량 조절 데이터셋입니다. 일일 칼로리 적자(CalorieDeficit)와 영양소(탄수화물, 단백질) 섭취 비중이 최종 체중 변동량(WeightChange_Kg)에 미치는 통계적 상관을 요약합니다.

### 129. [헌혈 희망자 자격 검격 및 혈액 보존](/practice/129_blood_donor_supply/)
헌혈 대상자 자격 및 부적격 판정 요인 데이터셋입니다. 혈중 헤모글로빈 지수(Hemoglobin_Level), 수축기 혈압 및 과거 헌혈 유예 이력이 최종 헌혈 성공(DonationSuccess)에 미치는 영향을 판독합니다.

### 130. [치과 임플란트 시술 사후 염증 부작용](/practice/130_dental_implant_complications/)
기저 골조직 조건 대비 임플란트 장기 안착 성공률 데이터셋입니다. 골밀도 T점수(BoneDensity_TScore), 임플란트 길이 및 흡연 여부가 사후 염증 부작용과 골융합 성공율(OsseointegrationSuccess)에 주는 영향을 진단합니다.

### 131. [바이오 의약품 콜드체인 온도 모니터링](/practice/131_cold_chain_temp/)
저온 의약품 물류 운송 안전성 회귀성 데이터셋입니다. 외기 온도(AmbientTemp)와 냉각재 연한 대비 온도 임계 이탈 누적 시간(OutRangeTempDuration_Mins)이 약품 오염 위험에 미치는 요인을 분석합니다.

### 132. [택배 라스트마일 배송 경로 효율성](/practice/132_lastmile_route_efficiency/)
도심 택배 지연 보틀넥 분석 데이터셋입니다. 편도 배송 거리(DeliveryDistance_Km)와 교통 체증 지수(TrafficCongestionIndex)가 배송 시간 내 정시 도착(OnTimeDelivery)에 미치는 영향을 분석합니다.

### 133. [항만 컨테이너 부두 정박 적체 시간](/practice/133_port_container_congestion/)
해상 물류 컨테이너 선박 하역 대기 행렬 데이터셋입니다. 선박당 컨테이너 화물량(ContainerQty)과 크레인 가동 효율이 항만 정박 대기 시간(PortWaitTime_Hours)에 미치는 상관성을 분석합니다.

### 134. [물류창고 피킹 로봇 충돌 방지 및 경로](/practice/134_warehouse_robot_picking/)
물류 자동화 피킹 로봇의 자율 주행 경로 데이터셋입니다. 창고 장애물 밀도(ObstacleDensity_Percent) 및 총 이동 거리가 충돌 경보(CollisionAlerts)와 작업 완수율에 주는 기여를 분석합니다.

### 135. [법인 차량 전기차 연비 및 정비 주기](/practice/135_fleet_maintenance_ev/)
전기 승용 플릿 배터리 열화 및 충전 효율 데이터셋입니다. 일일 주행거리, 충전 속도(kW) 및 배터리 수명 잔존율(BatteryHealth_Percent)이 유지 보수 시급도(MaintenanceUrgency)에 미치는 영향력을 규명합니다.

### 136. [도시 지하철 출퇴근 시간대 혼잡도](/practice/136_subway_rushhour_congestion/)
출퇴근 전철 수용량 및 플랫폼 혼잡 지표 데이터셋입니다. 승차 승객 수(BoardingPassengerCount)와 열차 배차 간격이 차량 내 혼잡도 점수(CongestionScore)와 운행 지연에 미치는 연계를 추적합니다.

### 137. [전기 자전거 공유 배터리 방전 속도](/practice/137_ebike_battery_drain/)
공유 모빌리티 배터리 수명 및 전력 방출 데이터셋입니다. 주행로 경사도 비율(InclineRatio_Percent)과 탑승자 몸무게, 평균 시속이 배터리 소모율(BatteryDrainRate_Percent)과 방전 위험에 미치는 상관성을 분석합니다.

### 138. [항공 화물 수송 파손 손실 청구율](/practice/138_air_cargo_damage/)
특수 고가 화물 적재 및 항공 화물 클레임 데이터셋입니다. 화물 중량(WeightTon), 취급 주의 파손 라벨(FragileFlag) 및 습도 조건이 최종 화물 파손 청구액(DamageClaimAmount_K)에 미치는 요인을 요약합니다.

### 139. [허브 터미널 크로스도킹 처리 효율](/practice/139_crossdocking_throughput/)
물류 분류 터미널 크로스도킹 화물 처리 속도 데이터셋입니다. 입고 트럭 대수(InboundTrucks)와 배차 교대 근무자 수가 화물 환적 소요 시간(CrossDockTimeMinutes) 및 처리량에 미치는 영향을 분석합니다.

### 140. [물류 배송 드론 풍속 저항 및 비행 한계](/practice/140_drone_delivery_wind/)
배송 드론 페이로드 한계와 풍속 저항 데이터셋입니다. 드론 비행 시 풍속(WindSpeedKmh)과 적재물 무게가 잔여 비행 가능 거리(FlightRangeRemaining_Km) 및 미션 중단(MissionAborted)에 미치는 기여를 규명합니다.

### 141. [원격 근무 스트레스 및 성과 상관성](/practice/141_remotework_productivity/)
비대면 원격 근무 피로도와 업무 생산성 데이터셋입니다. 주간 화상 회의 시간(MeetingHours_Weekly), 재택 일수 및 주관적 스트레스 수치가 태스크 완료율(TaskCompletionRate_Percent)에 미치는 상관성을 분석합니다.

### 142. [채용 플랫폼 광고 전환율 및 우수 인재](/practice/142_hr_recruitment_channels/)
채용 채널 획득 비용(CAC) 대비 인력 리텐션 가치 데이터셋입니다. 채널 광고 비용, 이력서 스크리닝 및 면접 전형 등급이 입사자 최종 고용 여부(FinalHired)와 1년 유지율에 미치는 영향을 분석합니다.

### 143. [사내 직무 순환 및 부서 이동 승진 소요](/practice/143_internal_job_mobility/)
사내 인재 육성 직무 순환 경력 개발 데이터셋입니다. 직무 로테이션 횟수(JobRotationCount), 업무 평가 등급 및 멘토링 참가 시간이 최종 승진 연차(YearsSinceLastPromotion)에 미치는 기여를 분석합니다.

### 144. [프리랜서 마켓 매칭 속도 및 서비스 단가](/practice/144_freelancer_gig_matching/)
긱 이코노미 중개 플랫폼 매칭 대기행렬 데이터셋입니다. 프로젝트 예산(ProjectBudget_K)과 요구 기술 수 및 프리랜서 평점이 매칭 소요 시간(MatchingTimeHours)에 주는 기여 요인을 규명합니다.

### 145. [공유 오피스 회의실 이용 예약 부도율](/practice/145_coworking_noshow_rate/)
회의실 자원 예약 노쇼 및 공유 오피스 운영 데이터셋입니다. 회의실 수용 인원(RoomCapacity), 사전 예약일수 및 회원 유형이 실제 부도 및 예약 취소(NoShowed)로 귀결되는 확률을 진단합니다.

### 146. [멘토링 프로그램 참여 신입사원 조기 잔존](/practice/146_corporate_mentorship/)
신입사원 온보딩 멘토링 프로그램 효과 데이터셋입니다. 멘토링 시간, 멘토 피드백 등급(MentorFeedbackScore) 및 직무 만족도가 신입사원 1년 잔존율(OneYearRetention)에 주는 실질 예방력을 대조합니다.

### 147. [영업 조직 성과급 지급 체계 효율성](/practice/147_sales_quota_attainment/)
영업 인센티브 보상 설계 및 실적 데이터셋입니다. 영업 목표액(TargetAmount_K)과 기본급 비중이 최종 개인 목표 달성률(QuotaAttained_Percent) 및 성과급 지급액에 주는 영향을 탐구합니다.

### 148. [코딩 테스트 성적 대비 입사 사후 성과](/practice/148_coding_test_vs_performance/)
IT 신입 개발자 선발 평가 도구 타당성 데이터셋입니다. 입사 코딩 테스트 성적(CodingTestScore) 및 면접 전형 결과가 사후 버그 수정 건수, 코드 리뷰 만족도 및 최종 성과(PerformanceScore_1Year)에 미치는 예측 타당도를 분석합니다.

### 149. [공장 근로 안전 수칙 위반 및 사고 위험](/practice/149_workplace_safety_incidents/)
산업 안전 보건 교육의 아차사고 방지 인과 데이터셋입니다. 안전 교육 이수 시간(SafetyTrainingHours)과 장비 조작 시간이 위험 직면 아차사고 건수(NearMissCount) 및 실제 사고 발생(AccidentOccurred)에 주는 영향을 분석합니다.

### 150. [기업 복지 포인트 사용처와 직원 리텐션](/practice/150_wellness_program_satisfaction/)
사내 복지 혜택과 인재 잔류 상관성 데이터셋입니다. 웰니스 복지 포인트 지출 규모(WellnessSpend_K), 피트니스 이용 빈도 및 직무 스트레스 지수가 직원 1년 잔류 확률(OneYearStay)에 미치는 상관관계를 분석합니다.

### 151. [도시 소음 공해 데시벨 및 민원 빈도](/practice/151_urban_noise_pollution/)
스마트 도시 소음 환경 기준 예측 데이터셋입니다. 시간당 도로 차량 흐름량(TrafficVolumeHourly) 및 고속도로 인접 거리가 실외 소음 데시벨(NoiseDecibel)과 소음 민원 빈도에 미치는 상관성을 분석합니다.

### 152. [태양광 패널 먼지 오염에 따른 효율 하강](/practice/152_solar_panel_dust_efficiency/)
기후 청소 주기 최적화 태양광 발전 효율 데이터셋입니다. 강수 없는 가뭄 일수(DaysWithoutRain)와 패널 표면 먼지 점수가 최종 일일 전력 생산량(PowerOutput_kWh) 및 발전 효율 감소율에 미치는 영향을 진단합니다.

### 153. [해상 풍력 발전기 풍향 변동 및 발전량](/practice/153_wind_turbine_output/)
풍력 발전기 돌풍 상황 피로도 및 출력 데이터셋입니다. 평균 풍속(WindSpeed_mps) 및 풍향 편차(WindDirectionDeviation)가 발전기 기어 박스 온도와 일일 최종 전력 출력(DailyOutput_MWh)에 미치는 기여를 추적합니다.

### 154. [지능형 스마트 계량기 상수도 누수 진단](/practice/154_smart_water_leakage/)
상수도 원격 지능형 검침 이상 유량 탐지 데이터셋입니다. 일일 일반 물 소비량과 심야 미세 유량(MidnightFlowRate_Lh), 압력 급강하 횟수가 실제 누수 점수(LeakScore) 및 확정 누수(ConfirmedLeak)에 주는 여파를 분석합니다.

### 155. [기후 산불 위험 지수 요인 분석](/practice/155_wildfire_risk_indices/)
기상 건조 지수와 산불 발화 위험 요인 데이터셋입니다. 토양 수분 함량(SoilMoisture_Percent), 가뭄 무강수 일수(DryDaysCount) 및 풍속이 연료 수분 함량(FMC)과 최종 산불 발생 여부(WildfireOccurred)에 미치는 인과성을 분석합니다.

### 156. [전기차 충전소 충전 대기 유휴 시간](/practice/156_ev_charging_wait_times/)
전기차 인프라 혼잡 및 외부 기온 대기 상관 데이터셋입니다. 충전기 시간당 점유율(HourlyChargerOccupancy_Percent)과 외부 온도가 실제 전기차 대기 시간(WaitTimeMinutes)과 혼잡도 수준에 주는 영향을 분석합니다.

### 157. [지자체 생활 쓰레기 배출량 및 재활용](/practice/157_municipal_waste_recycling/)
도시 가구 유형 밀집도 대비 쓰레기 배출 데이터셋입니다. 행정동별 1인 가구 비율(SingleHouseholdRatio_Percent)과 일일 생활 쓰레기 배출량이 분리수거 재활용률(RecyclingRate_Percent) 및 벌금 부과에 미치는 요인을 실증 분석합니다.

### 158. [해수면 온도(SST) 상승 및 산호초 백화](/practice/158_sea_temp_coral_bleaching/)
해양 기후 위기 생물 다양성 산호 군집 생존 데이터셋입니다. 해수면 수온 아노말리 편차(SeaTempAnomaly) 및 해양 산성도(pH) 지표가 산호 백화 비율(CoralBleachingRatio_Percent)과 치명적 폐사(SevereBleaching)에 주는 영향을 분석합니다.

### 159. [도시 숲 가로수 캐노피 면적과 도심 열섬](/practice/159_urban_forest_heat_island/)
도심 녹지화 정책 대비 asphalt 복사열 완화 데이터셋입니다. 가로수 수관 그늘 피복 비율(TreeCanopyCoverage_Percent)과 지면 알베도 반사율이 도심 표면 온도(SurfaceTempCelsius) 및 열섬 심각도에 미치는 완화 기여도를 분석합니다.

### 160. [고속철도 주변 선로 소음 진동 계측](/practice/160_highspeed_rail_vibration/)
고속철 속도 대비 지반 구조 안전성 계측 데이터셋입니다. 열차 운행 시속(TrainSpeedKmh) 및 선로 이격 거리가 진동 센서 측정 데시벨(VibrationDecibel)과 주파수 성분, 구조 안전 등급에 미치는 인과를 분석합니다.

### 161. [온라인 게임 매칭 공정성 지표 진단](/practice/161_game_matchmaking_fairness/)
멀티플레이어 대전 게임 MMR 밸런싱 데이터셋입니다. 대결 양 팀의 실력 지표 격차(MMR_Difference)와 통신 Latency 속도가 최종 게임 매칭 공정성 점수(FairnessScore) 및 중도 이탈률에 미치는 영향을 분석합니다.

### 162. [팟캐스트 오디오 시청 청취 중도 이탈](/practice/162_podcast_listener_dropoff/)
디지털 오디오 에피소드 청취 몰입도 분석 데이터셋입니다. 전체 오디오 녹음 분량(AudioLengthMinutes)과 삽입 광고 개수, 화자의 톤 스피치 주파수가 최종 독자 중도 이탈 시간(DropoffTimeMinutes)에 주는 영향을 추적합니다.

### 163. [인플루언서 피드 도달율 및 광고 반응](/practice/163_influencer_post_engagement/)
소셜 마케팅 팔로워 대비 게시물 락인 데이터셋입니다. 팔로워 규모(FollowersCount_K), 사용 해시태그 수 및 스폰서 광고 적용 여부가 포스트 도달 지표인 인게이지먼트율(EngagementRate_Percent)과 북마크 수에 주는 기여를 분석합니다.

### 164. [뉴스 기사 낚시성 헤드라인과 독자 체류](/practice/164_news_clickbait_engagement/)
뉴스 기사 어휘 극성 지수와 광고 노출 데이터셋입니다. 뉴스 제목의 자극성 지수(SensationalismScore) 및 지면 광고 밀도가 독자의 실제 뉴스 화면 체류 시간(ReaderDwellTimeSeconds)과 낚시성 유무(IsClickbait)에 주는 영향을 규명합니다.

### 165. [음원 스트리밍 플레이리스트 추천 스킵](/practice/165_music_playlist_skips/)
추천 음원의 템포(TempoBPM), 기존 곡들과의 청각적 유사성(SimilarityScore_Percent) 및 청취 히스토리 중첩도가 유저의 추천곡 스킵 횟수(SkipCount)에 미치는 관계를 요약합니다.

### 166. [가상현실 (VR) 멀미 지수 및 플레이 한계](/practice/166_vr_simulator_sickness/)
VR 몰입형 장치 성능 안정성 대비 피로도 데이터셋입니다. 시야각(FOV_Degrees) 범위와 렌더링 프레임 드롭율(FrameDropRate_Percent)이 사용자의 가상현실 멀미 증상 점수(SicknessScore) 및 세션 중단 여부에 미치는 영향을 분석합니다.

### 167. [커뮤니티 악성 댓글 오토 필터링 분석](/practice/167_online_forum_moderation/)
커뮤니티 청정도 유지를 위한 기계학습 필터링 데이터셋입니다. 텍스트 글자 수와 댓글 내 악성 단어 지수(ToxicityScore_Percent)가 타 사용자들의 댓글 신고 횟수(ReportCount) 및 시스템의 자동 제재 처리에 주는 영향을 규명합니다.

### 168. [전자책 독서 속도 및 북마크 독서 중단](/practice/168_ebook_reading_retention/)
가독성 향상 전자책 독서 유지 흐름 데이터셋입니다. 페이지 단어 조밀도(PageDensityWords) 및 줄간 격차가 사용자의 분당 글 읽기 속도(ReadingSpeed_WPM), 북마크 설정 후 중단 지점(BookmarkDropChapter)에 미치는 영향을 분석합니다.

### 169. [스트리머 실시간 방송 채팅 트래픽 스파이크](/practice/169_livestream_chat_spikes/)
실시간 스트리밍 방송 인터랙션 폭주 데이터셋입니다. 동시 접속 시청자 수(ConcurrentViewers)와 네트워크 레이턴시가 분당 실시간 채팅 유입 빈도(ChatRatePerMinute) 및 서버 부하 지수에 미치는 병목을 추적합니다.

### 170. [앱 마켓 릴리즈 버전별 평점 분석](/practice/170_app_store_rating_version/)
신규 릴리즈 앱 크래시 폭증에 따른 평점 리스크 데이터셋입니다. 배포 버전 등급, 앱 비정상 종료 빈도(CrashCount) 및 피드백 텍스트 길이가 최종 마켓 별점 만족 점수(RatingScore)와 부정적 리뷰 플래그에 주는 영향을 요약합니다.

### 171. [고교 학업 중도 탈락 위험 징후 진단](/practice/171_student_dropout_risk/)
학업 중단 선행 징후 통계 예방 데이터셋입니다. 무단결석 일수(AbsenceDays), 중간고사 종합 성적 및 학교 상담 횟수가 학부모 관여도(ParentEngagementScore) 수준별 학업 중도 탈락(DroppedOut)에 미치는 기여를 분석합니다.

### 172. [외국어 학습 어플 일일 스트릭과 암기력](/practice/172_language_app_retention/)
에빙하우스 망각곡선 주기 학습 능률 데이터셋입니다. 일일 연속 공부 스트릭 일수(DailyStreakDays), 학습 간격 시간(PracticeIntervalHours)이 단어 테스트 점수(QuizScore_Percent) 및 활성 잔존 여부에 주는 상관을 분석합니다.

### 173. [대학 장학금 지원 예산 분배 효율성](/practice/173_scholarship_gpa_progress/)
장학금 지원 규모가 학업 성과 성장에 미치는 기여 데이터셋입니다. 장학금 수혜 예산 규모(ScholarshipAmount_K)와 주당 학습 시간이 학생의 직전 학기 평점 대비 사후 평점(PostGPA) 성장에 미치는 효율 기여도를 분석합니다.

### 174. [부트캠프 수료생 구직 소요 시간 및 초임](/practice/174_bootcamp_job_placement/)
IT 직무 전환 교육의 취업 예측 변수 데이터셋입니다. 포트폴리오 프로젝트 제작 수, 코딩 테스트 전형 성적이 수료 후 정규직 취업 소요 일수(JobSearchDurationDays) 및 신입 초봉 금액에 미치는 요인을 요약합니다.

### 175. [모의평가(SAT/ACT) 수강 시간과 성적](/practice/175_test_prep_score_increase/)
자기주도 오답 학습의 성적 향상 시너지 데이터셋입니다. 모의고사 온라인 강의 시청 시간(LectureHoursWatched)과 자율 오답노트 정리 수(IncorrectNotesCreated)가 최종 모의평가 성적(FinalMockScore) 도약에 주는 시너지를 분석합니다.

### 176. [디지털 교과서 뷰어 인터랙션 로그](/practice/176_digital_textbook_interactions/)
스마트 학습 도구 상호작용 행동 성과 데이터셋입니다. 페이지별 형광펜 하이라이트(HighlightCount), 수기 메모 횟수 및 평균 페이지 체류 시간(PageDwellTimeAvg_Secs)이 학기 최종 시험 성적에 미치는 기여를 규명합니다.

### 177. [교사 소진율 및 공교육 교실 이탈 진단](/practice/177_teacher_burnout_turnover/)
교사 직무 스트레스와 행정 업무 부담 상관 데이터셋입니다. 주당 초과 근무 시간(WeeklyOvertimeHours), 담당 교실 학급 학생 수 및 행정 만족도가 교사 번아웃 지표(BurnoutIndex)와 퇴직 이탈 위기에 주는 영향을 분석합니다.

### 178. [과학 실험 보고서 서술형 정밀 평가](/practice/178_science_report_grades/)
보고서 구성 완결성 대비 최종 취득 학점 데이터셋입니다. 실험 보고서 내 삽입 수식 수(FormulaCount), 참고문헌 인용 수 및 텍스트 표질 비율(PlagiarismRatio_Percent)이 최종 레포트 성적(ReportGrade)에 주는 가중 효과를 분석합니다.

### 179. [온라인 튜터 매칭 만족도 및 재수강률](/practice/179_tutor_matching_success/)
개인 과외 중개 서비스 재구독 전환 데이터셋입니다. 배정 튜터의 교육 경력(TutorExpYears), 시간당 수업료 및 학생 만족 점수가 정규 강의 이수 횟수(LessonsCompleted)와 멤버십 재등록에 미치는 상관을 분석합니다.

### 180. [비대면 원격 화상 강의 시선집중 로그](/practice/180_classroom_eye_tracking/)
비대면 카메라 학습 태깅 수치와 학업 성취 데이터셋입니다. 화상 회의 화면 시선 이탈 비율(EyeGazeOutRatio_Percent), 집중 끄덕임 횟수(NodCount)가 단원 퀴즈 성적(QuizGrade) 및 통과 여부에 미치는 영향을 분석합니다.

### 181. [공장 선반 장비 예지정비 마모 진단](/practice/181_cnc_tool_wear/)
CNC 절삭날 고장 예방 마모도 예측 데이터셋입니다. 절삭 장비 모터 전류(SpindleCurrent) 및 진동 센서 값(VibrationRMS)의 복합 주파수가 날 마모 두께(WearDepth_microns)와 예비 정비 필요 여부에 주는 영향을 진단합니다.

### 182. [아파트 도시가스 동절기 난방 최적화](/practice/182_residential_gas_heating/)
동절기 세대 난방 소비 효율 및 단열 성능 데이터셋입니다. 최저 외부 기온(LowestTempCelsius), 아파트 건물 건축 연한 및 세대 설정 온도가 일일 도시가스 난방 소비량(GasConsumption_M3)에 미치는 영향력을 분석합니다.

### 183. [스마트 홈 실내 온도 조절기 제어 효율](/practice/183_smart_thermostat_control/)
지능형 홈 에너지 디바이스 제어 인자 데이터셋입니다. 에너지 절약 에코 모드 적용 시간(EcoModeDurationHours)과 외부 습도가 최종 전력 절감 비율(PowerSaved_Percent) 및 시스템 제어 효율 등급에 미치는 인과를 분석합니다.

### 184. [수력 발전소 유입수와 수위 제어](/practice/184_dam_inflow_power/)
하천 유입량 및 저수 수위에 따른 수력 발전 데이터셋입니다. 댐 유입 유량 속도, 저수지 만수위 높이(ReservoirLevel_Meters)가 발전 터빈 가동 효율 및 실제 생산 전력량(PowerGenerated_MWh)에 미치는 수자원 역학을 분석합니다.

### 185. [조립 라인 로봇 용접 품질 불량율 예측](/practice/185_welding_defect_detection/)
자동 조립 제조 라인 비파괴 초음파 오접합 탐지 데이터셋입니다. 용접 가열 온도, 냉각 속도 및 로봇 이동 속도가 비파괴 결함 탐지 강도(UltrasonicDefectScore)와 품질 불량 등급에 미치는 영향을 진단합니다.

### 186. [지열 열 교환 에너지 추출 성능 분석](/practice/186_geothermal_heat_recovery/)
지열 신재생 에너지 히트 펌프 열 회수율 데이터셋입니다. 지하 유입 유체 온도, 펌프 유체 유량 속도(FlowRate_Lps)가 최종 에너지 추출 성능(HeatExtracted_kW) 및 열효율 지표에 주는 기여 상관성을 규명합니다.

### 187. [근무조 교대 근무 패턴과 작업 실수 상관](/practice/187_workshift_errors_manufacturing/)
제조업 현장 교대 일정 배치와 품질 불량 오검수 데이터셋입니다. 주간 야간/심야 교대 횟수(WeeklyOvernightShifts), 라인 작업 조원 수 및 검수 정확도가 생산품 불량 발생 건수(DefectiveItemsProduced)에 미치는 영향을 분석합니다.

### 188. [대용량 ESS 배터리 충전 셀 온도 분산](/practice/188_battery_storage_thermal/)
배터리 랙 열 관리 시스템 냉각 속도 데이터셋입니다. 공기 순환 풍속(AirVelocity_mps) 및 충전 전류가 랙 내부 배터리 셀 최고 온도(CellMaxTempCelsius) 및 셀 온도 분산에 주는 열역학적 영향을 분석합니다.

### 189. [smart 가로등 디밍 통제 전력 절감량](/practice/189_smart_lighting_dimming/)
도시 공공 조명 에너지 절감 디밍 제어 데이터셋입니다. 시간당 도로 통행 차량 밀도(TrafficDensityHourly)와 가로등 조도 센서 값이 가로등 심야 디밍 비율 및 일일 총 전력 소비량(PowerConsumption_Wh)에 미치는 절감 효과를 요약합니다.

### 190. [화학 반응기 온도 임계점 경보 분석](/practice/190_chemical_reactor_safety/)
화학 제조 공정 폭주 반응 방지 안전 압력 온도 데이터셋입니다. 반응물 유입 유량, 반응기 압력(ReactorPressure_Bar) 및 아지테이터 회전 속도가 원자로 내부 반응 온도(ReactorTempCelsius) 폭증 경보에 주는 영향을 분석합니다.

### 191. [온실 토마토 줄기 두께 및 습도 제어](/practice/191_greenhouse_tomato_growth/)
정밀 시설 농업 VPD(수증기압포차) 생장 데이터셋입니다. 실내 습도, 토양 수분 공급량 및 증산 수증기압차(VPD_kPa)가 토마토 작물 줄기 발육 두께(StemDiameter_mm)와 생장 등급에 미치는 효율을 진단합니다.

### 192. [프로 축구 패스 전개 성공율 요인 진단](/practice/192_football_pass_accuracy/)
경기 공간 수비 압박 대비 패스 연결 확률 데이터셋입니다. 패스 타겟 수비수 인접 거리(DefenderDistance_Meters)와 패스 궤적 거리가 실 패스 전개 성공 비율(PassSuccess) 및 상대 압박 여부에 주는 영향을 분석합니다.

### 193. [와인 오크통 숙성 보관 가스 변동](/practice/193_wine_barrel_aging/)
숙성 창고 공기 환경 센서 기반 미세 산화 진단 데이터셋입니다. 오크통 주변 온도, 보관 습도 및 에탄올 센서 감도가 와인의 미세 아세트산(AceticAcid_ppm) 증가 및 오크통 숙성 등급에 미치는 관계를 요약합니다.

### 194. [스포츠 경기 티켓 동적 다이내믹 가격책정](/practice/194_sports_ticket_dynamic_pricing/)
스포츠 상대 전력 및 잔여석 대비 탄력 단가 데이터셋입니다. 상대 팀 리그 순위(OpponentRank) 및 경기 잔여 좌석 비중(RemainingSeatsRatio_Percent)이 최종 온라인 동적 티켓가(FinalTicketPrice_KRW) 형성에 미치는 요인을 규명합니다.

### 195. [커피 원두 로스팅 아티산 온도 프로파일](/practice/195_coffee_roasting_profiles/)
스페셜티 생두 가열 로스터기 ROR 온도 프로파일 데이터셋입니다. 로스터기 열풍 온도 상승률(RateOfRise_ROR) 및 투입 온도가 원두 수분 증발 구간(DevelopmentTimeRatio_Percent)과 프로 커핑 점수에 미치는 시너지를 분석합니다.

### 196. [드론 정밀 식생 지수(NDVI)와 수확량](/practice/196_drone_ndvi_crop_yield/)
드론 다중 스펙트럼 초분광 NDVI 카메라 수확 예측 데이터셋입니다. 경작지 일일 일조 시간과 드론 항공 촬영 NDVI 식생 지수 값(NDVI_Value)이 필지당 최종 농작물 수확량(CropYield_KgPerAcre)에 미치는 기여를 규명합니다.

### 197. [뷔페 레스토랑 미끼 메뉴별 잔반 음식 쓰레기](/practice/197_restaurant_food_waste/)
외식 프랜차이즈 고단가 메뉴 비중과 식재료 낭비 데이터셋입니다. 뷔페 테이블 이용 인원 및 육류 메뉴 제공 비율(MeatItemsRatio_Percent)이 식사 종료 후 남겨진 음식 쓰레기 무게(FoodWasteWeight_g)에 미치는 영향을 분석합니다.

### 198. [마라톤 페이스 오버페이스와 페이스 메이커](/practice/198_marathon_pace_bonking/)
마라톤 생리학적 에너지 고갈(Bonking) 리스크 데이터셋입니다. 하프 코스 통과 시간, 급수대 통과 수 및 기온이 레이스 후반부 페이스 저하율(PaceDropRatio_Percent)과 완주 탈진(Bonked)에 미치는 영향을 진단합니다.

### 199. [연안 어업 선박 출하량 및 어종 보존성](/practice/199_sustainable_fishery_catch/)
해수 수온 변동 대비 지속 가능 수산 자원 CPUE 데이터셋입니다. 조업 바다 수온, 출항 조업 시간 및 선박 규모가 단위 어획 노력당 어획량 지표(CPUE_Index)와 허용 쿼터량 초과 여부에 주는 관계를 분석합니다.

### 200. [피트니스 심박수 리커버리 시간과 체력](/practice/200_workout_heartrate_recovery/)
운동 부하 검사 1분 회복 심박 강하율과 체력 데이터셋입니다. 고강도 운동 시 피크 심박수(PeakHeartRate) 및 총 운동 시간이 운동 종료 60초 후 회복 심박 하강 수준(RecoveryHeartRate_60s)과 추정 VO2Max에 미치는 기여를 규명합니다.


---

## 🎯 학습 가이드 (어떻게 공부해야 하나요?)

1. **초급자:** 1번 `titanic`부터 10번 모듈까지 순서대로 진행하며 Pandas 코딩과 Seaborn 그래프 그리기에 익숙해집니다.
2. **중급자:** 21번 `wine`부터 시작하는 **Phase 3 (실전 CSV)** 파트를 집중적으로 공략하여, 실제 기업에서 다루는 실무 분석 워크플로우를 체화합니다.
3. **통계 집중:** 표의 맨 우측 열인 **'핵심 통계 개념'**이 굵은 글씨로 표시된 모듈(`tips`, `anscombe`, `car_crashes`, `housing`, `cancer`, `adult`)을 중점적으로 학습하세요. 수포자를 위한 친절한 비유와 수식이 포함되어 있습니다.
