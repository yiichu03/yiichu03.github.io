---
layout: page
title: "ViT-based Quadrotor End-to-End Obstacle Avoidance"
permalink: /projects/vit-drone/
---

<a href="/about/" style="font-size:0.85rem; opacity:0.7;">← Back to About</a>

<div style="margin: 1rem 0 2rem; padding: 0.6rem 1rem; background: #fff8e1; border-left: 3px solid #f0a500; border-radius: 0 6px 6px 0; font-size: 0.88rem;">
  📝 Detailed writeup coming soon. Key information is shown below.
</div>

**Period:** Sep 2024 – May 2025 · Bachelor's Thesis · NUS Chongqing Research Institute

**Tech stack:** Python · PyTorch · ROS Noetic · Flightmare · Dodgelib · ViT · ViT-LSTM · Ubuntu 20.04

---

## Overview

Traditional UAV controllers suffer from perception-to-control latency in high-speed agile flight. This thesis project implements a Vision Transformer (ViT) based end-to-end control framework for quadrotor obstacle avoidance, comparing it against CNN and LSTM baselines in forest simulation environments.

## What I Did

**Baseline reproduction**
- Reproduced the ViT and ViT-LSTM baselines from an ICRA 2025 paper within the Flightmare + Dodgelib simulation environment
- Ran comparative experiments confirming ViT's stronger generalization in unseen forest environments vs. CNN-based controllers

**Input modality extension**
- Rebuilt the expert data collection pipeline in Flightmare to record RGB frames, drone pose, and velocity commands
- Modified the model input from single-frame depth maps to multi-frame RGB image sequences
- Added an IMU parameter fusion channel to the ViT encoder to incorporate inertial information

**Results**
- Achieved **73.26% obstacle avoidance success rate** in forest simulation
- Validated closed-loop control on a local Ubuntu dual-boot setup using Flightmare + Dodgelib

---

*More details, training curves, and ablation results will be added here.*
