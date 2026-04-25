---
title: "Stairway to Success: An Online Floor-Aware Zero-Shot Object-Goal Navigation Framework via LLM-Driven Coarse-to-Fine Exploration"
slug: "ascent"
date: 2026-04-22 14:35:55 +0000
published_at: 2026-04-22 14:35:55 +0000
updated_at: 2026-04-23 06:33:14 +0000
source_path: "10 Literature Notes/ASCENT.md"
---

> Published: 2026-04-22
> Updated: 2026-04-23 06:33 UTC

## Citation

- Authors: Zeying Gong, Rong Li, Tianshuai Hu, Ronghe Qiu, Lingdong Kong, Lingfeng Zhang, Guoyang Zhao, Yiyi Ding, Junwei Liang
- Year: 2026 
- Venue: arXiv preprint
- Citekey: Gong2026ASCENT

## Reading Context

- Why I read this paper:
- Reading goal: quick scan / focused understanding / reproduction / related work
- My current stage: unread / skimming / deep reading / revisiting

## Part A — AI-generated scaffold

> Use this part to quickly build structure, but verify every important claim against the paper.

### AI Summary

- Problem: 这篇论文研究的是 **multi-floor zero-shot object-goal navigation**。目标是在**未知的多楼层建筑**里，仅根据目标物体类别（比如 “find the TV”）在线导航到目标，不依赖预构建全局地图，也不需要为新物体类别重新训练。作者认为现有方法主要卡在两点：一是默认单层环境，缺少跨楼层规划；二是 LLM 规划器调用过于频繁，成本和时延都高。
- Core idea: 核心想法是做一个 **floor-aware 的分层在线导航框架 ASCENT**：一方面显式维护按楼层分开的地图和楼层拓扑，解决“怎么上楼/下楼、怎么避免多层地图重叠”的问题；另一方面把决策做成 **coarse-to-fine**，先用便宜的视觉语义评分筛 frontier，再只在必要时调用 LLM 做楼层/区域级推理，从而兼顾推理能力与效率。
- Method: 方法分两大模块。
	1. **Multi-Floor Abstraction**：构建每层独立的 BEV 表示，包括用于探索的 `M_val` 和可通行/障碍表示 `M_obs`；检测楼梯，支持上楼梯直接检测、下楼梯通过深度异常区域辅助识别；维护跨层切换和楼梯缓存/黑名单。
	2. **Coarse-to-Fine Reasoning**：先对 frontier 做 coarse ranking，缓存 top-k 候选及其场景描述；当附近没有近处 frontier 且候选足够多时，再触发 LLM 做两级推理：先判断是否该换楼层，再在当前层内选更可能找到目标的区域。
- Main result: 论文声称在 ZS-OGN 上达到新的 SOTA：HM3D 上 65.4 SR / 33.5 SPL，相比 MFNP 提升 +7.1 SR 和 +6.8 SPL；MP3D 上 44.5 SR / 15.5 SPL，相比 MFNP 提升 +3.4 SR。它还把 LLM 调用次数降低了 90% 以上，并在 Unitree Go2 四足机器人上做了真实多楼层部署。
> ==所以HM3D和MP3D有提供多层的仿真场景是吗？？==
- One-sentence takeaway:这篇论文的主要价值是：把 **多楼层在线建图/拓扑** 和 **低频率 LLM 语义推理** 结合起来，首次比较系统地把 zero-shot object-goal navigation 从“单层”推进到“在线多楼层”。

### Abstract-style reading note

- Paper goal: 提出一个能在**未知多楼层环境**中执行 **zero-shot object-goal navigation** 的在线框架，避免现有方法对单层场景、预建图或重训练的依赖。
- Core challenge: 难点不只是目标检测，而是**跨楼层过渡**、**垂直空间推理**、**在线维护多层一致表示**，以及在保证推理质量的同时避免 LLM 带来的高调用成本与延迟。
- Authors' claim: 作者声称 ASCENT 是首个把**动态多楼层建图**和 **LLM-driven spatial reasoning** 统一起来的在线多楼层 ZS-OGN 框架，且在 HM3D、MP3D 和真实机器人部署中都表现出优势。

### Method

- Inputs / observations: 输入主要是 **RGB-D** 观测；系统还利用场景分类、图像标签、语义相似度，以及离线统计先验（物体-楼层先验、物体-房间先验）来辅助决策。低层控制依赖预训练 PointNav policy。
- Outputs / targets: 输出是导航动作。中间层面上，系统会输出：要去哪个 frontier、是否跨楼层、跨到哪一层、当前层里该去哪个区域。整体目标是平衡探索成本 `c_expl` 和到达目标相关的 exploitation cost `c_goal`。
>[!Main modules:] 
>1 **Multi-Floor Abstraction**
>- `M_val`：把语义相似度图 `M_ss` 和距离惩罚/探索代价图 `M_ec` 结合起来，为 frontier 打分。
>- `M_obs`：由深度构建的障碍图，但会把检测到的楼梯重标为可通行。
>- **Stair Detection**：上楼梯靠检测 + 分割；下楼梯靠深度值异常区域辅助发现。
>- **Cross-Floor Transition**：先走到楼梯 frontier，再切到楼梯前方的动态中间 waypoint，持续攀爬/下楼。
>
>2 **Coarse-to-Fine Reasoning**
>- **Coarse-Grained Assessment**：基于 `M_val` 选 top-k frontier，并对对应图像生成“房间类型 + 物体”的文字描述。
>- **Fine-Grained Decision**：必要时调用 LLM，先做 inter-floor reasoning，再做 intra-floor reasoning。

- Training objective: 这篇不是端到端重新训练一个 OGN policy 的论文。它强调 **zero-shot / training-free at task level**：不针对新目标类别做任务特定训练，而是组合现成的检测、分割、VLM/LLM 与统计先验。严格说，这里的“训练”更多体现在所调用的基础模型已预训练，而不是 ASCENT 自己再做 task-specific learning。这个点值得你在正文再核实一下作者对“zero-shot”的精确定义。
- Inference / rollout: 运行时，机器人先更新当前层的 BEV 表示与楼梯候选；默认直接选 `M_val` 最高的 frontier；只有当所有 frontier 都比较远且候选数足够时，才触发 LLM 推理。若存在楼梯相关 frontier，先决定是否换楼层；若不换层，则在当前层基于候选房间/区域描述选更可能有目标的区域。
- Key assumptions:
	- 环境基本是静态的；
	- 主要针对“正常楼梯”而不是螺旋或不规则楼梯；
	- 有可靠的 RGB-D 感知和较稳定的 PointNav 低层执行；
	- 离线统计先验来自 benchmark 训练集，因此方法虽然不做 task-specific retraining，但并非完全不依赖 in-domain statistics。

### Experiments

- Tasks / datasets: 在 Habitat 上的 ObjectGoal Navigation 设定下，评测 **HM3D** 和 **MP3D**。HM3D 验证集有 2000 个 episode、20 个场景、6 类目标；MP3D 验证集有 2195 个 episode、11 个场景、21 类目标。论文还特别统计了多楼层 episode 的占比：HM3D 验证集中约 65% 是多楼层，约 28% 需要显式跨层；MP3D 分别约为 73% 和 15%。
> ==所以是在habitat里面可以放狗吗？还是类似于一个坐标点的agent?==
- Baselines: 论文比较了多种 learning-based 和 zero-shot 方法，包括 ZSON、L3MVN、PixNav、VLFM、SG-Nav、OpenFMNav、ActPept、InstructNav、ApexNav，以及最关键的多楼层基线 **MFNP**。
- Main metrics: 主要指标是 **SR (Success Rate)** 和 **SPL (Success weighted by Path Length)**。另外还做了 LLM 调用次数、运行时长、跨楼层 episode 分析、ablation、真实部署和恢复机制分析。
- Best numbers worth remembering: 
	- HM3D: **65.4 SR / 33.5 SPL**
	- MP3D: **44.5 SR / 15.5 SPL**
	- 相对 MFNP：HM3D **+7.1 SR / +6.8 SPL**，MP3D **+3.4 SR**
	- 在 HM3D 的 different-floor start-end episodes 上：ASCENT **33.3 SR**，MFNP **13.4 SR**，VLFM **0.4 SR**
	- LLM 调用次数：单层场景 **2.0**，多层场景 **2.7**，显著低于其他 LLM planner。
- Strongest evidence: 最强证据不是总 SR 本身，而是**跨楼层 episode 的专项结果**和**效率分析**：
	1. 在不同楼层起终点 episode 上，相比单层方法和 MFNP 有明显优势；
	2. LLM 调用次数下降 90% 以上，但 SR 仍更高；
	3. 真实机器人演示了上楼找 “potted plant”、下楼找 “truck” 的案例。

### Innovation / contributions

- System contribution: 提出一个**在线多楼层 object-goal navigation 系统**，显式维护每层独立表示、楼梯可通行性和楼层拓扑，而不是把多楼层信息压到同一张图里。
- Algorithm contribution: 提出 **Coarse-to-Fine Reasoning**：不是每一步都问 LLM，而是先用视觉语义评分筛候选，再在高层离散决策点触发 LLM 做楼层/区域推理。
- Experimental contribution: 不只给总指标，还专门拆分 same-floor / different-floor 场景、做组件消融、模型配置对比、检测器对比、LLM 调用效率分析和真实机器人实验。
- Research perspective contribution: 这篇论文把 ZS-OGN 的关注点从“单层语义导航”推进到“**online floor-aware navigation**”，说明多楼层并不是边缘 case，而是 benchmark 和实际部署里都大量存在的核心场景。
    
### Limitations

- 环境动态性处理不足。作者明确说 OGN 假设静态环境，但真实部署里行人等动态障碍会影响 obstacle mapping 和导航表现。
- 楼梯假设较强。方法主要针对普通楼梯，对螺旋楼梯或不规则楼梯可能不适用。
- 仍依赖 perception 质量。作者用 `ASCENT-Ideal` 和 detector ablation 说明，性能上限受物体检测器影响明显。
- “zero-shot” 不是“无任何先验”。它没有为新类别重训练，但用了 benchmark training split 的楼层先验和房间先验。这个点在 related work / claim framing 里要保持清醒。
- 方法在视觉-几何不一致、楼梯 navmesh 损坏时会失败，论文 stress test 也承认这一点。

### AI Questions to Verify

- Which claims should I check in the figures/tables?
	- Table I：ASCENT 相对 MFNP、ApexNav 的主结果到底体现的是“多楼层能力”还是“整体规划更强”？
	- Table III：different-floor episodes 的提升是否才是真正最有说服力的结果？
	- Table IV / V / VI：性能提升到底来自架构设计、基础模型替换，还是 detector 改善？
	- Table VII：LLM 调用次数大幅减少时，是否同时牺牲了某些复杂场景下的推理细度？
- Which design choices seem most important?
	- 每层独立 BEV + 跨层拓扑，而不是多层合并地图；
	- 楼梯检测里的**上楼视觉检测 + 下楼深度启发**的双模态设计；
	- 只在必要时触发 LLM 的 coarse-to-fine 机制；
	- 物体-楼层、物体-房间的统计先验在 LLM 决策里扮演多大作用。
- Which details are still vague after only reading the abstract/introduction?
	- 垂直定位和楼层切换时，系统如何保证 localization 不崩；
	- `M_ss`、`M_ec` 的具体构造和累计方式；
	- 何时触发 inter-floor reasoning，何时直接走局部 frontier；
	- 真实机器人里哪些模块跑在本地、哪些跑在远端，以及这对可部署性意味着什么。

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

#### 1. 关于标题里面的zero-shot
GPT特意提醒：这里的 “zero-shot” 并不等于“完全没有任何先验知识”，后文其实还是用了统计先验和基础模型，只是**不做针对新目标类别的任务特定重训练**。这一点后面读方法时会更清楚。

#### 2. 这篇论文的balance
在摘要里面说方法有两部分组成，一是Multi-Floor Abstraction, 二是Coarse-to-Fine Reasoning.
Multi-Floor Abstration里面又涉及stair-aware obstacle mapping和cross-floor topology modeling，解决的是“机器人怎么知道楼层结构、楼梯在哪里、哪些地方能跨层”
对于Coarse-to-Fine Reasoning，则是偏“决策与推理”，希望平衡Frontier ranking和LLM-driven contextual analysis，因为纯局部frontier方法太贪心，纯LLM方法太慢太贵。

#### 3. 关于实验
==我有点好奇contribution里面提到的性能提升“We demonstrate state-of-the-art (SOTA) performance for ZS-OGN benchmarks, improving SR by 7.1% and SPL by 6.8% on HM3D, and SR by 3.4% on MP3D. ”==是针对有多层楼梯的场景去和其他方法比较的吗？如果其他方法没办法应对多层的场景，要如何比较呢？那岂不是一定会有提升吗？（因为前面好像也说了多层场景占比28%呢）

#### 4. GPT对于一些段落的精炼总结：
==摘要==
用论文摘要常见的 4 格结构记就是：
- **Problem**：多楼层 object-goal navigation 很难
- **Gap**：现有方法不够 online / 不够 floor-aware
- **Method**：ASCENT = Multi-Floor Abstraction + Coarse-to-Fine Reasoning
- **Result**：benchmark 更强，还做了真实机器人部署

==引言==
- 真实机器人需要在多楼层建筑里找目标物体。
- 这件事难，因为不仅要识别目标，还要跨层和做垂直推理。
- HM3D / MP3D 里多楼层任务很多，但现有 OGN 方法大多按单层设计。
- learning-based 方法泛化成本高，ZS-OGN 方法虽然不重训练，但通常也没处理好多楼层。
- 纯 LLM 规划太慢太贵，纯 VLM 局部匹配又太贪心。
- 所以作者提出 ASCENT：用 **Multi-Floor Abstraction + Coarse-to-Fine Reasoning** 同时解决多楼层和高效规划问题。
==相关工作==
如果把 Related Work + Fig. 2 一起压缩，你可以这么记：
**相关工作三条线**
第一条线是 **ZS-OGN**：  
已经有不少 zero-shot 方法，但大多默认单层。
第二条线是 **LLM-based OGN**：  
LLM 推理强，但太频繁调用会慢。
第三条线是 **multi-floor navigation**：  
有人做过多楼层，但常常依赖预建图，或者在地图表示、楼梯切换、楼层决策上还有不足。
**作者的方法定位**
ASCENT 就是想把这三条线接起来：
- 保留 **zero-shot**
- 兼顾 **multi-floor**
- 还要让 **LLM 用得少而精**

图 2 则把它总结为两个核心模块：

- **Multi-Floor Abstraction**：负责楼层内/楼层间表示
- **Coarse-to-Fine Reasoning**：负责跨楼层语义推理与决策



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
