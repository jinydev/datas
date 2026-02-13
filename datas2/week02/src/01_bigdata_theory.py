# 01_bigdata_theory.py
# 8. Python 문법 집중: 변수와 자료형

# 11. 정수형 (Integer)
user_count = 1500000 
print(f"사용자 수: {user_count} (타입: {type(user_count)})")

# 12. 실수형 (Float)
server_load = 55.4
print(f"서버 부하: {server_load}% (타입: {type(server_load)})")

# 13. 문자열 (String)
server_name = "Alpha-01"
print(f"서버 이름: {server_name} (타입: {type(server_name)})")

# 14. 불리언 (Boolean)
is_active = True
print(f"시스템 활성 상태: {is_active} (타입: {type(is_active)})")

# 17. 암시적 변환의 위험성
# 텍스트 파일에서 읽어온 상황을 가정
data_a = "100"
data_b = "200"

print("\n--- 암시적 변환 오류 ---")
result_bad = data_a + data_b
print(f"문자열 더하기 결과: {result_bad} (예상 밖의 결과!)")

# 16. 형 변환 (Type Casting)
result_good = int(data_a) + int(data_b)
print(f"형 변환 후 더하기: {result_good} (올바른 결과!)")

# 18. 응용 예제: 데이터 사이즈 추산
row_count = 5_000_000 # 500만 건 (가독성을 위한 언더바)
bytes_per_row = 256 # 바이트

total_bytes = row_count * bytes_per_row
total_mb = total_bytes / (1024 * 1024) # 메가바이트로 변환
total_gb = total_mb / 1024 # 기가바이트로 변환

print("\n--- 메모리 견적 ---")
print(f"총 데이터 건수: {row_count}")
print(f"예상 소요 메모리: {total_mb:.2f} MB ({total_gb:.4f} GB)")
