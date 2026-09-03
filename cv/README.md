# Academic CV

The website CV is generated from `Jia-Hao_Ji_CV.tex` during pull-request and production builds.

## Build locally

```bash
cd cv
latexmk -pdf -interaction=nonstopmode -halt-on-error Jia-Hao_Ji_CV.tex
```

The source is intentionally pdfLaTeX-compatible and uses the TeX Live `lato` package, so no private or system font files are required.

The deployment workflow copies the compiled PDF to both:

- `/Jia-Hao_Ji_CV.pdf` — canonical public URL
- `/resume_long.pdf` — legacy-compatible alias

After editing the CV, render both A4 pages and inspect them before merging.
