import os
import re
import json

practice_dir = "/Users/hojin9/dev/jinysite/datas/src/practice"
folders = [d for d in os.listdir(practice_dir) if os.path.isdir(os.path.join(practice_dir, d)) and d not in ['midterm', 'final', 'wrapup']]

domain_guides = {
    "healthcare": {
        "title": "🏥 의료 및 헬스케어 (Healthcare & Medicine)",
        "intro": "헬스케어 데이터 분석은 환자의 생체 신호, 임상 수치, 치료 이력 등을 통해 의료 서비스의 질을 높이고 환자 예후를 개선하는 분야입니다.",
        "points": [
            "**의사결정 리스크**: 의료 분야의 예측 실패는 환자 생명과 직접 연결되므로 오탐지(False Positive/Negative) 비용 분석이 타격 기준보다 극도로 정밀해야 합니다.",
            "**복약 및 행동 데이터**: 약물 복용 주기(순응도)나 건강 로그 데이터는 환자의 자가 간호 리스크 및 치료 성공율을 계측하는 선행 지표입니다.",
            "**생리학적 수치 범위**: HbA1c(당화혈색소), BMI, 혈압 등의 수치는 의학적 정규 기준선이 있어 단순 통계 분포를 넘어 생리학적 이상 여부를 함께 판독합니다."
        ]
    },
    "finance": {
        "title": "💰 금융 및 핀테크 (Finance & FinTech)",
        "intro": "금융 데이터 분석은 자산의 리스크 관리(Credit Risk), 투자 자산 평가, 이상 금융 거래 감지(FDS) 등을 해결하기 위한 통계적 검정 분야입니다.",
        "points": [
            "**리스크와 대출 부도(Default)**: 대출 연체 여부나 투자 손실 위험은 금융 자산 건전성을 지키기 위해 고도화된 스코어링 모형으로 분석됩니다.",
            "**소득 대비 부채 비율(DTI)**: 개인이 갚을 수 있는 능력 한도를 객관적으로 판단하는 지표로 금융 신용 여신 관리의 핵심 척도입니다.",
            "**자산 변동성(Volatility)**: 주가나 크립토 시세의 표준편차는 위험 자산의 위험도를 계산(VaR)하고 투자 포트폴리오를 다변화하는 기준이 됩니다."
        ]
    },
    "retail": {
        "title": "🛍️ 이커머스 및 리테일 (E-commerce & Retail)",
        "intro": "이커머스와 리테일 분석은 고객의 라이프 사이클(CLV), 구매 전환 여정, 이탈(Churn) 방지 및 상품 가격 탄력성을 규명하여 매출 성장을 이끄는 분야입니다.",
        "points": [
            "**고객 평생 가치(CLV)**: 신규 유입 단가 대비 고객 한 명이 장기적으로 기여하는 누적 가치 분석을 통해 마케팅 효율성을 판정합니다.",
            "**장바구니 포기(Abandonment) 및 이탈**: 이탈 직전 행동 로그(예: 가격 비교 빈도, 핫딜 대기 시간) 분석으로 맞춤형 쿠폰 처방 타겟을 고릅니다.",
            "**가격 탄력성(Elasticity)**: 가격의 미세 조정에 따라 판매 수량이 민감하게 변화하는 통계 패턴을 파악하여 적정 할인율을 제안합니다."
        ]
    },
    "manufacturing": {
        "title": "⚙️ 제조 및 스마트팩토리 (Manufacturing & Smart Factory)",
        "intro": "제조 데이터 분석은 설비의 진동/압력 센서 로그를 통해 고장을 사전에 감지하고(예지 보전) 공정 품질 불량을 최소화하는 분야입니다.",
        "points": [
            "**예지 보전(Predictive Maintenance)**: 부품 마모율과 가동 로그의 한계를 통계적으로 진단하여, 불시의 가동 중단(Downtime) 손실을 차단합니다.",
            "**공정 불량(Defect) 상관성**: 온/습도 상태와 용접 등 기계 압력값을 매칭해 결함 원인이 되는 핵심 물리 피처를 규명합니다.",
            "**설비 수명 주기**: 장비 사용 누적 로그를 활용해 부품의 신뢰성 통계(Weibull 분포 등)를 구하고 최적의 설비 가용성을 확보합니다."
        ]
    },
    "logistics": {
        "title": "🚚 물류 및 공급망 (Logistics & Supply Chain)",
        "intro": "물류 및 배송 분석은 재고 입출고 회전율, 운송 지연 시간(Lead Time), 라스트마일 최적 경로 및 재고 손실 관리를 다루는 유통 핵심 분야입니다.",
        "points": [
            "**재고 실무 리스크(Shrinkage)**: 창고 관리에서 장부 재고와 실재고의 불일치(유실, 도난)를 진단하여 공급망 보안 비용을 진단합니다.",
            "**배송 리드타임 지연 분석**: 날씨, 도로 상태 등의 다변수가 최종 라스트마일 배송에 미치는 통계적 유효 지연 분 단위(p-value)를 분석합니다.",
            "**크로스도킹 및 정박 혼잡도**: 터미널 내 하역 적체 시간을 최소화하기 위해 운송 차량 유입 스파이크를 분산 배치하고 시간 병목을 완화합니다."
        ]
    },
    "energy": {
        "title": "🔋 친환경 에너지 및 환경 (Energy & Environment)",
        "intro": "재생 에너지 발전 성능 예측, 스마트 그리드 수요 관리, 탄소 배출량 모니터링 등 지속 가능한 환경 인프라를 위한 데이터 분석 분야입니다.",
        "points": [
            "**수요와 공급 매칭(Demand/Supply)**: ESS(에너지저장장치) 배터리 충전 셀 온도 편차와 전력 소비 피크 구간을 연계해 그리드 안전성을 모니터링합니다.",
            "**재생 에너지의 외생 변수 의존성**: 풍속, 일사량, 패널 먼지 오염도 등 환경 요인이 발전 효율 하락에 기여하는 회귀식을 추계합니다.",
            "**기후 위험 지수 진단**: 해수면 온도 변화나 산불 위험 요인 등 환경적 이상치를 공간 융합 통계 기법으로 분석합니다."
        ]
    },
    "education": {
        "title": "🎓 에듀테크 및 교육 (EdTech & Education)",
        "intro": "교육 데이터 분석은 온라인 학습 로그, 학생 성적 성취도, 중도 탈락 위험(Dropout)을 식별해 개인화된 성취 성장을 지원하는 분야입니다.",
        "points": [
            "**학업 중도 탈락(Dropout) 예측**: 학생의 마지막 접속 주기, 인터랙션 클릭 감소 성향 등을 조기 진단하여 보충 처방 학습을 유도합니다.",
            "**학습 몰입 지표(Engagement)**: 뷰어 응답 반응성, 동영상 스키핑 분석으로 주의 분산 한계 지점을 식별해 맞춤 교과 콘텐츠를 기획합니다.",
            "**장학 지원 성과 측정**: 지원금 예산 배분 대비 학점 상승 성취 효과(ROI)의 통계적 정성 분석을 통해 예산 효율성을 제고합니다."
        ]
    },
    "media": {
        "title": "🎬 미디어 및 스트리밍 (Media & Entertainment)",
        "intro": "미디어 및 엔터테인먼트 분석은 음원/영상 시청 패턴, 유저 이탈, 콘텐츠 피드 도달율을 극대화하기 위한 행동 정량화 분야입니다.",
        "points": [
            "**추천 알고리즘 스킵율**: 사용자가 재생 중 스킵 버튼을 누르는 순간의 음원 특징점을 포착하여 추천 취향 유사성 스코어를 보정합니다.",
            "**낚시성 콘텐츠 필터링**: 뉴스 헤드라인 키워드와 독자 실제 체류시간 분산을 상관하여 체리피커 유저 행태를 차단합니다.",
            "**앱 마켓 피드백(Rating)**: 릴리즈 버전 변경 전후의 마일스톤 별점 분포와 감성 감정을 융합 평가하여 조기 업데이트 버그를 디버깅합니다."
        ]
    },
    "transport": {
        "title": "🚗 교통 및 스마트 시티 (Transportation & Urban Engineering)",
        "intro": "스마트 시티 교통 인프라 혼잡도 예측, 차량 호출 요금 동적 최적화, 기하학적 사고 지점 진단을 수행하는 시계열 공간 통계 분야입니다.",
        "points": [
            "**혼잡도 병목(Congestion)**: 지하철 및 전기차 충전소 유입 대기 시간 통계를 분석하여 병목 해소를 위한 요일/시간 분산 정책을 고안합니다.",
            "**다이내믹 요금(Dynamic Pricing)**: 실시간 차량 호출 수요 대비 공급 상태를 계량하여 수요 유도를 위한 가격 탄력선 경계를 설정합니다.",
            "**진동 및 소음 계측**: 철도 주변 소음 진동 통계를 측정하여 시민 주거 영향 반경의 통계 유의 범위를 분석합니다."
        ]
    },
    "hr": {
        "title": "👥 인사 및 조직 문화 (HR & Workplace Analysis)",
        "intro": "인적 자원 관리(HR Analytics)는 핵심 인재의 이탈(Attrition) 방지, 사내 직무 이동 성과, 복지 리텐션을 다루는 과학적 기업 운영 분야입니다.",
        "points": [
            "**직원 자발적 퇴사(Attrition)**: 야근 빈도, 직무 몰입도(Engagement), 급여 대비 승진 연한 격차 등을 통해 조기 이탈 리스크 직원을 경보합니다.",
            "**채용 채널 성과 분석**: 직무 코딩테스트 및 전형 결과와 입사 사후 실제 성과 데이터 간의 타당성(상관) 관계를 실증 분석합니다.",
            "**원격 근무 효율성**: 원격/사무실 하이브리드 근무자의 생산성 점수와 근무 만족도 분산 차이를 통계 검증(T-test 등)합니다."
        ]
    },
    "agriculture": {
        "title": "🌾 농업 및 스마트팜 (Agriculture & Smart Farm)",
        "intro": "정밀 농업 및 스마트팜 분석은 생육 모니터링 센서와 토양 상태 데이터를 활용해 농업 수확량을 극대화하고 환경 자원을 보호하는 분야입니다.",
        "points": [
            "**수확량 예측 모델링**: 드론 촬영 NDVI(정밀 식생 지수), 온도, 토양 수분을 복합 분석하여 수확 예상 톤량을 예측합니다.",
            "**온실 생육 환경 최적화**: 토마토 줄기 두께 및 일일 온/습도 분산 범위를 결합해 기후 병충해 발현 경계 임계점을 제어합니다.",
            "**지속 가능한 자원 이용**: 어종 보존성 등 해양 어획 데이터 시각화로 한계 생태 가치를 유지하는 균형 조업선을 설정합니다."
        ]
    },
    "food": {
        "title": "🍽️ 식음료 및 식당 운영 (Food & Beverage)",
        "intro": "식음료 품질 보전, 매장 잔반(음식 쓰레기) 유발 원인 식별, 고객 평판 및 팁 분산 분석을 다루는 식음료 비즈니스 운영 분야입니다.",
        "points": [
            "**음식 쓰레기(Food Waste) 절감**: 뷔페 미끼 메뉴 배치 및 계절별 선호 식자재 데이터를 통해 낭비되는 식자재 손실 원가를 예측합니다.",
            "**와인 품질 및 보관 숙성**: 오크통 저장 보관 가스 농도 분석 등을 통하여 최적의 에이징 타이밍과 화학적 보전 임계치를 판별합니다.",
            "**고객 대접 서비스(Tips)**: 팁 액수와 테이블 체류 시간, 성별/그룹 변수를 군집하여 고효율 고객 서비스 패턴을 발굴합니다."
        ]
    },
    "sports": {
        "title": "🏃 스포츠 및 웰니스 (Sports & Wellness)",
        "intro": "개인용 웨어러블 건강 기기 로그, 신체 활성 신호 데이터, 스포츠 경기 기록을 분석하여 효율적 성장과 경기력을 측정하는 분야입니다.",
        "points": [
            "**운동 피트니스 리커버리**: 운동 직후 심박수 회복 시간과 개인 체력 점수를 매칭해 고강도 적합성 페이스를 수치 제안합니다.",
            "**부상 방지 스트레스 측정**: HRV(심박 변이도) 점수를 활용해 스트레스 수위를 탐색하고 오버트레이닝 부상 한계를 사전에 차단합니다.",
            "**기록 통계 분석**: 마라톤 오버페이스 메이커 분석, 축구 전술 패스 성공 유의 조건 등을 분석해 스포츠 성과를 극대화합니다."
        ]
    }
}

domain_keywords = {
    "healthcare": ["diabetes", "apnea", "drug", "genomic", "medical", "rehab", "donor", "dental", "cancer", "health_exp", "healthexp"],
    "finance": ["loan", "volatility", "sentiment", "atm", "branch", "credit", "fraud", "funding", "dividend", "personal_finance", "reits"],
    "retail": ["clv", "abandonment", "click", "attribution", "elasticity", "stockout", "churn", "segmentation", "sales", "ecommerce", "pricing", "return", "conversion", "orders", "reviews", "loyalty", "wine_reviews", "netflix", "spotify", "airbnb", "superstore"],
    "manufacturing": ["wear", "defect", "welding"],
    "logistics": ["shipping", "delivery", "shrinkage", "route", "congestion", "throughput", "cargo", "warehouse", "crossdocking", "port_container"],
    "energy": ["solar", "grid", "consumption", "temp", "geothermal", "thermal", "dimming", "power", "reactor", "turbine", "leakage", "wildfire", "recycling", "coral", "island", "noise", "dust", "co2"],
    "education": ["dropout", "app_retention", "scholarship", "placement", "prep", "interactions", "burnout", "grades", "tutor", "tracking", "course", "student"],
    "media": ["activity", "gaming", "moderation", "ebook", "spikes", "rating_version", "podcast", "influencer", "clickbait", "skips", "sickness", "youtube"],
    "transport": ["rushhour", "battery", "wind", "hailing", "traffic", "vibration", "rideshare", "taxis", "geyser", "crashes"],
    "hr": ["attrition", "training", "salaries", "engagement", "productivity", "recruitment", "mobility", "gig", "noshow", "mentorship", "quota", "performance", "incidents", "wellness"],
    "agriculture": ["yield", "tomato", "ndvi", "fishery"],
    "food": ["roasting", "waste", "food", "tips", "wine", "barrel"],
    "sports": ["accuracy", "pace", "recovery", "tracker", "exercise"]
}

def get_domain(folder_name):
    # Match keywords
    clean_name = folder_name.lower()
    for domain, keywords in domain_keywords.items():
        for kw in keywords:
            if kw in clean_name:
                return domain
    return "finance" # default fallback

def format_domain_guide(domain_info):
    guide = f"## 🧐 실무 도메인 지식 가이드 (Domain Knowledge Guide)\n\n"
    guide += f"> **{domain_info['title']}**\n"
    guide += f"> {domain_info['intro']}\n>\n"
    for pt in domain_info['points']:
        guide += f"> * {pt}\n"
    guide += "\n"
    return guide

def strip_existing_guide(content):
    # Check if there is an existing Domain Knowledge Guide section and strip it
    pattern = re.compile(r'## 🧐 실무 도메인 지식 가이드 \(Domain Knowledge Guide\).*?(?=## Step 1:)', re.DOTALL)
    if pattern.search(content):
        return pattern.sub('', content)
    return content

updated_count = 0
for folder in sorted(folders):
    idx_path = os.path.join(practice_dir, folder, "index.md")
    if not os.path.exists(idx_path):
        continue
        
    with open(idx_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    domain = get_domain(folder)
    domain_info = domain_guides[domain]
    
    # Clean up existing guide if any
    clean_content = strip_existing_guide(content)
    
    # Generate the new guide
    guide_section = format_domain_guide(domain_info)
    
    # Insert right before Step 1
    step1_pos = clean_content.find("## Step 1:")
    if step1_pos != -1:
        new_content = clean_content[:step1_pos] + guide_section + "---\n\n" + clean_content[step1_pos:]
        
        with open(idx_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added domain guide to: {folder} ({domain})")
        updated_count += 1
        
        # Regenerate practice.ipynb to keep in sync
        # Strip Jekyll front matter
        clean_md = new_content
        if clean_md.startswith('---'):
            parts = clean_md.split('---', 2)
            if len(parts) >= 3:
                clean_md = parts[2].strip()
                
        # Remove 실행 결과 blockquotes for the notebook
        lines = clean_md.split('\n')
        new_lines = []
        skipping = False
        for line in lines:
            if re.match(r'^\s*>\s*\*\*💻\s*\[실행\s*결과\]\*\*', line):
                skipping = True
                continue
            if skipping:
                if line.strip().startswith('>') or line.strip() == '':
                    continue
                else:
                    skipping = False
            new_lines.append(line)
        clean_md = '\n'.join(new_lines)
        
        cells = []
        pattern = re.compile(r'```python\n(.*?)\n```', re.DOTALL)
        last_end = 0
        for match in pattern.finditer(clean_md):
            md_part = clean_md[last_end:match.start()].strip()
            if md_part:
                cells.append({
                    "cell_type": "markdown",
                    "source": [line + '\n' for line in md_part.split('\n')]
                })
            
            code_part = match.group(1).strip()
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + '\n' for line in code_part.split('\n')]
            })
            last_end = match.end()
        
        tail_part = clean_md[last_end:].strip()
        if tail_part:
            cells.append({
                "cell_type": "markdown",
                "source": [line + '\n' for line in tail_part.split('\n')]
            })
        
        notebook = {
            "cells": cells,
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "name": "python"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 2
        }
        
        ipynb_path = os.path.join(practice_dir, folder, "practice.ipynb")
        with open(ipynb_path, "w", encoding="utf-8") as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"\nSuccessfully added domain guides and updated notebooks for {updated_count} practices.")
