const fs = require('fs');

const file_path = 'd:\\site\\jinydev\\datas\\src\\python\\01_basic\\07_built_in_functions\\index.md';
let content = fs.readFileSync(file_path, 'utf-8');

const old_text = `위의 경우 \`year\` 변수가 숫자 2005가 아닌 문자열 \`"2005"\`로 저장되어 있기 때문에 나눗셈이나 빼기 연산이 불가능합니다. 이를 해결하기 위해 파이썬 내장 형 변환 캐스팅 함수를 사용할 수 있습니다.

**자료형 변환 함수 요약**
- **숫자형 → 문자열형**: \`str()\`을 사용해 숫자를 문자열로 안전하게 바꿉니다. 
- **문자열형 → 숫자형**: \`int()\`나 \`float()\`을 사용해 숫자 형태의 문자열을 계산 가능한 수치로 바꿉니다.
- **논리형 ↔ 다른 타입**: \`bool()\`은 값을 논리형(\`True\`/\`False\`)으로, \`int()\`는 빈 논리형을 1과 0으로 맵핑합니다. 비어있지 않은 문자열은 단어에 상관없이 \`True\` 로 평가됩니다 (\`bool("False") --> True\`).`;

const new_text = `위의 경우 \`year\` 변수가 숫자 2005가 아닌 문자열 \`"2005"\`로 저장되어 있기 때문에 2026 - "2005" 같은 수학적 연산을 시도하면 즉각 에러가 발생합니다. 종이 상자("2005")와 쇳덩어리 숫자(2026)는 연산이 불가능하기 때문입니다.

### 마법의 껍질 벗기기: 형 변환 (Casting)

![형 변환(Type Casting) 원리 웹툰](./img/type_casting_webtoon.png)
*(웹툰 비유: 계산기 로봇이 종이 박스("2005")를 보고 계산을 거부합니다. 그러자 주인공이 \`int()\`라는 마법의 칼로 종이 박스를 북북 찢어버리자, 그 안에서 진짜 쇳덩어리 숫자 \`2005\`가 등장하여 로봇이 기뻐하며 계산을 시작합니다!)*

![형 변환(Type Casting) 컨베이어 벨트 애니메이션](./img/built_in_casting_anim.svg)
*(다이어그램: 연산이 불가능한 점선 문자열 상자 \`"2005"\`가 \`int()\` 용광로 기계를 통과하자, 단단하고 덧셈 뺄셈이 가능한 정수 쇳덩어리 \`2005\`로 캐스팅(주조)되어 나오는 팩토리 애니메이션입니다.)*

이를 해결하기 위해 파이썬이 기본 제공하는 **형 변환(Casting)** 주문을 외워야 합니다.

**필수 형 변환 내장 함수 요약**
- **글자를 숫자로 (\`str\` $\\to$ \`int\`/\`float\`)**: \`int()\`나 \`float()\`을 사용해 숫자 형태의 문자열 껍데기를 벗겨내고 진짜 계산 가능한 수치(정수/실수)로 제련합니다.
- **숫자를 글자로 (\`int\`/\`float\` $\\to$ \`str\`)**: \`str()\`을 사용해 계산이 끝난 숫자를 다시 문자열 종이 박스에 포장합니다. (문장 더하기 \`+\`를 할 때 필수적입니다.)
- **논리 조작 (\`bool\`)**: \`bool()\`은 특정 값을 무조건 참(\`True\`)이나 거짓(\`False\`)으로 우격다짐 변환합니다. 빈 문자열(\`""\`)이나 \`0\`은 \`False\`가 되지만, 그 외의 텍스트("Hello")나 숫자(15)는 모두 \`True\`로 판별됩니다.`;

// Ensure exact line ending match
const normalizedOld = old_text.replace(/\\r\\n/g, '\\n');
content = content.replace(/\\r\\n/g, '\\n');

if (content.includes(normalizedOld)) {
    content = content.replace(normalizedOld, new_text);
    fs.writeFileSync(file_path, content, 'utf-8');
    console.log("Replace successful via Node.js!");
} else {
    console.log("Exact old text not found in Node.js script.");
}
