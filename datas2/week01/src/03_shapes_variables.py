# 03_shapes_variables.py
import matplotlib.pyplot as plt

# 3. Python 문법 집중: 할당
size = 10
x_offset = 2
y_offset = 5

# 5. 동적 좌표 & 6. 산술 연산
# 오프셋을 기준으로 사각형 정의
# (0,0) -> (10,0) -> (10,10) -> (0,10) -> (0,0) + Offsets
x = [x_offset, x_offset + size, x_offset + size, x_offset, x_offset]
y = [y_offset, y_offset, y_offset + size, y_offset + size, y_offset]

# 10. 문자열 변수
graph_title = f"Square of size {size} at ({x_offset}, {y_offset})"

plt.figure(figsize=(5, 5))
plt.plot(x, y, label='Parametric Square')

# 19. 응용 예제: 스케일링 된 사각형
# 리스트 컴프리헨션을 사용하여 좌표 계산 (미리보기)
scale = 0.5
x2 = [i * scale for i in x] 
y2 = [i * scale for i in y]
plt.plot(x2, y2, label='Scaled Square', linestyle='--')

plt.title(graph_title)
plt.legend()
plt.grid(True)

# 원점을 보기 위해 축 범위 설정
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.show()

# 12. 타입 확인
print(f"Type of size: {type(size)}")
print(f"Type of graph_title: {type(graph_title)}")
