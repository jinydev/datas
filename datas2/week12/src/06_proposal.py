# 간단한 제안서 생성기
def create_proposal():
    print("=== 프로젝트 제안서 작성 도우미 ===")
    title = input("1. 프로젝트 제목: ")
    reason = input("2. 분석 이유(배경): ")
    source = input("3. 데이터 출처: ")
    
    print("\n" + "="*30)
    print(f"[프로젝트 제안서]")
    print(f"* 주제: {title}")
    print(f"* 배경: {reason}")
    print(f"* 출처: {source}")
    print("="*30)
    print("훌륭한 주제네요! 다음주부터 본격적으로 분석해봅시다.")

# 실행 (Colab에서는 input을 받을 수 있습니다)
# create_proposal() 

print("위 함수를 실행하면 인터랙티브하게 제안서를 작성할 수 있습니다.")
