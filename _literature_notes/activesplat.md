---
title: "ActiveSplat: High-Fidelity Scene Reconstruction  through Active Gaussian Splatting"
slug: "activesplat"
date: 2026-05-07 12:53:57 +0000
published_at: 2026-05-07 12:53:57 +0000
updated_at: 2026-05-07 07:29:30 +0000
source_path: "10 Literature Notes/ActiveSplat.md"
---

> Published: 2026-05-07
> Updated: 2026-05-07 07:29 UTC

## Citation

- **Authors:** Yuetao Li, Zijia Kuang, Ting Li, Qun Hao, Zike Yan, Guyue Zhou, Shaohui Zhang
- **Year:** 2025  [RA-L 2025]
- **Venue:** IEEE Robotics and Automation Letters，RA-L；accepted May 2025
- **Citekey:** `li2025activesplat`
- **arXiv:** arXiv:2410.21955v2
- 开源代码：https://github.com/Li-Yuetao/ActiveSplat

## 1. 总结

Active Splat解决的是==未知==室内环境中的自主高保真3D重建问题，方法是用在线3D Gaussian Splatting dense map + Voronoi topological graph 做 active mapping、viewpoint selection 和 hierarchical path planning, 并在Gibson / Matterport3D上取得更高 completion ratio、completion accuracy 和较好的 novel-view rendering 质量。

## 2. Problem setting

### 2.1. robot type:
仿真中是 mobile agent；真实实验中是 Agile-X Ranger Mini omnidirectional mobile robot。

### 2.2. sensor:
主要使用 RGB-D；真实实验使用 Azure Kinect RGB-D sensor。论文中未明确说明使用 stereo camera。

### 2.3. Input:
posed RGB-D frames，即带 pose 的 RGB-D 图像；真实实验中 pose 由 line-based SLAM parallel thread 估计。

### 2.4. Output:
在线更新的 3D Gaussian map / high-fidelity reconstruction，以及用于探索的目标 view、target position、target rotation 和 planned path。

### 2.5. Environment:
室内 single-floor small / medium scenes；仿真环境来自 Gibson 和 Matterport3D，真实实验是 office scene。

### 2.6. Online or offline:
主系统是 online active mapping；另外有 optional post-processing，用 stored keyframes 对 Gaussian map 做 refinement。

### 2.7. Simulation or real robot:
两者都有；==主要定量评估在 Habitat simulator，真实机器人实验主要作为 qualitative evidence==。

## 3. Map / memory representation
它使用的是 hybrid map representation：

- Dense representation: explicit 3D Gaussian map，用于 RGB / depth / opacity rendering、visibility estimation、workspace extraction 和 reconstruction。
- Sparse representation: Voronoi graph / topological graph，用于 viewpoint position sampling、safe traversal、path planning 和 hierarchical planning。
- Derived auxiliary maps: top-down occupied map、obstacle map、workspace map。
- 不是 NeRF；不是 2D grid 作为核心决策表示；不是 latent memory；不是 world model；不是 VLM memory。

### 4. Exploration / navigation policy

说明它如何决定下一步去哪里：

- frontier?  
    不是 classical grid frontier。它有“push the boundary of the workspace”的行为，但候选点来自 Voronoi graph，不是直接检测 explored / unexplored grid frontier。
- next-best-view?  
    是。它做 active viewpoint selection，先选 target position，再选 target rotation。
- information gain?  
    没有显式 expected information gain formulation。它用 visibility / accumulated opacity、2D invisible region、3D convex hull volume、high-loss samples 来近似 coverage / incompleteness。
- learned policy?  
    否。论文中未明确说明使用 learned exploration policy。
- graph search?  
    是。它在 Voronoi graph 上选节点，并用 Dijkstra 找 shortest path。
- world model lookahead?  
    否。论文中未明确说明使用 world model lookahead。
- VLM / semantic prior?  
    否。论文中未明确说明使用 VLM 或 semantic prior。

### 5. Key technical idea

1. **Hybrid Gaussian + Voronoi map**  
    3D Gaussian map 提供 dense, view-dependent prediction；Voronoi graph 提供 sparse workspace abstraction。这个组合让系统既能评估哪里重建不完整，又能在可通行空间中高效规划。
2. **Decoupled viewpoint selection**  
    它把 viewpoint 拆成 position selection 和 rotation selection。position 从 Voronoi nodes 中选，rotation 通过 panorama visibility、low-visibility region clustering、high-loss samples 来确定。
3. **Topology-based hierarchical planning**  
    它把 Voronoi graph 动态划分为 local / global subregions，优先做 local fine-grained coverage，再切换到 global high-score subregion。这样减少 multi-room exploration 中的重复轨迹。


### 6. Evaluation
- Datasets / environments:  
    Gibson、Matterport3D、Habitat simulator；真实实验为 office scene。
- Baselines:  
    FBE、UPEN、ANM、NARUTO、ANM-S；另外有 Random、Position、Viewpoint、w/o HP 等 ablation baselines。
- Metrics:  
    completion ratio (%)、completion error / completion distance (cm)、PSNR、SSIM、LPIPS、Depth L1、path length、processing time。
- Real robot evidence:  
    有，但主要是 qualitative。真实平台为 Agile-X Ranger Mini + Azure Kinect；论文中未明确说明真实机器人上的完整定量指标。
- Main quantitative result:  
    在 observed data completeness 上，ActiveSplat 达到 Gibson 92.24% / 2.43 cm，Matterport3D 92.48% / 2.84 cm；对比 ANM-S 为 Gibson 92.10% / 2.83 cm，Matterport3D 89.74% / 4.14 cm。系统 headless mode 约 8 fps。
