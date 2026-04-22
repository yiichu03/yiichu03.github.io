---
title: "Stairway to Success: An Online Floor-Aware Zero-Shot Object-Goal Navigation Framework via LLM-Driven Coarse-to-Fine Exploration"
slug: "ASCENT"
date: 2026-04-22 14:35:55 +0000
published_at: 2026-04-22 14:35:55 +0000
updated_at: 2026-04-22 13:51:15 +0000
source_path: "10 Literature Notes/ASCENT.md"
---

> Published: 2026-04-22
> Updated: 2026-04-22 13:51 UTC

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

### AI Questions to Verify

- Which claims should I check in the figures/tables?
- Which design choices seem most important?
- Which details are still vague after only reading the abstract/introduction?

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

## AI prompts

### Prompt 1 — Quick scan

```text
I am reading the paper "{{title}}".
My goal is to decide whether it is worth a deep read.

Please give me:
1. the paper's main problem,
2. the core idea in plain language,
3. the 3 most important contributions,
4. the main evidence supporting the claim,
5. the likely limitations,
6. what kind of researcher should read this paper.

Keep it concise and grounded in the paper. If something is uncertain, say so explicitly.
```

### Prompt 2 — Focused deep reading

```text
I am reading the paper "{{title}}" for a focused technical understanding.
Please help me build a structured reading scaffold.

Output these sections:
- problem setting,
- assumptions,
- inputs and outputs,
- method pipeline,
- key modules and why they are needed,
- training objective,
- inference procedure,
- experiment design,
- strongest results,
- limitations.

Do not just paraphrase the abstract. Highlight what I should verify in the main paper.
```

### Prompt 3 — Robotics / embodied / code-oriented reading

```text
I am reading the paper "{{title}}" from a robotics / embodied AI perspective.
Please focus on:
- observation interface,
- action representation,
- temporal modeling,
- training target,
- rollout / control loop,
- what is algorithmic novelty versus system engineering,
- what would matter for reproduction on a real robot.

For each item, explain why it matters and list the details I should look for in the paper or code.
```

### Prompt 4 — Related-work comparison

```text
Help me place the paper "{{title}}" in the literature.

Compare it against the most relevant prior work in terms of:
- problem setting,
- method idea,
- data assumptions,
- evaluation setting,
- strengths,
- weaknesses.

Then tell me what the true novelty is, and what might just be better engineering or benchmarking.
```

## Publication

- Set `publish: github` to publish this note on `github.io`
- Or add `github` to `tags`
