const fs = require('fs');
const file_path = 'd:\\site\\jinydev\\datas\\src\\python\\01_basic\\07_math_module\\index.md';
let content = fs.readFileSync(file_path, 'utf-8');

const target_line = "## math 모듈의 함수들";

const fullListMarkdown = \`
## math 모듈의 모든 내장 함수 한눈에 보기

\`math\` 모듈은 다음과 같이 용도별로 수십 가지의 강력한 수학 함수들을 빈틈없이 제공합니다. 파이썬 공식 문서를 보면 더 자세한 사용법을 확인할 수 있지만, 데이터 분석이나 기초 수식을 다룰 때는 아래의 표본 리스트만으로도 충분합니다.

### 1. 기본 산술 및 통계 함수 (숫자 다듬기)
| 함수명 | 설명 | 예시 |
| --- | --- | --- |
| \`ceil(x)\` | **올림**: 값을 크거나 같은 가장 작은 정수로 만듭니다. | \`math.ceil(3.2)\` $\\to$ \`4\`|
| \`floor(x)\` | **내림**: 값을 작거나 같은 가장 큰 정수로 만듭니다. | \`math.floor(3.7)\` $\\to$ \`3\`|
| \`trunc(x)\` | **버림(절사)**: 소수점 이하를 무조건 날려버립니다. | \`math.trunc(-3.7)\` $\\to$ \`-3\` |
| \`fabs(x)\` | 실수 형태의 **절댓값**을 반환합니다. (음수를 양수로) | \`math.fabs(-5.5)\` $\\to$ \`5.5\` |
| \`factorial(x)\` | **팩토리얼(계승)** \`x!\`을 계산합니다. (경우의 수) | \`math.factorial(5)\` $\\to$ \`120\`|
| \`gcd(a, b)\` | 두 수의 **최대공약수**를 구합니다. | \`math.gcd(12, 16)\` $\\to$ \`4\`|
| \`1cm(a, b)\` | 두 수의 **최소공배수**를 구합니다. (파이썬 3.9+) | \`math.lcm(4, 5)\` $\\to$ \`20\`|
| \`prod(iterable)\` | 리스트 등 열거형 데이터 안의 모든 요소를 **곱합니다**. | \`math.prod([2, 3, 4])\` $\\to$ \`24\`|
| \`isclose(a, b)\` | 두 실수가 수학적으로 **거의 같은지** 확인합니다. | 부동소수점 오차 검증 시 필수 |

### 2. 거듭제곱 및 로그 함수 (스케일 조절)
| 함수명 | 설명 | 예시 |
| --- | --- | --- |
| \`pow(x, y)\` | \`x\`의 \`y\` 거듭제곱을 계산합니다. ($x^y$) | \`math.pow(2, 3)\` $\\to$ \`8.0\` |
| \`sqrt(x)\` | \`x\`의 **제곱근(루트)**을 구합니다. | \`math.sqrt(16)\` $\\to$ \`4.0\` |
| \`exp(x)\` | 자연상수 $e$의 \`x\` 거듭제곱을 구합니다. ($e^x$) | 자연 지수 성장 계산 |
| \`log(x, [base])\` | \`x\`의 **자연로그** (또는 지정된 밑) 값을 구합니다. | 데이터 정규화에 사용 |
| \`log10(x)\` | 밑이 10인 상용로그 값을 구합니다. | 과학 스케일 조절 |

### 3. 기하학 및 삼각함수 (차원과 각도)
| 함수명 | 설명 | 예시 |
| --- | --- | --- |
| \`pi\` | 상수 **원주율** (약 3.14159...) | \`math.pi\` |
| \`e\` | 상수 **자연대수** (약 2.71828...) | \`math.e\` |
| \`sin(x)\`, \`cos(x)\`, \`tan(x)\` | **삼각함수** (라디안 값 기준 작동) | 사인, 코사인 파동 생성 |
| \`radians(x)\` | 평범한 **각도(Degree)** 값을 라디안으로 변환 | \`math.radians(180)\` $\\to$ \`\\pi\`|
| \`degrees(x)\` | **라디안(Radian)** 값을 평범한 각도로 변환 | \`math.degrees(math.pi)\` $\\to$ \`180.0\`|
| \`hypot(x, y)\` | 피타고라스 정리로 **유클리드 거리**(대각선)를 계산 | 거리 측정 최적화 |
| \`dist(p, q)\` | 두 점(튜플 기반 좌표) 사이의 거리를 계산 | \`math.dist((0,0), (3,4))\` $\\to$ \`5.0\` |
\`;

if(content.includes(target_line)) {
    content = content.replace(target_line, target_line + "\\n" + fullListMarkdown);
    fs.writeFileSync(file_path, content, 'utf-8');
    console.log("Successfully injected the comprehensive math function list.");
} else {
    console.error("Target line not found.");
}
