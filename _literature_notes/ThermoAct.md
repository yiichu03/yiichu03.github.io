---
title: "ThermoAct: Thermal-Aware Vision-Language-Action Models  for Robotic Perception and Decision-Making"
slug: "ThermoAct"
date: 2026-04-18 14:37:44 +0000
published_at: 2026-04-18 14:37:44 +0000
updated_at: 2026-04-24 15:14:13 +0000
source_path: "10 Literature Notes/ThermoAct.md"
---

> Published: 2026-04-18
> Updated: 2026-04-24 15:14 UTC

## Citation

- Authors: Young-Chae Son, Dae-Kwan Ko, Yoon-Ji Choi, Soo-Chul Lim
- Year: 2026
- Venue: arXiv preprint（RAL 2026）
- Citekey: Son2026ThermoAct

## Reading Context

- Why I read this paper: 想看看别人是怎么把thermal用到具身智能任务里的，是利用了thermal的哪些优势，是怎么处理它的劣势的。
- Reading goal: related work / focused understanding
- My current stage: skimming

## Part A — AI-generated scaffold

> Use this part to quickly build structure, but verify every important claim against the paper.

### AI Summary

- Problem: 现有很多 VLA 主要依赖 RGB vision，能识别物体类别，但通常无法感知 **temperature** 这种物理属性，因此很难完成“pick the coldest coke”“turn off a hot hair straightener”这类依赖热信息的任务。
- Core idea: 提出 **ThermoAct**，把 **thermal image** 接入 VLA，同时引入 **VLM Planner + VLA Executor** 的 hierarchical framework，让 VLM 负责 high-level planning / sub-task decomposition，VLA 负责 low-level control。
- Method: 使用 **Gemini 2.0 Flash** 作为 **VLM Planner**，根据用户指令、thermal image 和 wrist RGB image 生成 sub-task plan；使用基于 **π0** 的 **VLA Executor**，输入 thermal image、wrist RGB、robot state 和当前 sub-task prompt，输出 joint actions、gripper control 和 done flag。
- Main result: 在 5 个 real-world tasks 上，作者的方法 **RGB-T** 的 overall average success rate 为 **76.8 ± 4.6**，高于 **RGB-RGB baseline** 的 **59.4 ± 17.1**；在 thermal-related subtasks 上平均成功率约 **82%**，相比 RGB-RGB 的 **42%** 提升明显。
- One-sentence takeaway: 这篇论文说明，**thermal-aware hierarchical VLA** 能让机器人在小数据条件下更好地完成与温度相关的 manipulation 和 safety tasks，但其空间感知仍受限，不能替代 depth/perception。

### Abstract-style reading note

- Paper goal: 将 **thermal information** 系统性地引入 **Vision-Language-Action** 框架，使机器人能够执行依赖温度感知的任务，并在安全相关场景中做出更合理的决策。
- Core challenge: 一方面，thermal 属性不是普通 RGB image 能直接表达的；另一方面，相关大规模 pretraining dataset 很少，直接训练 end-to-end flat VLA 去学复杂 long-horizon reasoning 成本高且不稳定。
- Authors' claim: 通过 **hierarchical architecture** 把 high-level reasoning 交给 VLM、把 low-level execution 交给 VLA，可以在有限 thermal data 条件下实现更稳定、更安全的机器人行为。 ^pnbjn7


### Method

- Inputs / observations:
- 对 **VLM Planner**：user task、thermal image、wrist RGB image、guideline prompt
- 对 **VLA Executor**：thermal image（external camera）、wrist RGB image、7-dim robot state、sub-task language prompt
- Outputs / targets:
- Main modules:
- Training objective:
- Inference / rollout:
- Key assumptions:

### Experiments

- Tasks / datasets:
- Baselines:
- Main metrics:
- Best numbers worth remembering:
- Strongest evidence:

### Innovation / contributions

- System contribution:
- Algorithm contribution:
- Experimental contribution:
- Research perspective contribution:

### Limitations

-

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
