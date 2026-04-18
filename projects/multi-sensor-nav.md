---
layout: page
title: "Multi-Sensor Robot Navigation"
permalink: /projects/multi-sensor-nav/
---

<style>
.liy-proj-topbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:1.8rem;flex-wrap:wrap;gap:.5rem}
.liy-back{font-size:.85rem;opacity:.7;text-decoration:none;color:inherit}.liy-back:hover{opacity:1}
.liy-lang-bar{display:flex}
.liy-lang-btn{padding:.25rem .8rem;font-size:.8rem;font-weight:600;border:1.5px solid var(--link-color,#3584e4);background:transparent;color:var(--link-color,#3584e4);cursor:pointer;transition:background .15s,color .15s}
.liy-lang-btn:first-child{border-radius:6px 0 0 6px}.liy-lang-btn:last-child{border-radius:0 6px 6px 0;border-left:none}
.liy-lang-btn.active{background:var(--link-color,#3584e4);color:#fff}
.liy-wip{margin:0 0 1.5rem;padding:.55rem .9rem;background:#fff8e1;border-left:3px solid #f0a500;border-radius:0 6px 6px 0;font-size:.86rem}
[data-mode="dark"] .liy-wip{background:#2d2200}
.liy-hidden{display:none!important}
</style>

<div class="liy-proj-topbar">
  <a class="liy-back" href="/about/">← About</a>
  <div class="liy-lang-bar">
    <button class="liy-lang-btn active" id="btn-en" onclick="liySetLang('en')">EN</button>
    <button class="liy-lang-btn" id="btn-zh" onclick="liySetLang('zh')">中文</button>
  </div>
</div>

<!-- ── English ── -->
<div id="liy-en">

<div class="liy-wip">📝 Detailed writeup coming soon — key information is shown below.</div>

## Multi-Sensor Robot Navigation Research

**Period:** Aug 2025 – Dec 2025 &nbsp;·&nbsp; NUS Robotics Navigation Project &nbsp;<span style="font-size:.8rem;font-weight:700;padding:.08rem .4rem;border-radius:3px;background:#ede8ff;color:#5b3ab0;text-transform:uppercase;letter-spacing:.05em">Research</span>

**Tech stack:** ROS2 · NVIDIA AGX Orin · BridgeDepth · NVBlox · Nav2 · LiDAR · Stereo Thermal Camera · RGB-D · 4D mmWave Radar · IEKF · VGICP

---

### Overview

This project focused on robot navigation in low-light and visually degraded environments where standard RGB cameras fail. The approach combined stereo thermal imaging, LiDAR, and RGB-D sensors into a unified navigation stack, deployed and validated on a real UGV (Unmanned Ground Vehicle).

### Sensor Pipeline & Calibration

- Built a stereo thermal / RGB-D / LiDAR multi-sensor data acquisition pipeline
- Implemented hardware-level time synchronization across heterogeneous sensors
- Completed intrinsic and extrinsic calibration for all sensor pairs

### Navigation Stack on AGX Orin

- Integrated BridgeDepth (thermal depth estimation), NVBlox (neural volumetric mapping), Nav2, and SLAM pose input on NVIDIA AGX Orin
- Validated point-goal navigation on a real UGV platform in indoor environments

### 4D Radar Odometry

- Connected RPM-Net (scan-to-scan soft correspondences) and Radar-Transformer (scan-to-submap hard correspondences) into a radar-inertial odometry backend (IEKF / VGICP)
- Evaluated on ColoRadar and SNAIL benchmark datasets
- Related work accepted as **ISPRS 2026 Extended Abstract**

---

*Figures, videos, and quantitative results will be added here.*

</div>

<!-- ── 中文 ── -->
<div id="liy-zh" class="liy-hidden">

<div class="liy-wip">📝 详细内容即将补充，以下为主要信息。</div>

## 多传感器机器人导航与定位研究

**时间：** 2025.08 – 2025.12 &nbsp;·&nbsp; NUS 机器人导航项目 &nbsp;<span style="font-size:.8rem;font-weight:700;padding:.08rem .4rem;border-radius:3px;background:#ede8ff;color:#5b3ab0;text-transform:uppercase;letter-spacing:.05em">科研</span>

**技术栈：** ROS2 · NVIDIA AGX Orin · BridgeDepth · NVBlox · Nav2 · LiDAR · 双目热红外相机 · RGB-D · 4D 毫米波雷达 · IEKF · VGICP

---

### 项目概述

本项目面向低照度与视觉退化环境中的机器人导航问题。在标准 RGB 相机失效的场景下，通过融合双目热红外成像、LiDAR 与 RGB-D 传感器，构建完整的导航栈，并在真实 UGV（无人地面车辆）上完成实机部署与验证。

### 传感器链路与标定

- 搭建双目热红外 / RGB-D / LiDAR 多传感器采集链路
- 实现跨异构传感器的硬件级时间同步
- 完成所有传感器对的内外参标定

### AGX Orin 上的导航栈

- 在 NVIDIA AGX Orin 上集成 BridgeDepth（热红外深度估计）、NVBlox（神经体积建图）、Nav2 与 SLAM 位姿输入
- 在室内环境下的真实 UGV 平台上完成 point-goal 导航实机验证

### 4D 雷达里程计

- 将 RPM-Net（scan-to-scan 软对应）与 Radar-Transformer（scan-to-submap 硬对应）接入雷达惯性里程计后端（IEKF / VGICP）
- 在 ColoRadar 与 SNAIL 基准数据集上完成评测
- 相关工作已被接受为 **ISPRS 2026 Extended Abstract**

---

*图片、视频与定量结果将在后续补充。*

</div>

<script>
function liySetLang(lang){
  var e=document.getElementById('liy-en'),z=document.getElementById('liy-zh');
  var be=document.getElementById('btn-en'),bz=document.getElementById('btn-zh');
  if(lang==='zh'){e.classList.add('liy-hidden');z.classList.remove('liy-hidden');be.classList.remove('active');bz.classList.add('active');}
  else{z.classList.add('liy-hidden');e.classList.remove('liy-hidden');be.classList.add('active');bz.classList.remove('active');}
  try{localStorage.setItem('liy-lang',lang);}catch(ex){}
}
(function(){
  var p=new URLSearchParams(window.location.search).get('lang');
  var s;try{s=localStorage.getItem('liy-lang');}catch(ex){}
  liySetLang(p||s||'en');
})();
</script>
