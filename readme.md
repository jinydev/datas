# 빅데이터 분석 (Big Data Analysis) 강의 노트

파이썬을 활용한 데이터 분석 입문 및 실무 활용을 위한 강의 노트 프로젝트입니다. 이 저장소는 수강생들이 데이터 분석의 기초부터 실전까지 체계적으로 학습할 수 있도록 구성된 온라인 웹사이트의 소스 코드를 담고 있습니다. Jekyll 기반의 정적 사이트로 만들어졌으며, Markdown 문서를 통해 강의 자료가 관리됩니다.

## 1. 주요 강의 내용

본 강의는 빅데이터 분석에 필수적인 파이썬 프로그래밍부터 데이터 분석 및 시각화 라이브러리 활용법까지 단계별로 다룹니다:

- **환경 구축 및 소개 (Setup & Intro):** 데이터 분석 환경(Anaconda, Jupyter Notebook 등) 설정 및 전체 과정 개요
- **파이썬 기초 (Python):** 데이터 분석을 위한 핵심 파이썬 문법 및 자료구조
- **데이터 수학/과학 (Numpy):** 고성능 수치 계산과 다차원 배열(Matrix) 연산을 위한 Numpy 기초
- **데이터 분석 (Pandas):** 정형 데이터 처리를 위한 Series/DataFrame 조작, 데이터 전처리 및 탐색적 데이터 분석(EDA)
- **데이터 시각화 (Matplotlib):** 분석 결과를 효과적으로 전달하기 위한 다양한 차트 및 시각화 기법

## 2. 개발 환경 설정 및 빌드 (Jekyll)

이 웹사이트는 **Ruby**와 **Jekyll**을 사용하여 정적 사이트로 빌드됩니다. 로컬 환경에서 문서를 작성하고 사이트를 띄워보려면 아래 과정을 진행하세요.

### 2.1. 설치 단계

macOS의 경우 시스템 기본 Ruby 권한 문제가 발생할 수 있으므로 Homebrew를 통해 최신 버전을 설치하는 것을 권장합니다.

```bash
# 1. 최신 Ruby 설치 (macOS)
brew install ruby

# 2. Bundler와 Jekyll 설치
gem install bundler jekyll

# 3. 프로젝트 루트 디렉토리에서 패키지 의존성 설치
bundle install
```

### 2.2. 로컬 서버 실행 및 사이트 빌드

마크다운 문서를 작성하면서 로컬에서 실시간으로 렌더링된 결과를 확인할 수 있습니다.

```bash
# 로컬 개발용 서버 실행 (접속 주소: http://127.0.0.1:4000)
bundle exec jekyll serve

# 핫 리로드(Live Reload) 서버 실행 (파일 저장 시 브라우저 자동 새로고침)
bundle exec jekyll serve --livereload

# 사이트 전체 빌드 (docs/ 폴더에 생성됨)
bundle exec jekyll build
```

- **Source**: `src/` (작업할 마크다운 파일 경로)
- **Destination**: `docs/` (빌드 결과물 출력 경로)

> **주의사항**: 빌드 대상은 `src` 폴더에 한정되며, 루트의 다른 폴더에 있는 파일은 빌드에 포함되지 않습니다. 
> **Troubleshooting**: `bundle` 관련 명령어를 찾을 수 없다는 오류가 발생한다면, 터미널 환경 설정(`.zshrc` 등)에 Ruby 경로가 제대로 추가되었는지 확인해 주세요. (예: `export PATH="/usr/local/opt/ruby/bin:$PATH"`)

### 2.3. 배포 (Deployment)

웹사이트는 GitHub Pages를 통해 배포됩니다. 배포 환경 구성 방법은 다음과 같습니다.

1. 수정한 내용을 `git push`로 저장소에 업로드합니다.
2. 저장소의 **Settings -> Pages** 메뉴로 이동합니다.
3. **Build and deployment** 항목 설정:
    - **Source**: Deploy from a branch
    - **Branch**: `main` (또는 `master`) 브랜치의 `/docs` 폴더 지정
4. **Custom Domain**: `datas.jiny.dev` (사용 중인 도메인이 있다면 설정)

설정이 완료되면 `docs` 폴더 내의 변경 사항이 자동으로 실제 사이트에 반영됩니다.

## 3. 기여 가이드 (Contributing)

본 프로젝트는 누구나 자유롭게 참여하고 개선할 수 있는 오픈소스 강의 자료를 지향합니다. 오타 수정, 내용 보강, 더 좋은 예제 추가 등 어떠한 형태의 기여도 환영합니다.

1. 이 저장소를 **Fork** 하여 본인의 계정으로 복사합니다.
2. 로컬 환경으로 clone 후 새로운 브랜치를 생성합니다. (`git checkout -b feature/new-content`)
3. 문서를 수정하거나 새로운 내용을 추가한 후 커밋합니다. (`git commit -m "docs: 판다스 기초 설명 보강"`)
4. 작업한 브랜치를 원격 저장소에 푸시합니다. (`git push origin feature/new-content`)
5. 원본 저장소에 **Pull Request(PR)**를 생성하여 변경 사항 리뷰를 요청합니다.

## 4. 라이선스 (License)

이 프로젝트에 포함된 문서 및 소스 코드는 **MIT 라이선스 (MIT License)** 하에 배포됩니다.
누구나 상업적 또는 비상업적 목적으로 자유롭게 활용, 복제, 수정, 배포할 수 있습니다. 라이선스의 자세한 내용은 저장소 내 `LICENSE` 파일이 존재할 경우 해당 파일을 참조하시기 바랍니다.
