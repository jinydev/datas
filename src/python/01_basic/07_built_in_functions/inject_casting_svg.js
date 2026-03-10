const fs = require('fs');

const filePath = 'd:\\site\\jinydev\\datas\\src\\python\\01_basic\\07_built_in_functions\\index.md';
let content = fs.readFileSync(filePath, 'utf-8');

// Target the existing webtoon description line using regex to avoid white-space issues
const targetRegex = /\*\(웹툰 비유: 계산기 로봇이 종이 박스\("2005"\)를 보고 계산을 거부합니다\. 그러자 주인공이 `int\(\)`라는 마법의 칼로 종이 박스를 북북 찢어버리자, 그 안에서 진짜 쇳덩어리 숫자 `2005`가 등장하여 로봇이 기뻐하며 계산을 시작합니다!\)\*/;

const newSvgText = `*(웹툰 비유: 계산기 로봇이 종이 박스("2005")를 보고 계산을 거부합니다. 그러자 주인공이 \`int()\`라는 마법의 칼로 종이 박스를 북북 찢어버리자, 그 안에서 진짜 쇳덩어리 숫자 \`2005\`가 등장하여 로봇이 기뻐하며 계산을 시작합니다!)*

![형 변환(Type Casting) 컨베이어 벨트 애니메이션](./img/built_in_casting_anim.svg)
*(다이어그램: 연산이 불가능한 점선 문자열 상자 \`"2005"\`가 \`int()\` 용광로 기계를 통과하자, 단단하고 덧셈 뺄셈이 가능한 정수 쇳덩어리 \`2005\`로 캐스팅(주조)되어 나오는 팩토리 애니메이션입니다.)*`;

if (targetRegex.test(content)) {
    content = content.replace(targetRegex, newSvgText);
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log('Successfully injected the Casting SVG animation.');
} else {
    console.error('Target line not found via regex.');
}
