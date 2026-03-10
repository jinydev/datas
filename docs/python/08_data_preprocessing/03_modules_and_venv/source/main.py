# 이 파일은 사령부(Main) 파일입니다. 방금 만든 my_tools 모듈을 불러옵니다!
import my_tools

# 방어막(if __name__ == "__main__") 덕분에 
# my_tools 파일에 적혀있던 테스트용 print() 문장들이 여기서는 하나도 뜨지 않습니다!
print("🚀 중앙 통제소 (main.py) 가 실행되었습니다.")

# my_tools 모듈 안에 선언된 함수들을 꺼내 씁니다.
result_add = my_tools.add(100, 200)
print(f"내가 만든 모듈로 덧셈 계산: {result_add}")

dirty_sensor_data = [90, 85, -100, "error_code", 400, None]
clean_data = my_tools.clean_data(dirty_sensor_data)

print("전처리 전 데이터:", dirty_sensor_data)
print("커스텀 필터로 청소된 데이터:", clean_data)
