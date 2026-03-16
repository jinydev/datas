const fs = require('fs');
const file_path = 'd:\\site\\jinydev\\datas\\src\\python\\01_basic\\07_math_module\\index.md';
let content = fs.readFileSync(file_path, 'utf-8');
const lines = content.split(/\\r?\\n/);

const idx_start = 53; // line 54
const idx_end = 84;   // line 85

const lines_before = lines.slice(0, idx_start).join('\\n');
const lines_after = lines.slice(idx_end + 1).join('\\n');

let new_content = "";
new_content += "### 제곱근(`sqrt`)과 강력한 거듭제곱(`pow`)\\n\\n";
new_content += "`math.sqrt()`(Square Root) 함수는 어떤 숫자의 제곱근(√)을 무조건 실수(`float`) 형태로 정확히 반환합니다. 파이썬 문법 자체에 거듭제곱(`**`) 기호가 이미 있지만, 전체적인 계산식의 형식을 수학적으로 일관성 있게 통일하기 위해 `math.pow(x, y)` 함수도 세트로 자주 쓰입니다.\\n\\n";
new_content += "**실전 응용: 피타고라스의 정리 (Pythagorean Theorem) 계산기**\\n";
new_content += "게임에서 캐릭터와 몬스터 사이의 대각선 거리를 구하거나, 통계 데이터의 유클리드 거리를 잴 때 가장 많이 쓰이는 기하학 공식입니다. 직각삼각형의 두 변의 길이(`A`, `B`)를 알고 있을 때, 빗변 대각선(`C`)의 길이를 $C = \\\\sqrt{A^2 + B^2}$ 수식을 통해 단숨에 구할 수 있습니다. \\n\\n";
new_content += "```python\\nimport math as m\\n\\n";
new_content += "side_a = 3\\nside_b = 4\\n\\n";
new_content += "# 피타고라스 정리 적용: 빗변 C = \u221A(a^2 + b^2)\\n";
new_content += "hypotenuse_c = m.sqrt(m.pow(side_a, 2) + m.pow(side_b, 2))\\n\\n";
new_content += "print(f\\\"가로 {side_a}, 세로 {side_b} 일 때, 대각선(빗변) 길이는 {hypotenuse_c} 입니다.\\\")\\n";
new_content += "```\\n\\n";
new_content += "### 천장, 바닥, 그리고 무자비한 절단 (올림/내림/버림)\\n\\n";
new_content += "수많은 소수점 데이터들을 통계적으로 단정하게 다듬기(Rounding) 위해 세 가지 함수를 사용합니다.\\n\\n";
new_content += "![수학의 올림, 내림, 버림 (Rounding Methods) 애니메이션](./img/math_rounding_anim.svg)\\n";
new_content += "*(다이어그램: 1. `ceil()`은 숫자를 엘리베이터 천장 층으로 강제로 끌어올립니다. 2. `floor()`는 숫자를 무거운 중력으로 바닥 층으로 끌어내립니다. 3. `trunc()`는 소수점 이하의 자잘한 숫자들을 칼로 무자비하게 단칼에 베어 버립니다.)*\\n\\n";
new_content += "1. **`math.ceil(x)` (올림)**: Ceiling(천장)의 약자로, 입력된 소수점 값보다 크거나 같은 **최소의 정수**(가장 가까운 위층)로 강제로 끌어올립니다.\\n";
new_content += "2. **`math.floor(x)` (내림)**: Floor(바닥)의 약자로, 입력된 값보다 작거나 같은 **최대 정수**(가장 가까운 아래층)로 무겁게 끌어내립니다.\\n";
new_content += "3. **`math.trunc(x)` (버림)**: Truncate(자르다)의 약자로, 향하는 방향(위/아래) 따위는 신경 쓰지 않고 무작정 소수점 부분을 날려버리고 정수 부분만 시원하게 취합니다.\\n\\n";
new_content += "```python\\nimport math as m\\n\\n";
new_content += "# 1. math.ceil (올림: 상승!)\\n";
new_content += "print(f\\\"3.1의 올림: {m.ceil(3.1)}\\\")    # 4\\n";
new_content += "print(f\\\"-3.7의 올림: {m.ceil(-3.7)}\\\")  # -3 \\n\\n";
new_content += "# 2. math.floor (내림: 하강!)\\n";
new_content += "print(f\\\"3.7의 내림: {m.floor(3.7)}\\\")   # 3\\n";
new_content += "print(f\\\"-3.1의 내림: {m.floor(-3.1)}\\\") # -4 \\n\\n";
new_content += "# 3. math.trunc (절사: 방향 무시 소수점 삭제)\\n";
new_content += "print(f\\\"3.999의 절사: {m.trunc(3.999)}\\\")    # 3\\n";
new_content += "print(f\\\"-3.999의 절사: {m.trunc(-3.999)}\\\")  # -3\\n";
new_content += "```";

const final_text = lines_before + '\\n' + new_content + '\\n' + lines_after;
fs.writeFileSync(file_path, final_text, 'utf-8');
console.log("Success!");
