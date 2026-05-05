---
layout: docs
title: 지니 웹사이트 구현 가이드 (AI 프롬프트용)
description: AI 어시스턴트(Claude, Gemini 등)가 일관성을 유지하며 Jekyll 웹사이트를 구현하기 위한 가이드라인입니다.
keywords: jekyll, guide, implementation, ai, prompt
url: /site/
---

# Jiny Big Data Analysis: AI 작성 및 구현 가이드

본 문서는 Claude, Gemini 등 AI 어시스턴트와 개발자가 **Jiny Big Data Analysis (지니 빅데이터 분석)** 강의 사이트 유지보수 및 콘텐츠 작성 시 **반드시 준수해야 할 규칙(System Prompt)**입니다. AI는 본 문서의 내용을 숙지하고 모든 작업에 일관되게 적용해야 합니다.

## 1. 프로젝트 기본 환경 (Project Overview)

- **프레임워크**: Jekyll 4.x (정적 사이트 생성기)
- **템플릿 언어**: Liquid
- **스타일링**: Bootstrap 5 + 커스텀 CSS (`docs.css`)
- **작업 디렉토리 (Source)**: `src/` (모든 개발 및 콘텐츠 작성은 여기서 진행)
- **배포 디렉토리 (Output)**: `docs/` (GitHub Pages 배포용, **직접 수정 절대 금지**)

## 2. 레이아웃 및 템플릿 시스템 (Layout System)

모든 Markdown 문서와 HTML 페이지는 `src/_layouts/`에 정의된 레이아웃을 따릅니다.

1. **`bootstrap.html` (최상위 마스터 래퍼)**
   - HTML5 뼈대, `<head>`, 전역 `<body>` 설정, 헤더/푸터 인클루드를 담당합니다.
   - **중요**: 인용구(blockquote), 테이블, 반응형 이미지 등에 대한 전역 인라인 CSS가 포함되어 있습니다. 전체 사이트에 영향을 주는 스타일 수정 시 이 파일을 확인하세요.
2. **`docs.html` (표준 강의 문서 레이아웃)**
   - **좌측 사이드바**: `navigation.yml` 기반 메뉴 (모바일 offcanvas 지원)
   - **메인 콘텐츠**: 실제 마크다운 내용 (`{{ content }}`)
   - **우측 목차(TOC)**: 문서 내 `h2`, `h3` 헤딩 기반 자동 생성 목차
   - **Breadcrumbs & Title**: 자동으로 렌더링되므로 마크다운 본문에 H1(`#`) 제목을 중복 작성할 필요가 없습니다.

**[적용 규칙]**
- 모든 강의 문서(Markdown)의 Front Matter에는 **반드시 `layout: docs`를 지정**해야 합니다.

## 3. 마크다운 작성 규칙 (Markdown Guidelines)

AI는 새로운 강의 콘텐츠를 작성할 때 다음 규칙을 엄격히 준수합니다.

### 3.1 Front Matter 필수 항목
모든 `.md` 파일 상단에 아래 형식을 포함하세요.
```yaml
---
layout: docs
title: [강의 제목]
description: [강의 내용에 대한 1~2줄 요약]
keywords: [키워드1, 키워드2, 쉼표로 구분]
url: /[섹션명]/[파일명]/  # (선택사항) 명시적인 URL 지정 시 사용
---
```

### 3.2 톤앤매너 및 언어 (Tone & Language)
- **언어**: 모든 강의 내용은 명확하고 자연스러운 **한국어**로 작성합니다.
- **어투**: 학습자를 대하는 친절하고 전문적인 존댓말(~합니다, ~알아보겠습니다, ~하세요)을 사용합니다.

### 3.3 이미지 (Images)
- **저장 위치**: `src/assets/img/` 또는 각 섹션별 이미지 폴더(예: `src/pandas/img/`)에 저장합니다.
- **문법**: `![대체 텍스트](/경로/이미지명.png)`
- **스타일**: 모든 이미지는 `max-width: 100%; height: auto;`가 전역 적용되어 반응형으로 동작합니다. 특정 썸네일 목적이 아니라면 크기를 하드코딩하지 마세요.

### 3.4 인용구 및 팁 (Callouts & Blockquotes)
강조 사항이나 참고 자료는 인용구 문법을 사용합니다.
```markdown
> **참고(Note)**: 팁이나 주의사항은 이와 같이 작성합니다.
```
- 렌더링 시 연한 회색 배경과 좌측 테두리가 적용된 깔끔한 박스로 표시됩니다.

### 3.5 코드 블록 (Code Blocks)
- 반드시 백틱 3개(```)와 함께 언어(예: `python`, `bash`, `html`)를 명시하세요.
- **다이어그램**: 구조나 흐름도를 표현할 때는 `mermaid` 언어를 사용하세요. (JS 클라이언트에서 자동 렌더링됨)

## 4. 네비게이션 시스템 (Navigation System)

좌측 사이드바 메뉴는 데이터 파일을 통해 관리됩니다.

- **설정 파일**: `src/_data/navigation.yml`
- **구조 예시**:
  ```yaml
  main:
    - title: 판다스 기초
      subitems:
        - title: 1. 판다스 소개
          url: /pandas/01_pandas_intro.html
  ```
- **[핵심 규칙]**: AI가 **새로운 마크다운 문서를 생성한 후에는 반드시 `navigation.yml`에 해당 문서의 URL을 추가**해야 사이드바에 정상적으로 노출됩니다.

## 5. CSS 및 스타일링 (Styling)

- **프레임워크**: Bootstrap 5 기본 클래스를 최대한 활용하세요. (예: `container`, `row`, `col`, `mb-3`)
- **커스텀 스타일**: `src/assets/css/docs.css`에서 컴포넌트(사이드바, TOC 등) 전용 스타일을 관리합니다.
- **전역 인라인 스타일**: `src/_layouts/bootstrap.html` 내부에 중요도 높은 전역 스타일이 정의되어 있습니다.

## 6. 빌드 명령어 (Build & Serve)

문서 수정 후 결과를 확인하는 명령어입니다.

```bash
# 로컬 개발 서버 실행 (실시간 변경 확인)
bundle exec jekyll serve

# 배포용 정적 빌드 (docs 폴더 생성)
bundle exec jekyll build
```

## 7. AI 자가 점검 체크리스트 (AI Maintenance Checklist)

사용자(USER)의 요청을 처리하기 전/후에 다음 사항을 스스로 점검하세요:

- [ ] **새 문서를 추가했는가?** -> `navigation.yml`을 업데이트했는지 확인.
- [ ] **스타일 변경이 필요한가?** -> `docs.css` 또는 `bootstrap.html`의 인라인 스타일을 확인.
- [ ] **레이아웃 구조가 깨지는가?** -> `docs.html` 파일이나 `_includes/sidebar.html`를 점검.
- [ ] **한국어 문법과 톤앤매너** -> 규칙(3.2)에 맞게 존댓말과 친절한 톤을 유지했는가?

