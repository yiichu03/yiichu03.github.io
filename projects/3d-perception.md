---
layout: page
title: "3D Perception — Model Fine-tuning & Distillation"
permalink: /projects/3d-perception/
---

<a href="/about/" style="font-size:0.85rem; opacity:0.7;">← Back to About</a>

<div style="margin: 1rem 0 2rem; padding: 0.6rem 1rem; background: #fff8e1; border-left: 3px solid #f0a500; border-radius: 0 6px 6px 0; font-size: 0.88rem;">
  📝 Detailed writeup coming soon. Key information is shown below.
</div>

**Period:** Apr 2025 – Aug 2025 · XiaoYu ZhiZao (Embodied AI startup, Internship)

**Tech stack:** Python · PyTorch · MAST3R · VGGT · Knowledge Distillation · 3D Point Cloud

---

## Overview

This internship focused on accelerating 3D reconstruction models for real-time robot arm planning. The core challenge: image-to-point-cloud inference from state-of-the-art reconstruction models (MAST3R, VGGT) is too slow for interactive robot planning loops. The goal was to reduce latency while maintaining output quality.

## What I Did

**MAST3R fine-tuning**
- Applied low-resolution ROPE (Rotary Position Embedding) fine-tuning to MAST3R to improve inference speed at reduced resolutions
- Tuned relative position encoding to maintain spatial accuracy at lower input resolution
- Benchmarked point cloud quality vs. inference speed trade-offs

**VGGT distillation**
- Designed a distillation loss function to transfer knowledge from the full VGGT model to a lightweight student
- Trained and evaluated the distilled model on indoor robot arm planning scenarios

---

*More details, quantitative results, and visualizations will be added here.*
