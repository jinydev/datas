const fs = require('fs');

const filePath = 'd:\\site\\jinydev\\datas\\src\\python\\01_basic\\07_built_in_functions\\index.md';
let content = fs.readFileSync(filePath, 'utf-8');

// Replacement 1: 입출력과 데이터 형 변환(Casting)
const oldCastingRegex = /## 입출력과 데이터 형 변환\(Casting\)[\s\S]*?temperature = 36\.5\nstatus = "현재 체온은 " \+ str\(temperature\) \+ "도 입니다\."\nprint\(status\)\n```/;

const newCasting = `## 입출력 (\`input\`과 \`print\`) 및 데이터 형 변환(Casting)

파이썬과 사용자가 대화를 나누는 가장 기본적인 창구가 바로 \`input()\`과 \`print()\` 내장 함수입니다. 
\`input()\` 함수를 통해 사용자의 키보드 입력을 받아낼 수 있는데, 아주 치명적인 특징이 하나 있습니다. **사용자가 숫자를 입력하더라도 파이썬은 무조건 텍스트 문자열(\`str\`) 박스로 감싸서 반환한다는 것입니다.**

\`\`\`python
year = input('당신이 태어난 년도는 ? ')
# 사용자가 2005를 입력
print("저장된 타입:", type(year)) # <class 'str'> (숫자가 아니라 글자 탈을 쓴 상태)
\`\`\`

위의 경우 \`year\` 변수가 숫자 2005가 아닌 문자열 \`"2005"\`로 저장되어 있기 때문에 2026 - "2005" 같은 수학적 연산을 시도하면 즉각 에러가 발생합니다. 종이 상자("2005")와 쇳덩어리 숫자(2026)는 연산이 불가능하기 때문입니다.

### 마법의 껍질 벗기기: 형 변환 (Casting)

![형 변환(Type Casting) 원리 웹툰](./img/type_casting_webtoon.png)
*(웹툰 비유: 계산기 로봇이 종이 박스("2005")를 보고 계산을 거부합니다. 그러자 주인공이 \`int()\`라는 마법의 칼로 종이 박스를 북북 찢어버리자, 그 안에서 진짜 쇳덩어리 숫자 \`2005\`가 등장하여 로봇이 기뻐하며 계산을 시작합니다!)*

이를 해결하기 위해 파이썬이 기본 제공하는 **형 변환(Casting)** 주문을 외워야 합니다.

**필수 형 변환 내장 함수 요약**
- **글자를 숫자로 (\`str\` $\\to$ \`int\`/\`float\`)**: \`int()\`나 \`float()\`을 사용해 숫자 형태의 문자열 껍데기를 벗겨내고 진짜 계산 가능한 수치(정수/실수)로 제련합니다.
- **숫자를 글자로 (\`int\`/\`float\` $\\to$ \`str\`)**: \`str()\`을 사용해 계산이 끝난 숫자를 다시 문자열 종이 박스에 포장합니다. (문장 더하기 \`+\`를 할 때 필수적입니다.)
- **논리 조작 (\`bool\`)**: \`bool()\`은 특정 값을 무조건 참(\`True\`)이나 거짓(\`False\`)으로 우격다짐 변환합니다. 빈 문자열(\`""\`)이나 \`0\`은 \`False\`가 되지만, 그 외의 텍스트("Hello")나 숫자(15)는 모두 \`True\`로 판별됩니다.

\`\`\`python
# 1. 입력과 동시에 껍질을 벗겨 숫자로 캐스팅 처리
year_num = int(input('당신이 태어난 년도는 ? '))
age = 2026 - year_num
print('선생님의 나이는:', age) # 이제 정상적으로 뺄셈 가능 대성공!

# 2. 숫자를 다시 글자로 포장하여 문장 합성하기
temperature = 36.5
# 에러 발생 방지: 서로 다른 타입(글자 + 숫자)은 더할 수 없으므로 str()로 포장
status = "현재 체온은 " + str(temperature) + "도 입니다."
print(status)
\`\`\``;

// Replacement 2: 문자열 메서드 시각화 추가
const oldStringMethodRegex = /## ① 문자열\(str\) 메서드\n\| 메서드 \| 설명 \|\n\| --- \| --- \|\n\| `upper\(\)`, `lower\(\)` \| 모든 문자를 일괄 대\/소문자로 변환합니다\. \|\n\| `replace\(old, new\)` \| 문자열 안에 존재하는 특정 패턴 `old`를 찾아 `new` 텍스트로 치환합니다\. \|\n\| `split\(sep\)` \| 구분자\(`sep`\)를 기준으로 하나의 거대한 문자열을 쪼개어 리스트 형태로 반환합니다\. \|\n\| `strip\(\)` \| 텍스트의 양쪽 끝에 붙어있는 불필요한 공백과 줄바꿈을 깔끔하게 제거합니다\. \|/;

const newStringMethod = `## ① 문자열(str) 고유 메서드

문자열 데이터는 텍스트를 자유자재로 다듬는 강력한 부가 기능(메서드)들을 점(\`.\`)을 통해 찍어낼 수 있습니다. 

![파이썬 문자열 메서드 시각화 애니메이션](./img/string_methods_anim.svg)
*(다이어그램: \`.upper()\`, \`.replace()\`, \`.split()\` 메서드가 텍스트 블록에 작용하여 데이터를 변형하거나 칼집을 내어 조각(리스트) 내는 과정을 보여줍니다.)*

| 핵심 메서드 | 실전 사용 예시 및 설명 |
| --- | --- |
| \`upper()\`, \`lower()\` | \`"hello".upper()\` $\\to$ \`"HELLO"\`<br>모든 문자를 일괄 대/소문자로 뻥튀기하거나 축소시킵니다. 로그인 시 아이디 대소문자 혼용 방지에 씁니다. |
| \`replace(A, B)\` | \`"apple".replace("a", "o")\` $\\to$ \`"opple"\`<br>문자열 안에 몰래 존재하는 특정 텍스트 \`A\`를 찾아 남김없이 \`B\`로 치환합니다. |
| \`split(구분자)\` | \`"I love Py".split(" ")\` $\\to$ \`["I", "love", "Py"]\`<br>지정한 기호(기본은 띄어쓰기)를 도마 삼아 거대한 문자열을 칼로 썰어 배열(리스트)에 담아줍니다. 문장 분석의 알파이자 오메가입니다. |
| \`strip()\` | \`"  hello  ".strip()\` $\\to$ \`"hello"\`<br>사용자 실수로 텍스트 양 끝에 붙어버린 우주 쓰레기(공백, 줄바꿈)들을 깔끔하게 진공청소기처럼 빨아들입니다. |`;

content = content.replace(oldCastingRegex, newCasting);
content = content.replace(oldStringMethodRegex, newStringMethod);

fs.writeFileSync(filePath, content, 'utf-8');
console.log('Successfully injected built_in expansions.');
