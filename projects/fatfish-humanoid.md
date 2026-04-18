---
layout: page
title: "Humanoid Robot Perception & Control Integration"
permalink: /projects/fatfish-humanoid/
---

<a href="/about/" style="font-size:0.85rem; opacity:0.7;">← Back to About</a>

<div style="margin: 1rem 0 2rem; padding: 0.6rem 1rem; background: #fff8e1; border-left: 3px solid #f0a500; border-radius: 0 6px 6px 0; font-size: 0.88rem;">
  📝 Detailed writeup coming soon. Key information is shown below.
</div>

**Period:** Feb 2026 – Mar 2026 · Fatfish AI (Internship)

**Platform:** Fourier N1 humanoid robot · NVIDIA AGX Orin (remote) · ROS2

**Tech stack:** Python · ROS2 · YOLO · RGB-D · WebSocket · rosbag · RTAB-Map

---

## Overview

Worked on the Fourier N1 humanoid robot platform, building a perception-to-control pipeline that connects on-robot RGB-D sensing, remote visual inference on an Orin compute node, and local arm joint control.

## What I Did

**Pipeline bring-up**
- Connected N1's on-robot RGB-D camera, remote YOLO-based visual inference running on Orin, and local upper-limb control into an end-to-end pipeline
- Resolved camera ownership conflicts, process scheduling issues, and network communication latency problems

**Visual following**
- Implemented cup/bottle visual following: detect target → estimate 3D centroid → command right arm to follow/approach
- Added RTT (round-trip time) feedback and system status diagnostics to help with real-hardware debugging

**On-site debugging**
- Managed rosbag recording for data collection and RTAB-Map for offline mapping
- Diagnosed and fixed inter-process conflicts during live bring-up sessions

---

*More details, system diagrams, and demo results will be added here.*
