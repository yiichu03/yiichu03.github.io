---
layout: page
title: "ViT Quadrotor Obstacle Avoidance"
permalink: /projects/vit-drone/
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
.liy-badge-thesis{font-size:.8rem;font-weight:700;padding:.08rem .4rem;border-radius:3px;background:#fff3e0;color:#b85c00;text-transform:uppercase;letter-spacing:.05em;vertical-align:middle}
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

  <h2>ViT-based Quadrotor End-to-End Obstacle Avoidance <span class="liy-badge-thesis">Thesis</span></h2>

  <p class="liy-meta"><strong>Period:</strong> Sep 2024 – May 2025 &nbsp;·&nbsp; NUS Chongqing Research Institute</p>
  <p class="liy-meta"><strong>Tech stack:</strong> Python · PyTorch · ROS Noetic · Flightmare · Dodgelib · ViT · ViT-LSTM · Ubuntu 20.04</p>

  <hr>

  <h3>Overview</h3>
  <p>Traditional UAV controllers suffer from perception-to-control latency in high-speed agile flight, especially when relying on classical pipelines. This thesis implements a Vision Transformer (ViT) based end-to-end control framework for quadrotor obstacle avoidance in forest environments, comparing it against CNN and LSTM-based baselines.</p>

  <h3>Baseline Reproduction</h3>
  <ul>
    <li>Reproduced the ViT and ViT-LSTM baselines from an ICRA 2025 paper within the Flightmare + Dodgelib simulation environment</li>
    <li>Ran comparative experiments confirming ViT's stronger out-of-distribution generalization compared to CNN-based controllers in unseen forest environments</li>
  </ul>

  <h3>Input Modality Extension</h3>
  <ul>
    <li>Rebuilt the expert data collection pipeline in Flightmare, recording RGB frames, drone pose, and velocity commands</li>
    <li>Modified the model input from single-frame depth maps to multi-frame RGB image sequences, allowing temporal context</li>
    <li>Added an IMU parameter fusion channel to the ViT encoder to incorporate inertial information</li>
  </ul>

  <h3>Results</h3>
  <ul>
    <li>Achieved <strong>73.26% obstacle avoidance success rate</strong> in forest simulation (Flightmare + Dodgelib)</li>
    <li>Validated closed-loop control on a local Ubuntu 20.04 dual-boot setup</li>
  </ul>

  <hr>
  <p style="opacity:.65;font-size:.85rem;">Training curves, ablation results, and simulation recordings will be added here.</p>
</div>

<!-- 中文 -->
<div id="liy-zh" class="liy-hidden">
  <div class="liy-wip">📝 详细内容即将补充，以下为主要信息。</div>

  <h2>基于 ViT 的四旋翼无人机端到端避障系统 <span class="liy-badge-thesis">毕设</span></h2>

  <p class="liy-meta"><strong>时间：</strong> 2024.09 – 2025.05 &nbsp;·&nbsp; 新加坡国立大学重庆研究院</p>
  <p class="liy-meta"><strong>技术栈：</strong> Python · PyTorch · ROS Noetic · Flightmare · Dodgelib · ViT · ViT-LSTM · Ubuntu 20.04</p>

  <hr>

  <h3>项目概述</h3>
  <p>传统无人机控制器在高速敏捷飞行中存在感知到控制的延迟问题，尤其是在依赖经典管线的情况下。本毕设基于 Vision Transformer（ViT）实现四旋翼无人机端到端避障控制框架，并在树林仿真环境中与 CNN 和 LSTM 基线进行比较。</p>

  <h3>基线复现</h3>
  <ul>
    <li>在 Flightmare + Dodgelib 仿真环境中复现 ICRA 2025 论文的 ViT 与 ViT-LSTM 基线</li>
    <li>对比实验确认 ViT 在陌生树林环境中相比 CNN 控制器具有更强的分布外泛化性</li>
  </ul>

  <h3>输入模态扩展</h3>
  <ul>
    <li>基于 Flightmare 重构专家数据采集流程，记录 RGB 图像、无人机位姿与速度指令</li>
    <li>将模型输入从单帧深度图改为多帧 RGB 图像序列，引入时序上下文</li>
    <li>在 ViT 编码器中增加 IMU 参数融合通道以引入惯性信息</li>
  </ul>

  <h3>结果</h3>
  <ul>
    <li>在树林仿真环境（Flightmare + Dodgelib）中达到 <strong>73.26% 避障成功率</strong></li>
    <li>在本地 Ubuntu 20.04 双系统上完成闭环控制验证</li>
  </ul>

  <hr>
  <p style="opacity:.65;font-size:.85rem;">训练曲线、消融实验结果与仿真录像将在后续补充。</p>
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
