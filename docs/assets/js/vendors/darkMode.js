// Darkmode
// 다크 모드 전환 기능을 제공하는 JavaScript 파일
// 테마 아이콘을 동적으로 업데이트하고, 사용자의 테마 설정을 저장합니다

(() => {
    "use strict";

    // 로컬 스토리지에서 저장된 테마 가져오기
    const getStoredTheme = () => localStorage.getItem("theme");
    // 로컬 스토리지에 테마 저장하기
    const setStoredTheme = (theme) => localStorage.setItem("theme", theme);

    // 선호하는 테마 가져오기 (저장된 테마 또는 시스템 설정)
    const getPreferredTheme = () => {
        const storedTheme = getStoredTheme();
        if (storedTheme) {
            return storedTheme;
        }

        return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    };

    // 테마 설정하기
    const setTheme = (theme) => {
        if (theme === "auto" && window.matchMedia("(prefers-color-scheme: dark)").matches) {
            document.documentElement.setAttribute("data-bs-theme", "dark");
        } else {
            document.documentElement.setAttribute("data-bs-theme", theme);
        }
    };

    // 드롭다운 아이콘 업데이트하기
    // 현재 활성화된 테마에 맞는 아이콘을 푸터의 테마 버튼에 표시합니다
    const updateDropdownIcon = (theme) => {
        const themeIconActive = document.querySelector(".theme-icon-active");
        const iconElement = document.querySelector(`[data-bs-theme-value="${theme}"] .theme-icon`);

        if (themeIconActive && iconElement) {
            themeIconActive.innerHTML = iconElement.outerHTML;
        }
    };

    // 초기 테마 설정
    setTheme(getPreferredTheme());

    // 활성 테마 표시하기
    const showActiveTheme = (theme, focus = false) => {
        const themeSwitcherText = document.querySelector(".bs-theme-text");
        const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`);

        // 모든 테마 버튼에서 active 클래스 제거
        document.querySelectorAll("[data-bs-theme-value]").forEach((element) => {
            element.classList.remove("active");
            element.setAttribute("aria-pressed", "false");
        });

        // 선택된 테마 버튼에 active 클래스 추가
        btnToActive.classList.add("active");
        btnToActive.setAttribute("aria-pressed", "true");
        const themeSwitcherLabel = `${themeSwitcherText.textContent} (${btnToActive.dataset.bsThemeValue})`;

        // 드롭다운 아이콘 업데이트
        updateDropdownIcon(theme);

        if (focus) {
            btnToActive.focus();
        }
    };

    // 시스템 테마 변경 감지
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => {
        const storedTheme = getStoredTheme();
        if (storedTheme !== "light" && storedTheme !== "dark") {
            setTheme(getPreferredTheme());
        }
    });

    // DOM 로드 완료 후 초기화
    window.addEventListener("DOMContentLoaded", () => {
        showActiveTheme(getPreferredTheme());

        // 모든 테마 토글 버튼에 클릭 이벤트 리스너 추가
        document.querySelectorAll("[data-bs-theme-value]").forEach((toggle) => {
            toggle.addEventListener("click", () => {
                const theme = toggle.getAttribute("data-bs-theme-value");
                setStoredTheme(theme);
                setTheme(theme);
                showActiveTheme(theme, true);
            });
        });
    });
})();
