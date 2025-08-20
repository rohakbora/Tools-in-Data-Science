---

marp: true
title: Product Documentation — Marp Demo
author: Rahul Bora — [23f1000897@ds.study.iitm.ac.in](mailto:23f1000897@ds.study.iitm.ac.in)
theme: custom-docs
paginate: true
footer: "Product Docs — \$page / \$pages"
-----------------------------------------

<style>
/* Custom Marp theme defined inline */
@theme custom-docs {
  section {
    background: #0b1220;
    color: #e6edf3;
    font-family: "Inter", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  }
  h1, h2, h3 { color: #93c5fd; }
  a { color: #60a5fa; }
  code { background: rgba(255,255,255,0.08); padding: 0.2em 0.4em; border-radius: 6px; }
  pre code { background: transparent; }
  blockquote { color: #a5b4fc; border-left: 4px solid #334155; padding-left: 12px; }
  footer { color: #9aa4b2; }
}
</style>

<!-- _class: lead -->

# Product Documentation

A maintainable, version-controlled presentation built with **Marp**.

**Author:** Rahul Bora
**Email:** [23f1000897@ds.study.iitm.ac.in](mailto:23f1000897@ds.study.iitm.ac.in)

---

<!-- A slide with a full-bleed background image -->

![bg cover](images/hero.jpg)

# Overview

Ship consistent docs across formats: **HTML**, **PDF**, **PPTX**.

---

## Repository Layout

```
product-docs/
├─ slides.md           # This file
├─ images/             # Assets used by slides
├─ themes/             # Optional external themes
└─ package.json        # Build scripts
```

* Maintain in Git for review & history.
* Export via CLI or VS Code Marp extension.

---

<!-- _header: **Install & Build** -->

## Tooling

```bash
# Local dev server
npx @marp-team/marp-cli -s .

# HTML for web
marp slides.md -o dist/slides.html

# PDF (allow local assets)
marp slides.md --pdf --allow-local-files

# PowerPoint
marp slides.md --pptx
```

> Tip: Add npm scripts (`start`, `build`, `pdf`, `pptx`) for one-liners.

---

<!-- _backgroundColor: #111827 -->

<!-- _color: #fca5a5 -->

## Versioning Strategy

* Treat slides like code (PRs, reviews, CI).
* Use semantic slide sections for stable anchors.
* Keep image assets small; prefer SVG when possible.

---

## Feature Specs (Example)

**Goal:** Document API rate limiting behavior.

```json
{
  "limit": 1200,
  "window": "1m",
  "burst": 100
}
```

* Include **sample requests**, **responses**, and **edge cases**.
* Link to changelog for backwards-incompatible updates.

---

## Algorithmic Complexity (Math)

We analyze the indexing algorithm:

Inline: \$O(n \log n)\$ for sort-and-merge.

Block math:

$$
T(n) = a\,T\!\left(\frac{n}{b}\right) + f(n)\\
T(n) = 2\,T\!\left(\frac{n}{2}\right) + n \;\Rightarrow\; T(n) = O(n\log n)
$$

---

## Theming & Branding

* Using the **custom-docs** theme defined inline via `@theme`.
* Override colors, typography, and component styles.

```css
/* themes/custom.css (optional external theme) */
section { font-size: calc(1.1vw + 1.1vh); }
```

---

## Background Variants

![bg fit](images/diagram.png)

* Use `![bg]`, `![bg fit]`, or `![bg cover]` for imagery.
* Keep high-contrast text for accessibility.

---

## Code Snippets

```python
from time import perf_counter

def benchmark(fn, *args, **kwargs):
    t0 = perf_counter(); result = fn(*args, **kwargs); t1 = perf_counter()
    return result, t1 - t0
```

```javascript
console.log("Build version:", process.env.GIT_COMMIT_SHA)
```

---

## Directives Showcase

<!-- _class: lead -->

* `_class: lead` for opening emphasis
* `_backgroundColor` and `_color` per-slide styling
* `_header` / `_footer` to add context

<!-- _footer: "Support: 23f1000897@ds.study.iitm.ac.in" -->

---

## Export Targets

* **HTML** for GitHub Pages
* **PDF** for formal review and archival
* **PPTX** for conference uploads

> Use CI to auto-build outputs on `main`.

---

## Thanks!

Docs contact: **[23f1000897@ds.study.iitm.ac.in](mailto:23f1000897@ds.study.iitm.ac.in)**

Questions? File an issue in the repo.
