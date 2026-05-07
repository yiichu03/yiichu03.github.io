---
title: "Perception-Aware Autonomous Exploration  in Feature-Limited Environments"
slug: "perception-aware-autonomous-exploration"
date: 2026-05-07 12:53:57 +0000
published_at: 2026-05-07 12:53:57 +0000
updated_at: 2026-05-07 09:54:37 +0000
source_path: "10 Literature Notes/Perception-Aware Autonomous Exploration.md"
---

> Published: 2026-05-07
> Updated: 2026-05-07 09:54 UTC

## Citation

- Authors: Moji Shi, Rajitha de Silva, Hang Yu, Riccardo Polvara, Marija Popović
- Year: 2026
- Venue: arXiv preprint, arXiv:2603.15605v1
- Citekey: `shi2026perceptionaware`



## 1. 总结

这篇论文提出一种 **perception-aware frontier exploration** 框架，在 UAV 使用 stereo camera + VIO 探索弱纹理环境时，把 visual feature quality 同时用于 frontier subgoal selection 和 yaw trajectory optimization，从而提升 feature tracking 稳定性、降低 VIO drift，并在 odometry error 阈值约束下取得更高探索完成率。

## 2. Problem setting:

### 2.1 Robot type:

UAV / quadrotor，不是地面轮式机器人。

### 2.2 Sensor:
stereo camera；状态估计使用 VIO，具体实验中使用 OpenVINS。

### 2.3 Input:
RGB image、depth image、VIO pose、occupancy / frontier map、online R2D2 feature map。

### 2.4 Output:
下一探索 subgoal，即 frontier viewpoint；以及到该 subgoal 的 collision-free position trajectory 和 optimized yaw trajectory。

### 2.5 Environment:
unknown indoor 3D environments，重点是 feature-limited / weakly textured environments。

### 2.6 Online or offline:
Online exploration。

### 2.7 Simulation or real robot
两者都有；Gazebo simulation + real-world indoor UAV experiment。


## 3. Map / memory representation

它主要使用 **3D occupancy / frontier voxel map + global visual feature map**。

具体来说：

- exploration 层面使用 frontier voxels，并对 frontier voxels 聚类，类似 FUEL / Frontier Information Structure。
- perception 层面维护一个 online global feature map：每个 visual feature 有 3D position 和 feature quality score。
- feature quality 来自 R2D2 repeatability / confidence。
- trajectory 层面使用 safe flight corridor + Bezier curve 表示 position trajectory，yaw trajectory 也用 1D Bezier curve 表示。
- 不是 NeRF、3DGS、topological graph、latent memory、world model，也不是 foundation mapper。
- 论文中未明确说明使用 frame tokens、trajectory memory 或 streaming 3D foundation mapper 表示。


## 4. Exploration / navigation policy

说明它如何决定下一步去哪里：

- frontier?  
    是。它是 frontier-based exploration，先对 frontier voxels 聚类，再采样 candidate viewpoints。
- next-best-view?  
    有 NBV-like 的 candidate viewpoint scoring，但论文主要表述为 frontier selector，而不是标准 next-best-view formulation。
- information gain?  
    部分是。coverage utility 用 candidate viewpoint 能观测到的 unknown voxels 数量表示，等价于一种几何覆盖收益。
- learned policy?  
    否。没有 learned exploration policy。R2D2 是 learned feature detector / descriptor，但 policy 本身不是学习式。
- graph search?  
    局部路径生成中使用 RRT 生成 collision-free reference path，然后用 minimum-snap Bezier optimization 平滑。global exploration decision 不是 graph search policy。
- world model lookahead?  
    否。论文中未明确说明使用 world model lookahead 或长时域预测。
- VLM / semantic prior?  
    否。没有使用 VLM，也没有 semantic prior。

核心决策函数是对每个 frontier viewpoint 计算 composite score：距离惩罚 + coverage utility + visible feature quality utility，然后选择最高分 subgoal。


## 5. Key technical idea

- **Perception-aware frontier selection**  
    它不是只选最近或信息增益最大的 frontier，而是把 expected visual feature quality 加入 frontier score。这样机器人会偏向既能扩展未知空间、又能维持 VIO feature tracking 的 frontier。
- **Online global feature map for exploration scoring**  
    系统在线构建 R2D2 feature map，把每个 feature 的 3D position 和 confidence / repeatability score 存起来。candidate viewpoint 的 perceptual utility 通过统计其视野内可见 feature quality 得到。
- **Continuous yaw trajectory optimization**  
    在 position path 已确定后，它优化 yaw，使相机尽量保持对高质量特征的可见性，并补偿机器人平移导致的 relative angular motion。这个设计直接服务于减少 motion blur、feature loss 和 VIO drift。

## 6. Evaluation

- Datasets / environments:  
    Gazebo simulation 中构造了三个 10 m × 10 m 环境：Low-Texture、Medium-Texture、High-Texture。另有一个 real-world 10 m × 10 m indoor room，包含 fake plants、textured cubes、mostly textureless black walls。
- Baselines:  
    FUEL；LA coupled with a simple frontier selector。
- Metrics:  
    tracked visual features per frame；image-plane feature distribution；exploration success rate under VIO position error thresholds 1.0 m / 2.0 m / 3.0 m；exploration rate；real-world VIO RMSE / max error。
- Real robot evidence:  
    有。使用 custom-built UAV、ZED Mini stereo camera、NVIDIA Jetson Orin NX，在真实室内环境中实验；最终 OpenVINS position RMSE 为 0.6958 m，maximum error 为 1.3069 m。
- Main quantitative result:  
    论文摘要称，相比忽略 feature quality 或不优化 continuous yaw 的 baseline，方法在 odometry error 超过指定阈值前平均实现约 **30% higher coverage**。表格结果中，在 Low-Texture map、3.0 m odometry threshold 下，Ours 为 0.470±0.139，FUEL 为 0.317±0.128，LA 为 0.176±0.087；在 High / Medium texture 环境中 Ours 也基本保持最高 success exploration rate。
