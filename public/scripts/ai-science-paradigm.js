/*
 * Alex Chen's Frontend Experience Architecture (v3.1 - Narrative Reflow Edition)
 */
const LectureExperience = {
    isReducedMotion: window.matchMedia('(prefers-reduced-motion: reduce)').matches,
    typedInstance: null,
   
    init() {
        gsap.registerPlugin(ScrollTrigger);
        this.initTOC();
        this.initMermaid();
        this.initVisualizations();
    },
    initVisualizations() {
        // Didactic animations for core concepts
        this.createParadigm1Viz();
        this.createParadigm2Viz();
        // Core interactive D3 visualizations
        this.createManhattanPlot();
        this.createNnTrainingViz();
        this.createCorrelationPlot();
        // Process and structure visualizations
        this.initTokenizationViz();
        this.initSmileMatrix();
        // AI mechanism animations
        this.createNeuralNetworkAnimation();
        this.createPredictionEngineViz();
       
        // Explainable AI interactive element
        this.createXaiHeatmapViz();
       
        // Dynamic text for case study
        this.initTypedJS();
    },
   

    initTOC() {
        const tocList = document.getElementById('toc-list');
        const headings = document.querySelectorAll('#content h2[id], #content h3[id]');
        if (!tocList || headings.length === 0) return;
        
        headings.forEach(heading => {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.textContent = heading.textContent;
            a.href = `#${heading.id}`;
            a.dataset.targetId = heading.id;
            if(heading.tagName === 'H3') { li.className = 'toc-level-3'; }
            li.appendChild(a);
            tocList.appendChild(li);
        });
        
        const tocLinks = tocList.querySelectorAll('a');
        const indicator = document.getElementById('toc-indicator');
        
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                const id = entry.target.getAttribute('id');
                const link = tocList.querySelector(`a[href="#${id}"]`);
                if (entry.isIntersecting && entry.intersectionRatio > 0.5) {
                    tocLinks.forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                    if (!this.isReducedMotion && link && indicator) {
                        gsap.to(indicator, { top: link.offsetTop, height: link.offsetHeight, duration: 0.4, ease: 'power3.out' });
                    }
                }
            });
        }, { rootMargin: "-50% 0px -50% 0px", threshold: [0, 0.5, 1] });
        
        headings.forEach(heading => observer.observe(heading));
    },
    initMermaid() { mermaid.initialize({ startOnLoad: true, theme: 'default' }); },
   
    // --- Visualization Modules ---
    createParadigm1Viz() {
        // Objective: Animate Mendel's experiment to make it a dynamic story, not a static image.
        const svg = d3.select("#paradigm1-viz");
        const plant1 = svg.append("g").attr("id", "plant1");
        plant1.append("rect").attr("x", 50).attr("y", 100).attr("width", 10).attr("height", 60).attr("fill", "#38a169");
        plant1.append("circle").attr("cx", 55).attr("cy", 90).attr("r", 15).attr("fill", "#38a169");
        plant1.append("text").attr("x", 55).attr("y", 180).attr("text-anchor", "middle").text("Pure Tall (TT)");
       
        const plant2 = svg.append("g").attr("id", "plant2");
        plant2.append("rect").attr("x", 150).attr("y", 120).attr("width", 10).attr("height", 40).attr("fill", "#68d391");
        plant2.append("circle").attr("cx", 155).attr("cy", 110).attr("r", 15).attr("fill", "#68d391");
        plant2.append("text").attr("x", 155).attr("y", 180).attr("text-anchor", "middle").text("Pure Short (tt)");
        const cross = svg.append("g").attr("id", "cross-arrow");
        cross.append("path").attr("d", "M 100 80 Q 200 40 300 80").attr("stroke", "var(--color-text)").attr("fill", "none").attr("stroke-width", 2);
        cross.append("path").attr("d", "M 295 70 L 300 80 L 290 80 Z").attr("fill", "var(--color-text)");
        const offspring = svg.append("g").attr("id", "offspring");
        offspring.append("rect").attr("x", 300).attr("y", 100).attr("width", 10).attr("height", 60).attr("fill", "#38a169");
        offspring.append("circle").attr("cx", 305).attr("cy", 90).attr("r", 15).attr("fill", "#38a169");
        offspring.append("text").attr("x", 305).attr("y", 180).attr("text-anchor", "middle").text("Hybrid Tall (Tt)");
       
        if (!this.isReducedMotion) {
            gsap.set([plant1.node(), plant2.node(), cross.node(), offspring.node()], { autoAlpha: 0 });
            const tl = gsap.timeline({ scrollTrigger: { trigger: svg.node(), start: "top 80%" } });
            tl.to([plant1.node(), plant2.node()], { autoAlpha: 1, y: -10, stagger: 0.2, duration: 0.5, ease: 'power2.out' })
              .to(cross.node(), { autoAlpha: 1, scale: 1.1, duration: 0.4, ease: 'back.out(1.7)', transformOrigin: 'center' }, "-=0.2")
              .to(offspring.node(), { autoAlpha: 1, y: -10, duration: 0.5, ease: 'power2.out' });
        }
    },
    createParadigm2Viz() {
        // Objective: Visually represent the concept of a theoretical model by animating planetary motion.
        const svg = d3.select("#paradigm2-viz");
        svg.append("circle").attr("cx", 200).attr("cy", 100).attr("r", 20).attr("fill", "#f6e05e");
        const orbit = svg.append("ellipse").attr("cx", 200).attr("cy", 100).attr("rx", 150).attr("ry", 50).attr("class", "orbit-path").attr("fill", "none").attr("stroke-width", 2);
        const earth = svg.append("circle").attr("id", "earth").attr("r", 8);
        const formula = svg.append("text").attr("x", 200).attr("y", 180).attr("text-anchor", "middle").style("font-family", "monospace").style("font-size", "1.2em").text("F = G(m₁m₂)/r²");
        if (!this.isReducedMotion) {
            gsap.set(earth.node(), { transformOrigin: "200px 100px" });
            gsap.to(earth.node(), {
                duration: 8,
                repeat: -1,
                ease: "none",
                motionPath: {
                    path: orbit.node(),
                    align: orbit.node(),
                    alignOrigin: [0.5, 0.5]
                },
            });
            gsap.from(formula.node(), {
                scrollTrigger: { trigger: svg.node(), start: "top 80%" },
                autoAlpha: 0, y: 20, duration: 0.8, ease: "power2.out"
            });
        } else {
             earth.attr("cx", 350).attr("cy", 100);
        }
    },
    createManhattanPlot() { /* Unchanged: this is a robust, data-driven D3 plot that works well. */ const container = d3.select("#manhattan-plot-container"); container.selectAll("*").remove(); const width = container.node().getBoundingClientRect().width; const height = 400; const margin = { top: 20, right: 20, bottom: 40, left: 50 }; const numPoints = 1000; const data = d3.range(numPoints).map(i => { let pValue = Math.pow(10, -Math.random() * 5); if (Math.sin(i/50) > 0.95 || Math.sin(i/150) > 0.98) { pValue = Math.pow(10, - (7 + Math.random() * 5)); } return { pos: i, negLogP: -Math.log10(pValue), pValue: pValue }; }); const significanceThreshold = 7.3; const xScale = d3.scaleLinear().domain([0, numPoints]).range([margin.left, width - margin.right]); const yScale = d3.scaleLinear().domain([0, d3.max(data, d => d.negLogP) + 1]).range([height - margin.bottom, margin.top]); const svg = container.append("svg").attr("viewBox", `0 0 ${width} ${height}`); svg.append("g").attr("transform", `translate(0, ${height - margin.bottom})`).call(d3.axisBottom(xScale).ticks(5)); svg.append("g").attr("transform", `translate(${margin.left}, 0)`).call(d3.axisLeft(yScale)); svg.append("text").attr("class", "axis-label").attr("x", width / 2).attr("y", height - 5).text("Genomic Position"); svg.append("text").attr("class", "axis-label").attr("transform", "rotate(-90)").attr("x", -height / 2).attr("y", 15).attr("text-anchor", "middle").text("-log10(P-value)"); const tooltip = d3.select("#tooltip"); const significanceLine = svg.append("line").attr("class", "significance-line").attr("x1", margin.left).attr("x2", width - margin.right).attr("y1", yScale(significanceThreshold)).attr("y2", yScale(significanceThreshold)); const dots = svg.selectAll(".snp-dot").data(data).enter().append("circle").attr("class", "snp-dot").attr("cx", d => xScale(d.pos)).attr("cy", d => yScale(d.negLogP)).attr("r", 3).style("fill", d => d.negLogP > significanceThreshold ? 'var(--plot-significant-color)' : 'var(--color-primary)').attr("opacity", 0.7).on("mouseover", (event, d) => tooltip.style("opacity", 1).html(`SNP pos: ${d.pos}<br>p-value: ${d.pValue.toExponential(2)}`)).on("mousemove", (event) => tooltip.style("left", (event.pageX + 15) + "px").style("top", (event.pageY - 28) + "px")).on("mouseout", () => tooltip.style("opacity", 0)); if (!this.isReducedMotion) { gsap.from(dots.nodes(), { scrollTrigger: { trigger: "#manhattan-plot-container", start: "top 80%" }, attr: { r: 0 }, duration: 1, ease: "elastic.out(1, 0.5)", stagger: 0.002 }); gsap.from(significanceLine.node(), { scrollTrigger: { trigger: "#manhattan-plot-container", start: "top 80%" }, opacity: 0, duration: 0.5, delay: 0.5 }); } },
    initTokenizationViz() { /* Unchanged: Clear, effective process visualization. */ const dna = "ATTCGATTACAGATTACA"; const k = 3; const tokensContainer = document.querySelector('#tokenization-viz .tokens-container'); const vectorsContainer = document.querySelector('#tokenization-viz .vectors-container'); let tokens = []; for (let i = 0; i <= dna.length - k; i++) { tokens.push(dna.substring(i, i + k)); } tokens.forEach(token => { const span = document.createElement('span'); span.className = 'token-span'; span.textContent = token; tokensContainer.appendChild(span); const vectorDiv = document.createElement('div'); vectorDiv.className = 'vector-viz'; for (let j = 0; j < 5; j++) { const bar = document.createElement('div'); bar.className = 'vector-bar'; bar.style.height = `${Math.random() * 20 + 5}px`; vectorDiv.appendChild(bar); } vectorsContainer.appendChild(vectorDiv); }); if (!this.isReducedMotion) { gsap.from("#tokenization-viz .token-span", { scrollTrigger: { trigger: "#tokenization-viz", start: "top 80%" }, opacity: 0, y: -20, scale: 0.5, stagger: 0.1, duration: 0.5, ease: 'back.out(1.7)' }); gsap.from("#tokenization-viz .vector-viz", { scrollTrigger: { trigger: "#tokenization-viz", start: "top 60%" }, opacity: 0, y: 20, stagger: 0.1, duration: 0.5, ease: 'power2.out', delay: 0.5 }); } },
    initSmileMatrix() { /* Unchanged: Simple, effective, and interactive. */ const table = document.getElementById('smile-matrix-table'); const slider = document.getElementById('opacity-slider'); const matrix = [ [0,0,1,1,1,1,0,0],[0,1,0,0,0,0,1,0],[1,0,1,0,0,1,0,1],[1,0,0,0,0,0,0,1], [1,0,1,0,0,1,0,1],[1,0,0,1,1,0,0,1],[0,1,0,0,0,0,1,0],[0,0,1,1,1,1,0,0] ]; matrix.forEach(rowData => { const row = table.insertRow(); rowData.forEach(cellData => { const cell = row.insertCell(); cell.className = cellData === 1 ? 'pixel-on' : 'pixel-off'; }); }); slider.addEventListener('input', (e) => { table.style.setProperty('--pixel-opacity', e.target.value); table.querySelectorAll('.pixel-on').forEach(cell => cell.style.opacity = e.target.value); }); },
    createNnTrainingViz() {
        // Objective: Animate the core concept of 'learning' as a process of function fitting.
        const container = d3.select("#nn-training-viz");
        container.selectAll("*").remove();
        const width = 500, height = 300;
        const margin = { top: 20, right: 20, bottom: 30, left: 40 };
        const svg = container.append("svg").attr("viewBox", `0 0 ${width} ${height}`);
        const data = d3.range(50).map(() => ({ x: Math.random() * 10, y: 2 * Math.random() * 10 + 3 + (Math.random() - 0.5) * 5 }));
        const xScale = d3.scaleLinear().domain([0, 10]).range([margin.left, width - margin.right]);
        const yScale = d3.scaleLinear().domain([d3.min(data, d => d.y), d3.max(data, d => d.y)]).range([height - margin.bottom, margin.top]);
       
        svg.append("g").attr("transform", `translate(0, ${height - margin.bottom})`).call(d3.axisBottom(xScale));
        svg.append("g").attr("transform", `translate(${margin.left}, 0)`).call(d3.axisLeft(yScale));
       
        svg.selectAll(".data-point").data(data).enter().append("circle").attr("class", "data-point").attr("cx", d => xScale(d.x)).attr("cy", d => yScale(d.y)).attr("r", 4).attr("opacity", 0.7);
       
        const line = svg.append("line").attr("class", "regression-line");
        if (!this.isReducedMotion) {
            gsap.fromTo(line.node(), { attr: { x1: xScale(0), y1: yScale(15), x2: xScale(10), y2: yScale(5) } }, {
                attr: { y1: yScale(3), y2: yScale(23) },
                duration: 2, ease: "power2.inOut",
                scrollTrigger: { trigger: container.node(), start: "top 70%", toggleActions: "play pause resume reverse" }
            });
        } else {
             line.attr("x1", xScale(0)).attr("y1", yScale(3)).attr("x2", xScale(10)).attr("y2", yScale(23));
        }
    },
    createNeuralNetworkAnimation() { /* Unchanged: A complex animation that clearly illustrates forward propagation. */ const container = d3.select("#nn-viz-container"); container.selectAll("*").remove(); const width = container.node().getBoundingClientRect().width; const height = 250; const svg = container.append("svg").attr("viewBox", `0 0 ${width} ${height}`); const layers = [ { count: 4, x: 50 }, { count: 6, x: width / 2 - 50 }, { count: 6, x: width / 2 + 50 }, { count: 2, x: width - 50 } ]; const nodes = [], links = []; layers.forEach((layer, i) => { const layerNodes = d3.range(layer.count).map(j => ({ layer: i, id: `n-${i}-${j}`, x: layer.x, y: (height / (layer.count + 1)) * (j + 1) })); nodes.push(...layerNodes); if (i > 0) { layerNodes.forEach(node => { layers[i - 1].nodes.forEach(prevNode => links.push({ source: prevNode, target: node })); }); } layer.nodes = layerNodes; }); svg.selectAll('.nn-connection').data(links).enter().append('line').attr('class', 'nn-connection').attr('x1', d => d.source.x).attr('y1', d => d.source.y).attr('x2', d => d.target.x).attr('y2', d => d.target.y); const nodeElements = svg.selectAll('.nn-neuron').data(nodes).enter().append('circle').attr('class', 'nn-neuron').attr('id', d => d.id).attr('cx', d => d.x).attr('cy', d => d.y).attr('r', 8); if (!this.isReducedMotion) { const tl = gsap.timeline({ scrollTrigger: { trigger: '#nn-viz-container', start: 'top 70%', toggleActions: 'play restart play reverse' }, }); const animateSignal = (path) => { const signal = svg.append('circle').attr('class', 'nn-signal').attr('r', 5).attr('cx', path[0].x).attr('cy', path[0].y).style('opacity', 0); tl.to(signal.node(), { opacity: 1, duration: 0.1 }); for(let i = 0; i < path.length; i++) { tl.to(`#${path[i].id}`, { classList: "+=activated", duration: 0.1 }, "<"); if (i < path.length - 1) { tl.to(signal.node(), { motionPath: { path: [path[i], path[i+1]] }, duration: 0.4, ease: 'power1.inOut' }); } } tl.to(signal.node(), { opacity: 0, duration: 0.2 }); }; const path1 = [layers[0].nodes[1], layers[1].nodes[2], layers[2].nodes[0], layers[3].nodes[1]]; const path2 = [layers[0].nodes[2], layers[1].nodes[4], layers[2].nodes[3], layers[3].nodes[0]]; animateSignal(path1); tl.add(() => animateSignal(path2), ">-0.5"); tl.add(() => nodeElements.classed('activated', false), "+=0.5"); } },
    createPredictionEngineViz() {
        // Objective: Animate the data flow to clearly show the "input -> black box -> output" process.
        const svg = d3.select("#prediction-engine-viz");
        svg.selectAll("*").remove(); // Clear previous content
        svg.append("text").attr("x", 50).attr("y", 50).text("Input: X_new");
        svg.append("path").attr("d", "M50 80 C 60 60, 80 60, 90 80 S 120 100, 130 80").attr("stroke", "var(--color-primary)").attr("fill", "none").attr("stroke-width", 2);
        svg.append("line").attr("x1", 150).attr("y1", 90).attr("x2", 200).attr("y2", 90).attr("stroke", "var(--color-text)").attr("stroke-width", 2).attr("marker-end", "url(#arrow)");
        svg.append("rect").attr("x", 210).attr("y", 60).attr("width", 100).attr("height", 60).attr("rx", 5).attr("class", "ai-box");
        svg.append("text").attr("x", 260).attr("y", 95).attr("text-anchor", "middle").text("AI Model f̂");
        svg.append("line").attr("x1", 320).attr("y1", 90).attr("x2", 370).attr("y2", 90).attr("stroke", "var(--color-text)").attr("stroke-width", 2).attr("marker-end", "url(#arrow)");
        svg.append("text").attr("x", 425).attr("y", 50).attr("text-anchor", "middle").text("Output: Y_pred");
        svg.append("rect").attr("x", 380).attr("y", 70).attr("width", 90).attr("height", 40).attr("rx", 5).attr("fill", "var(--color-highlight-bg)");
        svg.append("text").attr("x", 425).attr("y", 95).attr("text-anchor", "middle").text("High Affinity");
        svg.append("defs").append("marker").attr("id", "arrow").attr("viewBox", "0 0 10 10").attr("refX", 5).attr("refY", 5).attr("markerWidth", 6).attr("markerHeight", 6).attr("orient", "auto-start-reverse").append("path").attr("d", "M 0 0 L 10 5 L 0 10 z").attr("fill", "var(--color-text)");
        const signal = svg.append("circle").attr("r", 5).attr("class", "data-flow").attr("cx", 50).attr("cy", 90).attr("opacity", 0);
        if (!this.isReducedMotion) {
            gsap.timeline({ scrollTrigger: { trigger: svg.node(), start: "top 80%", toggleActions: "play none none reverse" }})
                .to(signal.node(), { opacity: 1, duration: 0.2 })
                .to(signal.node(), { attr: { cx: 425 }, duration: 2, ease: "power1.inOut" })
                .to(signal.node(), { opacity: 0, duration: 0.2 });
        }
    },
    createXaiHeatmapViz() { /* Unchanged: A great interactive element demonstrating XAI. */ const canvas = document.getElementById('xai-canvas'); const ctx = canvas.getContext('2d'); const btn = document.getElementById('xai-button'); const width = canvas.width; const height = canvas.height; const cellSize = 20; const cells = []; const anomalousIndices = new Set([25, 46, 47, 67, 88]); for (let y = 0, i=0; y < height/cellSize; y++) { for (let x = 0; x < width/cellSize; x++, i++) { cells.push({ x: x * cellSize + cellSize/2, y: y * cellSize + cellSize/2, isAnomalous: anomalousIndices.has(i) }); } } function drawCells() { ctx.clearRect(0, 0, width, height); ctx.fillStyle = getComputedStyle(document.body).getPropertyValue('--color-text'); ctx.strokeStyle = getComputedStyle(document.body).getPropertyValue('--color-border'); cells.forEach(cell => { ctx.beginPath(); ctx.arc(cell.x, cell.y, cell.isAnomalous ? 6 : 4, 0, Math.PI * 2); ctx.fill(); }); } function drawHeatmap() { const highColor = getComputedStyle(document.body).getPropertyValue('--heatmap-color-high'); const lowColor = getComputedStyle(document.body).getPropertyValue('--heatmap-color-low'); cells.forEach(cell => { if (cell.isAnomalous) { const gradient = ctx.createRadialGradient(cell.x, cell.y, 0, cell.x, cell.y, cellSize * 2); gradient.addColorStop(0, highColor); gradient.addColorStop(1, lowColor.replace('0.5', '0')); ctx.fillStyle = gradient; ctx.fillRect(0, 0, width, height); } }); } drawCells(); btn.addEventListener('click', () => { drawCells(); drawHeatmap(); }); new MutationObserver(drawCells).observe(document.documentElement, { attributes: true, attributeFilter: ['class'] }); },
    createCorrelationPlot() { /* Unchanged: Perfectly illustrates the correlation vs causation point. */ const container = d3.select("#correlation-plot-container"); container.selectAll("*").remove(); const width = container.node().getBoundingClientRect().width; const height = 300; const margin = { top: 20, right: 50, bottom: 40, left: 50 }; const n = 12; const data = d3.range(n).map(i => { const base = Math.sin(i / (n - 1) * Math.PI) * 50 + 10; return { month: i, icecream: base + Math.random() * 10, drowning: base * 0.1 + Math.random() * 2 }; }); const xScale = d3.scaleLinear().domain([0, n - 1]).range([margin.left, width - margin.right]); const y1Scale = d3.scaleLinear().domain([0, d3.max(data, d => d.icecream)]).range([height - margin.bottom, margin.top]); const y2Scale = d3.scaleLinear().domain([0, d3.max(data, d => d.drowning)]).range([height - margin.bottom, margin.top]); const svg = container.append("svg").attr("viewBox", `0 0 ${width} ${height}`); svg.append("g").attr("transform", `translate(0, ${height - margin.bottom})`).call(d3.axisBottom(xScale).tickFormat(d => `M${d+1}`)); svg.append("g").attr("transform", `translate(${margin.left}, 0)`).call(d3.axisLeft(y1Scale)).selectAll("text, line").style("stroke", "var(--correlation-color-1)"); svg.append("g").attr("transform", `translate(${width - margin.right}, 0)`).call(d3.axisRight(y2Scale)).selectAll("text, line").style("stroke", "var(--correlation-color-2)"); svg.append("text").attr("class", "axis-label line-icecream").attr("x", margin.left + 5).attr("y", margin.top).text("冰淇淋销量").attr("fill", "var(--correlation-color-1)"); svg.append("text").attr("class", "axis-label line-drowning").attr("x", width - margin.right - 5).attr("y", margin.top).attr("text-anchor", "end").text("溺水人数").attr("fill", "var(--correlation-color-2)"); const line1 = svg.append("path").datum(data).attr("class", "line-path line-icecream").attr("d", d3.line().x(d => xScale(d.month)).y(d => y1Scale(d.icecream))); const line2 = svg.append("path").datum(data).attr("class", "line-path line-drowning").attr("d", d3.line().x(d => xScale(d.month)).y(d => y2Scale(d.drowning))); if (!this.isReducedMotion) { [line1, line2].forEach(line => { const length = line.node().getTotalLength(); gsap.from(line.node(), { strokeDasharray: length, strokeDashoffset: length, duration: 2, ease: 'power2.inOut', scrollTrigger: { trigger: "#correlation-plot-container", start: 'top 75%' } }); }); } },
    initTypedJS() { /* Unchanged: Adds a nice dynamic touch to an otherwise static case study. */ if (this.isReducedMotion) { document.getElementById('typed-output').textContent = '将会诱导细胞周期停滞在G1期，并下调E2F靶基因的表达。'; return; } ScrollTrigger.create({ trigger: "#typed-output", start: "top 80%", onEnter: () => { if (!this.typedInstance) { this.typedInstance = new Typed('#typed-output', { strings: ['将会诱导细胞周期停滞在G1期，并下调E2F靶基因的表达。'], typeSpeed: 50, startDelay: 500, showCursor: true, }); } }, once: true }); }
};
document.addEventListener('DOMContentLoaded', () => {
    LectureExperience.init();
});
