const fs = require('fs');

const file_path = 'd:\\site\\jinydev\\datas\\src\\python\\01_basic\\07_math_module\\index.md';
let content = fs.readFileSync(file_path, 'utf-8');

// Section 1: 제곱근과 지수, 로그 함수
const targetRegex1 = /### 제곱근과 지수, 로그 함수[\s\S]*?print\(m\.sqrt\(4\)\)\n```/;

const newText1 = `### 제곱근(\`sqrt\`)과 강력한 거듭제곱(\`pow\`)

\`math.sqrt()\`(Square Root) 함수는 어떤 숫자의 제곱근(√)을 무조건 실수(\`float\`) 형태로 정확히 반환합니다. \`math.pow(x, y)\`는 \`x\`의 \`y\`승을 계산합니다. 파이썬 자체에 \`**\` 연산자가 있긴 하지만 통계나 과학 계산식의 흐름을 통일하기 위해 \`math.pow\`도 자주 사용됩니다.

**실전 응용: 피타고라스의 정리 (Pythagorean Theorem) 계산기**
게임 개발이나 데이터 거리 측정을 할 때, 직각삼각형의 두 변의 길이(\`A\`, \`B\`)를 알면 대각선 빗변(\`C\`)의 길이를 \`C = √(A² + B²)\` 공식을 통해 구할 수 있습니다. 

\`\`\`python
import math as m

# 직각삼각형의 두 변
side_a = 3
side_b = 4

# 피타고라스 정리 적용: C = √(a^2 + b^2)
hypotenuse_c = m.sqrt(m.pow(side_a, 2) + m.pow(side_b, 2))

print(f"변 A={side_a}, B={side_b} 일 때, 빗변 C의 길이는 {hypotenuse_c} 입니다.")
\`\`\``;


// Section 2: 천정과 바닥값, 내림 함수
const targetRegex2 = /### 천정과 바닥값, 내림 함수[\s\S]*?print\(m\.trunc\(3\.1415\)\)\n```/;

const newText2 = `### 천장, 바닥, 그리고 무자비한 절단 (올림/내림/버림)

수많은 소수점 데이터들을 통계적으로 단정하게 다듬기(Rounding) 위해 세 가지 함수를 사용합니다.

![수학의 올림, 내림, 버림 (Rounding Methods) 애니메이션](./img/math_rounding_anim.svg)
*(다이어그램: 1. \`ceil()\`은 숫자를 엘리베이터 천장 층으로 강제로 끌어올립니다. 2. \`floor()\`는 숫자를 무거운 중력으로 바닥 층으로 끌어내립니다. 3. \`trunc()\`는 소수점 이하의 자잘한 숫자들을 칼로 무자비하게 단칼에 베어 버립니다.)*

1.  **\`math.ceil(x)\` (올림)**: Ceiling(천장)의 약자로, 입력된 소수점 값보다 크거나 같은 **최소의 정수**(가장 가까운 위층)로 강제로 끌어올립니다. (예: 물건을 담기 위해 필요한 최소 박스 개수 계산 시 쓰입니다.)
2.  **\`math.floor(x)\` (내림)**: Floor(바닥)의 약자로, 입력된 값보다 작거나 같은 **최대 정수**(가장 가까운 아래층)로 무겁게 끌어내립니다. (예: 제한된 예산 안에서 구매 가능한 최대 아이템 개수 계산 시 쓰입니다.)
3.  **\`math.trunc(x)\` (버림)**: Truncate(자르다)의 약자로, 양수/음수 위아래층 방향 따위는 신경 쓰지 않고 소수점 자체를 그냥 날려버리고 정수 부분만 남깁니다.

\`\`\`python
import math as m

# 1. math.ceil (올림: 무조건 위로!)
print(f"3.1의 올림: {m.ceil(3.1)}")    # 4 (3과 4 사이에서 위층인 4로)
print(f"-3.7의 올림: {m.ceil(-3.7)}")  # -3 (-4와 -3 사이에서 위층인 -3으로)

# 2. math.floor (내림: 무조건 아래로!)
print(f"3.7의 내림: {m.floor(3.7)}")   # 3 (3과 4 사이에서 아래층인 3으로)
print(f"-3.1의 내림: {m.floor(-3.1)}") # -4 (-4와 -3 사이에서 아래층인 -4로)

# 3. math.trunc (절사: 방향 무시 소수점 삭제)
print(f"3.999의 절사: {m.trunc(3.999)}")    # 3
print(f"-3.999의 절사: {m.trunc(-3.999)}")  # -3 
\`\`\``;

if (targetRegex1.test(content) && targetRegex2.test(content)) {
    content = content.replace(targetRegex1, newText1);
    content = content.replace(targetRegex2, newText2);
    fs.writeFileSync(file_path, content, 'utf-8');
    console.log("Both Regex replaces successful via Node.js!");
} else {
    if (!targetRegex1.test(content)) console.log("Regex 1 not found");
    if (!targetRegex2.test(content)) console.log("Regex 2 not found");
}
