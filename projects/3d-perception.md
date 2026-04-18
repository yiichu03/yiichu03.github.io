---
layout: page
title: "3D Perception — Fine-tuning & Distillation"
permalink: /projects/3d-perception/
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

  <h2>3D Perception — Model Fine-tuning &amp; Distillation <span class="liy-badge-intern">Internship</span></h2>

  <p class="liy-meta"><strong>Period:</strong> Apr 2025 – Aug 2025 &nbsp;·&nbsp; XiaoYu ZhiZao</p>
  <p class="liy-meta"><strong>Tech stack:</strong> Python · PyTorch · MAST3R · VGGT · Knowledge Distillation · 3D Point Cloud</p>

  <hr>

  <h3>Overview</h3>
  <p>This internship focused on accelerating 3D reconstruction models for real-time robot arm planning. State-of-the-art reconstruction models (MAST3R, VGGT) can produce high-quality point clouds from images end-to-end, but their inference speed does not meet the requirements of interactive robot planning loops. The goal was to reduce latency while maintaining output quality.</p>

  <h3>MAST3R Fine-tuning</h3>
  <ul>
    <li>Applied low-resolution ROPE (Rotary Position Embedding) fine-tuning to MAST3R to improve inference speed at reduced input resolutions</li>
    <li>Tuned relative position encoding to maintain spatial accuracy under lower resolution inputs</li>
    <li>Benchmarked the trade-off between point cloud quality and inference speed across different resolution settings</li>
  </ul>

  <h3>VGGT Distillation</h3>
  <ul>
    <li>Designed a distillation loss function to transfer knowledge from the full VGGT model to a lightweight student network</li>
    <li>Trained and evaluated the distilled model on indoor robot arm planning scenarios</li>
    <li>Targeted improvement in image-to-point-cloud inference throughput</li>
  </ul>

  <hr>
  <p style="opacity:.65;font-size:.85rem;">Quantitative results (speed vs. quality curves) and visual comparisons will be added here.</p>
</div>

<!-- 中文 -->
<div id="liy-zh" class="liy-hidden">
  <div class="liy-wip">📝 详细内容即将补充，以下为主要信息。</div>

  <h2>3D 感知——端到端重建模型微调与蒸馏 <span class="liy-badge-intern">实习</span></h2>

  <p class="liy-meta"><strong>时间：</strong> 2025.04 – 2025.08 &nbsp;·&nbsp; 小雨智造</p>
  <p class="liy-meta"><strong>技术栈：</strong> Python · PyTorch · MAST3R · VGGT · 知识蒸馏 · 3D 点云</p>

  <hr>

  <h3>项目概述</h3>
  <p>本实习面向机器人手臂规划的实时 3D 重建加速问题。主流重建模型（MAST3R、VGGT）能从图像端到端生成高质量点云，但推理速度不满足交互式机器人规划的实时性要求。目标是在保持输出质量的前提下降低推理延迟。</p>

  <h3>MAST3R 微调</h3>
  <ul>
    <li>对 MAST3R 进行低分辨率 ROPE（旋转位置编码）微调，提升低分辨率输入下的推理速度</li>
    <li>调整相对位置编码以在较低输入分辨率下保持空间精度</li>
    <li>对不同分辨率设置下点云质量与推理速度的权衡进行基准测试</li>
  </ul>

  <h3>VGGT 蒸馏</h3>
  <ul>
    <li>设计蒸馏 loss 函数，将 VGGT 全量模型的知识迁移到轻量学生网络</li>
    <li>在室内机械臂规划场景下训练和评估蒸馏模型</li>
    <li>目标：提升图像到点云的推理吞吐量</li>
  </ul>

  <hr>
  <p style="opacity:.65;font-size:.85rem;">速度与质量的定量对比曲线和可视化结果将在后续补充。</p>
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
