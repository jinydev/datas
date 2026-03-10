# 1. Map() 예제 (일괄 변경)
# 숫자 리스트를 문자열 리스트로 일괄 변경
numbers = [1, 2, 3, 4, 5]
str_numbers_map = list(map(str, numbers)) 
print("1. Map을 이용한 일괄 타입 변환:", str_numbers_map)

# 가격을 10% 인상하여 람다 함수 매핑
prices = [1000, 2500, 3000]
tax_prices = list(map(lambda x: int(x * 1.1), prices))
print("2. Map + Lambda를 이용한 일괄 가격 인상 (+10%):", tax_prices)

# 2. Filter() 예제 (조건 필터링)
raw_data = [1, -5, 10, 3, -2, 8]
# 조건: x가 0 이상(True)인 데이터만 살림
positives_filter = list(filter(lambda x: x > 0, raw_data))
print("3. Filter + Lambda 양수만 걸러내기:", positives_filter)

# 3. Map & Filter 콤보 활용 
dirty_sales_usd = [10, "error", 50, -20, 100, None]

# 1단계: 정수형이면서 0보다 큰 정상 데이터 찾기
clean_usd = list(filter(lambda x: isinstance(x, int) and x > 0, dirty_sales_usd))
print(f"4. 오염된 데이터 체인 1단계 (거름망): {clean_usd}")

# 2단계: 정상 데이터 1300배 환전 적용
krw_sales = list(map(lambda x: x * 1300, clean_usd))
print(f"5. 오염된 데이터 체인 2단계 (맵핑): {krw_sales}")
