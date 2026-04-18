---
layout: page
title: "DRL-based Indoor Autonomous Exploration"
permalink: /projects/drl-exploration/
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
.liy-badge{font-size:.8rem;font-weight:700;padding:.08rem .4rem;border-radius:3px;background:#ede8ff;color:#5b3ab0;text-transform:uppercase;letter-spacing:.05em;vertical-align:middle}
.liy-meta{font-size:.88rem;margin:.4rem 0;opacity:.85}
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
  <div class="liy-wip">📝 Detailed writeup coming soon — key information is shown below.</div>

  <h2>DRL-based Indoor Autonomous Exploration <span class="liy-badge">Research</span></h2>

  <p class="liy-meta"><strong>Period:</strong> Dec 2025 – Present &nbsp;·&nbsp; NUS CORE Lab</p>
  <p class="liy-meta"><strong>Tech stack:</strong> ROS2 Humble · PyTorch · Ray · OctoMap · OccupancyGrid · ARiADNE · TARE · Livox/Hesai SLAM · Unity · Gazebo</p>

  <hr>

  <h3>Overview</h3>
  <p>Traditional frontier-based planners like TARE struggle in structured indoor environments — narrow corridors, T-junctions, and dead-ends cause <code>goal=NaN</code> failures and premature exploration termination. This project replaces TARE with ARiADNE, a DRL-based autonomous explorer, integrated into an existing ROS2 navigation stack via a minimal-substitution strategy.</p>

  <h3>Failure Analysis</h3>
  <ul>
    <li>Diagnosed TARE's parameter coupling issues, <code>goal=NaN</code> failures, and frontier utility collapse in narrow corridor and junction scenarios</li>
    <li>Mapped out the 3D point cloud SLAM → 2D OccupancyGrid perception-planning interface to identify integration points</li>
  </ul>

  <h3>System Integration</h3>
  <ul>
    <li>Integrated ARiADNE into the existing ROS2 navigation chain with minimal changes to surrounding components</li>
    <li>Connected Livox/Hesai SLAM output, OctoMap/OccupancyGrid, and waypoint interfaces</li>
    <li>Preserved the downstream local planner / path follower to minimize system disruption</li>
  </ul>

  <h3>Validation</h3>
  <ul>
    <li>Built smoke-test and experiment orchestration workflows in Unity and Gazebo environments</li>
    <li>Pre-trained ARiADNE checkpoint completed exploration in all 5 test episodes</li>
    <li>Confirmed weight compatibility between the training repository and the ROS2 inference repository</li>
  </ul>

  <hr>
  <p style="opacity:.65;font-size:.85rem;">Exploration videos, quantitative comparison with TARE, and system diagrams will be added here.</p>
</div>

<!-- 中文 -->
<div id="liy-zh" class="liy-hidden">
  <div class="liy-wip">📝 详细内容即将补充，以下为主要信息。</div>

  <h2>基于 DRL 的室内自主探索导航系统重构 <span class="liy-badge">科研</span></h2>

  <p class="liy-meta"><strong>时间：</strong> 2025.12 – 至今 &nbsp;·&nbsp; 新加坡国立大学 CORE Lab</p>
  <p class="liy-meta"><strong>技术栈：</strong> ROS2 Humble · PyTorch · Ray · OctoMap · OccupancyGrid · ARiADNE · TARE · Livox/Hesai SLAM · Unity · Gazebo</p>

  <hr>

  <h3>项目概述</h3>
  <p>传统 frontier-based 规划器（如 TARE）在结构化室内场景——窄走廊、T 型路口、死角——中容易出现 <code>goal=NaN</code> 失效和过早结束探索的问题。本项目以"最小替换"策略将 TARE 替换为 ARiADNE（基于 DRL 的自主探索器），将其接入现有 ROS2 导航链路。</p>

  <h3>失效分析</h3>
  <ul>
    <li>诊断 TARE 在窄走廊和路口场景下的参数耦合问题、<code>goal=NaN</code> 失效与 frontier utility 崩溃问题</li>
    <li>梳理 3D 点云 SLAM → 2D 占用栅格感知-规划接口，确定集成替换点</li>
  </ul>

  <h3>系统集成</h3>
  <ul>
    <li>采用"最小替换"策略将 ARiADNE 接入现有 ROS2 导航链路，对周边组件改动最小</li>
    <li>打通 Livox/Hesai SLAM 输出、OctoMap/OccupancyGrid 与 waypoint 接口</li>
    <li>保留下游 local planner / path follower，最小化系统改动</li>
  </ul>

  <h3>验证</h3>
  <ul>
    <li>在 Unity 与 Gazebo 环境中建立 smoke test 与实验编排流程</li>
    <li>预训练 ARiADNE checkpoint 在 5 个测试 episode 上均完成探索任务</li>
    <li>确认训练仓与 ROS2 推理仓的权重兼容性</li>
  </ul>

  <hr>
  <p style="opacity:.65;font-size:.85rem;">探索过程视频、与 TARE 的定量对比和系统结构图将在后续补充。</p>
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
