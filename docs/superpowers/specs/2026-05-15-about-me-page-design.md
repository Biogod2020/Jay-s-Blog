# About Me Page Integration Design Spec

## 1. Overview
Introduce a highly maintainable, standalone "About Me" page into the Astro blog. The page will feature an immersive, narrative-driven academic profile with a classic two-column sticky layout. Content will be driven entirely by a Markdown file to decouple the narrative text from UI components, ensuring future ease of maintenance.

## 2. Architecture & File Structure
- **Content Source**: `src/content/about/index.md` (or a standard markdown file in `src/pages` depending on current Astro setup).
  - Will house the newly drafted narrative text.
- **Astro Page**: `src/pages/about.astro`
  - The main route. Fetches and renders the Markdown content alongside the layout components.
- **UI Components**:
  - `ProfileSidebar.astro`: Left sticky sidebar containing the avatar, core contact details, and a Call-To-Action (CTA) button linking to the PDF resume.
- **Navigation Update**: 
  - Modify the existing blog header/navigation component to include a prominent "About Me" link pointing to `/about`.

## 3. UI/UX Design & Layout
- **Desktop Layout**: 
  - Two-column CSS Grid.
  - Left column: Sticky positioning (`sticky top-8`), acting as a persistent business card.
  - Right column: Scrollable prose section.
- **Mobile Layout**:
  - Responsive single-column stack. Profile info renders at the top, narrative scrolls below.
- **Styling**: 
  - Utilize Tailwind's `@tailwindcss/typography` plugin (`prose`, `prose-slate`, `prose-a:text-blue-600`) for elegant, out-of-the-box reading aesthetics.

## 4. Narrative Content Structure (Written from Scratch)
The Markdown content will be structured into three main narrative arcs, avoiding raw resume bullet points:
1. **The Intersection of Medicine & AI**: Contextualizing the MD candidate background with computational research at MSRA.
2. **Engineering for Biology**: Narrative storytelling behind the creation of `SpatialDataAgent` and autonomous spatial omics tools.
3. **Future Outlook**: A closing vision on the integration of foundation models with clinical neuroscience.

## 5. Asset Management
- Transfer `resume_long.pdf` (and the profile avatar if not already present) into the blog's `public/` directory (e.g., `public/resume_long.pdf`) to ensure reliable static linking from the download button.
