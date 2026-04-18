---
layout: page
title: "Humanoid Robot Perception & Control"
permalink: /projects/fatfish-humanoid/
---

<style>
h1.dynamic-title,#page-title{display:none!important}
.liy-proj-topbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:1.8rem;flex-wrap:wrap;gap:.5rem}
.liy-back{font-size:.85rem;opacity:.7;text-decoration:none;color:inherit}.liy-back:hover{opacity:1}
.liy-lang-bar{display:flex}
.liy-lang-btn{padding:.25rem .8rem;font-size:.8rem;font-weight:600;border:1.5px solid var(--link-color,#3584e4);background:transparent;color:var(--link-color,#3584e4);cursor:pointer;transition:background .15s,color .15s}
.liy-lang-btn:first-child{border-radius:6px 0 0 6px}.liy-lang-btn:last-child{border-radius:0 6px 6px 0;border-left:none}
.liy-lang-btn.active{background:var(--link-color,#3584e4);color:#fff}
.liy-wip{margin:0 0 1.5rem;padding:.55rem .9rem;background:#fff8e1;border-left:3px solid #f0a500;border-radius:0 6px 6px 0;font-size:.86rem}
[data-mode="dark"] .liy-wip{background:#2d2200}
.liy-badge-intern{font-size:.8rem;font-weight:700;padding:.08rem .4rem;border-radius:3px;background:#e3f5e9;color:#2d7d4f;text-transform:uppercase;letter-spacing:.05em;vertical-align:middle}
.liy-meta{font-size:.88rem;margin:.4rem 0;opacity:.85}
.liy-contrib-box{margin-top:1.5rem;padding:.8rem 1.1rem;border:1.5px solid var(--link-color,#3584e4);border-radius:8px}
.liy-contrib-box h3{margin-top:0}
.liy-note{font-size:.86rem;opacity:.75;font-style:italic;margin:1rem 0}
.liy-hidden{display:none!important}
</style>

<div class="liy-proj-topbar">
  <a class="liy-back" href="/about/">← About</a>
  <div class="liy-lang-bar">
    <button class="liy-lang-btn active" id="btn-en" onclick="liySetLang('en')">EN</button>
    <button class="liy-lang-btn" id="btn-zh" onclick="liySetLang('zh')">中文</button>
  </div>
</div>

<!-- English -->
<div id="liy-en">
  <div class="liy-wip">📝 More details will be added here — content below is a working draft.</div>

  <h2>Humanoid Robot Perception &amp; Control Integration <span class="liy-badge-intern">Internship</span></h2>

  <p class="liy-meta"><strong>Period:</strong> Feb 2026 – Mar 2026 &nbsp;·&nbsp; Fatfish AI</p>
  <p class="liy-meta"><strong>Platform:</strong> Fourier N1 humanoid robot · NVIDIA AGX Orin (remote) · ROS2</p>
  <p class="liy-meta"><strong>Tech stack:</strong> Python · ROS2 · YOLO · RGB-D · SLAM · WebSocket · Web UI · rosbag</p>

  <hr>

  <h3>Project Overview</h3>
  <p>The project built a visual-following system on the Fourier N1 humanoid robot platform. The core pipeline runs object detection on a remote Orin compute unit and sends results back to the robot for arm control — a design driven by the N1's limited onboard compute. The system enables the robot to detect a target object, estimate its 3D position, and track it with the right arm.</p>
  <p class="liy-note">The algorithm design of the visual following pipeline was led by the team. My involvement focused on system integration, UI development, and on-site engineering work described below.</p>

  <div class="liy-contrib-box">
    <h3>My Contributions</h3>

    <p><strong>Algorithm understanding &amp; system integration</strong></p>
    <ul>
      <li>Studied and documented the visual-following algorithm architecture: RGB-D capture → YOLO detection → 3D centroid estimation → arm joint command</li>
      <li>Integrated components across the N1-to-Orin communication link, understanding how each module interacts</li>
    </ul>

    <p><strong>Web UI &amp; frontend–backend connection</strong></p>
    <ul>
      <li>Developed the web-based control and monitoring UI</li>
      <li>Connected the frontend status display to the backend control system</li>
      <li>Added RTT (round-trip time) monitoring so latency between Orin inference and robot control was visible during debugging</li>
    </ul>

    <p><strong>SLAM &amp; environment mapping</strong></p>
    <ul>
      <li>Used SLAM (RTAB-Map) for offline environment mapping during bring-up sessions</li>
      <li>Managed rosbag recording for data collection</li>
    </ul>

    <p><strong>On-site debugging</strong></p>
    <ul>
      <li>Resolved camera device ownership conflicts between multiple processes</li>
      <li>Fixed network routing and ROS topic remapping issues across the N1–Orin link</li>
      <li>Diagnosed and cleared process scheduling conflicts during live bring-up</li>
    </ul>
  </div>

  <hr>
  <p style="opacity:.65;font-size:.85rem;">System architecture diagram, UI screenshots, and demo footage will be added here.</p>
</div>

<!-- 中文 -->
<div id="liy-zh" class="liy-hidden">
  <div class="liy-wip">📝 详细内容将陆续补充，以下为草稿版本。</div>

  <h2>人形机器人感知与控制联调 <span class="liy-badge-intern">实习</span></h2>

  <p class="liy-meta"><strong>时间：</strong> 2026.02 – 2026.03 &nbsp;·&nbsp; Fatfish AI</p>
  <p class="liy-meta"><strong>平台：</strong> Fourier N1 人形机器人 · NVIDIA AGX Orin（远端） · ROS2</p>
  <p class="liy-meta"><strong>技术栈：</strong> Python · ROS2 · YOLO · RGB-D · SLAM · WebSocket · Web UI · rosbag</p>

  <hr>

  <h3>项目内容</h3>
  <p>本项目在 Fourier N1 人形机器人平台上构建视觉跟随系统。核心链路将目标检测运行在远端 Orin 算力节点上，推理结果传回机器人用于手臂控制——这一设计由 N1 本机算力有限决定。系统实现了机器人检测目标物体、估计其 3D 位置并以右臂进行跟随。</p>
  <p class="liy-note">视觉跟随算法的设计由团队主导；我的参与主要集中在系统集成、UI 开发与现场工程工作，详见下方。</p>

  <div class="liy-contrib-box">
    <h3>我的工作</h3>

    <p><strong>算法理解与系统集成</strong></p>
    <ul>
      <li>学习并梳理视觉跟随算法架构：RGB-D 采集 → YOLO 检测 → 3D 中心估计 → 手臂关节指令</li>
      <li>在 N1 到 Orin 的通信链路中集成各模块，理解各组件间的交互方式</li>
    </ul>

    <p><strong>Web UI 与前后端连接</strong></p>
    <ul>
      <li>开发基于 Web 的控制与监控 UI 界面</li>
      <li>打通前端状态展示与后端控制系统的连接</li>
      <li>增加 RTT（往返时间）监控，使调试时 Orin 推理与机器人控制之间的延迟可视化</li>
    </ul>

    <p><strong>SLAM 与环境建图</strong></p>
    <ul>
      <li>使用 SLAM（RTAB-Map）进行现场 bring-up 阶段的离线环境建图</li>
      <li>管理 rosbag 数据录制</li>
    </ul>

    <p><strong>现场联调</strong></p>
    <ul>
      <li>解决多进程间的相机设备归属冲突</li>
      <li>修复 N1–Orin 链路上的网络路由与 ROS topic 重映射问题</li>
      <li>诊断并处理现场 bring-up 过程中的进程调度冲突</li>
    </ul>
  </div>

  <hr>
  <p style="opacity:.65;font-size:.85rem;">系统架构图、UI 截图与 Demo 视频将在后续补充。</p>
</div>

<script>
function liySetLang(lang){
  var e=document.getElementById('liy-en'),z=document.getElementById('liy-zh');
  var be=document.getElementById('btn-en'),bz=document.getElementById('btn-zh');
  if(lang==='zh'){e.classList.add('liy-hidden');z.classList.remove('liy-hidden');be.classList.remove('active');bz.classList.add('active');}
  else{z.classList.add('liy-hidden');e.classList.remove('liy-hidden');be.classList.add('active');bz.classList.remove('active');}
  try{localStorage.setItem('liy-lang',lang);}catch(x){}
}
(function(){var p=new URLSearchParams(window.location.search).get('lang');var s;try{s=localStorage.getItem('liy-lang');}catch(x){}liySetLang(p||s||'en');})();
</script>
