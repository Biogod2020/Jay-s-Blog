# Curriculum Vitae

The website publishes two CV formats from maintainable pdfLaTeX sources:

- `Jia-Hao_Ji_CV.tex` - the primary one-page research CV with portrait
- `Jia-Hao_Ji_Academic_CV.tex` - the complete two-page academic CV

The one-page source uses the existing public portrait at `public/avatar.jpg`. Both sources use TeX Live packages only; no private fonts or image assets are required.

## Build locally

From the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error cv/Jia-Hao_Ji_CV.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error cv/Jia-Hao_Ji_Academic_CV.tex
```

## Public URLs

The deployment workflow publishes:

- `/Jia-Hao_Ji_CV.pdf` - primary one-page CV with portrait
- `/resume_long.pdf` - legacy-compatible alias of the one-page CV
- `/Jia-Hao_Ji_Academic_CV.pdf` - complete two-page academic CV

After editing either source, confirm the intended page count, render every page at high resolution, inspect the portrait crop and text layout, and verify fonts and hyperlinks before merging.
