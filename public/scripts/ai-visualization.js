document.addEventListener('DOMContentLoaded', () => {
    // Initialize visualizations
    renderDashboardDemo();
    if(document.getElementById('slide-container')) renderSlide();
    
    // Initialize Mermaid if present
    initMermaid();
});

function copyToClipboard(id) {
    const text = document.getElementById(id).innerText;
    const textarea = document.createElement("textarea");
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
    alert("Prompt 已复制，请粘贴给 AI！");
}

// 简单的交互演示：根据选择高亮 / 变暗不同 response bar
function filterResponseBarsDemo() {
    const select = document.getElementById('group-filter-demo');
    if (!select) return;
    const value = select.value;
    const bars = document.querySelectorAll('.response-bar-demo');
    bars.forEach(bar => {
        const type = bar.getAttribute('data-type');
        if (value === 'all') {
            bar.classList.remove('opacity-30');
        } else if (value === 'responder') {
            if (type === 'CR' || type === 'PR') {
                bar.classList.remove('opacity-30');
            } else {
                bar.classList.add('opacity-30');
            }
        }
    });
}

// 炫彩仪表盘：随机生成数据 + 渐变色条
function renderDashboardDemo(refresh) {
    const bars = document.querySelectorAll('.response-bar-demo');
    if (!bars.length) return;
    const colors = {
        CR: 'linear-gradient(135deg, #22d3ee, #6366f1)',
        PR: 'linear-gradient(135deg, #34d399, #22c55e)',
        SD: 'linear-gradient(135deg, #cbd5e1, #94a3b8)',
        PD: 'linear-gradient(135deg, #fca5a5, #f43f5e)'
    };
    bars.forEach(bar => {
        const type = bar.getAttribute('data-type');
        // 随机高度，CR/PR 稍高，SD/PD 较低
        const base = (type === 'CR' || type === 'PR') ? 40 : 20;
        const height = base + Math.round(Math.random() * 40); // px
        bar.style.height = `${height}px`;
        bar.style.backgroundImage = colors[type] || '#cbd5e1';
        bar.style.opacity = 1;
    });
    // 如果刷新后保持当前筛选状态
    if (!refresh) {
        filterResponseBarsDemo();
    } else {
        filterResponseBarsDemo();
    }
}

// Reveal.js mock slide logic
let currentSlide = 0;
const slides = [
    `<h1 class="text-3xl font-bold text-white mb-2">期刊俱乐部</h1><p class="text-orange-400 font-mono">单细胞 RNA-seq 分析</p>`, 
    `<h2 class="text-xl text-white mb-4">代码示例</h2><pre class="bg-slate-800 p-4 rounded text-left text-xs text-green-200 font-mono overflow-x-auto"><code>import scanpy as sc
adata = sc.read_h5ad('data.h5ad')
sc.pl.umap(adata, color=['leiden'])</code></pre>`, 
    `<h2 class="text-xl text-white mb-4">交互式图表</h2><div class="flex gap-2 justify-center items-end h-24"><div class="w-8 bg-blue-500 hover:bg-blue-400 h-12 rounded transition-all cursor-pointer" title="NK 细胞: 12%"></div><div class="w-8 bg-purple-500 hover:bg-purple-400 h-20 rounded transition-all cursor-pointer" title="T 细胞: 45%"></div><div class="w-8 bg-rose-500 hover:bg-rose-400 h-16 rounded transition-all cursor-pointer" title="B 细胞: 23%"></div></div><p class="text-xs text-slate-400 mt-2">将鼠标悬停查看数值</p>`
];

function renderSlide() {
    const container = document.getElementById('slide-container');
    if (!container) return;
    container.style.opacity = 0;
    setTimeout(() => {
        container.innerHTML = slides[currentSlide];
        container.style.opacity = 1;
    }, 200);
}

window.changeSlide = function(dir) {
    currentSlide = (currentSlide + dir + slides.length) % slides.length;
    renderSlide();
}

// GCS Calculator Logic
window.calcGCS = function() {
    const eyeEl = document.getElementById('eye');
    const verbalEl = document.getElementById('verbal');
    const motorEl = document.getElementById('motor');
    
    if (!eyeEl || !verbalEl || !motorEl) return;

    const e = parseInt(eyeEl.value);
    const v = parseInt(verbalEl.value);
    const m = parseInt(motorEl.value);
    const score = e + v + m;
    const box = document.getElementById('gcs-result-box');
    const scoreEl = document.getElementById('gcs-score');
    const statusEl = document.getElementById('gcs-status');

    scoreEl.innerText = score;

    if (score <= 8) {
        box.className = "mt-6 p-4 rounded-xl bg-red-500 text-white shadow-lg animate-pulse";
        statusEl.innerText = "重度损伤，考虑气管插管";
    } else if (score <= 12) {
        box.className = "mt-6 p-4 rounded-xl bg-orange-100 text-orange-900";
        statusEl.innerText = "中度损伤";
    } else {
        box.className = "mt-6 p-4 rounded-xl bg-emerald-100 text-emerald-900";
        statusEl.innerText = "正常";
    }
}

// Toggle Modal
window.toggleModal = function() {
    const el = document.getElementById('fig1-modal');
    if(el) el.classList.toggle('hidden');
}

// Toggle Anki
window.toggleAnkiDemo = function() {
    const front = document.getElementById('anki-front');
    const back = document.getElementById('anki-back');
    const label = document.getElementById('anki-toggle-label');
    if (!front || !back) return;
    const showingFront = !front.classList.contains('hidden');
    if (showingFront) {
        front.classList.add('hidden');
        back.classList.remove('hidden');
        label.innerText = '隐藏答案';
    } else {
        back.classList.add('hidden');
        front.classList.remove('hidden');
        label.innerText = '显示答案';
    }
}

// Gemini API Call
const apiKey = ""; // Placeholder
async function callGemini() {
    const input = document.getElementById('gemini-input').value;
    if (!input.trim()) return;

    const outputDiv = document.getElementById('gemini-output');
    const outputContent = outputDiv.querySelector('div');
    const loadingDiv = document.getElementById('gemini-loading');

    outputDiv.classList.add('hidden');
    loadingDiv.classList.remove('hidden');

    try {
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{
                    parts: [{ text: `Please act as a medical professor. Explain the following academic text in simple, easy-to-understand Chinese for a medical student. Highlight 3 key technical terms in bold. Text: ${input}` }]
                }]
            })
        });
        const data = await response.json();
        if (data.error) {
             throw new Error(data.error.message);
        }
        const text = data.candidates[0].content.parts[0].text;

        outputContent.innerHTML = text.replace(/\*\*(.*?)\*\*/g, '<strong class="text-purple-700">$1</strong>').replace(/\n/g, '<br>');
        loadingDiv.classList.add('hidden');
        outputDiv.classList.remove('hidden');
    } catch (e) {
        console.error(e);
        loadingDiv.classList.add('hidden');
        outputDiv.classList.remove('hidden');
        outputContent.innerHTML = '<span class="text-red-500">API 调用失败，请检查网络或 API Key。</span>';
    }
}
window.callGemini = callGemini;

// CSS Animation Trigger
function activateSignal() {
    const ligand = document.getElementById('ligand');
    const signal = document.getElementById('signal');
    if (!ligand || !signal) return;

    // Bind
    ligand.style.top = 'calc(100% - 50px)'; 

    // Signal Transduction
    setTimeout(() => {
        signal.style.opacity = '1';
        signal.style.boxShadow = '0 0 10px #facc15';
    }, 1000);

    // Reset
    setTimeout(() => {
        ligand.style.top = '40px';
        signal.style.opacity = '0';
        signal.style.boxShadow = 'none';
    }, 3000);
}
window.activateSignal = activateSignal;

// Mermaid Logic
function initMermaid() {
    if (window.mermaid) {
        mermaid.initialize({
            startOnLoad: false,
            theme: document.documentElement.classList.contains('dark') ? 'dark' : 'default',
            securityLevel: 'loose'
        });
        renderMermaid();
        
        // Re-init on theme change
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.attributeName === 'class') {
                    const isDark = document.documentElement.classList.contains('dark');
                    mermaid.initialize({ theme: isDark ? 'dark' : 'default', securityLevel: 'loose' });
                    renderMermaid();
                }
            });
        });
        observer.observe(document.documentElement, { attributes: true });
    } else {
        // Retry if mermaid script hasn't loaded yet
        setTimeout(initMermaid, 100);
    }
}

async function renderMermaid() {
    const input = document.getElementById('mermaid-input');
    const output = document.getElementById('mermaid-output');
    
    if (!input || !output) return;

    try {
        const graphDefinition = input.value;
        // Clear previous content and create fresh container
        const id = 'mermaid-' + Date.now();
        output.innerHTML = '<div class="mermaid" id="' + id + '">' + graphDefinition + '</div>';
        
        if (window.mermaid && mermaid.run) {
            await mermaid.run({
                nodes: [document.getElementById(id)]
            });
        }
    } catch (error) {
        output.innerHTML = '<div class="text-red-500 text-xs p-4">Syntax Error: ' + error.message + '</div>';
        console.error(error);
    }
}
window.renderMermaid = renderMermaid;

// Expose other functions to global scope
window.copyToClipboard = copyToClipboard;
window.filterResponseBarsDemo = filterResponseBarsDemo;
window.renderDashboardDemo = renderDashboardDemo;