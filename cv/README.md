# One-Page Research CV

The website CV is generated from `Jia-Hao_Ji_CV.tex` during pull-request and production builds. It is designed as a single A4 research resume and uses the existing public profile image at `public/avatar.jpg`.

## Build locally

From the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error cv/Jia-Hao_Ji_CV.tex
```

The source is pdfLaTeX-compatible and uses the TeX Live `lato` package, so no private or system font files are required.

The deployment workflow copies the compiled PDF to both:

- `/Jia-Hao_Ji_CV.pdf` - canonical public URL
- `/resume_long.pdf` - legacy-compatible alias

After editing the CV, confirm that the output remains exactly one A4 page, then render it at high resolution and inspect the portrait crop, text wrapping, column alignment, and hyperlinks before merging.
