---

marp: true
math: katex
paginate: true
headingDivider: 2
size: 16:9
color: #e5e7eb
backgroundColor: #0b1220
style: |
section {
padding: 56px;
}
footer {
font-size: 0.8rem;
color: #9ca3af;
}
/\* Use the theme by name */
section.product-docs h1, section.product-docs h2 {
letter-spacing: 0.2px;
}
section.product-docs strong {
color: #8b5cf6; /* accent \*/
}
section.product-docs .pill {
display: inline-block;
padding: 0.25rem 0.6rem;
border: 1px solid #374151;
border-radius: 999px;
font-size: 0.9rem;
}

# Use a custom Marp theme

# (Declared below via `<style>` with `@theme`)

theme: product-docs
footer: 'Page \${page} / \${total}'
-----------------------------------

<!-- _class: product-docs lead -->

# Product Documentation

### Built with **Marp** for maintainability

* Version-controlled Markdown → HTML / PDF / PPTX
* Developer-friendly: reviews & diffs in PRs
* Presenter-friendly: live speaker notes

**Author:** [23f1000897@ds.study.iitm.ac.in](mailto:23f1000897@ds.study.iitm.ac.in)

---

<!-- _class: product-docs -->

## Why Marp for Docs Presentations?

* Single source of truth: `slides.md` in repo
* Convert via CLI: `marp slides.md --html --pdf`
* Theming via CSS; brand-ready
* Works with GitHub Pages

**Tip:** Add a CI job to export HTML/PDF on every push.

---

<!-- _class: product-docs -->

## Background Image Slide

![bg](assets/product-hero.jpg)

> Showcase the product UI or an architectural diagram as the background.

---

<!-- _class: product-docs -->

## Algorithmic Complexity (Math)

We analyze the end-to-end pipeline complexity:

$T(n) = T_1(n) + T_2(n) = O(n \log n) + O(n) = O(n \log n)$

For amortized cost of batched updates:

$\bar{c} = \frac{\sum_{i=1}^{m} c_i}{m}$

---

<!-- _class: product-docs -->

## Code Snippet (fenced)

```ts
// Minimal typed API client
export async function getUser(id: string) {
  const r = await fetch(`/api/users/${id}`);
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return (await r.json()) as { id: string; name: string };
}
```

---

<!-- _class: product-docs -->

## Release Packaging

* **CLI**: `marp slides.md -o dist/index.html`
* **PDF**: `marp slides.md -o dist/slides.pdf`
* **PPTX**: `marp slides.md -o dist/slides.pptx`
* **Pages**: publish `dist/` to GitHub Pages

**Footnote:** Keep `assets/` checked in so images resolve.

---

<!-- _class: product-docs -->

## Contact

**Technical Writer:** [23f1000897@ds.study.iitm.ac.in](mailto:23f1000897@ds.study.iitm.ac.in)

* Repo contains `slides.md`, `theme.css` (inlined below), and `assets/`.
* Use PRs for copy reviews and versioning.

---

<!--
  Custom theme definition embedded in this Markdown
  You can also extract this into `theme-product-docs.css` and reference it via `--theme` CLI flag.
-->

<style>
/* @theme product-docs */
@import "uncover";

:root {
  --background-color: #0b1220;
  --foreground-color: #e5e7eb;
  --accent: #8b5cf6;
  --muted: #9ca3af;
  --slide-border: #111827;
}

section {
  /* Subtle border and elevated look */
  box-shadow: 0 10px 30px rgba(0,0,0,0.35);
  border: 1px solid var(--slide-border);
}

section h1, section h2, section h3 {
  color: var(--foreground-color);
}

section a { color: var(--accent); }

section.lead h1 {
  font-size: 2.6em;
}

/* Page number styling (works with footer paginate) */
footer {
  letter-spacing: .02em;
}
</style>
