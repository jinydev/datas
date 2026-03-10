const fs = require('fs');

const filePath = 'd:\\site\\jinydev\\datas\\src\\python\\01_basic\\06_various_operators\\index.md';
let content = fs.readFileSync(filePath, 'utf-8');

const oldSectionRegex = /## ☕ Java vs 🐍 Python 스나이퍼 비교[\s\S]*?가독성이 압도적으로 높습니다\./;
const newSection = `## ☕ Java vs 🐍 Python 스나이퍼 비교

### 1. 연산 후 데이터 타입의 탈바꿈 (동적 타입 vs 정적 타입)

![파이썬 무한 정수 폭발 없는 웹툰](./img/python_infinite_int_webtoon.png)
*(웹툰 비유: 자바 로봇은 딱 정해진 'int' 철제 상자에 거대한 숫자를 욱여넣으려다 펑 하고 터져버리지만(오버플로우), 유연한 파이썬 뱀파우치는 숫자가 아무리 커져도 마법처럼 무한히 스르륵 늘어납니다!)*

*   **Java (엄격함)**: 처음 변수를 선언할 때 만들어둔 상자(메모리)의 크기와 타입을 절대 바꿀 수 없습니다. 만약 \`int\` 상자 두 개를 나누기 연산(\`/\`)하면 소수점은 무자비하게 버려지고 억지로 정수만 남깁니다. 행여나 곱셈이나 거듭제곱 연산 결과가 너무 거대해져서 상자 허용치를 초과하면 데이터가 엉뚱한 값으로 파괴되는 **'오버플로우(Overflow)'** 대참사가 발생합니다. 또한, 실수(\`double\`) 연산 결과를 정수(\`int\`) 상자에 넣으려 하면 **컴파일 시스템 에러**가 뿜어져 나옵니다.
*   **Python (유연함)**: 연산 결과에 따라 **데이터의 타입이 물 흐르듯 아주 자연스럽게 변신**합니다. 파이썬의 나눗셈 연산자 \`/\`는 정수끼리 나누더라도 소수점 아래를 잃지 않고 **무조건 실수(\`float\`) 타입으로 자동 변환**하여 깔끔하게 내어줍니다. 파이썬의 상자(변수)는 그저 이름표 스티커에 불과하므로, 어제 정수형(int)이던 변수에 오늘 실시한 나눗셈 결과(float)를 담아도 전혀 에러가 나지 않습니다. 숫자가 1만 자리가 넘어가도 파이썬이 알아서 무한대 크기(Arbitrary-precision)로 늘려주므로 **오버플로우 폭발이 아예 존재하지 않습니다.**

### 2. 파이썬만의 독특하고 훌륭한 산술 연산자
*   **Java**: 몫만 정확히 구하거나(정수 나눗셈 외), 거듭제곱을 하려면 \`Math.pow()\` 같은 복잡한 외부 수학 클래스를 불러와야 합니다.
*   **Python**: 데이터 분석 최적화 언어답게 몫 연산자 \`//\` (버림 나눗셈)와 거듭제곱 연산자 \`**\`를 기본 문법 자체에 내장하고 있습니다. (\`2 ** 3 = 8\`)

### 3. 논리 연산자 (Word vs Symbol)
*   **Java**: 기호 기반의 논리 연산자 \`&&\` (AND), \`||\` (OR), \`!\` (NOT) 을 사용합니다.
*   **Python**: 사람이 읽기 편하도록 영단어 그대로 **\`and\`**, **\`or\`**, **\`not\`**을 사용합니다. 가독성이 압도적으로 높습니다.`;

content = content.replace(oldSectionRegex, newSection);
fs.writeFileSync(filePath, content, 'utf-8');
console.log('Successfully injected Java vs Python type handling section.');
