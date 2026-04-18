---
layout: page
title: "DRL-based Indoor Autonomous Exploration"
permalink: /projects/drl-exploration/
---

<a href="/about/" style="font-size:0.85rem; opacity:0.7;">← Back to About</a>

<div style="margin: 1rem 0 2rem; padding: 0.6rem 1rem; background: #fff8e1; border-left: 3px solid #f0a500; border-radius: 0 6px 6px 0; font-size: 0.88rem;">
  📝 Detailed writeup coming soon. Key information is shown below.
</div>

**Period:** Dec 2025 – Present · NUS Robotics Navigation Project

**Tech stack:** ROS2 Humble · PyTorch · Ray · OctoMap · OccupancyGrid · ARiADNE · TARE · Livox/Hesai SLAM · Unity · Gazebo

---

## Overview

Traditional frontier-based planners like TARE struggle in structured indoor environments — narrow corridors, T-junctions, and dead-ends cause goal=NaN failures and premature exploration termination. This project replaces TARE with ARiADNE, a DRL-based autonomous explorer, integrated into an existing ROS2 navigation stack via a minimal-substitution approach.

## What I Did

**Failure analysis**
- Diagnosed TARE's parameter coupling issues, goal=NaN failures, and frontier utility collapse in narrow corridors and junction scenarios
- Mapped out the 3D point cloud SLAM → 2D OccupancyGrid perception-planning interface

**System integration**
- Integrated ARiADNE into the existing ROS2 navigation chain using a minimal-substitution strategy
- Connected Livox/Hesai SLAM output, OctoMap/OccupancyGrid, and waypoint interfaces
- Preserved the downstream local planner / path follower to minimize system disruption

**Validation**
- Built smoke-test and experiment orchestration workflows in Unity and Gazebo environments
- Pre-trained ARiADNE checkpoint completed exploration in all 5 test episodes
- Confirmed weight compatibility between the training repo and ROS2 inference repo

---

*More details, figures, and results will be added here.*
