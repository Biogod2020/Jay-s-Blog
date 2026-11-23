I am a doctoral-stage student in the **eight-year clinical medicine program at Fudan University Shanghai Medical College**, trained in neurology. I am advised by Prof. Jin-Tai Yu (neurology, Huashan Hospital) and Prof. Zhiyuan Yuan (Fudan Institute of Science and Technology for Brain-inspired Intelligence), and I graduate in June 2027.

My research has one aim: **let a small team carry out a large biomedical data project.** Public archives hold years of valuable data, but it is stored in inconsistent formats with missing descriptions, so most of it never reaches an AI model. I build agents that do this cleanup at scale and checks that keep every output traceable to its source, so that people can trust what the agents produce.

## What I have built

### SpatialDataAgent: making public spatial-omics data usable

**First author · [bioRxiv preprint](https://www.biorxiv.org/content/10.64898/2026.05.27.727615v2) · [ICLR 2027 submission](https://openreview.net/forum?id=iB4on39JQE)** · [5-minute explainer film](/#research)

Spatial transcriptomics measures gene expression at known positions in a tissue section. A decade of these datasets sits in public archives, but each lab stored them differently across 12 platforms. I proposed and led an agent workflow that finds the datasets, writes the conversion code, checks the result against the original files, repairs what fails, and withholds anything that still does not pass. Every released sample was also checked by eye for image–expression alignment.

The resulting resource holds **12,163 samples across 42 species, including 8,211 with paired tissue images and 635 million spatial observations**. Using it, we found that when the number of training patches is held fixed, models that predict gene expression from tissue images transfer better to new studies if the patches come from more studies.

### CaseReportAgent: learning clinical decisions in the order they were made

**Research lead · manuscript in preparation**

Case reports are written after the outcome is known, so the early facts often give the answer away. CaseReportAgent rewrites published case reports as time-ordered clinical logs: each event cites the sentence or image it came from and may refer only to earlier events, so a case can be replayed at any decision point.

So far **152,258 case reports** have been rebuilt. Fine-tuning Qwen3 models on up to 80,000 decision points reduced how often a 4B model repeated an error that the case report itself documented, from 27.9% to 12.0%. The same method exposed a problem in medical AI evaluation: across 8 external benchmarks, **1–75% of questions leak their answer**.

### Choosing the right answer in multi-agent systems

**Co-first author · [arXiv:2608.25937](https://arxiv.org/abs/2608.25937)**

When several AI agents answer a question, the correct answer is often already among them, yet majority voting discards it when a popular wrong answer outnumbers it. I designed a selection rule that combines answer frequency with an LLM judge's score. Across 5 benchmarks and 16,278 questions, keeping the candidate answers fixed and changing only this rule raised accuracy from **63.82% to 70.82–70.95%**.

### Spatial organisation of Alzheimer's disease

**Co-first author · under review at *Science***

This study links reactive microglia in subpallial brain regions to the vulnerability of cholinergic neurons in Alzheimer's disease. I registered the spatial transcriptomics sections and ran most of the quantitative spatial analysis, including the GOLD index, which tests whether microglial expression states change with distance from amyloid plaques.

### BioMed-Banana: cell segmentation from an image-editing model

**Study design and main implementation · manuscript in preparation**

Adapting a segmentation model to a new tissue or stain usually needs many annotated images. I adapted the open image-editing model Qwen-Image-Edit to draw coloured cell masks. With 128 training images it reached panoptic quality 0.625 on 2,722 PanNuke test images, above Cellpose-SAM (0.602), which was trained on 22,826 images.

## What comes next

The next resource applies the same approach to **brain MRI**: scans from many sources and sequences, with consistent metadata, quality records and a link back to every original file, built for AI pretraining and neuroscience analysis.

Behind it is a question I want to answer properly: how the yield of reliable data changes as agents get more compute and more varied sources, and at which points a short human check is worth more than another round of automatic repair.

## Earlier training

- **Prof. Bin Song's lab, Fudan University (2021–2023):** single-cell RNA-seq pipelines for iPSC-derived dopaminergic progenitor transplantation in Parkinson's disease.
- **Prof. Fei Lan's lab, Institutes of Biomedical Sciences (2019–2021):** wet-lab training in molecular assays, DNA methylation and epigenetics.
- **Clinical:** core rotations at Fudan-affiliated hospitals; internal medicine elective at Queen Mary Hospital, The University of Hong Kong (2025); exchange student at UCLA (2021–2022).

## Teaching

I make medical education videos in Chinese and English on [Bilibili](https://space.bilibili.com/645730045/) and [YouTube](https://www.youtube.com/@JayJi-wm7yp/playlists), and have taught probability and statistics as a volunteer at middle schools in Guizhou and Guangdong. I also share the agent tools I build, such as [dsh-article-review](https://github.com/Biogod2020/dsh-article-review) and [simple-fig-skill](https://github.com/Biogod2020/simple-fig-skill), so other researchers can use them.

## Background

I grew up in Guangzhou in a Teochew family. A provincial top-ten result in the National Biology Olympiad first drew me to research. I speak Mandarin, Cantonese, Teochew and English.

![At UC Berkeley](/life_photo.jpg)

*At UC Berkeley during my UCLA exchange, 2021–2022.*

![At HKUST](/hkust_photo.jpg)

*Visiting HKUST during my HKU clinical elective, 2025.*
