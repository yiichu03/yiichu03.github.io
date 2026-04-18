---
layout: page
title: "Multi-Sensor Robot Navigation Research"
permalink: /projects/multi-sensor-nav/
---

<a href="/about/" style="font-size:0.85rem; opacity:0.7;">← Back to About</a>

<div style="margin: 1rem 0 2rem; padding: 0.6rem 1rem; background: #fff8e1; border-left: 3px solid #f0a500; border-radius: 0 6px 6px 0; font-size: 0.88rem;">
  📝 Detailed writeup coming soon. Key information is shown below.
</div>

**Period:** Aug 2025 – Dec 2025 · NUS Robotics Navigation Project

**Tech stack:** ROS2 · NVIDIA AGX Orin · BridgeDepth · NVBlox · Nav2 · LiDAR · Stereo Thermal Camera · RGB-D · 4D mmWave Radar · IEKF · VGICP

---

## Overview

This project focused on robot navigation in low-light and visually degraded environments where standard RGB cameras fail. The approach combined stereo thermal imaging, LiDAR, and RGB-D sensors into a unified navigation stack deployed on a UGV (Unmanned Ground Vehicle).

## What I Did

**Sensor pipeline & calibration**
- Built a stereo thermal / RGB-D / LiDAR multi-sensor data acquisition pipeline
- Implemented hardware-level time synchronization across heterogeneous sensors
- Completed intrinsic and extrinsic calibration

**Navigation stack on Orin**
- Integrated BridgeDepth (thermal depth estimation), NVBlox (neural volumetric mapping), Nav2, and SLAM pose input on NVIDIA AGX Orin
- Validated point-goal navigation on a real UGV platform

**4D Radar odometry**
- Connected RPM-Net (scan-to-scan soft correspondences) and Radar-Transformer (scan-to-submap hard correspondences) into a radar-inertial odometry backend (IEKF / VGICP)
- Evaluated on ColoRadar and SNAIL benchmark datasets
- Related work accepted as **ISPRS 2026 Extended Abstract**

---

*More details, figures, and results will be added here.*
