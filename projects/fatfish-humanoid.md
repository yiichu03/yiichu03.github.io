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
.liy-contrib-box{margin-top:1.5rem;padding:.8rem 1.1rem;border:1.5px solid var(--link-color,#3584e4);border-radius:8px;}
.liy-contrib-box h3{margin-top:0;}
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

<div class="liy-wip">📝 More details will be added here — content below is a working draft.</div>

## Humanoid Robot Perception & Control Integration

**Period:** Feb 2026 – Mar 2026 &nbsp;·&nbsp; Fatfish AI (Internship) &nbsp;<span style="font-size:.8rem;font-weight:700;padding:.08rem .4rem;border-radius:3px;background:#e3f5e9;color:#2d7d4f;text-transform:uppercase;letter-spacing:.05em">Internship</span>

**Platform:** Fourier N1 humanoid robot · NVIDIA AGX Orin (remote) · ROS2

**Tech stack:** Python · ROS2 · YOLO · RGB-D · SLAM · WebSocket · Web UI · rosbag

---

### Project Overview

The project built a visual-following system on the Fourier N1 humanoid robot platform. The core pipeline runs object detection on a remote Orin compute unit and sends results back to the robot for arm control — a design driven by the N1's limited onboard compute. The system enables the robot to detect a target object, estimate its 3D position, and track it with the right arm.

*The algorithm design of the visual following pipeline was led by the team; my involvement focused on system integration, UI, and on-site engineering work described below.*

---

<div class="liy-contrib-box">

### My Contributions

**Algorithm understanding & system integration**
- Studied and documented the visual-following algorithm architecture: RGB-D capture → YOLO detection → 3D centroid estimation → arm joint command
- Integrated components across the N1-to-Orin communication link, understanding how each module interacts

**Web UI & frontend–backend connection**
- Developed the web-based control and monitoring UI
- Connected the frontend status display to the backend control system
- Added RTT (round-trip time) monitoring so latency between Orin inference and robot control was visible during debugging

**SLAM & environment mapping**
- Used SLAM (RTAB-Map) for offline environment mapping during bring-up sessions
- Managed rosbag recording for data collection

**On-site debugging**
- Resolved camera device ownership conflicts between multiple processes
- Fixed network routing and ROS topic remapping issues across the N1–Orin link
- Diagnosed and cleared process scheduling conflicts during live bring-up

</div>

---

*System architecture diagram, UI screenshots, and demo footage will be added here.*

</div>

<!-- ── 中文 ── -->
<div id="liy-zh" class="liy-hidden">

<div class="liy-wip">📝 详细内容将陆续补充，以下为草稿版本。</div>

## 人形机器人感知与控制联调

**时间：** 2026.02 – 2026.03 &nbsp;·&nbsp; Fatfish AI（实习） &nbsp;<span style="font-size:.8rem;font-weight:700;padding:.08rem .4rem;border-radius:3px;background:#e3f5e9;color:#2d7d4f;text-transform:uppercase;letter-spacing:.05em">实习</span>

**平台：** Fourier N1 人形机器人 · NVIDIA AGX Orin（远端） · ROS2

**技术栈：** Python · ROS2 · YOLO · RGB-D · SLAM · WebSocket · Web UI · rosbag

---

### 项目内容

本项目在 Fourier N1 人形机器人平台上构建视觉跟随系统。核心链路将目标检测运行在远端 Orin 算力节点上，推理结果传回机器人用于手臂控制——这一设计由 N1 本机算力有限决定。系统实现了机器人检测目标物体、估计其 3D 位置并以右臂进行跟随。

*视觉跟随算法的设计由团队主导；我的参与主要集中在系统集成、UI 开发与现场工程工作，详见下方。*

---

<div class="liy-contrib-box">

### 我的工作

**算法理解与系统集成**
- 学习并梳理视觉跟随算法架构：RGB-D 采集 → YOLO 检测 → 3D 中心估计 → 手臂关节指令
- 在 N1 到 Orin 的通信链路中集成各模块，理解各组件间的交互方式

**Web UI 与前后端连接**
- 开发基于 Web 的控制与监控 UI 界面
- 打通前端状态展示与后端控制系统的连接
- 增加 RTT（往返时间）监控，使调试时 Orin 推理与机器人控制之间的延迟可视化

**SLAM 与环境建图**
- 使用 SLAM（RTAB-Map）进行现场 bring-up 阶段的离线环境建图
- 管理 rosbag 数据录制

**现场联调**
- 解决多进程间的相机设备归属冲突
- 修复 N1–Orin 链路上的网络路由与 ROS topic 重映射问题
- 诊断并处理现场 bring-up 过程中的进程调度冲突

</div>

---

*系统架构图、UI 截图与 Demo 视频将在后续补充。*

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
