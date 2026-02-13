---
layout: default
title: "1주차 환경설정: VS Code 가이드"
---

# 1주차 환경설정: VS Code 가이드

> **학습목표**: 로컬 데이터 분석 환경인 VS Code를 설치하고, Python 및 Jupyter 확장 프로그램을 설정하여 분석 환경을 구축합니다.

## 1.2.2. VS Code 설치 및 설정 (Visual Studio Code Setup)

### 1) VS Code 소개 (Introduction)
> **Visual Studio Code (VS Code)**는 마이크로소프트가 만든 **세계 1위 코드 에디터**입니다. 
> 가볍고 강력하여 웹 개발, 데이터 분석, 인공지능 등 모든 분야에서 표준처럼 사용됩니다.

---

### 2) VS Code 설치 방법 (Installation)
1.  **다운로드**: [VS Code 공식 홈페이지](https://code.visualstudio.com/)에 접속합니다.
2.  **설치**: 운영체제(Windows, macOS)에 맞는 버전을 다운로드하여 설치합니다.
3.  **실행**: 설치가 완료되면 VS Code를 실행합니다.

![VS Code 실행 화면](./img/image-20260211185451602.png)

---

### 3) 파이썬 패키지 설치 (Python Extension)
VS Code에서 파이썬 코드를 작성하고 실행하려면 **Python 확장 프로그램**이 필요합니다.

1.  좌측 활동바에서 **네모 블록 아이콘(Extensions)**을 클릭합니다.
2.  검색창에 `Python`을 입력합니다.
3.  **Python (Microsoft)** 항목을 찾아 `Install` 버튼을 클릭합니다.

> **설치되는 항목**:
> - <img src="https://raw.githubusercontent.com/microsoft/vscode-python/main/images/icon.png" width="20"/> **Python**: 파이썬 코드의 자동 완성(IntelliSense), 디버깅(Debugging), 실행 환경 등을 지원하는 핵심 도구입니다.

---

### 4) 주피터 노트북 패키지 설치 (Jupyter Extension)
데이터 분석의 필수 도구인 `.ipynb` 파일을 VS Code에서 실행하기 위해 설치합니다.

1.  Extensions 메뉴에서 `Jupyter`를 검색합니다.
2.  **Jupyter (Microsoft)** 항목을 찾아 `Install` 버튼을 클릭합니다.
    *(보통 Python 확장을 설치하면 자동으로 함께 설치됩니다.)*

> **설치되는 항목**:
> - <img src="https://raw.githubusercontent.com/microsoft/vscode-jupyter/main/icon.png" width="20"/> **Jupyter**: VS Code 내에서 주피터 노트북 파일을 열고, 코드를 셀 단위로 실행하며, 결과를 시각화할 수 있게 해주는 도구입니다.

> **꿀팁 🍯**: 메뉴를 한글로 보고 싶다면 `Korean Language Pack`을 검색해서 추가로 설치해 주세요!
