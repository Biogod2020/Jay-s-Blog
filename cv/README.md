# Curriculum Vitae

The website publishes three CV formats from maintainable LaTeX sources:

- `Jia-Hao_Ji_CV.tex` - the primary one-page English research CV with portrait
- `Jia-Hao_Ji_Academic_CV.tex` - the complete two-page English academic CV
- `Jia-Hao_Ji_CV_zh.tex` - the one-page Chinese research CV with portrait

The one-page sources use the existing public portrait at `public/avatar.jpg`. All sources rely only on TeX Live packages; no private fonts or image assets are required.

## Build locally

From the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error cv/Jia-Hao_Ji_CV.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error cv/Jia-Hao_Ji_Academic_CV.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error cv/Jia-Hao_Ji_CV_zh.tex
```

The Chinese version uses `ctexart` with the TeX Live Fandol font set and must be compiled with XeLaTeX.

## Public URLs

The deployment workflow publishes:

- `/Jia-Hao_Ji_CV.pdf` - primary one-page English CV with portrait
- `/resume_long.pdf` - legacy-compatible alias of the one-page English CV
- `/Jia-Hao_Ji_Academic_CV.pdf` - complete two-page English academic CV
- `/Jia-Hao_Ji_CV_zh.pdf` - one-page Chinese CV with portrait

After editing a source, confirm the intended page count, render every page at high resolution, inspect the portrait crop and text layout, and verify fonts and hyperlinks before merging.
