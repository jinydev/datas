---
layout: python
title: "06. Java vs Python 예외 처리 비교"
description: "Java와 Python의 예외 처리 패러다임(catch vs except, 체크 예외 유무) 차이를 비교하고, 파이썬 코딩에 필요한 관련 영단어를 학습합니다."
keywords: "파이썬, python, 자바 파일, java python 비교, catch except, checked exception, 예외처리 언어 비교, 코딩 영단어"
---

# 5. Java vs Python 스나이퍼 비교 및 요약 정리

## ☕ Java vs 🐍 Python 스나이퍼 비교

### 1. 키워드의 차이 (catch vs except)
*   **Java**: 자바에서는 `try { } catch (Exception e) { } finally { }` 구문을 사용합니다.
*   **Python**: 파이썬은 목적어 성격이 강한 `catch` 대신 전치사 성격의 **`try ... except ... finally:`** 키워드를 사용합니다. 기능은 완전히 똑같습니다. 단지 콜론(`:`)과 들여쓰기 블록을 쓴다는 점만 다릅니다.

### 2. 체크 예외(Checked Exception)의 부재
*   **Java**: 파일 입출력(IOException) 등을 다룰 때 `try-catch`로 감싸거나 메서드 시그니처에 `throws`를 붙이지 않으면 아예 컴파일 자체가 안 되는 깐깐한 Checked Exception 시스템이 있습니다.
*   **Python**: 파이썬에는 컴파일러가 강제하는 **Checked Exception 개념이 없습니다**. 파일을 열 때 `try-except`로 감싸지 않아도 문법적 오류를 내뿜지 않습니다. 전적으로 개발자의 책임과 논리(Logical)에 맡깁니다.

---

## 🎧 Vibe Coding

> **🗣️ 학생 프롬프트 (AI에게 이렇게 명령해 보세요):**
> "파이썬으로 간단한 리스트의 평균을 구하는 계산기 함수를 만들어봐. 단, 빈 리스트가 들어와서 0으로 나누기 오류(`ZeroDivisionError`)가 발생하거나, 요소 중에 문자가 섞여 있어서 타입 오류(`TypeError`)가 발생할 수 있으니, `try-except` 구문으로 철저하게 예외 처리를 감싼 코드로 작성해 줘. 각 에러마다 귀여운 이모지와 함께 안내 문구를 출력해야 해."

---

## 📝 코딩 영단어 학습

*   **Syntax**: 구문, 문법 규칙. (`Syntax Error`는 파이썬 언어의 철자법이나 문법 체계를 틀린 것입니다.)
*   **Logic**: 논리, 타당성. (`Logical Error`는 컴퓨터는 시킨 대로 잘 했는데, 시킨 사람의 생각 자체가 틀린 것입니다.)
*   **Except**: ~을 제외하고. (`try...except` 구조에서는 "내가 시도해 보라(try)고 한 구문 외에 예기치 못하게 벌어진 빗나간 일들(except)은 이렇게 예외적으로 조치해"라는 의미로 쓰입니다.)
*   **Finally**: 마침내, 결국. (어떤 험난한 과정이나 에러가 있었든 간에 프로그램이 종료되기 전에 '무조건 마지막으로' 수행되는 약속된 공간입니다.)
