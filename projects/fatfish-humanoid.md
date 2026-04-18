---
layout: page
title: "Humanoid Robot Perception & Control"
permalink: /projects/fatfish-humanoid/
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

## Humanoid Robot Perception & Control Integration

**Period:** Feb 2026 – Mar 2026 &nbsp;·&nbsp; Fatfish AI (Internship) &nbsp;<span style="font-size:.8rem;font-weight:700;padding:.08rem .4rem;border-radius:3px;background:#e3f5e9;color:#2d7d4f;text-transform:uppercase;letter-spacing:.05em">Internship</span>

**Platform:** Fourier N1 humanoid robot · NVIDIA AGX Orin (remote) · ROS2

**Tech stack:** Python · ROS2 · YOLO · RGB-D · WebSocket · rosbag · RTAB-Map

---

### Overview

Worked on the Fourier N1 humanoid robot platform, building a perception-to-control pipeline that connects on-robot RGB-D sensing, remote visual inference on an Orin compute node, and local upper-limb control. The key constraint: the N1 robot has limited onboard compute, so heavy vision inference runs remotely on an Orin unit and results are streamed back over the network.

### Pipeline Bring-up

- Connected N1's on-robot RGB-D camera, remote YOLO-based visual inference on Orin, and local arm joint control into an end-to-end pipeline
- Resolved camera ownership conflicts between multiple processes, process scheduling issues, and network communication latency
- Managed rosbag recording for data collection and RTAB-Map for offline mapping sessions

### Visual Following

- Implemented cup/bottle visual following: detect target object → estimate 3D centroid from depth → command right arm to follow / approach
- Added RTT (round-trip time) monitoring and system status diagnostics to the control UI to assist real-hardware debugging

### On-site Debugging

- Diagnosed and fixed inter-process conflicts arising during live bring-up
- Handled network configuration, camera device assignment, and ROS topic remapping issues across the N1-to-Orin link

---

*System architecture diagram and demo footage will be added here.*

</div>

<!-- ── 中文 ── -->
<div id="liy-zh" class="liy-hidden">

<div class="liy-wip">📝 详细内容即将补充，以下为主要信息。</div>

## 人形机器人感知与控制联调

**时间：** 2026.02 – 2026.03 &nbsp;·&nbsp; Fatfish AI（实习） &nbsp;<span style="font-size:.8rem;font-weight:700;padding:.08rem .4rem;border-radius:3px;background:#e3f5e9;color:#2d7d4f;text-transform:uppercase;letter-spacing:.05em">实习</span>

**平台：** Fourier N1 人形机器人 · NVIDIA AGX Orin（远端） · ROS2

**技术栈：** Python · ROS2 · YOLO · RGB-D · WebSocket · rosbag · RTAB-Map

---

### 项目概述

在 Fourier N1 人形机器人平台上，构建从机器人本机 RGB-D 感知到远端 Orin 视觉推理、再到本机上肢关节控制的完整感知-控制链路。关键约束：N1 本机算力有限，重型视觉推理在远端 Orin 上运行，结果通过网络实时回传。

### 链路 Bring-up

- 打通 N1 本机 RGB-D 相机采集、Orin 远端 YOLO 视觉推理与本机上肢控制端到端链路
- 处理多进程间的相机归属冲突、进程调度问题与网络通信延迟
- 管理 rosbag 数据采集与 RTAB-Map 离线建图

### 视觉跟随

- 实现 cup/bottle 视觉跟随：目标检测 → 基于深度的 3D 中心估计 → 右臂跟随/接近
- 在控制 UI 中增加 RTT（往返时间）监控与系统状态诊断，辅助实机调试

### 现场联调

- 诊断并修复现场 bring-up 时的进程冲突问题
- 处理 N1 到 Orin 链路的网络配置、相机设备归属与 ROS topic 重映射问题

---

*系统架构图与 Demo 视频将在后续补充。*

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
