---
title: "AI: The Fourth Paradigm of Scientific Discovery"
description: "An interactive lecture handout for future medical scientists on AI as the fourth paradigm of scientific discovery: its core ideas, how it works, and where it is already being used."
pubDate: 2025-12-01
externalScripts:
  - "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"
  - "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"
  - "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/MotionPathPlugin.min.js"
  - "https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"
  - "https://unpkg.com/typed.js@2.1.0/dist/typed.umd.js"
localScripts:
  - "/scripts/ai-science-paradigm.js"
localStyles:
  - "/styles/ai-science-paradigm.css"
lang: en
---

<div class="text-center mb-12 -mt-4">
  <p class="text-xl text-gray-600 dark:text-gray-300 mb-2">An interactive lecture handout for future medical scientists</p>
  <p class="text-sm font-medium text-indigo-600 dark:text-indigo-400">Compiled by Jia-Hao (Jay) Ji | Shanghai Medical College, Fudan University, eight-year MD program, class of 2019</p>
</div>

## Introduction: On the Threshold of a Scientific Revolution

The arrival of the computer revolutionized science. Calculations once thought impossible became routine, and sheer computational burden stopped being what held research back. The influence runs both ways: computer science has pushed other fields forward, and progress in those fields has in turn suggested new ways to solve problems in computer science. Few people would have guessed that results from artificial intelligence could also be applied to medical science, and that they might even open a new era for it.

For a long time, AI was associated with self-driving cars, voice assistants, and board games. Its use in scientific research, and in medical science in particular, is driving a deeper and quieter revolution. AI is no longer just a "tool" for working faster; it is becoming a new "paradigm" for doing science. The philosopher of science Thomas Kuhn argued that science does not advance by steady accumulation but through a series of "paradigm shifts." Each shift changes the basic framework through which we see the world, the methods we use to study problems, and the standards by which we judge what is true. Science has already gone through three major paradigms. Today we have the chance to witness, and take part in, the birth of the fourth.

This handout sets out the core idea of "AI as the fourth paradigm of scientific discovery." We will first look back at how the scientific method evolved, to understand why AI arrived as the natural next step at this particular moment. We will then examine AI's "worldview" (that everything can be turned into data) and the basic principle by which it works. Finally, through a series of current medical research examples, we will see how AI, acting as an accurate "prediction engine" and a sharp "hypothesis generator," is speeding up the whole path from basic research to clinical translation.

> Whether you go on to be a clinician, a basic scientist, or, like me, a physician-scientist, understanding and mastering this new paradigm will be your key to the future of medical science. Let's begin.

## Chapter 1: The Evolution of the Scientific Method: From Newton and Mendel to Deep Learning

To see why the fourth paradigm is revolutionary, we first need to look at how its predecessors paved the way. Science, at its core, builds simplified models of the real world in order to understand how it works and to make predictions. As the frontier of inquiry moved from the cosmos down to the inside of the cell, the "language" and "tools" we use to build models had to evolve too.

### 1.1 The First Paradigm: Empirical Science

This is the oldest paradigm, rooted in thousands of years of human observation of and generalization about the natural world. Its core is **experiment** and **observation**. From Aristotle's classification of plants and animals to the foundations of modern experimental science, this paradigm deals with relatively simple, linear cause-and-effect relationships.

<figure class="viz-container">
<svg id="paradigm1-viz" viewBox="0 0 400 200"></svg>
<figcaption>The first paradigm: carefully designed experiments (such as Mendel's pea crosses) to observe and generalize cause and effect directly.</figcaption>
</figure>

#### Classic case: Mendel's pea experiments

Heredity is a central part of biology. In his pea-crossing experiments, Mendel reduced the whole phenomenon of inheritance to a few independent, controllable variables (such as seed color and shape). Even so, his experiments posed a practical problem: how do you quickly work out where each crossed plant sits in the line of inheritance, so you can match it to its phenotype? Mendel's work produced many sets of data covering dozens of cross combinations, each to be matched against hundreds or thousands of experimental records. Matching across two large datasets like that is a little like running hundreds of thousands of search-engine queries at once, a computational load that would have been unimaginable. But because the amount of data was still modest, Mendel's rigorous reasoning and clever experimental design were enough to uncover the underlying laws. It was a triumph of human intelligence on a low-dimensional problem with clear cause and effect.

### 1.2 The Second Paradigm: Theoretical Science

As observational tools improved, scientists accumulated large amounts of data that simple empirical generalization could not explain. Theoretical science arose in response. It was no longer content to describe "what" happens; it tried to explain "why," using a set of universal, abstract mathematical axioms and models.

<figure class="viz-container">
<svg id="paradigm2-viz" viewBox="0 0 400 200"></svg>
<figcaption>The second paradigm: building abstract mathematical models (such as Newton's law of universal gravitation) to explain observations and make predictions.</figcaption>
</figure>

#### Classic case: Newton's gravitation and Einstein's relativity

Newton never "observed" gravity itself, but he built an elegant mathematical model (`F = G(m1*m2)/r^2`). The model not only explained the planetary motions known at the time, it also accurately predicted the existence of bodies no one had yet seen. Einstein's relativity took theoretical reasoning even further. This was science's second leap: from concrete observation to abstract theory, capturing the large-scale structure of the universe in compact equations.

### 1.3 The Third Paradigm: Computational and Statistical Science

In the second half of the 20th century, the computer brought a third revolution. On one side, for problems whose theoretical models were too complex to solve analytically (weather forecasting, fluid dynamics), we could now run **simulations** with large amounts of computing power. On the other side, fields such as biology began producing huge, noisy datasets that neither human reasoning nor compact theoretical models could handle. **Statistics** became the bridge between data and conclusions.

#### Core application: genome-wide association studies (GWAS)

In the 21st century, with the Human Genome Project completed and sequencing costs falling exponentially, we could for the first time systematically study the genetic basis of common complex diseases such as diabetes and hypertension. GWAS is the core statistical tool designed for this kind of "many causes, one outcome" problem.

The idea is simple: compare the frequencies of millions of genetic variants (SNPs) across the genomes of a "case" group and a "control" group. If a SNP is significantly more frequent in cases than in controls, we say it is statistically associated with the disease. The results are usually shown as a "Manhattan plot," in which each point is a SNP and a higher position on the Y axis means a stronger association. The strongest signals rise like skyscrapers, so the whole plot looks like the Manhattan skyline, which is where the name comes from.

<figure>
<div id="manhattan-plot-container" class="viz-container"></div>
<figcaption>The third paradigm: using computation and statistics (such as a GWAS Manhattan plot) to find statistical associations in massive datasets.</figcaption>
</figure>

#### Limits of the third paradigm:

Statistical methods such as GWAS were a big step forward, but their limits have become increasingly clear. For the most part they can tell us "where" an association lies, but not "why," and they struggle with complex interactions between genes. It is precisely where the third paradigm stalls that a more powerful tool for high-dimensional, nonlinear systems arrives: artificial intelligence.

## Chapter 2: AI's Worldview: Everything Can Be Data

We now know that science needs a new way to handle massive, complex data. The most basic reason AI can play this role is its particular "worldview": **everything in the world can be represented as data.**

For a machine to understand and work on a complex biological problem, we first have to "translate" the problem into a language the machine understands: structured data. This act of translation, or "representation," is the foundation of the whole field of AI for Science. The internal structure of each kind of biological entity determines which data representation suits it best.

### 2.1 Genomics: The Code of Life Is a Sequence

- **Data representation: string / sequence**

  The core information in a strand of DNA or RNA lies in the linear order of its four bases, A, T, C, G (or U). Structurally this closely resembles human language, where letters form words, sentences, and paragraphs. So we can represent a gene sequence directly as a long string, such as `"ATTCGATTACA..."`.

- **AI model: natural language processing (NLP) models such as the Transformer**

  The Transformer, which has excelled at translation and text generation in recent years, is above all good at capturing long-range dependencies in a sequence (how one word is influenced by another word far earlier in the text). That ability fits genomics well: a gene's function can be regulated by an enhancer tens of thousands of base pairs away. By "reading" huge numbers of gene sequences, the model learns the "grammar" and "semantics" of the genetic language, and can then predict gene function, identify regulatory elements, and even judge whether a mutation is pathogenic.

<figure>
<div id="tokenization-viz" class="viz-container tokenization-flow">
<h4>DNA sequence processing pipeline</h4>
<div class="dna-sequence">ATTCGATTACAGATTACA</div>
<div class="arrow-down">↓ Tokenization (k-mer=3)</div>
<div class="tokens-container"></div>
<div class="arrow-down">↓ Embedding (convert to vectors)</div>
<div class="vectors-container"></div>
</div>
<figcaption>Turning a DNA sequence into a vector representation a machine can use. The sequence is split into tokens, and each token is mapped to a point in a high-dimensional vector space (an embedding) that captures its biological meaning.</figcaption>
</figure>

### 2.2 Proteomics and Drug Discovery: Molecules Are Social Networks

- **Data representation: graph**

  The function of a protein or small-molecule drug depends not only on which atoms it contains but on how those atoms are connected and arranged in three-dimensional space. This structure of "entities (atoms)" and "relationships (chemical bonds)" maps neatly onto a mathematical "graph," in which each atom is a **node** and each chemical bond is an **edge**.

- **AI model: graph neural network (GNN)**

  A GNN is an AI model built specifically for graph-structured data. It works by mimicking how information spreads through a network: each node repeatedly gathers information from its neighbors and combines it with its own features to update its state. After a few rounds of "message passing," each atom node carries rich information about its local chemical environment. This lets GNNs predict protein function, identify where a drug binds its target, and even design entirely new molecular structures from scratch.

<figure>
<pre class="mermaid">
graph TD;
A[Cα] -- peptide bond --> B(N);
A -- side chain --> C{R};
A -- carbonyl --> D[C=O];
B -- H --> E[H];
</pre>
<figcaption>A graph representation of the basic structure of an amino acid. Atoms are nodes and chemical bonds are edges. Graph neural networks (GNNs) are designed to learn from exactly this kind of structured data.</figcaption>
</figure>

### 2.3 Medical Imaging: An Image Is a Matrix of Pixels

- **Data representation: matrix / tensor**

  Whether it is a pathology slide, a CT scan, or an MRI, inside a computer it is a grid of pixels or voxels. A grayscale image can be represented as a two-dimensional matrix, where each element's value is that pixel's gray level. A color image is three-dimensional, usually made of three matrices for the red (R), green (G), and blue (B) channels.

- **AI model: convolutional neural network (CNN) / Vision Transformer (ViT)**

  A CNN imitates how the visual cortex processes information. It scans the image layer by layer with "convolution kernels" (small sliding-window filters), picking out local features such as edges, textures, and shapes, and gradually combining them into higher-level concepts (such as "nucleus" or "tumor region"). The more recent ViT splits an image into small patches and, borrowing the way Transformers handle sequences, analyzes the global relationships among those patches. These models are changing the daily work of radiologists and pathologists, enabling automated detection, segmentation, and benign-versus-malignant classification of tumors and lesions.

#### A simple example: a smiley face as a matrix

Picture an 8x8-pixel black-and-white smiley face. We can represent it with an 8x8 matrix in which `1` means a black pixel and `0` means a white one. That matrix is the world as the AI "sees" it.

<figure>
<div id="smile-matrix-viz" class="viz-container">
<table id="smile-matrix-table"></table>
<div class="slider-control">
<label for="opacity-slider">Adjust image brightness</label>
<input type="range" id="opacity-slider" min="0" max="1" step="0.01" value="1">
</div>
</div>
<figcaption>An 8x8 matrix can represent a simple smiley-face image. By analyzing thousands of such matrices along with their labels ("smiling face," "crying face"), an AI learns to recognize the patterns of different expressions.</figcaption>
</figure>

## Chapter 3: AI's "Brain": Learning the Mapping Rules of the Universe

So we have learned to "translate" the biological world into data. What, then, is AI's core task? It can be summed up in a deceptively simple formula, the "first principle" for understanding modern AI in science:

```
Y = f(X)
```

The formula describes a **mapping**. `X` is the input (such as a gene sequence), `Y` is the output (such as disease risk), and `f` is the law of nature that connects them. To a large extent, the central goal of scientific research is to uncover and understand this function `f`. In the life sciences, `f` is almost always extremely complex, high-dimensional, and nonlinear.

AI's task is to "read" huge numbers of `(X, Y)` pairs and build an approximation `f̂` that comes as close as possible to the true `f`.

<figure>
<div id="nn-training-viz" class="viz-container"></div>
<figcaption>How AI learns: through repeated adjustment, it finds the function curve (the rule) that best fits the data points (the observed facts).</figcaption>
</figure>

### 3.1 The Modern Form of `f`: Neural Networks

The tool AI uses to approximate `f` is the **artificial neural network (ANN)**. Inspired by the biological brain, it consists of a large number of simple computing units, called "neurons," connected to one another.

Its learning process (also called "training") works like this:

1. **Forward pass:** Feed a known input `X` into the network and let the signal pass layer by layer until the output layer produces a prediction `Y_pred`.
2. **Compute the loss:** Compare the prediction `Y_pred` with the true label `Y_true`. The gap between them is called the "loss" or "error."
3. **Backpropagation and gradient descent:** This is the key step. The model works out how much each connection weight "contributed" to the loss, then nudges those weights slightly in the direction that reduces it. Think of a blindfolded hiker trying to reach the bottom of a valley: at each step he feels with his feet for the steepest way down (the gradient) and takes a small step that way.
4. **Iterate:** Repeat these steps billions of times, using huge amounts of data to keep "polishing" the weights. In the end, the network learns an accurate mapping from `X` to `Y`.

<figure>
<div id="nn-viz-container" class="viz-container"></div>
<figcaption>Animation of a forward pass through a neural network. The signal starts at the input layer (left), passes through the hidden layers, and produces a prediction at the output layer (right). Learning consists of repeatedly adjusting the connection weights between neurons to make the predictions as accurate as possible.</figcaption>
</figure>

## Chapter 4: AI's Two Roles: Prediction Engine and Hypothesis Generator

A well-trained model `f̂` is like an expert who has mastered a particular field. In research, we can use it at two levels.

### 4.1 Role one: an accurate "prediction engine"

This is the most direct use of AI. Once we have the function `f̂`, we can run large-scale, fast, low-cost **in silico experiments**. Given a completely new input `X_new`, the model directly computes the corresponding prediction `Y_pred`.

In drug discovery, for example, we can feed the molecular structures `X` of millions of compounds into a model, predict their activity and toxicity `Y` within a few days, and send only the few dozen top-scoring candidates to the lab for validation. That is a fundamental gain in efficiency.

<figure class="viz-container">
<svg id="prediction-engine-viz" viewBox="0 0 500 200"></svg>
<figcaption>Prediction engine: feed new, unseen data (such as candidate drug molecules) into a trained model and get a prediction directly (such as drug activity).</figcaption>
</figure>

### 4.2 Role two: a sharp "hypothesis generator"

Predicting "what" matters, but science ultimately wants to understand "why." AI models are often criticized as "black boxes": we see the inputs and outputs but not the reasoning in between. **Explainable AI (XAI)** methods developed in recent years aim to open that box and give us a look at how the model reaches its decisions.

The input features a model attends to most when it makes a judgment are themselves high-quality, data-driven scientific hypotheses. When analyzing pathology images, for example, XAI can highlight the cell regions that contribute most to the model's call of "poor prognosis." Those regions may be new biomarkers that human pathologists had never noticed.

<figure>
<div id="xai-heatmap-viz" class="viz-container">
<canvas id="xai-canvas" width="400" height="300"></canvas>
<button id="xai-button">Run XAI analysis</button>
</div>
<figcaption>Hypothesis generator: XAI methods (such as heatmaps) visualize the AI's "attention" and reveal the features that matter most for a prediction (such as a particular cell population in a pathology image), pointing human scientists to new research directions.</figcaption>
</figure>

#### Key warning: correlation ≠ causation

This is the "first commandment" to keep in mind whenever you use AI for scientific discovery. AI is extremely good at finding complex **correlations** in data, but it cannot by itself establish **causation**. A classic example: on days when ice cream sales are higher, more people drown. The two are strongly correlated, but we cannot conclude that "eating ice cream causes drowning." The real common cause is hot summer weather, which drives up both ice cream sales and the number of people swimming.

<figure>
<div id="correlation-plot-container" class="viz-container"></div>
<figcaption>Ice cream sales (blue) and drowning deaths (orange) over time. The two are strongly correlated, but the underlying driver is temperature.</figcaption>
</figure>

<div class="warning-box">
<strong>Experiment is the only test of causation</strong>
AI's role is to sift through massive data and surface the "strong correlations" most worth studying, as **scientific hypotheses**. Verifying the **causal mechanism** behind a hypothesis still requires the gold standard of science: **carefully designed, controlled experiments**. Together, AI and human scientists form a closed loop: **AI generates hypotheses, humans test causation, and knowledge advances in an upward spiral.**
</div>

## Chapter 5: Case Studies: The Fourth Paradigm in Medicine

Theory has to be proven in practice. The three cases below show, from different angles, how the fourth paradigm is being applied in current medical research.

<div class="case-study">
<div>
### 5.1 Case one: AlphaFold2, where prediction is discovery
- **Field:** Structural biology
- **Mapping `Y=f(X)`:** `3D protein structure = f(amino acid sequence)`
- **Core contribution [prediction]:** A protein's function is determined by its precise three-dimensional fold. For decades, solving a protein's structure experimentally was slow and laborious. DeepMind's AlphaFold2 learned from a vast set of sequence-structure pairs and, for the first time, reached prediction accuracy comparable to experimental methods.
- **Clinical translation:** Using similar techniques, scientists have rapidly designed new proteins that can neutralize multiple snake venoms, a possible route to broad-spectrum antivenom. Traditional methods take years; AI shortened the cycle to weeks. Here, **accurate prediction is itself the core of both the discovery and its translation.**
</div>
<figure>
<img src="https://ars.els-cdn.com/content/image/1-s2.0-S0041010123003707-ga1.jpg" alt="AlphaFold2 Protein Structure Prediction">
<figcaption>Protein structure prediction aiding antivenom development</figcaption>
</figure>
</div>

<div class="case-study">
<div>
### 5.2 Case two: Cell2Sentence, simulating life in a computer
- **Field:** Drug screening, systems biology
- **Mapping `Y=f(X)`:** `experimental outcome (text) = f(experimental conditions (text))`
- **Core contribution [prediction]:** The researchers had a large language model (LLM) "read" a vast body of biomedical literature to learn the internal "logic" of experiments. Once trained, the model can make remarkable "zero-shot" predictions.
- **Clinical translation:** Given a completely new experimental condition, the model predicts the most likely outcome, for example:
  **Input:** A549 cells treated with palbociclib.
  **AI prediction:** <span id="typed-output"></span>
</div>
<figure>
<img src="https://substackcdn.com/image/fetch/$s_!AvjH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a771189-fa64-4d2f-bd81-4053aaa31e7d_1482x1228.png" alt="Cell2Sentence Concept">
<figcaption>Language models enabling in silico experiments</figcaption>
</figure>
</div>

<div class="case-study">
<div>
### 5.3 Case three: digital pathology, AI as "microscope" and "compass"
- **Field:** Oncology, neurodegenerative disease
- **Mapping `Y=f(X)`:** `patient prognosis = f(digital pathology image)`
- **Core contribution [hypothesis generation]:** By learning from large collections of pathology images paired with clinical data, AI models can predict disease progression more accurately than human experts. More importantly, through heatmaps and similar techniques, the model can show us what it was looking at when it made its call: microscopic patterns the human eye can hardly detect.
- **Clinical translation:** The patterns AI finds are new **digital biomarkers**. They are data-driven, quantifiable scientific hypotheses that point scientists toward the molecular mechanisms hidden behind morphology.
</div>
<figure>
<img src="https://www.researchgate.net/publication/371650508/figure/fig5/AS%3A11431281210578389%401702055011438/Representative-whole-slide-images-and-attention-heatmaps-of-Fuhrman-grading-for-A.tif" alt="Digital Pathology Heatmap">
<figcaption>Pathology heatmaps help us find microscopic patterns the human eye misses</figcaption>
</figure>
</div>

## Chapter 6: The Future and Your Role: Being a Medical Scientist in the Age of Human-AI Collaboration

The fourth paradigm is not the end point of science but a new starting point. Along with large opportunities, it brings challenges:

- **Data:** High-quality, large-scale, well-annotated datasets are the "fuel" for training strong AI models.
- **Ethics and bias:** Biases in training data are "learned" and amplified by AI models, leading to inequities in care.
- **Explainability and trust:** In high-stakes clinical decisions, making models more explainable is key to putting them into use.

Facing this future, your role as a new-generation medical scientist is not to compete with machines but to become a "conductor" who works well with AI. The core skills you will need are:

<div class="roles-container">
<div class="role-card">
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
<path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3v11.25A2.25 2.25 0 006 16.5h12M3.75 3h16.5M3.75 3v16.5M19.5 3v11.25A2.25 2.25 0 0117.25 16.5H6.75" />
<path stroke-linecap="round" stroke-linejoin="round" d="M16.5 6.75h.008v.008h-.008v-.008z" />
<path stroke-linecap="round" stroke-linejoin="round" d="M9.75 12h.008v.008h-.008V12z" />
</svg>
<h4>1. Deep domain knowledge</h4>
<p>Only you truly understand the biology of disease and what patients and clinicians need. AI cannot replace you in asking the most important, most insightful scientific question.</p>
</div>
<div class="role-card">
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
<path stroke-linecap="round" stroke-linejoin="round" d="M6.75 7.5l3 2.25-3 2.25m4.5 0h3m-9 8.25h13.5A2.25 2.25 0 0021 18V6a2.25 2.25 0 00-2.25-2.25H5.25A2.25 2.25 0 003 6v12a2.25 2.25 0 002.25 2.25z" />
</svg>
<h4>2. Computational thinking</h4>
<p>You need to understand the principle that "everything is data," and be able to break a complex biological question down and recast it as a data-mapping problem an AI can work on.</p>
</div>
<div class="role-card">
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
<path stroke-linecap="round" stroke-linejoin="round" d="M12 18.75a6 6 0 006-6v-1.5m-6 7.5a6 6 0 01-6-6v-1.5m6 7.5v3.75m-3.75 0h7.5M12 15.75a3 3 0 01-3-3V4.5a3 3 0 116 0v8.25a3 3 0 01-3 3z" />
</svg>
<h4>3. Critical thinking</h4>
<p>You need a clear grasp of AI's limits, especially the difference between correlation and causation. Your central job is to design the most rigorous experiments to confirm or refute the hypotheses AI proposes.</p>
</div>
</div>

> Medical breakthroughs will increasingly come from the meeting point of human and machine intelligence. AI frees us from heavy, repetitive data analysis so that we can put our limited energy into the most creative parts of the work: asking important questions, designing elegant experiments, and arriving at deeper explanations of how the world works.<br><br>That is the promise of the fourth paradigm of science. Welcome aboard.

<div id="tooltip"></div>
