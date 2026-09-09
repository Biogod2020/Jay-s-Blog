# Site maintenance and verification

## September 2026 editorial refactor

The existing article bodies and routes are retained. Shared layouts, language links, subscription feeds and build checks were replaced or consolidated. The site remains statically generated and has no server-side application endpoint, database, WeChat uploader or custom runner.

RSS/HTML checks validate generated output; browser checks cover the homepage, profile, archive, subscription page and a representative long article on desktop/mobile, plus a sample of legacy mathematics, diagrams and WebGL. They do not constitute a proof that every external source link and every interactive state works indefinitely.

`site-review` build artifacts include screenshots and individual audit reports. The dependency audit is separate from the rendering checks.

## Dependency security remains a separate maintenance task

The inherited package lock was kept during this layout refactor. The registry audit on 9 September 2026 reported 16 affected dependency entries: 1 critical, 9 high, 3 moderate and 3 low. Its suggested Astro remediation crosses major framework versions. A successful visual or RSS check must not be described as a clean security audit.

Several advisories concern development or server-rendered features, which are not public services on this static site. Other advisories concern build-time image processing, so static hosting does not eliminate all relevance. Only trusted source and image inputs should enter a build; do not expose the development server or attach unrelated credentials to pull-request jobs.

Upgrade the framework and associated image/build dependencies on a dedicated branch, migrate content APIs as required, regenerate the lock, rerun `npm audit` and all site/browser checks, and verify that every existing article URL still builds before merging. Avoid an unreviewed `npm audit fix --force` on the publishing branch.

## Search-engine verification

The code exposes crawlable HTML, robots.txt, sitemaps, canonical URLs, reciprocal language alternates, article metadata and structured data. Domain ownership and sitemap submission inside Google Search Console are account-level operations, not performed by a site build. Submission and structured data do not guarantee indexing or a particular search appearance.
