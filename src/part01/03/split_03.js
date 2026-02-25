const fs = require('fs');
const path = require('path');

const baseDir = '/Users/hojin8/docs/070.강의/c01.빅데이터분석/src/part01/03';
const originalFile = path.join(baseDir, 'index.md');

const content = fs.readFileSync(originalFile, 'utf8');
const lines = content.split('\n');

const headerPattern = /^###\s+(\d+)\.\s+(.*)/;
const sectionPattern = /^##\s+SECTION/;

const sections = [];
let currentSectionContent = [];
let currentTitle = '';
let currentNum = '';

let introLines = [];
let globalCount = 1;

for (const line of lines) {
    const match = line.match(headerPattern);
    if (match) {
        if (currentTitle) {
            sections.push({
                gNum: globalCount - 1,
                num: currentNum,
                title: currentTitle,
                content: currentSectionContent
            });
        }

        currentNum = match[1];
        currentTitle = match[2].trim();

        if (introLines.length > 0) {
            currentSectionContent = [...introLines, line];
            introLines = [];
        } else {
            currentSectionContent = [line];
        }
        globalCount++;
    } else if (line.match(sectionPattern) || (!currentTitle && line.trim() !== '')) {
        if (currentTitle && line.match(sectionPattern)) {
            introLines.push(line);
        } else {
            if (!currentTitle) {
                introLines.push(line);
            } else {
                currentSectionContent.push(line);
            }
        }
    } else {
        if (currentTitle) {
            currentSectionContent.push(line);
        } else {
            introLines.push(line);
        }
    }
}

if (currentTitle) {
    sections.push({
        gNum: globalCount - 1,
        num: currentNum,
        title: currentTitle,
        content: currentSectionContent
    });
}

let count = 0;
for (const section of sections) {
    let safeTitle = section.title.replace(/[\\/*?:"<>|()]/g, '').replace(/ /g, '_');

    let gNumStr = section.gNum.toString().padStart(2, '0');
    let filename = `${gNumStr}_${safeTitle}.md`;
    let outFile = path.join(baseDir, filename);

    let header = `---\nlayout: docs\ntitle: "${section.gNum.toString().padStart(2, '0')}. ${section.title}"\n---\n\n`;

    fs.writeFileSync(outFile, header + section.content.join('\n'), 'utf8');
    count++;
}

console.log(`Split ${count} files successfully.`);
