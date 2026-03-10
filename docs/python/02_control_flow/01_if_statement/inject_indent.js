const fs = require('fs');

const file_path = 'd:\\site\\jinydev\\datas\\src\\python\\02_control_flow\\01_if_statement\\index.md';
let content = fs.readFileSync(file_path, 'utf-8');

const target_regex = /### 블록 문장 조건문 if[\\s\\S]*?만드시 콜론 \\`:\\`으로 헤더를 마무리해야 합니다\\./;

const new_content = \`### 파이썬은 왜 중괄호 {} 를 쓰지 않을까? (들여쓰기 블록)

파이썬은 C, Java와 같은 기존 언어들과 달리 **중괄호 \`{}\` 대신 오직 '들여쓰기(Indentation)'**만을 사용하여 코드 블록을 묶고 구분합니다.

![파이썬 들여쓰기와 중괄호의 차이 웹툰](./img/python_indentation_webtoon.png)
*(웹툰 비유: 왼쪽의 다른 언어 프로그래머는 수많은 중괄호 \`{}\` 거미줄에 갇혀 코드의 논리를 잃고 괴로워하고 있습니다. 하지만 오른쪽의 파이썬 프로그래머는 완벽하게 정렬된 '들여쓰기 블록 계단'을 가뿐하게 오르며 코드를 식별합니다!)*

#### 가독성이 왕이다 (Readability Counts)
파이썬 창시자 귀도 반 로섬(Guido van Rossum)은 **"코드는 작성되는 시간보다 다른 사람에 의해서 읽히는 시간이 훨씬 길다"**고 굳게 믿었습니다. 

자바나 C에서는 중괄호만 맞으면 띄어쓰기를 엉망으로 섞어 써도 컴퓨터는 군말 없이 실행해 줍니다. 하지만 파이썬은 **"사람의 눈에 보이는 시각적 들여쓰기 구조가 곧 실제 컴퓨터가 인식하는 논리 구조와 100% 동일하도록"** 프로그래머에게 강제합니다. 덕분에 코딩을 어제 시작한 초보자가 짠 코드든, 구글의 천재 해커가 짠 코드든 파이썬 코드는 항상 자를 대고 일직선으로 자른 듯 반듯하고 일관되어 **가독성이 폭발적으로 높아지는 마법**이 일어납니다.

관례적으로 **스페이스 4칸**을 사용합니다. 블록을 시작하기 전(예: \`if\` 조건식 끝)에는 반드시 콜론 \`:\`을 찍어 "이제부터 새로운 블록 계단이 시작된다"고 인터프리터에게 예고해야 합니다.\`;

// Fallback manual replace if regex misses
let lines = content.split(/\\r?\\n/);
let start_idx = -1;
let end_idx = -1;

for(let i=0; i<lines.length; i++) {
    if(lines[i].includes("### 블록 문장 조건문 if")) {
        start_idx = i;
    }
    if(start_idx !== -1 && lines[i].includes("파이썬은 C, Java와 같은 블록 구조 언어지만")) {
        // Find the end of this paragraph
        end_idx = i + 1; // Assuming it's short
        break;
    }
}

if(start_idx !== -1 && end_idx !== -1) {
    const lines_before = lines.slice(0, start_idx).join('\\n');
    const lines_after = lines.slice(end_idx + 1).join('\\n');
    
    fs.writeFileSync(file_path, lines_before + '\\n' + new_content + '\\n\\n' + lines_after, 'utf-8');
    console.log("Success: Replaced block indentation explanation.");
} else {
    console.log("Failed to find target paragraphs.");
}
