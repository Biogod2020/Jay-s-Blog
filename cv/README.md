# Curriculum Vitae

The website publishes two PDF versions from maintainable pdfLaTeX sources:

- `Jia-Hao_Ji_One_Page_CV.tex` — the primary one-page research CV with profile photo
- `Jia-Hao_Ji_CV.tex` — the complete two-page academic CV

The profile photo is read from `../public/avatar.jpg`; no private font or image assets are required.

## Build locally

```bash
cd cv
latexmk -pdf -interaction=nonstopmode -halt-on-error Jia-Hao_Ji_One_Page_CV.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error Jia-Hao_Ji_CV.tex
```

Both sources are pdfLaTeX-compatible and use TeX Live packages only.

## Public URLs

The deployment workflow publishes:

- `/Jia-Hao_Ji_CV.pdf` — primary one-page CV
- `/resume_long.pdf` — legacy-compatible alias of the one-page CV
- `/Jia-Hao_Ji_Academic_CV.pdf` — complete two-page academic CV

After editing either source, confirm the page count, render every page at high resolution, inspect for clipping or overlap, and verify that fonts and hyperlinks remain intact before merging.
