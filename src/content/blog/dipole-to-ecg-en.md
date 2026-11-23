---
title: "The Physics of the ECG: From the Electric Dipole to the Cardiac Vector"
description: "As medical students we learn the rules of the ECG, but what physics lies behind them? Starting from the electric dipole, this post works through the field theory behind the ECG and shows where the P-QRS-T waveform physically comes from."
pubDate: 2025-12-29
lang: en
---

<header class="pt-24 pb-20 px-4 sm:px-6 lg:px-8 max-w-5xl mx-auto text-center" id="intro">
<div class="inline-block px-4 py-1.5 mb-6 rounded-full bg-slate-100 text-slate-600 text-sm font-semibold border border-slate-200">
            Chapter 1: Physical Foundations
        </div>
<h1 class="font-serif">
            From the <span class="text-medical-600">Electric Dipole</span><br/>to Reading the ECG
        </h1>
<p class="text-xl text-slate-600 max-w-2xl mx-auto mt-8 leading-relaxed">
            As medical students we know ECG rules like "the P wave represents atrial depolarization," but behind those rules sits a more basic question: <strong>how does the electrochemical storm inside cardiac muscle cells cross the surrounding tissue and end up drawing a regular tracing on paper at the body surface?</strong>
            To answer it, we do not need more physiology. We need to go back to a field that seems far away but turns out to be essential: the theory of electric fields in classical physics.
        </p>
</header>
<main class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pb-32">
<!-- SECTION 1: Physical concept -->
<section id="dipole">
<h2>
<span class="text-medical-600 mr-3">01.</span> What Is an Electric Dipole?
            </h2>
<p>
                To decode the heart's electrical signal, we have to start from a basic physical model: the <strong>electric dipole</strong>. In physics, it is defined as a system of two point charges <strong>of equal magnitude (\(q\)) and opposite sign (\(+,
                    -\))</strong>, held a very small distance apart (\(d\)).
            </p>
<p>
                You can think of it as a tiny battery, with a positive pole at one end and a negative pole at the other. To describe this system, physicists use a vector, the <strong>electric dipole
                    moment</strong>, written \(\vec{P}\), which captures both the strength and the direction of the dipole.
            </p>
<div class="formula-block">
<p class="font-mono text-sm text-slate-500 mb-2">Definition Formula</p>
                $$ \vec{P} = q \cdot \vec{d} $$
                <ul class="list-disc pl-5 mt-4 text-base">
<li>\(\vec{P}\): the electric dipole moment vector; its magnitude and direction are what matter.</li>
<li>\(q\): the charge, which sets the strength of the dipole.</li>
<li>\(\vec{d}\): the displacement vector pointing from the negative charge to the positive charge.</li>
</ul>
<blockquote class="border-yellow-400 bg-yellow-50/50 p-4 rounded-md mt-6 text-sm not-italic">
<strong>⚠️ Mind the direction convention:</strong><br/>
                    Physics defines the direction of the dipole moment strictly as <strong>from the negative charge to the positive charge</strong> (\( - \to + \)). Cardiac vector theory inherits this convention unchanged: the arrow of the vector always points toward the positive end of the field.
                </blockquote>
</div>
<figure>
<div class="flex justify-center bg-slate-50/50 rounded-lg p-4 border border-slate-200">
<svg class="overflow-visible w-full max-w-md mx-auto" viewBox="-200 -150 400 300">
<defs>
<radialGradient cx="50%" cy="50%" fx="30%" fy="30%" id="grad-plus" r="50%">
<stop offset="0%" stop-color="#ff99aa"></stop>
<stop offset="100%" stop-color="#e11d48"></stop>
</radialGradient>
<radialGradient cx="50%" cy="50%" fx="30%" fy="30%" id="grad-minus" r="50%">
<stop offset="0%" stop-color="#bae6fd"></stop>
<stop offset="100%" stop-color="#0284c7"></stop>
</radialGradient>
<marker id="arrowhead" markerHeight="7" markerWidth="10" orient="auto" refX="9" refY="3.5">
<polygon fill="#334155" points="0 0, 10 3.5, 0 7"></polygon>
</marker>
</defs>
<g>
<path d="M -80 0 Q -40 -60 0 -60 Q 40 -60 80 0" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 4" opacity="0.6"></path>
<path d="M -80 0 Q -50 -100 0 -100 Q 50 -100 80 0" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 4" opacity="0.6"></path>
<path d="M -80 0 Q -60 -160 0 -160 Q 60 -160 80 0" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 4" opacity="0.6"></path>
<path d="M -80 0 Q -40 60 0 60 Q 40 60 80 0" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 4" opacity="0.6"></path>
<path d="M -80 0 Q -50 100 0 100 Q 50 100 80 0" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 4" opacity="0.6"></path>
<path d="M -80 0 Q -60 160 0 160 Q 60 160 80 0" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 4" opacity="0.6"></path>
</g>
<circle cx="-80" cy="0" r="20" fill="url(#grad-minus)" style="filter: drop-shadow(0 0 5px rgba(14, 165, 233, 0.5))"></circle>
<text fill="white" font-family="sans-serif" font-weight="bold" text-anchor="middle" x="-80" y="5">-</text>
<circle cx="80" cy="0" r="20" fill="url(#grad-plus)" style="filter: drop-shadow(0 0 5px rgba(225, 29, 72, 0.5))"></circle>
<text fill="white" font-family="sans-serif" font-weight="bold" text-anchor="middle" x="80" y="5">+</text>
<line stroke="#334155" stroke-width="3" x1="-50" x2="50" y1="0" y2="0" marker-end="url(#arrowhead)"></line>
<text font-size="14" font-weight="bold" fill="#334155" text-anchor="middle" x="0" y="25">P⃗</text>
</svg>
</div>
<figcaption>Figure 1: A simple electric dipole. It sets up an electric field in the surrounding space, and the potential at any point is determined by that point's position relative to the dipole.</figcaption>
</figure>
<h4>Why this physical model matters for medicine</h4>
<p>
                This abstract-looking model matters because the electric dipole is the source of an electric field. It produces a measurable field in the space around it, which in the body means the conductive fluids and tissues. If we place electrodes at any two points in that field (say, on the wrist and the ankle), there will be a <strong>potential difference</strong>, that is, a voltage, between them.
            </p>
<p>
                Seen this way, <strong>an ECG machine is essentially a very sensitive voltmeter. Its core job is to measure, precisely, the tiny potential differences that cardiac activity produces at different sites on the body surface.</strong>
</p>
</section>
<hr class="section-divider"/>
<!-- SECTION 1.5: Measurement principle and derivation -->
<section id="measurement">
<h2>
<span class="text-indigo-600 mr-3">1.5</span> Derivation: How Does a Voltmeter "See" a Vector?
            </h2>
<p>
                "Where the cardiac vector points, the lead facing it shows a tall wave" is a useful rule of thumb. But to really master quantitative ECG analysis, such as judging axis deviation precisely, we need to go beyond intuition, return to the <strong>superposition principle</strong> of physics, and derive step by step the projection formula that ultimately determines the waveform.
            </p>
<h3>Step one: from field strength to potential</h3>
<ol>
<li class="mb-6">
<strong>Electric field strength (E)</strong>: a point charge \(q\) produces, at distance \(r\), a field of magnitude:
                    <div class="py-4">
                        $$ E = k \cdot \frac{q}{r^2} $$
                    </div>
                    This is the force per unit positive charge at that point.
                </li>
<li>
<strong>Electric potential (V)</strong>: the potential is defined as the work done by the field in moving a unit positive charge from that point to infinity. Integrating gives:
                    <div class="py-4">
                        $$ V = \int_r^\infty E dr = \int_r^\infty k \frac{q}{r^2} dr = k \cdot \frac{q}{r} $$
                    </div>
</li>
</ol>
<blockquote>
<strong>Key point:</strong>
                Potential is a scalar and has no direction. This means the total potential at a point in space is simply the <strong>algebraic sum</strong> of the potentials produced there by each individual charge. That property greatly simplifies the analysis of complex charge systems such as a dipole, and it is the mathematical basis for everything that follows.
            </blockquote>
<h3>Stage one: set up the geometry</h3>
<p>
                Let us build an analytical model. Consider a dipole whose negative charge \(-q\) and positive charge \(+q\) are separated by \(d\). Our goal is to compute the potential at an arbitrary point A whose distance from the center of the dipole is \(r\).
            </p>
<figure>
<div class="flex justify-center bg-slate-50/50 p-4 rounded-lg border border-slate-200">
<svg class="overflow-visible w-full max-w-md mx-auto" viewbox="0 0 400 260">
<line stroke="#e2e8f0" x1="50" x2="350" y1="200" y2="200"></line>
<circle cx="200" cy="200" fill="#94a3b8" r="3"></circle><text class="text-xs fill-slate-400" text-anchor="middle" x="200" y="220">Center O</text>
<line stroke="#334155" stroke-width="2" x1="160" x2="240" y1="200" y2="200"></line>
<circle cx="160" cy="200" fill="#0284c7" r="8"></circle>
<circle cx="240" cy="200" fill="#e11d48" r="8"></circle><text class="text-[10px] fill-slate-500" text-anchor="middle" x="160" y="185">-q</text><text class="text-[10px] fill-slate-500" text-anchor="middle" x="240" y="185">+q</text>
<circle cx="320" cy="60" fill="#0ea5e9" r="4"></circle><text class="font-bold fill-medical-600" x="330" y="55">A (probe)</text>
<line stroke="#94a3b8" stroke-dasharray="4" x1="160" x2="320" y1="200" y2="60"></line><text class="text-xs fill-slate-400" transform="rotate(-40, 220, 120)" x="220" y="120">r₂</text>
<line stroke="#94a3b8" stroke-dasharray="4" x1="240" x2="320" y1="200" y2="60"></line><text class="text-xs fill-slate-400" transform="rotate(-60, 290, 140)" x="290" y="140">r₁</text>
<line stroke="#0ea5e9" stroke-width="2" x1="200" x2="320" y1="200" y2="60"></line><text class="text-sm font-bold fill-medical-500" transform="rotate(-50, 250, 110)" x="250" y="110">r</text>
<path d="M 240 200 A 40 40 0 0 0 225 170" fill="none" stroke="#64748b" stroke-width="2"></path><text class="text-sm font-serif fill-slate-600" x="245" y="180">θ</text>
</svg>
</div>
<figcaption>Figure 2-1: Geometry of a dipole and a distant measurement point A.</figcaption>
</figure>
<h3>Stage two: the far-field approximation</h3>
<p>
                In the real ECG setting, the size of the heart (corresponding to \(d\)) is much smaller than its distance to the surface electrodes (corresponding to \(r\)). This physical fact (\(r \gg d\)) lets us use a mathematical simplification called the "far-field approximation."
            </p>
<div class="formula-block">
<p>By the superposition principle, the total potential at A, \(V_A\), is the algebraic sum of the contributions from the two charges:</p>
                $$ V_A = V_+ + V_- = k \cdot \frac{q}{r_1} + k \cdot \frac{-q}{r_2} = kq \left( \frac{1}{r_1} -
                \frac{1}{r_2} \right) $$
                <p class="mt-4">When \(r\) is large enough, the lines from the two charges to A are nearly parallel. From the geometry we get:</p>
<ul class="list-none pl-0">
<li>\( r_1 \approx r - \frac{d}{2}\cos\theta \)</li>
<li>\( r_2 \approx r + \frac{d}{2}\cos\theta \)</li>
</ul>
<p class="mt-4">Substituting these into the expression and simplifying (dropping higher-order terms) gives:</p>
                $$ \frac{1}{r_1} - \frac{1}{r_2} \approx \frac{r_2 - r_1}{r^2} \approx \frac{d \cos\theta}{r^2} $$
            </div>
<figure>
<div class="bg-slate-50/50 rounded-lg p-8 border border-slate-200 flex flex-col items-center gap-8">
<div class="w-full">
<svg class="overflow-visible w-full max-w-md mx-auto" viewbox="0 0 250 200">
<line stroke="#334155" stroke-width="3" x1="50" x2="200" y1="100" y2="100"></line>
<circle cx="50" cy="100" fill="#0284c7" r="10"></circle>
<circle cx="200" cy="100" fill="#e11d48" r="10"></circle>
<line stroke="#94a3b8" stroke-dasharray="4" x1="50" x2="230" y1="100" y2="20"></line>
<line stroke="#94a3b8" stroke-dasharray="4" x1="200" x2="250" y1="100" y2="78"></line>
<line stroke="#ef4444" stroke-width="2" x1="200" x2="180" y1="100" y2="42"></line>
<!-- Right-angle mark -->
<line stroke="#ef4444" stroke-width="2" x1="177" x2="183" y1="45" y2="39"></line>
<text class="text-xs fill-red-600 font-bold" x="110" y="60">Path diff ≈ d·cosθ</text><text class="text-sm fill-slate-500" x="125" y="120">Distance d</text>
</svg>
</div>
<div class="w-full text-sm text-slate-600 leading-relaxed italic">
                        "The geometric heart of the far-field approximation is that, when the observation point is very far away, the two rays from the positive and negative charges are almost parallel. The difference in their path lengths to the observation point is then just the projection of the dipole length \(d\) onto the ray direction, namely \(d
                        \cos\theta\)."
                    </div>
</div>
<figcaption>Figure 2-2: The geometry behind the far-field approximation.</figcaption>
</figure>
<h3>Result: the projection law</h3>
<p>
                Finally, substituting the definition of the dipole moment, \(P = qd\), into the simplified expression gives the central equation of ECG physics:
            </p>
<div class="formula-block text-center">
<p class="text-medical-700 font-mono text-xs mb-4 uppercase tracking-widest">The Core ECG Equation</p>
<div class="text-3xl md:text-4xl font-bold text-slate-800">
                    $$ V \propto \frac{P \cdot \cos\theta}{r^2} $$
                </div>
</div>
<p>In clinical practice, the distance \(r\) between an exploring electrode and the heart can be treated as roughly constant. The formula therefore leads to an important conclusion: <strong>the voltage (amplitude) a lead records at any instant is proportional to the projection of the heart's total dipole moment vector \(\vec{P}\)
                    onto that lead's axis.</strong></p>
</section>
<hr class="section-divider"/>
<!-- SECTION 2: Physiological link (MODIFIED SECTION) -->
<section id="heart">
<h2>
<span class="text-heart-red mr-3">02.</span> The Heart: A System of Billions of Moving Dipoles
            </h2>
<p class="lead">
                So far we have built a dry physical model. The real challenge is to connect it to wet, living, moving tissue. To do that we need a thought experiment that zooms in on a single cardiac muscle cell and answers a basic question: <strong>from a physicist's point of view, why can a living cell be treated as an electric dipole?</strong>
</p>
<h3>2.1 The microscopic view: how a single cell creates a field</h3>
<p>
                We do not need complicated biochemistry to answer this. We can look at the charge distribution of the cell in its different physiological states from a purely physical angle, as a boundary problem in electrostatics.
            </p>
<h4>State one: rest (the silent cylinder)</h4>
<p>
                Physiologically, cardiac myocytes use active transport such as the <strong>sodium-potassium pump (Na⁺-K⁺
                    pump)</strong> to keep pumping positive ions (mainly Na⁺) out of the cell while maintaining a high intracellular K⁺ concentration. This creates stable ion gradients across the membrane, which show up as a resting potential that is <strong>negative inside and positive outside</strong>.
            </p>
<p>
                In a physical model, the myocyte can be treated as a uniformly charged, infinitely long cylindrical shell. By <strong>Gauss's law</strong>, for a system with cylindrical symmetry, the field outside is the same as if all the charge were concentrated on the central axis. At rest, the positive charge layer on the outer surface of the membrane and the negative layer on the inner surface share the same axis and carry equal amounts of charge.
            </p>
<div class="flex flex-col items-center gap-8 my-8">
<div class="w-full flex justify-center py-10 bg-slate-50/30 rounded-2xl border border-slate-100">
<svg class="w-full max-w-2xl h-auto" viewbox="0 0 600 240">
<!-- Perspective cylinder -->
<defs>
<lineargradient id="cylinder-grad" x1="0%" x2="0%" y1="0%" y2="100%">
<stop offset="0%" stop-color="#f1f5f9"></stop>
<stop offset="50%" stop-color="#e2e8f0"></stop>
<stop offset="100%" stop-color="#f1f5f9"></stop>
</lineargradient>
</defs>
<!-- Back half of the cylinder -->
<path d="M 100 60 L 500 60 A 30 60 0 0 1 500 180 L 100 180" fill="none" stroke="#cbd5e1" stroke-dasharray="4 4"></path>
<!-- Cylinder body -->
<rect fill="url(#cylinder-grad)" height="120" opacity="0.4" width="400" x="100" y="60"></rect>
<ellipse cx="100" cy="120" fill="#f8fafc" rx="30" ry="60" stroke="#94a3b8" stroke-width="2"></ellipse>
<path d="M 100 60 L 500 60 M 100 180 L 500 180" stroke="#94a3b8" stroke-width="2"></path>
<ellipse cx="500" cy="120" fill="#f8fafc" rx="30" ry="60" stroke="#94a3b8" stroke-width="2"></ellipse>
<!-- Charge distribution labels -->
<!-- Outer positive charges -->
<g fill="#3b82f6" font-size="14" font-weight="bold" text-anchor="middle">
<text x="300" y="50">+</text><text x="250" y="50">+</text><text x="350" y="50">+</text>
<text x="300" y="200">+</text><text x="250" y="200">+</text><text x="350" y="200">+</text>
</g>
<!-- Inner negative charges -->
<g fill="#ef4444" font-size="14" font-weight="bold" text-anchor="middle">
<text x="300" y="85">-</text><text x="250" y="85">-</text><text x="350" y="85">-</text>
<text x="300" y="165">-</text><text x="250" y="165">-</text><text x="350" y="165">-</text>
</g>
<!-- Measurement annotation -->
<line marker-end="url(#probe-dot)" marker-start="url(#probe-dot)" stroke="#0f172a" stroke-width="1" x1="550" x2="550" y1="40" y2="200"></line>
<text class="text-[10px] fill-slate-500 font-mono" transform="rotate(90, 560, 120)" x="560" y="120">GAUSSIAN SURFACE</text>
<text class="text-sm font-serif italic fill-slate-400" text-anchor="middle" x="300" y="125">Net
                            Enclosed Charge = 0</text>
</svg>
</div>
<div class="w-full">
<div class="formula-block py-4 text-center">
                        $$ \oint_S \vec{E} \cdot d\vec{A} = \frac{Q_{encl}}{\varepsilon_0} = 0 \implies \vec{E}_{total}
                        = 0 $$
                    </div>
<blockquote>
<strong>Conclusion:</strong> Because the charge layers inside and outside the cell cancel each other out symmetrically at the macroscopic level, the net enclosed charge is zero for any observation point outside the cylinder. So <strong>a resting cell produces no measurable field in the space outside it</strong>, and the ECG records a flat baseline.
                    </blockquote>
</div>
</div>
<h4>State two: a propagating action potential and the "moving dipole"</h4>
<p>
                When a myocyte is stimulated, its Na⁺ channels open and positive charge floods into the cell. In a single long cylindrical cell, this depolarization does not happen everywhere at once; it travels from one end to the other like a row of falling dominoes.
            </p>
<p>
                While it travels, the cell is divided into an <b>excited (depolarized) region</b> and a <b>resting (not yet depolarized) region</b>. What matters is the boundary between them, the wavefront:
            </p>
<div class="formula-block">
<p class="font-mono text-sm text-slate-500 mb-2">A calculus view of the physics</p>
<p>Let the cell axis be \(x\) and the extracellular potential be \(\Phi_e\). At the wavefront, the potential jumps sharply from low to high. From basic calculus:</p>
                $$ E(x) = -\frac{d\Phi_e}{dx} $$
                <p class="mt-2 text-sm text-slate-600">Because \(\Phi_e\) changes most steeply with distance at the wavefront, the <strong>potential gradient</strong> is largest there. In this narrow transition zone the symmetry is broken, and a microscopic electric field radiates out into the surrounding space.</p>
</div>
<h5>The source and the sink of the field</h5>
<p>To avoid the heavy volume-conductor equations, we can understand this "wavefront battery" with a minimal model:</p>
<ul>
<li><strong>Current sink: the depolarized region.</strong> Behind the wave, Na⁺ has just flowed in, so the density of positive charge outside the membrane drops sharply. This acts as a <strong>low-potential "negative pole"</strong> (\(\Phi_{sink}\)).</li>
<li><strong>Current source: the resting region.</strong> Ahead of the wave, the cell has not yet been reached by the stimulus, and the outside of the membrane still carries a high density of positive charge. This acts as a <strong>high-potential "positive pole"</strong> (\(\Phi_{source}\)).</li>
</ul>
<p><strong>The reasoning:</strong> The fiber may be long, but a significant potential difference \(\Delta \Phi = \Phi_{source} - \Phi_{sink} &gt; 0\) exists only near the wavefront, where the jump occurs. Physically, this narrow voltage drop is exactly equivalent to a <strong>moving electric dipole</strong>. Its strength reflects how sharply the local voltage changes, and its vector points from negative (sink) to positive (source), that is, always in the direction the wave is traveling.</p>
<figure>
<div class="overflow-x-auto bg-slate-50/50 p-4 rounded-lg border border-slate-200">
<svg class="w-full" viewbox="0 0 700 400">
<defs>
<lineargradient id="grad-potential" x1="0%" x2="100%" y1="0%" y2="0%">
<stop offset="40%" stop-color="#fee2e2"></stop>
<stop offset="60%" stop-color="#dbeafe"></stop>
</lineargradient>
<marker id="arrow-solid" markerheight="10" markerwidth="10" orient="auto" refx="9" refy="3.5">
<polygon fill="#0f172a" points="0 0, 10 3.5, 0 7"></polygon>
</marker>
</defs>
<g transform="translate(50, 50)"><text fill="#64748b" font-size="12" font-weight="bold" x="0" y="-20">1. Extracellular charge distribution</text>
<rect fill="white" height="80" rx="40" stroke="#94a3b8" stroke-width="2" width="600" x="0" y="0"></rect>
<rect fill="url(#grad-potential)" height="70" opacity="0.3" rx="35" width="590" x="5" y="5"></rect>
<line stroke="#0f172a" stroke-dasharray="6 4" stroke-width="2" x1="300" x2="300" y1="-10" y2="90"></line><text fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle" x="300" y="110">Wavefront</text>
<g fill="#ef4444" font-family="monospace" font-size="18" font-weight="bold"><text text-anchor="middle" x="150" y="-5">- - -</text><text text-anchor="middle" x="150" y="100">-
                                    - -</text><text fill="#b91c1c" font-sans="true" font-size="12" text-anchor="middle" x="150" y="45">Low \(\Phi\)</text></g>
<g fill="#3b82f6" font-family="monospace" font-size="18" font-weight="bold"><text text-anchor="middle" x="450" y="-5">+ + +</text><text text-anchor="middle" x="450" y="100">+
                                    + +</text><text fill="#1d4ed8" font-sans="true" font-size="12" text-anchor="middle" x="450" y="45">High \(\Phi\)</text></g>
</g>
<g transform="translate(50, 220)"><text fill="#64748b" font-size="12" font-weight="bold" x="0" y="-20">2. Equivalent physical model</text>
<path d="M 150 -50 L 150 40" stroke="#cbd5e1" stroke-dasharray="4"></path>
<path d="M 450 -50 L 450 40" stroke="#cbd5e1" stroke-dasharray="4"></path>
<g transform="translate(0, 40)">
<circle cx="150" cy="0" fill="#ef4444" r="20"></circle><text fill="white" font-size="18" font-weight="bold" text-anchor="middle" x="150" y="5">-</text><text fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle" x="150" y="35">Sink
                                    (-q)</text>
<circle cx="450" cy="0" fill="#3b82f6" r="20"></circle><text fill="white" font-size="18" font-weight="bold" text-anchor="middle" x="450" y="5">+</text><text fill="#3b82f6" font-size="10" font-weight="bold" text-anchor="middle" x="450" y="35">Source
                                    (+q)</text>
<line marker-end="url(#arrow-solid)" stroke="#0f172a" stroke-width="4" x1="180" x2="420" y1="0" y2="0"></line>
<rect fill="white" height="30" rx="4" width="100" x="250" y="-15"></rect><text fill="#0f172a" font-size="16" font-weight="bold" text-anchor="middle" x="300" y="5">P = q·d</text>
</g>
</g>
<g transform="translate(50, 340)"><text fill="#059669" font-size="14" font-weight="bold" text-anchor="middle" x="300" y="20">Conclusion: the vector ( → ) points the same way as the depolarization wave ( → )</text></g>
</svg>
</div>
<figcaption>Figure 2.2: The equivalent dipole generator. The resting region ahead of the depolarization wave (high potential) and the depolarized region behind it (low potential) together form an equivalent electric dipole whose vector points in the direction the wave travels.</figcaption>
</figure>
<h5>The reasoning: why does the vector point "forward"?</h5>
<p>"A depolarization vector heading toward the positive electrode gives an upward deflection" is a golden rule of ECG reading. It is not something to memorize, though. It follows necessarily from three steps of reasoning:</p>
<ol>
<li><strong>Physics definition:</strong> By convention, the dipole moment vector \(\vec{P}\)
                    always points <strong>from the center of negative charge to the center of positive charge</strong>.</li>
<li><strong>Physiological state:</strong>
                    At the depolarization wavefront, the region <strong>behind</strong> the wave is depolarized, with low extracellular potential, so it is the effective negative pole. The region <strong>ahead</strong> of the wave is still resting, with high extracellular potential, so it is the effective positive pole.</li>
<li><strong>Conclusion:</strong> Putting the two together, the vector \(\vec{P}\)
                    must point from behind (negative) to ahead (positive). Therefore, <strong>the direction of the depolarization vector is exactly the direction in which the depolarization wave travels through the tissue.</strong></li>
</ol>
<blockquote>
<strong>💡 Question to think about:</strong> What about repolarization?<br/>
                During repolarization, the region behind the wave returns to rest first (outside becomes positive), while the region ahead is still depolarized (outside negative). The field is now "negative ahead, positive behind," so by definition the dipole vector points from front (negative) to back (positive). This is why the direction of repolarization waves (such as the T wave) is more complicated than that of depolarization waves.
            </blockquote>
<hr class="subsection-divider"/>
<!-- REPLACEMENT SECTION: replaces the original Figures 2.3 and 2.4 -->
<h3>2.2 The central paradox: why do we only measure the external field?</h3>
<p>
    Thinking further, we run into a tricky physical problem. As the depolarization wave travels, two circuits with opposite directions actually form, one inside the cell and one outside. To understand what the ECG machine is really measuring, we need to turn the biological picture into a physical circuit model.
</p>
<!-- Figure one: spatial charges and dipole distribution -->
<figure class="my-12">
<div class="flex justify-center bg-slate-50/50 rounded-lg p-6 border border-slate-200">
<svg class="overflow-visible w-full max-w-2xl mx-auto" viewbox="0 0 700 450">
<defs>
<lineargradient id="grad-cell-2" x1="0%" x2="100%" y1="0%" y2="0%">
<stop offset="48%" stop-color="#fee2e2"></stop> <!-- Depolarized -->
<stop offset="52%" stop-color="#e0f2fe"></stop> <!-- Resting -->
</lineargradient>
<marker id="arrow-red-straight" markerheight="8" markerwidth="8" orient="auto" refx="7" refy="4">
<path d="M0,0 L8,4 L0,8" fill="#dc2626"></path>
</marker>
<marker id="arrow-blue-straight" markerheight="8" markerwidth="8" orient="auto" refx="7" refy="4">
<path d="M0,0 L8,4 L0,8" fill="#0284c7"></path>
</marker>
</defs>
<!-- Title -->
<text fill="#334155" font-size="16" font-weight="700" text-anchor="middle" x="350" y="30">Fig. 2-3: Membrane Charges and Opposing Dipoles</text>
<!-- 1. External Field (Top) -->
<g transform="translate(50, 105)">
<!-- External Dipole Vector -->
<line marker-end="url(#arrow-blue-straight)" stroke="#0284c7" stroke-width="3" x1="400" x2="200" y1="-45" y2="-45"></line>
<text fill="#0284c7" font-size="13" font-weight="bold" text-anchor="middle" x="300" y="-60">External Dipole (P_out)</text>
<!-- Charges Outside Top -->
<g font-family="monospace" font-size="18" font-weight="700">
<text fill="#dc2626" text-anchor="middle" x="120" y="0">- - - -</text>
<text fill="#0284c7" text-anchor="middle" x="480" y="0">+ + + +</text>
</g>
</g>
<!-- 2. The Cell Body -->
<g transform="translate(50, 130)">
<!-- Membrane Rect -->
<rect fill="url(#grad-cell-2)" height="140" rx="12" stroke="#64748b" stroke-width="3" width="600" x="0" y="0"></rect>
<!-- Wavefront Line -->
<line stroke="#94a3b8" stroke-dasharray="6 4" stroke-width="2" x1="300" x2="300" y1="0" y2="140"></line>
<!-- Charges Inside -->
<g font-family="monospace" font-size="18" font-weight="700">
<text fill="#0284c7" text-anchor="middle" x="120" y="35">+ + + +</text>
<text fill="#dc2626" text-anchor="middle" x="480" y="35">- - - -</text>
<text fill="#0284c7" text-anchor="middle" x="120" y="115">+ + + +</text>
<text fill="#dc2626" text-anchor="middle" x="480" y="115">- - - -</text>
</g>
<!-- Internal Dipole Vector -->
<line marker-end="url(#arrow-red-straight)" stroke="#dc2626" stroke-width="5" x1="200" x2="400" y1="75" y2="75"></line>
<text fill="#dc2626" font-size="14" font-weight="700" text-anchor="middle" x="300" y="60">Internal Dipole (P_in)</text>
</g>
<!-- 3. Labels and Bottom Field -->
<g transform="translate(50, 295)">
<!-- Region Labels -->
<text fill="#334155" font-size="13" font-weight="700" text-anchor="middle" x="150" y="20">DEPOLARIZED</text>
<text fill="#334155" font-size="13" font-weight="700" text-anchor="middle" x="450" y="20">RESTING</text>
<!-- Bottom External Charges -->
<g font-family="monospace" font-size="18" font-weight="700" transform="translate(0, 55)">
<text fill="#dc2626" text-anchor="middle" x="120" y="0">- - - -</text>
<text fill="#0284c7" text-anchor="middle" x="480" y="0">+ + + +</text>
</g>
<!-- Wavefront Propagation -->
<text fill="#64748b" font-size="13" font-style="italic" font-weight="700" text-anchor="middle" x="300" y="110">Wavefront Propagation →</text>
</g>
</svg>
</div>
<figcaption>Figure 2-3: Charge distribution and dipole directions at the action potential wavefront. Note that the intracellular field (red) points from high to low potential (to the right), while the extracellular field (blue), because the induced charges are arranged the opposite way, points in the opposite direction (to the left).</figcaption>
</figure>
<p>
    To understand what the signal measured at the body surface physically is, we can turn this biological picture into a classic physical circuit: a <b>three-rail "ladder" equivalent circuit</b>.
</p>
<!-- Figure two: three-rail ladder equivalent circuit -->
<figure class="my-12">
<div class="flex flex-col items-center bg-slate-50/50 rounded-lg p-8 border border-slate-200">
<svg class="overflow-visible w-full max-w-xl mx-auto" viewbox="0 0 500 350">
<!-- ... existing SVG definitions ... -->
<defs>
<g id="battery-right">
<line stroke="currentColor" stroke-width="2" x1="-15" x2="-5" y1="0" y2="0"></line>
<line stroke="currentColor" stroke-width="2" x1="-5" x2="-5" y1="-10" y2="10"></line>
<line stroke="currentColor" stroke-width="4" x1="5" x2="5" y1="-20" y2="20"></line>
<line stroke="currentColor" stroke-width="2" x1="5" x2="15" y1="0" y2="0"></line>
</g>
<g id="battery-left">
<line stroke="currentColor" stroke-width="2" x1="-15" x2="-5" y1="0" y2="0"></line>
<line stroke="currentColor" stroke-width="4" x1="-5" x2="-5" y1="-20" y2="20"></line>
<line stroke="currentColor" stroke-width="2" x1="5" x2="5" y1="-10" y2="10"></line>
<line stroke="currentColor" stroke-width="2" x1="5" x2="15" y1="0" y2="0"></line>
</g>
<marker id="arrow-flow" markerheight="8" markerwidth="8" orient="auto" refx="7" refy="4">
<path d="M0,0 L8,4 L0,8" fill="#64748b"></path>
</marker>
</defs>
<text fill="#475569" font-size="14" font-weight="bold" text-anchor="middle" x="250" y="20">Fig. 2-4: Three-Rail Equivalent Circuit Model</text>
<!-- Top Horizontal Line: Body Fluid (R_ext) -->
<g transform="translate(0, 60)">
<text fill="#334155" font-size="11" font-weight="bold" x="50" y="-15">Layer 3: Body Fluid</text>
<line stroke="#0f172a" stroke-width="2" x1="100" x2="400" y1="0" y2="0"></line>
<rect fill="white" height="20" stroke="none" width="40" x="230" y="-10"></rect>
<path d="M 230 0 L 235 -8 L 245 8 L 255 -8 L 265 8 L 270 0" fill="none" stroke="#0f172a" stroke-width="2"></path>
<text fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle" x="250" y="25">R_ext (fluid resistance)</text>
<path d="M 180 0 L 180 -35 L 320 -35 L 320 0" fill="none" stroke="#64748b" stroke-dasharray="4"></path>
<circle cx="250" cy="-35" fill="white" r="15" stroke="#64748b" stroke-width="2"></circle>
<text fill="#64748b" font-size="12" font-weight="bold" text-anchor="middle" x="250" y="-30">V</text>
<text fill="#64748b" font-size="10" font-weight="bold" text-anchor="middle" x="250" y="-55">ECG machine</text>
</g>
<!-- Connections -->
<line stroke="#94a3b8" stroke-width="2" x1="100" x2="100" y1="60" y2="160"></line>
<line stroke="#94a3b8" stroke-width="2" x1="400" x2="400" y1="60" y2="160"></line>
<!-- Middle Line -->
<g transform="translate(0, 160)">
<text fill="#0284c7" font-size="11" font-weight="bold" x="50" y="-15">Layer 2: Extracellular</text>
<line stroke="#0284c7" stroke-width="2" x1="100" x2="400" y1="0" y2="0"></line>
<g class="text-sky-600" transform="translate(250, 0) scale(1.5)">
<use href="#battery-left"></use>
<text fill="currentColor" font-size="8" font-weight="bold" text-anchor="middle" x="-25" y="5">+</text>
<text fill="currentColor" font-size="8" font-weight="bold" text-anchor="middle" x="25" y="5">-</text>
</g>
<text fill="#0284c7" font-size="11" font-weight="bold" text-anchor="middle" x="250" y="45">External Source (P_out)</text>
</g>
<!-- Membrane Resistors -->
<g>
<line stroke="#dc2626" stroke-width="2" x1="100" x2="100" y1="160" y2="260"></line>
<rect fill="white" height="30" stroke="none" width="20" x="90" y="195"></rect>
<path d="M 100 195 L 92 200 L 108 210 L 92 220 L 100 225" fill="none" stroke="#dc2626" stroke-width="2"></path>
<text fill="#dc2626" font-size="10" font-weight="bold" text-anchor="end" x="85" y="215">R_mem</text>
<line stroke="#dc2626" stroke-width="2" x1="400" x2="400" y1="160" y2="260"></line>
<rect fill="white" height="30" stroke="none" width="20" x="390" y="195"></rect>
<path d="M 400 195 L 392 200 L 408 210 L 392 220 L 400 225" fill="none" stroke="#dc2626" stroke-width="2"></path>
<text fill="#dc2626" font-size="10" font-weight="bold" text-anchor="start" x="415" y="215">R_mem</text>
</g>
<!-- Bottom Line -->
<g transform="translate(0, 260)">
<text fill="#dc2626" font-size="11" font-weight="bold" x="50" y="20">Layer 1: Intracellular</text>
<line stroke="#dc2626" stroke-width="2" x1="100" x2="400" y1="0" y2="0"></line>
<g class="text-red-600" transform="translate(250, 0) scale(1.5)">
<use href="#battery-right"></use>
<text fill="currentColor" font-size="8" font-weight="bold" text-anchor="middle" x="-25" y="5">-</text>
<text fill="currentColor" font-size="8" font-weight="bold" text-anchor="middle" x="25" y="5">+</text>
</g>
<text fill="#dc2626" font-size="11" font-weight="bold" text-anchor="middle" x="250" y="45">Internal Source (P_in)</text>
</g>
<path d="M 140 240 L 140 180" marker-end="url(#arrow-flow)" stroke="#cbd5e1" stroke-dasharray="4" stroke-width="1"></path>
<text fill="#94a3b8" font-size="10" font-style="italic" x="145" y="210">Current Loop</text>
<text fill="#94a3b8" font-size="9" x="145" y="225">Restricted by R_mem</text>
</svg>
</div>
<figcaption>Figure 2-4: The three-rail "ladder" equivalent circuit for ECG generation.</figcaption>
</figure>
<h4>Derivation: why is the ECG signal so small?</h4>
<p>
    The circuit in Figure 2-4 shows the physical mechanism that generates the ECG:
</p>
<ul class="list-disc pl-5 my-6 space-y-3">
<li><strong>Bottom rail (intracellular, Layer 1):</strong> This is where the electrical energy originates (\(P_{in}\)). The source voltage created by the jump away from the resting potential is large, on the order of 100 mV.</li>
<li><strong>Vertical paths (cell membrane, R_mem):</strong> For current to flow from inside the cell to the body surface, it first has to force its way across the lipid bilayer. Because the membrane is an insulator, \(R_{mem}\) here is enormous (typically in the megaohm range).</li>
<li><strong>Top rail (body surface, Layer 3):</strong> Our voltmeter (the ECG machine) measures the voltage drop across the conductive body-fluid resistance \(R_{ext}\).</li>
</ul>
<div class="formula-block">
<p class="font-mono text-sm text-slate-500 mb-4 tracking-wider uppercase">Derivation of Surface Potential</p>
<p>By the voltage-divider rule for resistors in series, the potential measured at the surface, \(V_{measure}\), relates to the source voltage \(V_{source}\) as:</p>
<div class="py-4">
        $$ V_{measure} \approx V_{source} \times \frac{R_{ext}}{2R_{mem} + R_{ext}} $$
    </div>
<p class="mt-4">
        In living tissue, the membrane resistance \(R_{mem}\) is far larger than the body-fluid resistance \(R_{ext}\) (the denominator is huge). This means:
    </p>
<p class="mt-6 leading-relaxed">
<span class="bg-yellow-100 px-1 py-0.5 border-b-2 border-yellow-300 text-slate-900 font-medium">
<strong>The signal the ECG picks up at the body surface is, in essence, the potential difference produced by the "extracellular dipole," carried directly by the extracellular space (the body-fluid conductor)</strong>.
        </span>
</p>
<p class="mt-4 text-slate-700">
        This resolves the "central paradox" raised above. The energy of the ECG comes from inside the cell, but because of this voltage-divider effect, what we actually measure is the "extracellular projection," an indirect view of the electrical storm inside the cell.
    </p>
</div>
<hr class="subsection-divider"/>
<h3>2.3 The macroscopic field: from microscopic summation to surface projection</h3>
<p class="lead">
                We now have a physical model for the electrical activity of a single cell. Next we need to zoom out from the microscopic to the macroscopic scale and understand how the whole heart, billions of myocytes working together, produces regular voltage fluctuations in the volume conductor around it that an instrument can record.
            </p>
<h4>1. The core idea: why does the sum of billions of signals still obey the projection law?</h4>
<p>
                A natural question: the heart is made of billions of microscopic dipoles. Is the potential measured at the surface just a messy algebraic sum of all their signals? Or is there an elegant mathematical way in which these microscopic vectors "condense" into one?
            </p>
<p>
                The answer lies in the <strong>principle of linear superposition</strong>. The total potential \(V\) at any point on the body surface is indeed the sum of the potentials \(V_i\) produced there by all the microscopic dipoles \(\vec{p}_i\).
                Using the core formula we derived, this means:
                $$ V = \sum V_i \propto \frac{1}{r^2} \sum (p_i \cdot \cos\theta_i) $$
            </p>
<p>
                Geometrically, \(p_i \cdot \cos\theta_i\) is exactly the projection of the microscopic vector \(\vec{p}_i\)
                onto the direction of observation (the lead axis). A basic linear property of vector algebra then gives a neat result: <strong>the algebraic sum of the projections of all the microscopic vectors is exactly equal to the projection of their sum (the total vector \(\vec{P}\)).</strong>
</p>
<figure class="flex flex-col gap-8 items-center bg-slate-50 p-8 rounded-lg border border-slate-200">
<div class="prose prose-slate w-full">
<h6>Visual Proof Logic</h6>
<p>This figure shows geometrically that the <strong>vector sum</strong> and the <strong>potential sum</strong> are equivalent.</p>
<ul class="not-prose list-none pl-0">
<li><span class="text-blue-600 font-bold">Blue vectors:</span> the dipole produced by each microscopic myocyte, $\vec{p}_i$</li>
<li><span class="text-slate-800 font-bold">Black vector:</span> the total cardiac vector formed by adding all the microscopic dipoles, $\vec{P}$</li>
<li><span class="text-rose-600 font-bold">Red projection:</span> the voltage the surface electrodes actually record along this lead axis, $V$</li>
</ul>
<blockquote>"The lengths of the 'shadows' all the small arrows cast on the axis add up to exactly the length of the 'shadow' cast by the one big arrow."</blockquote>
</div>
<div class="w-full overflow-x-auto border border-slate-200 rounded-md p-2">
<div class="relative h-[400px]" style="min-width: 500px;">
<svg class="absolute inset-0 w-full h-full" preserveaspectratio="xMidYMid meet" viewbox="0 0 800 650">
<defs>
<marker id="arr-blue" markerheight="10" markerwidth="10" orient="auto" refx="9" refy="5">
<path d="M0,0 L10,5 L0,10" fill="#3b82f6"></path>
</marker>
<marker id="arr-black" markerheight="12" markerwidth="12" orient="auto" refx="11" refy="6">
<path d="M0,0 L12,6 L0,12" fill="#0f172a"></path>
</marker>
</defs>
<line stroke="#e2e8f0" stroke-dasharray="15 10" stroke-width="2" x1="50" x2="750" y1="550" y2="150"></line>
<g transform="translate(150, 520)">
<line marker-end="url(#arr-blue)" stroke="#3b82f6" stroke-width="4" x1="0" x2="140" y1="0" y2="-140"></line>
<line marker-end="url(#arr-blue)" stroke="#60a5fa" stroke-width="4" x1="140" x2="300" y1="-140" y2="-200"></line>
<line marker-end="url(#arr-blue)" stroke="#3b82f6" stroke-width="4" x1="300" x2="420" y1="-200" y2="-400"></line>
<line marker-end="url(#arr-black)" stroke="#0f172a" stroke-width="6" x1="0" x2="420" y1="0" y2="-400"></line>
<line stroke="#94a3b8" stroke-dasharray="8 6" stroke-width="2" x1="420" x2="520" y1="-400" y2="-200"></line>
<line opacity="0.9" stroke="#f43f5e" stroke-linecap="round" stroke-width="12" x1="0" x2="520" y1="0" y2="-200"></line>
</g>
</svg>
</div>
</div>
<figcaption>Illustration: summing vectors and taking projections are equivalent. Mathematically, adding up the projections is the same as adding the vectors first and then projecting.</figcaption>
</figure>
<h4>Conclusion: what the surface voltage physically is</h4>
<p>This derivation means that although the heart's electrical activity comes from the complex cooperation of billions of cells, at the scale of macroscopic physical measurement we do not need to track every microscopic event. <strong>The heart's overall electrical activity at any given instant can be reduced exactly to a single equivalent "net dipole" vector
                    \(\vec{P}\).</strong></p>
<p>The potential differences we measure at the body surface are therefore not random noise. They reflect the field that this macroscopic net vector \(\vec{P}\)
                sets up in space. Every rise and fall of the ECG is a faithful record, over time, of the geometric projection of this net vector onto a particular lead axis.</p>
<h4>2. Applying the projection principle: the standard ECG, frame by frame</h4>
<p>We can now apply all of these physical principles to a complete cardiac cycle and see exactly where each part of the standard ECG comes from. The figure below shows how the net cardiac vector changes as different regions of the heart depolarize and recover, and how its projection onto a lead axis produces the familiar P-QRS-T complex.
            </p>
<figure>
<img alt="ECG waveform generation from cardiac vectors" class="mx-auto h-auto w-full max-w-3xl border border-slate-200 rounded-lg shadow-sm" src="/images/dipole-to-ecg/心电轴与心电图.png"/>
<figcaption>
                    Figure 3: The cardiac electrical cycle and the corresponding ECG waveform. Each wave arises from the net vector created by a specific physiological event and its projection onto a one-dimensional lead axis.
                </figcaption>
</figure>
<p>Let us go through the process step by step:</p>
<h5>Atrial depolarization → P wave</h5>
<p>The cardiac cycle begins when the sinoatrial node fires and a depolarization wave spreads across the atria. The net vector it produces points roughly from upper right to lower left. As the figure shows, this vector points toward the positive end of the lead axis, so its projection is positive and is recorded as an upright, rounded <b>P wave</b>.</p>
<h5>Ventricular depolarization → QRS complex</h5>
<p>Ventricular depolarization is more complicated. It can be divided in time into three main phases, which together make up the <b>QRS complex</b>:</p>
<ol>
<li><strong>Septal depolarization:</strong>
                    The impulse first travels down the bundle of His to the interventricular septum, where depolarization spreads from left to right. This produces a brief, small vector pointing up and to the right. It points away from the positive end of the lead axis, and its negative projection forms the initial downward <b>Q wave</b>.</li>
<li><strong>Depolarization of the main ventricular mass:</strong>
                    Next, depolarization spreads rapidly through the Purkinje network into the walls of both ventricles. Because the left ventricular wall is much thicker, its dipoles far outweigh those of the right ventricle, so the net vector is a large one pointing down and to the left. It produces a large positive projection on the lead axis, forming the tall <b>R wave</b>.
                </li>
<li><strong>Basal depolarization:</strong>
                    Finally, the base of the ventricles (the region near the atrioventricular ring) depolarizes. Here the wave travels upward, so the net vector points up, again away from the positive end of the lead axis. Its negative projection forms the downward <b>S wave</b> after the R wave.</li>
</ol>
<h5>Ventricular repolarization → T wave</h5>
<p>After depolarization, the ventricles repolarize. As discussed in the "question to think about" above, ventricular repolarization runs in the opposite order to depolarization (from epicardium to endocardium). As a result, the equivalent dipole vector of repolarization points in roughly the same direction as the depolarization (R-wave) vector. This repolarization vector, pointing down and to the left, also produces a positive projection on the lead axis and is recorded as a broader <b>T wave</b>.
            </p>
<aside class="bg-slate-50 border border-slate-200 rounded-lg p-8 my-16">
<h4 class="mt-0">📚 Bottom line: what is an ECG actually showing us?</h4>
<p>
                    We have now gone all the way from abstract physics to concrete waveforms. When we look at an ECG, we should not see isolated letters P, Q, R, S, and T. We should see it as a "film": a projected film of how the size and direction of the heart's net dipole vector change continuously through the cardiac cycle.
                </p>
<ul>
<li>
<strong>Morphology:</strong> The full shape of the P-QRS-T complex is a faithful record of how the projection of the heart's three-dimensional electrical vector onto a particular one-dimensional lead axis changes in length and direction over time.
                    </li>
<li>
<strong>The physical basis of clinical diagnosis:</strong>
                        Any disease that disturbs the sequence of electrical conduction, the distribution of myocardial mass, or the process of repolarization (such as myocardial infarction, bundle branch block, or ventricular hypertrophy) must change the "trajectory" of this moving vector, and so leaves a recognizable, characteristic change in the shape of its projection on the ECG.
                    </li>
</ul>
</aside>
</section>
<hr class="section-divider">
<!-- Summary of the whole post -->
<section id="summary">
<h2>Key Points</h2>
<p>Working from first principles as above, we can distill the complexity of the ECG into a few core physical principles:</p>
<ul>
<li><strong>The dipole is the basic unit:</strong> The basic physical model of cardiac electrical activity is the electric dipole, whose vector points from negative charge to positive charge.</li>
<li><strong>A moving boundary creates the signal:</strong> Only at the advancing front of a depolarization or repolarization wave is the symmetry of the charge distribution broken, producing a net dipole moment that can be measured at the macroscopic scale.</li>
<li><strong>The ECG is a one-dimensional projection:</strong> In essence, the ECG observes and records the heart's complex, changing three-dimensional electrical vector as projected onto a particular one-dimensional lead axis.</li>
<li><strong>The projection determines the waveform:</strong> How the magnitude and direction of the net cardiac vector change over time, as projected onto a one-dimensional lead axis, determines precisely the polarity, amplitude, and shape of the P-QRS-T complex.</li>
</ul>
</section>
</hr></main>

