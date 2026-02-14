---
layout: docs
title: Jiny Website Implementation Guide
description: Guidelines for AI to maintain consistency in the Jekyll website implementation.
keywords: jekyll, guide, implementation, ai
url: /site/
---

# Jiny Website Implementation Guide

This document serves as a comprehensive guide for AI assistants and developers to maintain consistency when working on the **Jiny Big Data Analysis** lecture site.

## 1. Project Overview

-   **Framework**: Jekyll 4.x
-   **Templating**: Liquid
-   **Styling**: Bootstrap 5 + Custom CSS (`docs.css`)
-   **Source Directory**: `src`
-   **Output Directory**: `docs` (configured for GitHub Pages)
-   **Repository Structure**:
    ```text
    /
    ├── src/                # Content and Source
    │   ├── _data/          # Data files (navigation.yml)
    │   ├── _includes/      # Partial templates (header, sidebar, footer)
    │   ├── _layouts/       # Page layouts (docs, bootstrap, default)
    │   ├── assets/         # CSS, JS, Images
    │   ├── 01_week/        # Lecture content directories
    │   └── index.md        # Landing page
    ├── docs/               # Generated static site (do not edit directly)
    ├── _config.yml         # Jekyll configuration
    └── Gemfile             # Ruby dependencies
    ```

## 2. Layout System

### Key Layout Files (`src/_layouts/`)

1.  **`bootstrap.html`**
    *   **Role**: The master wrapper.
    *   **Content**: HTML5 boilerplate, `<head>` (meta, CSS links), `<body>`, header/footer includes, and JS scripts.
    *   **Critical**: Contains **inline CSS** overrides for global elements like blockquotes and tables. **Edit this file for global style fixes.**

2.  **`default.html`**
    *   **Role**: Intermediate layout.
    *   **Usage**: Usually just sets `layout: docs` or `layout: bootstrap`.

3.  **`docs.html`**
    *   **Role**: The standard documentation layout.
    *   **Structure**:
        *   **Left Sidebar**: Navigation menu (responsive offcanvas).
        *   **Main Content**: Lecture notes (`{{ content }}`).
        *   **Right Sidebar**: Table of Contents (TOC), visible on large screens.
    *   **Features**: Includes Breadcrumbs and Page Title automatically.

### Usage Rule
*   **Lecture Notes**: ALWAYS use `layout: docs` in front matter.
*   **Landing Pages**: Use `layout: docs` (or `default` if strictly minimal).

## 3. Content Guidelines (Markdown)

### Front Matter Standard
Every lecture file (`.md`) MUST have:
```yaml
---
layout: docs
title: [Lecture Title]
description: [Short Summary]
keywords: [comma, separated, tags]
url: /[week_folder]/[filename]/  # Optional, but creating explicit URLs is safer
---
```

### Image Handling
*   **Storage**: Place images in `src/assets/img/` or specific week folders like `src/01_week/img/`.
*   **Syntax**: `![Alt Text](/path/to/image.png)`
*   **Styling**: Images are globally styled to be responsive:
    ```css
    img {
        max-width: 100%;
        height: auto;
    }
    ```
    *Do not hardcode width unless creating a specific thumbnail.*

### Callouts & Blockquotes
*   **Note/Tip**: Use standard blockquotes.
    ```markdown
    > **Note**: This is a standard note style.
    ```
*   **Visual**: Rendered with a light gray background (`#f8f9fa`) and gray left border (`#dee2e6`) for a neutral, clean look.

### Code Blocks
*   Use triple backticks with language:
    ```python
    def hello():
        print("world")
    ```
*   **Mermaid**: Use `mermaid` language for diagrams (rendered clientside via JS).

## 4. Navigation System

### Sidebar Configuration
*   **File**: `src/_data/navigation.yml`
*   **Structure**:
    ```yaml
    main:
      - title: Week 1
        subitems:
          - title: Intro
            url: /01_week/01_intro.html
    ```
*   **Logic**:
    *   Top-level items become collapsible groups.
    *   `subitems` become links within the group.
    *   The Sidebar automatically adds `active` classes based on the current page URL.

### Adding New Content
1.  Create markdown file in appropriate `src/XX_week/` folder.
2.  Add Front Matter.
3.  **Crucial**: Add entry to `src/_data/navigation.yml` to appear in the sidebar.

## 5. Styling & CSS

*   **Framework**: Bootstrap 5 (loaded via CDN or local minified CSS).
*   **Custom Styles**: `src/assets/css/docs.css`.
    *   Use this for component-specific overrides (e.g., Sidebar styling, TOC positioning).
*   **Inline Overrides**: Found in `src/_layouts/bootstrap.html`.
    *   Why? For high-priority overrides that persist across layouts.
    *   Current overrides: Blockquote styles, Image responsiveness, Header link decoration.

## 6. Build & Deployment

### Local Development
*   **Start Server**:
    ```bash
    bundle exec jekyll serve
    ```
    *Access at `http://localhost:4000`*

### Production Build
*   **Build Command**:
    ```bash
    bundle exec jekyll build
    ```
    *Generated files go to `docs/` folder.*

## 7. AI Maintenance Checklist
When the user asks for changes, check these areas:
-   [ ] **New Page?** -> Check `navigation.yml`.
-   [ ] **Style Change?** -> Check `docs.css` first, then `bootstrap.html` for inline styles.
-   [ ] **Layout Issue?** -> Check `docs.html` or `_includes/sidebar.html`.
-   [ ] **Image Issue?** -> Verify `max-width: 100%` rule.

---
*Created by Antigravity Agent on 2026-02-14*
