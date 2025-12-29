document.addEventListener('DOMContentLoaded', () => {
    // --- Slide Navigation Logic ---
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const currentSlideSpan = document.getElementById('currentSlide');
    const totalSlidesSpan = document.getElementById('totalSlides');
    let currentIndex = 0;

    if (slides.length > 0) {
        totalSlidesSpan.textContent = slides.length;
        
        // Initial fade/slide setup
        showSlide(currentIndex);

        function showSlide(index) {
            slides.forEach((slide, i) => {
                slide.classList.toggle('active', i === index);
            });
            currentSlideSpan.textContent = index + 1;
            
            prevBtn.disabled = index === 0;
            nextBtn.disabled = index === slides.length - 1;

            window.scrollTo(0, 0);
        }

        function nextSlide() {
            if (currentIndex < slides.length - 1) {
                currentIndex++;
                showSlide(currentIndex);
            }
        }

        function prevSlide() {
            if (currentIndex > 0) {
                currentIndex--;
                showSlide(currentIndex);
            }
        }

        nextBtn.addEventListener('click', nextSlide);
        prevBtn.addEventListener('click', prevSlide);

        document.addEventListener('keydown', (e) => {
            if (document.getElementById('lightbox').classList.contains('hidden')) {
                // Only navigate if lightbox is closed
                if (e.key === 'ArrowRight' || e.key === 'Space') {
                    // Prevent default space scrolling
                    if(e.key === 'Space') e.preventDefault();
                    nextSlide();
                } else if (e.key === 'ArrowLeft') {
                    prevSlide();
                }
            } else {
                // Lightbox shortcuts
                if (e.key === 'Escape') closeLightbox();
            }
        });
    }

    // --- Lightbox Logic ---
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.getElementById('lightbox-close');
    const allImages = document.querySelectorAll('.slide img'); // Select all images within slides

    let scale = 1;
    let pointX = 0;
    let pointY = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;

    // Open Lightbox
    allImages.forEach(img => {
        img.style.cursor = 'zoom-in';
        img.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent bubbling
            openLightbox(img.src);
        });
    });

    function openLightbox(src) {
        lightboxImg.src = src;
        lightbox.classList.remove('hidden');
        document.body.style.overflow = 'hidden'; // Disable scroll
        resetZoom();
    }

    function closeLightbox() {
        lightbox.classList.add('hidden');
        document.body.style.overflow = ''; // Enable scroll
    }

    closeBtn.addEventListener('click', closeLightbox);
    
    // Close on background click (optional, but good UX)
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox || e.target.classList.contains('lightbox-content')) {
            closeLightbox();
        }
    });

    // Reset Zoom
    function resetZoom() {
        scale = 1;
        pointX = 0;
        pointY = 0;
        updateTransform();
    }
    
    // Reset on double click
    lightboxImg.addEventListener('dblclick', resetZoom);

    // Zoom (Wheel)
    lightbox.addEventListener('wheel', (e) => {
        e.preventDefault();
        const delta = e.deltaY > 0 ? -0.1 : 0.1;
        const newScale = scale + delta;
        
        // Limit zoom
        if (newScale > 0.5 && newScale < 5) {
            scale = newScale;
            updateTransform();
        }
    });

    // Pan (Drag)
    lightboxImg.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.clientX - pointX;
        startY = e.clientY - pointY;
        lightboxImg.style.cursor = 'grabbing';
        e.preventDefault(); // Prevent default drag behavior
    });

    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        e.preventDefault();
        pointX = e.clientX - startX;
        pointY = e.clientY - startY;
        updateTransform();
    });

    window.addEventListener('mouseup', () => {
        isDragging = false;
        lightboxImg.style.cursor = 'grab';
    });

    function updateTransform() {
        lightboxImg.style.transform = `translate(${pointX}px, ${pointY}px) scale(${scale})`;
    }
});
