# 1. split() 자르기
sentence = "Python is very powerful"
words = sentence.split()
print("1. 공백 기준 자르기:", words) # ['Python', 'is', 'very', 'powerful']

csv_data = "홍길동,25,seoul,010-1234-5678"
user_info = csv_data.split(",")
print("2. 쉼표 기준 자르기:", user_info) # ['홍길동', '25', 'seoul', '010-1234-5678']

# 2. join() 이어 붙이기
pieces = ["010", "1234", "5678"]
phone_number = "-".join(pieces)
print("3. 조각 이어 붙이기:", phone_number) # 010-1234-5678

# 3. strip() 양끝 공백 벗기기
dirty_text = "   \n\t  불가사리 \n  "
clean_text = dirty_text.strip()
print(f"4. 청소 전: '{dirty_text}', 청소 후: '{clean_text}'")

# 4. replace() 교체하기 (불순물 마스킹)
price = "$1,500"
clean_price = price.replace("$", "").replace(",", "")
print("5. 불순물 치환으로 정수 추출:", int(clean_price)) # 1500

# 5. 파이프라인 형태의 문자열 정제 (실무)
raw_data = "   \n [속보] 파이썬, 우주 정복... 가격은 $99,999 \n\n "
final_clean_data = raw_data.strip().replace("[속보] ", "").replace("$", "").replace(",", "")
print("6. 파이프라인 풀 체인 결과:", final_clean_data)

# 6. 정규표현식(Regex)을 이용한 전화번호 패턴 추출
import re
text = "제 연락처는 010-1234-5678 이고, 업무용 폰은 010-9876-5432입니다."
phone_pattern = r"\d{3}-\d{3,4}-\d{4}"

phones = re.findall(phone_pattern, text)
print("7. 정규표현식 패턴 모두 찾기:", phones)

masked_text = re.sub(phone_pattern, "***-****-****", text)
print("8. 개인정보 마스킹:", masked_text)
