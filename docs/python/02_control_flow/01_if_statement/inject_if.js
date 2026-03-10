const fs = require('fs');

const file_path = 'd:\\site\\jinydev\\datas\\src\\python\\02_control_flow\\01_if_statement\\index.md';
let content = fs.readFileSync(file_path, 'utf-8');

// 1. Inject Webtoon at the very beginning under the title
const webtoon_injection = \`## 조건문 if

![if 조건문의 논리 (클럽의 가드 로봇) 웹툰](./img/if_statement_bouncer_webtoon.png)
*(웹툰 비유: 클럽 입구에 선 무서운 가드 로봇이 '나이가 20살 이상인가?'라는 조건식(Velocity표지판)을 들고 있습니다. 15살 로봇은 '거짓(False)' 판정을 받아 쫓겨나고, 25살 로봇은 '참(True)' 판정을 받아 문 안으로 통과하는 재미있는 분기(Branching) 상황입니다.)*

\`;
content = content.replace("## 조건문 if\\n", webtoon_injection);

// 2. Append standard educational sections at the end of the file
const footer_expansions = \`
---

## ☕ Java vs 🐍 Python 스나이퍼 비교

### 1. 블록 구조 (중괄호 vs 들여쓰기)
*   **Java**: 블록을 정의할 때 중괄호 \`{ }\` 를 사용합니다. 들여쓰기(Indentation)는 사람의 눈을 위해 정렬하는 것일 뿐, 논리에는 1도 영향을 미치지 않습니다.
*   **Python**: 중괄호가 아예 없습니다! 오직 **스페이스 4칸 들여쓰기**만으로 코드 블록을 인식합니다. 들여쓰기가 한 칸이라도 어긋나면 자비 없이 \`IndentationError\`가 터지는, 지구상에서 들여쓰기에 가장 집착하는 언어입니다.

### 2. 조건부 괄호
*   **Java**: \`if (n % 2 == 0) {\` 와 같이 논리식을 반드시 **소괄호 \`( )\`** 로 감싸야 합니다.
*   **Python**: \`if n % 2 == 0:\` 처럼 소괄호를 생략하는 것이 기본이자 파이썬다움(Pythonic)입니다. 대신 문장 끝에 반드시 콜론(\`:\`)을 찍어 "문장이 끝났고 이제부터 블록이 시작된다"고 인터프리터에게 외쳐야 합니다.

### 3. 다중 분기 구문
*   **Java**: \`else if\` 로 단어를 띄워서 작성합니다.
*   **Python**: \`elif\` 라는 독특한 축약 키워드를 사용합니다. 

---

## 🎧 Vibe Coding

> **🗣️ 학생 프롬프트 (AI에게 이렇게 명령해 보세요):**
> "파이썬에서 점수를 입력받아 A, B, C, D, F 학점을 매겨주는 간단한 성적 판별기를 만들어줘. 단, if, elif, else가 정확히 어떻게 분기되는지 옆에 자세한 주석을 달아주고, 내가 잘못된 값(음수나 100점 초과)을 넣었을 때의 중첩 if문 예외처리도 추가해줘."

---

## 코딩 영단어 학습 📝

*   **\`if\`**: 만약 ~라면. (현실의 가정문과 똑같이, 코드 세계에서 선택의 기로를 만듭니다.)
*   **\`else\`**: 그 밖의, 다른. (모든 `if`와 `elif`의 검증을 통과하지 못한 '나머지 찌꺼기' 값들이 모조리 들어가는 쓰레기통이자 최후의 보루입니다.)
*   **\`elif\`**: else if 의 줄임말. (파이썬에서만 쓰는 독특한 줄임말입니다. 두 번째, 세 번째 플랜B 조건들을 계속해서 추가할 때 씁니다.)
*   **\`Indent (Indentation)\`**: 들여쓰다, 톱니 모양. (파이썬 코드의 목숨줄입니다. 콜론 뒤에 스페이스바 4번을 쳐서 코드를 우측으로 파이게 만드는 행위를 말합니다.)
\`;

if (!content.includes("## ☕ Java vs 🐍 Python 스나이퍼 비교")) {
    content += footer_expansions;
    fs.writeFileSync(file_path, content, 'utf-8');
    console.log("Successfully injected the webtoon and appended the footer expansions.");
} else {
    console.log("Footer already exists. Skipping append.");
}
