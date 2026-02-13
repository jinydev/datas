# 빅데이터 분석 (Big Data Analysis)

파이썬을 활용한 데이터 분석 입문 강의 노트 프로젝트입니다.
Jekyll 기반의 정적 사이트로 구성되어 있으며, `src` 폴더의 Markdown 파일을 변환하여 `docs` 폴더에 웹사이트를 생성합니다.

## 1. 환경 설정 (Prerequisites)

이 프로젝트는 **Ruby**와 **Jekyll**을 사용합니다.
macOS 환경을 기준으로 Homebrew를 사용하여 설치하는 것을 권장합니다.

### 1.1. Ruby 설치 (Homebrew)
시스템 Ruby(Mac 기본)는 버전이 낮거나 권한 문제가 발생할 수 있으므로, Homebrew로 최신 Ruby를 설치합니다.

```bash
brew install ruby
```

### 1.2. Bundler & Jekyll 설치
Ruby 패키지 매니저인 Gem을 사용하여 Bundler와 Jekyll을 설치합니다.

```bash
gem install bundler jekyll
```

## 2. 프로젝트 설치 (Installation)

프로젝트 루트 디렉토리에서 필요한 의존성 패키지(Gem)를 설치합니다.
이 프로젝트는 프로젝트 내 `vendor/bundle` 경로에 패키지를 설치하도록 설정되어 있습니다.

```bash
# 의존성 설치
bundle install
```

## 3. 사이트 빌드 (Build)

`src` 폴더의 내용을 기반으로 `docs` 폴더에 정적 사이트를 생성합니다.

```bash
bundle exec jekyll build
```

*   **Source**: `src/`
*   **Destination**: `docs/`

> **중요**: `src` 폴더 외의 파일(루트의 다른 폴더 등)은 빌드에 포함되지 않습니다.

## 4. 로컬 서버 실행 (Serve)

로컬에서 실시간으로 변경 사항을 확인하려면 다음 명령어를 사용합니다.
**반드시 Homebrew로 설치된 Ruby를 사용하기 위해 PATH를 설정해야 합니다.**

```bash
# Ruby 경로 설정 (맥OS 기준)
export PATH="/usr/local/opt/ruby/bin:$PATH"

# 서버 실행
bundle exec jekyll serve
```

웹 브라우저에서 [http://127.0.0.1:4000](http://127.0.0.1:4000) 으로 접속하여 확인할 수 있습니다.

> **오류 해결**: 만약 `Could not find 'bundler'` 오류가 발생한다면, 위 `export PATH...` 명령어를 먼저 실행했는지 확인하세요.

### 4.1. `jekyll` 명령어 직접 실행 (Optional)
`bundle exec` 없이 `jekyll` 명령어를 직접 실행하려면, Homebrew Ruby의 Gem 바이너리 경로가 PATH에 포함되어야 합니다.
만약 `command not found: jekyll` 오류가 발생한다면 다음 설정을 확인하세요.

```bash
# .zshrc 파일에 추가 (이미 추가되어 있다면 `source ~/.zshrc` 실행)
export PATH="/usr/local/opt/ruby/bin:$PATH"
export PATH="/usr/local/lib/ruby/gems/3.4.0/bin:$PATH"
```

### 4.2. Ruby 버전 문제 해결 (Troubleshooting)
만약 계속해서 `Gem::FilePermissionError` 또는 `Ruby 2.6` 관련 오류가 발생한다면, 현재 터미널이 시스템 기본 Ruby를 사용하고 있는 것입니다.
다음 명령어로 현재 사용 중인 Ruby 버전을 확인하세요.

```bash
which ruby
# 예상 결과: /usr/local/opt/ruby/bin/ruby (Homebrew Ruby)
# 잘못된 결과: /usr/bin/ruby (Mac 시스템 Ruby)

ruby -v
# 예상 결과: ruby 3.4.x
# 잘못된 결과: ruby 2.6.x
```

**해결 방법**:
터미널에서 아래 명령어를 **직접 실행**하여 PATH를 강제로 적용한 후 다시 시도하세요.

```bash
export PATH="/usr/local/opt/ruby/bin:$PATH"
bundle exec jekyll serve
```


**권장 사항**: 프로젝트 의존성 관리를 위해 가급적 **`bundle exec jekyll serve`** 명령어를 사용하는 것이 좋습니다.

## 5. 배포 (Deployment)

GitHub Pages를 통해 배포됩니다.

1.  수정한 내용을 `git push`로 GitHub 저장소에 업로드합니다.
2.  GitHub Repository Settings -> **Pages** 메뉴로 이동합니다.
3.  **Build and deployment** 설정:
    *   **Source**: Deploy from a branch
    *   **Branch**: `main` (또는 `master`)
    *   **Folder**: `/docs`
4.  **Custom Domain**: `datas.jiny.dev` (설정된 경우)

설정이 완료되면 `docs` 폴더의 내용이 자동으로 게시됩니다.
