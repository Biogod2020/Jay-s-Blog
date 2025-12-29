import os
import glob

def build():
    # Helper to read file content
    def read_file(path):
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return ""

    # HTML Skeleton
    header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TeamPath Presentation</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body class="antialiased">
    <div id="presentation-container">
"""

    footer = """
    </div>

    <!-- Lightbox Modal -->
    <div id="lightbox" class="lightbox hidden">
        <div class="lightbox-controls">
            <span class="lightbox-hint">Scroll to Zoom • Drag to Pan • Double Click to Reset</span>
            <button id="lightbox-close" class="lightbox-btn" title="Close">×</button>
        </div>
        <div class="lightbox-content">
            <img id="lightbox-img" src="" alt="Zoom View">
        </div>
    </div>

    <!-- Navigation Controls -->
    <div class="controls">
        <button id="prevBtn" class="control-btn" title="Previous Slide (Arrow Left)">←</button>
        <button id="nextBtn" class="control-btn" title="Next Slide (Arrow Right/Space)">→</button>
    </div>
    <div class="slide-counter">
        <span id="currentSlide">1</span> / <span id="totalSlides">0</span>
    </div>

    <script src="js/main.js"></script>
</body>
</html>
"""

    # Get all partials sorted by name
    partials_dir = "partials"
    partial_files = sorted(glob.glob(os.path.join(partials_dir, "*.html")))
    
    slides_content = ""
    for p_file in partial_files:
        content = read_file(p_file)
        # Wrap each partial in a slide div
        slides_content += f'\n        <div class="slide">\n            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">\n{content}\n            </div>\n        </div>\n'

    # Combine
    full_html = header + slides_content + footer

    # Write output
    with open("index.html", "w", encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Build complete! Generated index.html with {len(partial_files)} slides.")

if __name__ == "__main__":
    build()
