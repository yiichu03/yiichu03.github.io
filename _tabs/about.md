---
layout: page
title: About
icon: fas fa-user
order: 1
---

<style>
/* ── Language Toggle ── */
.liy-lang-bar {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1.6rem;
  gap: 0;
}
.liy-lang-btn {
  padding: 0.28rem 0.9rem;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  border: 1.5px solid var(--link-color, #3584e4);
  background: transparent;
  color: var(--link-color, #3584e4);
  cursor: pointer;
  transition: background 0.15s, color 0.15s;
}
.liy-lang-btn:first-child { border-radius: 6px 0 0 6px; }
.liy-lang-btn:last-child  { border-radius: 0 6px 6px 0; border-left: none; }
.liy-lang-btn.active {
  background: var(--link-color, #3584e4);
  color: #fff;
}

/* ── Profile Header ── */
.liy-profile {
  display: flex;
  align-items: flex-start;
  gap: 2rem;
  margin-bottom: 2rem;
}
.liy-avatar {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  object-fit: cover;
  object-position: top;
  flex-shrink: 0;
  border: 3px solid var(--border-color, #e0e0e0);
}
.liy-profile-info { flex: 1; }
.liy-profile-info h1 {
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0 0 0.3rem 0;
}
.liy-name-sub {
  display: inline-block;
  font-size: 1.1rem;
  font-weight: 400;
  opacity: 0.6;
  margin-left: 0.4rem;
}
.liy-affil {
  font-size: 0.95rem;
  opacity: 0.8;
  margin: 0 0 0.5rem 0;
}
.liy-seeking {
  display: inline-block;
  font-size: 0.82rem;
  font-weight: 600;
  padding: 0.2rem 0.7rem;
  border-radius: 20px;
  background: #e8f4fd;
  color: #1a6fa8;
  margin-bottom: 0.9rem;
}
[data-mode="dark"] .liy-seeking {
  background: #1a3550;
  color: #7ec8f0;
}
.liy-contacts {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  align-items: center;
}
.liy-contact-link {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.85rem;
  padding: 0.22rem 0.7rem;
  border-radius: 6px;
  border: 1px solid var(--border-color, #ddd);
  color: inherit;
  text-decoration: none !important;
  transition: border-color 0.15s;
}
.liy-contact-link:hover { border-color: var(--link-color, #3584e4); }

/* ── Section styling ── */
.liy-section { margin-top: 2rem; }
.liy-section h2 {
  font-size: 1.1rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  padding-bottom: 0.4rem;
  border-bottom: 2px solid var(--link-color, #3584e4);
  margin-bottom: 1rem;
}

/* ── Skills ── */
.liy-skill-group { margin-bottom: 0.7rem; display: flex; align-items: baseline; gap: 0.5rem; flex-wrap: wrap; }
.liy-skill-label { font-size: 0.78rem; font-weight: 600; opacity: 0.6; min-width: 5.5rem; flex-shrink: 0; }
.liy-skill-tags { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.liy-tag {
  font-size: 0.78rem;
  padding: 0.15rem 0.55rem;
  border-radius: 4px;
  background: #eef2f8;
  color: #2d4a7a;
}
[data-mode="dark"] .liy-tag { background: #1e2d45; color: #93b4db; }

/* ── Experience Timeline ── */
.liy-exp-list { display: flex; flex-direction: column; gap: 1.2rem; }
.liy-exp-item {
  border-left: 3px solid var(--link-color, #3584e4);
  padding-left: 1rem;
}
.liy-exp-header { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.3rem; }
.liy-exp-title { font-weight: 700; font-size: 0.97rem; }
.liy-exp-date { font-size: 0.78rem; opacity: 0.6; white-space: nowrap; }
.liy-exp-org { font-size: 0.83rem; opacity: 0.75; margin: 0.15rem 0 0.4rem 0; }
.liy-exp-body { font-size: 0.88rem; line-height: 1.65; }
.liy-exp-body ul { margin: 0.3rem 0 0 1rem; padding: 0; }
.liy-exp-body li { margin-bottom: 0.25rem; }

/* ── Publications ── */
.liy-pub-item {
  background: #f5f8fc;
  border-left: 3px solid var(--link-color, #3584e4);
  border-radius: 0 6px 6px 0;
  padding: 0.75rem 1rem;
  font-size: 0.88rem;
  line-height: 1.6;
}
[data-mode="dark"] .liy-pub-item { background: #1a2535; }
.liy-pub-venue {
  display: inline-block;
  font-weight: 700;
  font-size: 0.75rem;
  padding: 0.1rem 0.5rem;
  border-radius: 4px;
  background: var(--link-color, #3584e4);
  color: #fff;
  margin-bottom: 0.35rem;
}
.liy-pub-accepted {
  font-size: 0.75rem;
  color: #2e8b57;
  font-weight: 600;
  margin-left: 0.4rem;
}
[data-mode="dark"] .liy-pub-accepted { color: #5dbb8a; }

/* ── Education ── */
.liy-edu-list { display: flex; flex-direction: column; gap: 0.9rem; }
.liy-edu-item { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.3rem; }
.liy-edu-left .liy-edu-school { font-weight: 700; font-size: 0.97rem; }
.liy-edu-left .liy-edu-degree { font-size: 0.85rem; opacity: 0.8; margin-top: 0.1rem; }
.liy-edu-right { text-align: right; font-size: 0.82rem; opacity: 0.65; }

/* ── Responsive ── */
@media (max-width: 600px) {
  .liy-profile { flex-direction: column; align-items: center; text-align: center; }
  .liy-contacts { justify-content: center; }
  .liy-exp-header { flex-direction: column; }
  .liy-edu-item { flex-direction: column; }
  .liy-edu-right { text-align: left; }
}

.liy-hidden { display: none !important; }
</style>

<!-- Language Toggle -->
<div class="liy-lang-bar">
  <button class="liy-lang-btn active" id="btn-en" onclick="liySetLang('en')">EN</button>
  <button class="liy-lang-btn" id="btn-zh" onclick="liySetLang('zh')">中文</button>
</div>

<!-- ════════════════════════ ENGLISH ════════════════════════ -->
<div id="liy-en">

<div class="liy-profile">
  <img src="/assets/img/avatar.jpg" alt="Liu Yi" class="liy-avatar">
  <div class="liy-profile-info">
    <h1>Liu Yi <span class="liy-name-sub">刘弈</span></h1>
    <p class="liy-affil">M.Eng. Computer Engineering &nbsp;·&nbsp; National University of Singapore</p>
    <span class="liy-seeking">🔍 Seeking research internship opportunities in robotics &amp; AI</span>
    <div class="liy-contacts">
      <a class="liy-contact-link" href="mailto:e1538633@u.nus.edu">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
        e1538633@u.nus.edu
      </a>
      <a class="liy-contact-link" href="https://github.com/yiichu03" target="_blank" rel="noopener">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0 1 12 6.844a9.59 9.59 0 0 1 2.504.337c1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.02 10.02 0 0 0 22 12.017C22 6.484 17.522 2 12 2z"/></svg>
        yiichu03
      </a>
    </div>
  </div>
</div>

<div class="liy-section">
  <h2>About Me</h2>
  <p>I am a Master's student in Computer Engineering at the National University of Singapore (NUS), with a strong interest in robot autonomy and intelligent systems. My work spans multi-sensor navigation (thermal, LiDAR, 4D radar), SLAM, end-to-end learning for robotic control, and real-world system deployment on UGV and humanoid robot platforms.</p>
  <p>I enjoy bridging learning-based methods with practical robotic systems — getting things to actually run on hardware is what excites me most.</p>
</div>

<div class="liy-section">
  <h2>Research Interests</h2>
  <ul>
    <li>Multi-sensor robot navigation — thermal, LiDAR, 4D mmWave radar</li>
    <li>SLAM and autonomous exploration in unknown environments</li>
    <li>End-to-end learning for robotic perception and control</li>
    <li>Embodied AI and humanoid robot systems</li>
  </ul>
</div>

<div class="liy-section">
  <h2>Skills</h2>
  <div class="liy-skill-group">
    <span class="liy-skill-label">Languages</span>
    <div class="liy-skill-tags">
      <span class="liy-tag">Python</span><span class="liy-tag">C++</span><span class="liy-tag">PyTorch</span><span class="liy-tag">ROS2</span>
    </div>
  </div>
  <div class="liy-skill-group">
    <span class="liy-skill-label">Tools &amp; Env</span>
    <div class="liy-skill-tags">
      <span class="liy-tag">Linux</span><span class="liy-tag">Git</span><span class="liy-tag">Docker</span><span class="liy-tag">Isaac Sim</span><span class="liy-tag">Gazebo</span><span class="liy-tag">NVIDIA AGX Orin</span>
    </div>
  </div>
  <div class="liy-skill-group">
    <span class="liy-skill-label">Sensors</span>
    <div class="liy-skill-tags">
      <span class="liy-tag">LiDAR</span><span class="liy-tag">RGB-D</span><span class="liy-tag">Stereo Thermal Camera</span><span class="liy-tag">4D mmWave Radar</span>
    </div>
  </div>
  <div class="liy-skill-group">
    <span class="liy-skill-label">Methods</span>
    <div class="liy-skill-tags">
      <span class="liy-tag">Transformer / ViT</span><span class="liy-tag">SLAM</span><span class="liy-tag">Nav2</span><span class="liy-tag">DRL</span><span class="liy-tag">3D Point Cloud</span><span class="liy-tag">Knowledge Distillation</span>
    </div>
  </div>
</div>

<div class="liy-section">
  <h2>Experience</h2>
  <div class="liy-exp-list">

    <div class="liy-exp-item">
      <div class="liy-exp-header">
        <span class="liy-exp-title">Multi-Sensor Robot Navigation Research</span>
        <span class="liy-exp-date">Aug 2025 – Dec 2025</span>
      </div>
      <div class="liy-exp-org">Robotics Navigation Project &nbsp;·&nbsp; NUS</div>
      <div class="liy-exp-body">
        <ul>
          <li>Built a stereo thermal / RGB-D / LiDAR data acquisition pipeline with hardware-level time synchronization and intrinsic/extrinsic calibration for low-light and visually degraded environments.</li>
          <li>Integrated BridgeDepth, NVBlox, Nav2, and SLAM pose input on NVIDIA AGX Orin for point-goal navigation on a UGV; validated the full system on real hardware.</li>
          <li>Connected RPM-Net (scan-to-scan soft correspondences) and Radar-Transformer (scan-to-submap hard correspondences) into a radar-inertial odometry backend (IEKF / VGICP); evaluated on ColoRadar and SNAIL datasets.</li>
        </ul>
      </div>
    </div>

    <div class="liy-exp-item">
      <div class="liy-exp-header">
        <span class="liy-exp-title">DRL-based Indoor Autonomous Exploration</span>
        <span class="liy-exp-date">Dec 2025 – Present</span>
      </div>
      <div class="liy-exp-org">Robotics Navigation Project &nbsp;·&nbsp; NUS</div>
      <div class="liy-exp-body">
        <ul>
          <li>Identified failure modes of the TARE planner in narrow corridors and junctions (goal=NaN, frontier utility collapse); restructured the 3D SLAM → 2D OccupancyGrid perception-planning interface.</li>
          <li>Replaced TARE with ARiADNE (DRL-based explorer) using a minimal-substitution strategy, integrating Livox/Hesai SLAM, OctoMap/OccupancyGrid, and waypoint interfaces while keeping the downstream local planner.</li>
          <li>Built smoke-test and experiment orchestration workflows in Unity and Gazebo; pre-trained checkpoint completed exploration in all 5 test episodes, confirming weight compatibility between training and ROS2 inference repos.</li>
        </ul>
      </div>
    </div>

    <div class="liy-exp-item">
      <div class="liy-exp-header">
        <span class="liy-exp-title">Humanoid Robot Perception &amp; Control Integration</span>
        <span class="liy-exp-date">Feb 2026 – Mar 2026</span>
      </div>
      <div class="liy-exp-org">Fatfish AI &nbsp;·&nbsp; Robotics Intern</div>
      <div class="liy-exp-body">
        <ul>
          <li>On the Fourier N1 platform: connected on-robot RGB-D capture, remote visual inference on Orin, and local arm control into a unified pipeline.</li>
          <li>Implemented cup/bottle visual following for the right arm; added RTT feedback and status diagnostics to assist real-hardware debugging sessions.</li>
          <li>Resolved process conflicts, network communication issues, and camera ownership conflicts during on-site bring-up.</li>
        </ul>
      </div>
    </div>

    <div class="liy-exp-item">
      <div class="liy-exp-header">
        <span class="liy-exp-title">3D Perception Intern — Model Fine-tuning &amp; Distillation</span>
        <span class="liy-exp-date">Apr 2025 – Aug 2025</span>
      </div>
      <div class="liy-exp-org">XiaoYu ZhiZao (Embodied AI startup)</div>
      <div class="liy-exp-body">
        <ul>
          <li>Fine-tuned MAST3R with low-resolution ROPE and relative position encoding to accelerate inference while maintaining point cloud quality.</li>
          <li>Designed a distillation loss and applied it to VGGT to speed up image-to-point-cloud inference for robot arm planning.</li>
        </ul>
      </div>
    </div>

    <div class="liy-exp-item">
      <div class="liy-exp-header">
        <span class="liy-exp-title">ViT-based Quadrotor End-to-End Obstacle Avoidance</span>
        <span class="liy-exp-date">Sep 2024 – May 2025</span>
      </div>
      <div class="liy-exp-org">Bachelor's Thesis &nbsp;·&nbsp; NUS Chongqing Research Institute</div>
      <div class="liy-exp-body">
        <ul>
          <li>Reproduced ViT / ViT-LSTM baselines from an ICRA 2025 paper; verified superior generalization of ViT in unseen forest environments.</li>
          <li>Rebuilt the expert data pipeline in Flightmare, recording RGB frames, pose, and velocity commands; modified input from single-frame depth to RGB image sequences with an IMU fusion channel.</li>
          <li>Achieved 73.26% obstacle avoidance success rate in forest simulation (Flightmare + Dodgelib), validated via closed-loop control on a local Ubuntu dual-boot setup.</li>
        </ul>
      </div>
    </div>

  </div>
</div>

<div class="liy-section">
  <h2>Publications</h2>
  <div class="liy-pub-item">
    <div><span class="liy-pub-venue">ISPRS 2026</span><span class="liy-pub-accepted">✓ Extended Abstract — Accepted</span></div>
    <div style="margin-top:0.3rem;">
      <strong>Deep Radar Point Matching for 4D Radar-Inertial Odometry</strong><br>
      <span style="opacity:0.75;">Integrating learned scan-to-scan and scan-to-submap radar correspondences (RPM-Net, Radar-Transformer) into an IEKF/VGICP radar-inertial odometry backend. Evaluated on ColoRadar and SNAIL datasets.</span>
    </div>
  </div>
</div>

<div class="liy-section">
  <h2>Education</h2>
  <div class="liy-edu-list">
    <div class="liy-edu-item">
      <div class="liy-edu-left">
        <div class="liy-edu-school">National University of Singapore (QS #8)</div>
        <div class="liy-edu-degree">M.Eng. Computer Engineering &nbsp;·&nbsp; GPA 4.7 / 5.0</div>
        <div class="liy-edu-degree" style="opacity:0.6;">Robotics and Embodied AI (A+), Machine Learning with Applications (A)</div>
      </div>
      <div class="liy-edu-right">Aug 2025 – Dec 2026<br>Singapore</div>
    </div>
    <div class="liy-edu-item">
      <div class="liy-edu-left">
        <div class="liy-edu-school">Beijing Jiaotong University (211)</div>
        <div class="liy-edu-degree">B.Eng. Computer Science &nbsp;·&nbsp; GPA 3.76 / 4.0</div>
        <div class="liy-edu-degree" style="opacity:0.6;">First-Class Scholarship, Outstanding Graduate Thesis</div>
      </div>
      <div class="liy-edu-right">Sep 2021 – Jun 2025<br>Beijing, China</div>
    </div>
  </div>
</div>

</div><!-- /liy-en -->


<!-- ════════════════════════ 中文 ════════════════════════ -->
<div id="liy-zh" class="liy-hidden">

<div class="liy-profile">
  <img src="/assets/img/avatar.jpg" alt="刘弈" class="liy-avatar">
  <div class="liy-profile-info">
    <h1>刘弈 <span class="liy-name-sub">Liu Yi</span></h1>
    <p class="liy-affil">计算机工程硕士 &nbsp;·&nbsp; 新加坡国立大学</p>
    <span class="liy-seeking">🔍 正在寻找机器人方向科研实习机会</span>
    <div class="liy-contacts">
      <a class="liy-contact-link" href="mailto:e1538633@u.nus.edu">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
        e1538633@u.nus.edu
      </a>
      <a class="liy-contact-link" href="https://github.com/yiichu03" target="_blank" rel="noopener">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0 1 12 6.844a9.59 9.59 0 0 1 2.504.337c1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.02 10.02 0 0 0 22 12.017C22 6.484 17.522 2 12 2z"/></svg>
        yiichu03
      </a>
    </div>
  </div>
</div>

<div class="liy-section">
  <h2>关于我</h2>
  <p>我目前是新加坡国立大学（NUS）计算机工程专业的硕士生，专注于机器人自主能力与智能系统研究。研究内容涵盖多传感器导航（热红外、LiDAR、4D 雷达）、SLAM、机器人控制的端到端学习，以及在 UGV 和人形机器人平台上的实机系统部署。</p>
  <p>我的兴趣在于将学习方法与真实机器人系统相结合，让系统能在真实硬件上稳定运行是我最有动力做的事。</p>
</div>

<div class="liy-section">
  <h2>研究兴趣</h2>
  <ul>
    <li>多传感器机器人导航——热红外、LiDAR、4D 毫米波雷达</li>
    <li>SLAM 与未知环境自主探索</li>
    <li>机器人感知与控制的端到端学习</li>
    <li>具身 AI 与人形机器人系统</li>
  </ul>
</div>

<div class="liy-section">
  <h2>专业技能</h2>
  <div class="liy-skill-group">
    <span class="liy-skill-label">编程语言</span>
    <div class="liy-skill-tags">
      <span class="liy-tag">Python</span><span class="liy-tag">C++</span><span class="liy-tag">PyTorch</span><span class="liy-tag">ROS2</span>
    </div>
  </div>
  <div class="liy-skill-group">
    <span class="liy-skill-label">工具与环境</span>
    <div class="liy-skill-tags">
      <span class="liy-tag">Linux</span><span class="liy-tag">Git</span><span class="liy-tag">Docker</span><span class="liy-tag">Isaac Sim</span><span class="liy-tag">Gazebo</span><span class="liy-tag">NVIDIA AGX Orin</span>
    </div>
  </div>
  <div class="liy-skill-group">
    <span class="liy-skill-label">传感器</span>
    <div class="liy-skill-tags">
      <span class="liy-tag">LiDAR</span><span class="liy-tag">RGB-D</span><span class="liy-tag">双目热红外相机</span><span class="liy-tag">4D 毫米波雷达</span>
    </div>
  </div>
  <div class="liy-skill-group">
    <span class="liy-skill-label">算法方向</span>
    <div class="liy-skill-tags">
      <span class="liy-tag">Transformer / ViT</span><span class="liy-tag">SLAM</span><span class="liy-tag">Nav2</span><span class="liy-tag">DRL</span><span class="liy-tag">3D 点云</span><span class="liy-tag">知识蒸馏</span>
    </div>
  </div>
</div>

<div class="liy-section">
  <h2>经历</h2>
  <div class="liy-exp-list">

    <div class="liy-exp-item">
      <div class="liy-exp-header">
        <span class="liy-exp-title">多传感器机器人导航与定位研究</span>
        <span class="liy-exp-date">2025.08 – 2025.12</span>
      </div>
      <div class="liy-exp-org">机器人导航研究项目 &nbsp;·&nbsp; 新加坡国立大学</div>
      <div class="liy-exp-body">
        <ul>
          <li>面向低照度与视觉退化场景，搭建双目热红外 / RGB-D / LiDAR 多传感器采集链路，完成硬件时间同步、内外参标定。</li>
          <li>在 NVIDIA AGX Orin 上集成 BridgeDepth、NVBlox、Nav2 与 SLAM 位姿输入，实现 UGV 上的 point-goal 导航并完成实机验证。</li>
          <li>将 RPM-Net（scan-to-scan 软对应）与 Radar-Transformer（scan-to-submap 硬对应）接入雷达惯性里程计后端（IEKF / VGICP），在 ColoRadar 与 SNAIL 数据集上完成评测。</li>
        </ul>
      </div>
    </div>

    <div class="liy-exp-item">
      <div class="liy-exp-header">
        <span class="liy-exp-title">基于 DRL 的室内自主探索导航系统重构</span>
        <span class="liy-exp-date">2025.12 – 至今</span>
      </div>
      <div class="liy-exp-org">机器人导航研究项目 &nbsp;·&nbsp; 新加坡国立大学</div>
      <div class="liy-exp-body">
        <ul>
          <li>分析 TARE 规划器在窄走廊、路口场景下的 goal=NaN 与 frontier utility 失效问题，梳理 3D 点云 SLAM 到 2D 占用栅格的感知-规划接口。</li>
          <li>采用"最小替换"策略将 ARiADNE（DRL 自主探索器）接入现有 ROS2 导航链路，打通 Livox/Hesai SLAM、OctoMap/OccupancyGrid 与 waypoint 接口，保留下游 local planner。</li>
          <li>在 Unity 与 Gazebo 中建立 smoke test 与实验编排流程；预训练 checkpoint 在 5 个测试 episode 上均完成探索，验证了训练仓与 ROS2 推理仓的权重兼容性。</li>
        </ul>
      </div>
    </div>

    <div class="liy-exp-item">
      <div class="liy-exp-header">
        <span class="liy-exp-title">人形机器人感知与控制联调</span>
        <span class="liy-exp-date">2026.02 – 2026.03</span>
      </div>
      <div class="liy-exp-org">Fatfish AI &nbsp;·&nbsp; 机器人实习生</div>
      <div class="liy-exp-body">
        <ul>
          <li>在 Fourier N1 平台上打通机器人本机 RGB-D 采集、Orin 远程视觉推理与本机上肢控制链路。</li>
          <li>实现 cup-follow / bottle-follow 目标的右臂视觉跟随，增加 RTT 反馈与状态诊断模块，用于现场联调。</li>
          <li>处理控制进程冲突、网络通信与相机归属等系统问题，支持实机 bring-up 调试。</li>
        </ul>
      </div>
    </div>

    <div class="liy-exp-item">
      <div class="liy-exp-header">
        <span class="liy-exp-title">3D 感知实习——端到端重建模型微调与蒸馏</span>
        <span class="liy-exp-date">2025.04 – 2025.08</span>
      </div>
      <div class="liy-exp-org">小雨智造（具身智能初创公司）</div>
      <div class="liy-exp-body">
        <ul>
          <li>对 MAST3R 进行低分辨率 ROPE 微调和相对位置编码微调，在保持点云质量的同时加速推理。</li>
          <li>设计蒸馏 loss，对 VGGT 进行蒸馏，提升机械臂规划场景下的图像到点云推理速度。</li>
        </ul>
      </div>
    </div>

    <div class="liy-exp-item">
      <div class="liy-exp-header">
        <span class="liy-exp-title">基于 ViT 的四旋翼无人机端到端避障系统</span>
        <span class="liy-exp-date">2024.09 – 2025.05</span>
      </div>
      <div class="liy-exp-org">本科毕业设计 &nbsp;·&nbsp; 新加坡国立大学重庆研究院</div>
      <div class="liy-exp-body">
        <ul>
          <li>复现 ICRA 2025 论文中的 ViT / ViT-LSTM 基线，验证 ViT 在陌生仿真环境中更优的泛化性。</li>
          <li>基于 Flightmare 重构专家数据采集流程，将输入从单帧深度图改为 RGB 图像序列并引入 IMU 融合通道。</li>
          <li>在树林仿真环境（Flightmare + Dodgelib）中实现 73.26% 避障成功率，并通过本地 Ubuntu 双系统完成闭环控制验证。</li>
        </ul>
      </div>
    </div>

  </div>
</div>

<div class="liy-section">
  <h2>论文</h2>
  <div class="liy-pub-item">
    <div><span class="liy-pub-venue">ISPRS 2026</span><span class="liy-pub-accepted">✓ Extended Abstract — 已接受</span></div>
    <div style="margin-top:0.3rem;">
      <strong>Deep Radar Point Matching for 4D Radar-Inertial Odometry</strong><br>
      <span style="opacity:0.75;">将 RPM-Net（scan-to-scan 软对应）与 Radar-Transformer（scan-to-submap 硬对应）接入 IEKF/VGICP 雷达惯性里程计，在 ColoRadar 与 SNAIL 数据集上完成评测。</span>
    </div>
  </div>
</div>

<div class="liy-section">
  <h2>教育背景</h2>
  <div class="liy-edu-list">
    <div class="liy-edu-item">
      <div class="liy-edu-left">
        <div class="liy-edu-school">新加坡国立大学（QS 第 8）</div>
        <div class="liy-edu-degree">硕士 · 计算机工程 &nbsp;·&nbsp; GPA 4.7 / 5.0</div>
        <div class="liy-edu-degree" style="opacity:0.6;">Robotics and Embodied AI (A+) &nbsp;·&nbsp; Machine Learning with Applications (A)</div>
      </div>
      <div class="liy-edu-right">2025.08 – 2026.12<br>新加坡</div>
    </div>
    <div class="liy-edu-item">
      <div class="liy-edu-left">
        <div class="liy-edu-school">北京交通大学（211）</div>
        <div class="liy-edu-degree">本科 · 计算机科学与技术 &nbsp;·&nbsp; GPA 3.76 / 4.0</div>
        <div class="liy-edu-degree" style="opacity:0.6;">一等学习奖学金 &nbsp;·&nbsp; 校级优秀毕业设计</div>
      </div>
      <div class="liy-edu-right">2021.09 – 2025.06<br>北京</div>
    </div>
  </div>
</div>

</div><!-- /liy-zh -->

<script>
function liySetLang(lang) {
  var en = document.getElementById('liy-en');
  var zh = document.getElementById('liy-zh');
  var btnEn = document.getElementById('btn-en');
  var btnZh = document.getElementById('btn-zh');
  if (lang === 'zh') {
    en.classList.add('liy-hidden');
    zh.classList.remove('liy-hidden');
    btnEn.classList.remove('active');
    btnZh.classList.add('active');
  } else {
    zh.classList.add('liy-hidden');
    en.classList.remove('liy-hidden');
    btnEn.classList.add('active');
    btnZh.classList.remove('active');
  }
  try { localStorage.setItem('liy-lang', lang); } catch(e) {}
}
(function() {
  try {
    var saved = localStorage.getItem('liy-lang');
    if (saved === 'zh') liySetLang('zh');
  } catch(e) {}
})();
</script>
