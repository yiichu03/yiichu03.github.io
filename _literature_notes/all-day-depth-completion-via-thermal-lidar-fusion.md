---
title: "All-day Depth Completion via Thermal-LiDAR Fusion"
slug: "all-day-depth-completion-via-thermal-lidar-fusion"
date: 2026-04-25 19:01:30 +0000
published_at: 2026-04-25 19:01:30 +0000
updated_at: 2026-04-25 19:01:11 +0000
source_path: "10 Literature Notes/All-day Depth Completion via Thermal-LiDAR Fusion.md"
---

> Published: 2026-04-25
> Updated: 2026-04-25 19:01 UTC

## Citation  
  
- Authors: Janghyun Kim, Minseong Kweon, Jinsun Park, Ukcheol Shin  
- Year: 2025  
- Venue: arXiv preprint  
- Citekey: kim2025allday  
  
## Reading Context  
  
- Why I read this paper: 这篇论文直接讨论 thermal 与 LiDAR 融合做 dense depth completion，和我关心的“用 thermal 作为弱光/恶劣天气下的鲁棒感知线索”相关。虽然它不是 exploration / navigation planner 论文，但可以帮助我理解 thermal 在几何补全、深度边界、稀疏 LiDAR 辅助监督方面的作用。  
- Reading goal: focused understanding  
- My current stage: unread / skimming  
  
## Part A — AI-generated scaffold  
  
> Use this part to quickly build structure, but verify every important claim against the paper.  
  
### AI Summary  
  
- Problem: 现有 depth completion 多依赖 RGB + sparse LiDAR，在白天或光照良好场景表现较好，但在夜间、雨天、低光照等 all-day / adverse conditions 下，RGB 图像退化明显；同时恶劣天气下 LiDAR ground truth 也可能出现大量缺失，导致监督不足。  
- Core idea: 用 thermal image 替代或补充 RGB 作为 depth completion 的视觉引导信号，并利用 monocular depth foundation model 产生 pseudo-depth，帮助缓解 thermal 图像边界模糊和 LiDAR GT 缺失问题。  
- Method: 论文提出 COPS，即 COntrastive learning and Pseudo-Supervision framework。核心做法是：输入 thermal image + sparse LiDAR，由 depth completion network 输出 dense depth；同时冻结 Depth Anything V2 生成 pseudo-depth map，用 pseudo-depth 做 depth-aware contrastive learning 和 scale-invariant pseudo-supervision。  
- Main result: 在 MS2 和 ViViD 数据集上，thermal + LiDAR 在夜间、雨天、低光照室内场景中通常比 RGB + LiDAR 更稳定；COPS 可以集成到 NLSPN、GuideNet、LRRU 等现有 depth completion 网络上，并在多数指标上进一步提升 thermal-LiDAR depth completion 性能。  
- One-sentence takeaway: 这篇论文的关键价值不是提出新的导航方法，而是证明 thermal-LiDAR fusion 在全天候 dense depth perception 中比 RGB-LiDAR 更鲁棒，并给出一种利用 depth foundation model 改善 thermal depth completion 的训练框架。  
  
### Abstract-style reading note  
  
- Paper goal: 系统评估 thermal-LiDAR depth completion 在不同光照、天气和室内外环境中的可行性，并提出一个训练框架提升 thermal-guided depth completion 的边界清晰度和补全精度。  
- Core challenge: thermal 图像虽然不依赖可见光，但存在低对比度、噪声、模糊边界等问题；同时在雨天/低光照等场景中，LiDAR GT 也可能稀疏或缺失，导致 dense depth 监督不充分。  
- Authors' claim: thermal image 在恶劣光照和天气下比 RGB 更适合作为 depth completion 的视觉引导；通过 foundation-model pseudo-depth 进行 contrastive learning 和 pseudo-supervision，可以缓解 thermal 图像边界模糊和 GT 缺失问题。  
  
### Method  
  
- Inputs / observations:  
- thermal image  
- sparse LiDAR depth  
- 训练时额外使用 frozen Depth Anything V2 从 thermal image 生成 pseudo-depth map  
- 对比实验中也使用 RGB + LiDAR 作为基线输入  
  
- Outputs / targets:  
- dense depth map  
- 目标是在 sparse LiDAR 和 thermal/RGB 图像引导下恢复稠密深度  
  
- Main modules:  
- Depth Completion Network:  
- 使用现有 encoder-decoder 类型 depth completion 网络，例如 NLSPN、GuideNet、LRU/LRRU 等。  
- thermal 图像是单通道，因此通过复制通道适配常见三通道输入格式。  
- Pseudo-depth Generation:  
- 使用冻结的 Depth Anything V2 从 thermal image 生成 pseudo-depth。  
- pseudo-depth 不在 inference 时作为额外输入，而主要用于训练监督。  
- COPS:  
- depth-aware contrastive learning：根据 pseudo-depth 将像素划分为不同 depth pseudo-class，再构造 positive / negative pairs。  
- pseudo-supervision：用 pseudo-depth 通过 scale-invariant loss 提供额外 dense supervision。  
- stage-learning strategy：前半训练使用 scale-invariant pseudo-supervision 强化全局结构，后半训练使用 contrastive loss 强化局部边界和相对深度关系。  
  
- Training objective:  
- 基础 depth completion loss:  
- smooth edge loss  
- smooth L1 loss against ground-truth depth  
- pseudo-depth supervision:  
- scale-invariant loss，用于减少对绝对尺度偏差的敏感性  
- contrastive loss:  
- 基于 pseudo-depth slicing 和 margin sampling 构造正负样本  
- 目标是让相近深度区域的特征更接近，让容易混淆的近邻深度类别更可分  
- total loss:  
- base loss + weighted pseudo loss  
  
- Inference / rollout:  
- inference 阶段只需要 depth completion network，输入 thermal image + sparse LiDAR。  
- Depth Anything V2 和 COPS 主要用于训练阶段，因此作者强调不会给标准 encoder-decoder inference 增加额外计算量。  
  
- Key assumptions:  
- 仍然需要 sparse LiDAR 作为输入，因此这不是 pure thermal depth estimation。  
- 需要 thermal 与 LiDAR 数据对齐。  
- pseudo-depth foundation model 对 thermal image 生成的深度先验足够可靠，至少能提供有用的相对结构和边界信息。  
- 实验重点是 depth completion，不直接验证对 SLAM、navigation 或 exploration 的下游收益。  
  
### Experiments  
  
- Tasks / datasets:  
- Task: thermal-LiDAR / RGB-LiDAR depth completion  
- Outdoor benchmark: MS2 dataset  
- 包含 RGB、thermal、LiDAR  
- 覆盖 day / night / rain 场景  
- Indoor benchmark: ViViD dataset  
- 包含 RGB、thermal、sparse depth  
- 覆盖 indoor-bright / indoor-dark 场景  
  
- Baselines:  
- CSPN  
- S2D  
- NLSPN  
- GuideNet  
- DySPN  
- CompletionFormer  
- LRRU  
- BP-Net（部分设置中使用，ViViD 中因预处理/稀疏深度限制被排除）  
  
- Main metrics:  
- RMSE  
- MAE  
- iRMSE  
- iMAE  
  
- Best numbers worth remembering:  
- MS2 上，thermal + LiDAR 在 night / rain 场景整体明显优于 RGB + LiDAR。  
- LRRU 在 MS2 thermal domain 中表现最强，average RMSE 约为 2.286 m，MAE 约为 1.290 m。  
- COPS + LRRU 在 MS2 上进一步将 RMSE 从 2.286 降到 2.236，MAE 从 1.290 降到 1.250。  
- ViViD 上，thermal domain 在 indoor-bright 和 indoor-dark 之间性能变化很小，而 RGB domain 在低光照下退化更明显。  
- COPS + LRRU 在 ViViD 上将 RMSE 从 0.187 降到 0.178，MAE 从 0.084 降到 0.073。  
  
- Strongest evidence:  
- Table I: MS2 上 RGB + LiDAR 与 thermal + LiDAR 的系统性对比，尤其 night / rain 场景下 thermal 更稳定。  
- Table II: ViViD 上 indoor-bright / indoor-dark 对比，显示 thermal 对光照变化更鲁棒。  
- Table III: COPS 集成到 NLSPN、GuideNet、LRRU 后，多数指标有提升，说明方法不是只适配单一网络。  
- Fig. 4 / Fig. 5 / Fig. 6 / Fig. 7: 定性结果显示 thermal 在低光、雨天和暗室内场景中更能保留结构，COPS 对边界和空缺区域有补全效果。  
  
### Innovation / contributions  
  
- System contribution:  
- 将 thermal-LiDAR depth completion 作为一个系统性 benchmark 问题来研究，并比较多个主流 RGB-based depth completion 网络在 thermal modality 下的表现。  
- 给出现有 depth completion 网络迁移到 thermal input 的实验流程。  
  
- Algorithm contribution:  
- 提出 COPS 框架，用 depth foundation model 生成 pseudo-depth，并将其用于两类训练信号：  
- depth-aware contrastive learning  
- pseudo-depth scale-invariant supervision  
- 通过 depth slicing 和 margin sampling 定义 depth completion 中的 positive / negative sample，而不是依赖语义标签。  
  
- Experimental contribution:  
- 在 MS2 和 ViViD 两个数据集上覆盖室内/室外、白天/夜晚、雨天/低光照等多种条件。  
- 对 RGB + LiDAR 与 thermal + LiDAR 进行系统对比，证明 thermal 在恶劣条件下更稳定。  
- 验证 COPS 可以作为训练增强模块集成到不同 depth completion backbone。  
  
- Research perspective contribution:  
- 对我的研究来说，这篇论文提供了一个重要证据：thermal 不只是“夜视图像”，也可以作为几何感知和 dense depth recovery 的有效 cue。  
- 但它仍然依赖 LiDAR sparse depth，因此更像是“thermal 替代 RGB guidance”的阶段，而不是“thermal 完全替代 LiDAR”的最终方案。  
- 它可以作为后续从 LiDAR/RGB-D stack 迁移到 thermal-centric perception stack 的 perception-side 参考。  
  
### Limitations  
  
- 仍然依赖 sparse LiDAR 输入，不是 pure thermal 或 stereo thermal-only depth completion。  
- 论文重点是 dense depth prediction，不直接讨论 localization degradation、navigation failure recovery 或 exploration planner 如何利用 thermal cue。  
- Depth Anything V2 作为 pseudo-depth teacher 的可靠性需要进一步验证，尤其是在 thermal domain 和不同场景分布下是否存在偏差。  
- thermal 图像本身低纹理、低对比、噪声和边界模糊的问题仍未完全解决；COPS 是训练层面的缓解，不一定能覆盖所有真实机器人场景。  
- 实验主要是 benchmark-level depth completion，缺少真实机器人闭环导航或 exploration 下游任务验证。  
- 如果目标是最终只使用双目 thermal camera，这篇论文还没有解决 stereo thermal matching、thermal-only scale recovery、thermal odometry / mapping 等问题。  
  
### AI Questions to Verify  
  
- Which claims should I check in the figures/tables?  
- Table I 中 thermal + LiDAR 是否在所有 MS2 day/night/rain 子集都优于 RGB + LiDAR，还是主要优势集中在 night / rain？  
- Table II 中 ViViD indoor-bright 与 indoor-dark 的 thermal 性能差异是否真的很小？  
- Table III 中 COPS 对不同 backbone 的提升是否稳定，是否存在某些指标退化，例如 GuideNet 的 MAE 或 iRMSE。  
- Fig. 4 / Fig. 7 的 qualitative comparison 是否能支持“thermal 更鲁棒”的说法，还是只展示了典型成功案例。  
- Fig. 5 / Fig. 6 中 COPS 是否主要改善边界、上方空缺区域和细小物体，还是整体视觉上差异有限。  
  
- Which design choices seem most important?  
- 使用 Depth Anything V2 生成 pseudo-depth，而不是直接用 sparse LiDAR GT。  
- 将 pseudo-depth 离散成 depth pseudo-classes，用于 contrastive learning。  
- margin sampling 只关注容易混淆的近邻 depth class，而不是所有负样本。  
- stage-learning：先用 scale-invariant pseudo-supervision 学全局结构，再用 contrastive loss 学局部边界。  
- inference 阶段不引入 Depth Anything V2，因此方法主要增加训练成本，不增加部署成本。  
  
- Which details are still vague after only reading the abstract/introduction?  
- Depth Anything V2 对 thermal image 的输入适配方式是否充分，是否只是直接输入复制通道后的 thermal 图像。  
- pseudo-depth 的 absolute scale 是否稳定，scale-invariant loss 在多大程度上弥补了尺度偏差。  
- COPS 的提升主要来自 pseudo-supervision 还是 contrastive learning，需要看 ablation。  
- 对不同 weather / lighting 的性能提升是否均匀，还是在特定场景更明显。  
- thermal-LiDAR 标定误差、时间同步误差是否会显著影响结果。  
- 该方法是否能迁移到 mobile robot navigation stack 中，例如用于 local traversability、obstacle inflation、frontier validation 或 recovery cue。

## Part B — My own reading notes

> This part matters more. Keep your own judgment, confusion, disagreement, and research taste here.

### My summary

- Problem:
- Method:
- Main result:

### Why it matters

-

### What I now understand

-

### Questions, clarifications, and current understanding



### Useful details

- Definitions / notation:
- Key hyperparameters / settings:
- Important implementation details:
- Figures / tables worth revisiting:


### Relation to my work

-

### Doubts / disagreements

-

### Open questions

-

### My take

- What is genuinely strong here?
- What feels over-claimed or task-specific?
- What should I borrow for my own research?

### Next actions

- Re-read sections:
- Check code / project page:
- Compare with:
- Whether to publish to GitHub:
