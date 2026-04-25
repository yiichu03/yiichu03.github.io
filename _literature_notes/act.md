---
title: "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware"
slug: "act"
date: 2026-04-02 14:40:21 +0000
published_at: 2026-04-02 14:40:21 +0000
updated_at: 2026-04-05 13:43:53 +0000
source_path: "10 Literature Notes/ACT.md"
---

> Published: 2026-04-02
> Updated: 2026-04-05 13:43 UTC

## Citation

- Authors: Tony Z. Zhao, Vikash Kumar, Sergey Levine, Chelsea Finn
- Year: 2023
- Venue: arXiv
- Citekey: Zhao2023ALOHA

## Reading Context

- Why I read this paper:
- Reading goal:
- My current stage:

## Part A — AI-generated scaffold

> The content in this part is AI-generated and should be treated as a scaffold to verify against the paper, figures, tables, and code.

### AI Summary

- Problem:
  如何让**低成本双臂机器人**完成高精度、强接触、依赖视觉闭环反馈的精细操作任务。传统方案通常依赖昂贵硬件、精确传感器或复杂建模，而这篇论文想证明：是否可以通过学习方法，让便宜但不够精确的硬件也能做 fine manipulation。

- Core idea:
  论文不是只提出一个网络模块，而是把**低成本遥操作数据采集系统**和**适合精细操作的动作建模方式**一起设计：用 ALOHA 采高质量示范，用 ACT 一次预测未来一段动作序列，再通过 temporal ensembling 和 CVAE 处理动作平滑性与示范多模态。

- Method:
  论文提出了一个完整系统，包括：
  1. **ALOHA**：一个低成本、开源的双臂遥操作系统，用 leader-follower 的**关节空间映射**采集高质量示范；
  2. **ACT (Action Chunking with Transformers)**：一次预测未来一段动作序列，而不是单步动作，以减轻 imitation learning 中的 compounding error；
  3. **Temporal Ensembling**：在每个时刻融合多个重叠 chunk 对同一时刻动作的预测，让动作更平滑；
  4. **CVAE + Transformer**：把人类示范中的多模态和噪声显式建模出来。

- Main result:
  在 6 个真实世界双手精细操作任务上，ACT 只用大约 **50 条示范 / 约 10 分钟数据**，就能学会开杯盖、装电池、拉拉链袋、贴胶带、穿鞋等任务；其中一些任务达到 **80%–90% 以上成功率**，显著优于 BC-ConvMLP、BeT、RT-1、VINN 等基线。

- One-sentence takeaway:
  这篇论文最强的地方在于证明了：**精细双手操作的提升，不只是模型更强，而是“数据采集系统 + 动作表示 + 训练目标”一起设计得更对。**

### Abstract-style reading note

- Paper goal:
  构建一个便宜、可复现的双臂系统，让机器人从真实示范中直接学会精细双手操作。

- Core challenge:
  1. 精细操作要求毫米级精度和闭环视觉反馈；
  2. 行为克隆容易出现 compounding error；
  3. 人类示范存在停顿、随机性和多模态。

- Authors' claim:
  单步动作预测不适合这类任务，应该把动作按 chunk 建模，并把系统设计成适合采集高质量示范的形式。

### Why it matters

- 这篇论文的重要性不只是“又提出了一个 Transformer 变体”，而是展示了：
  **机器人精细操作的性能，取决于硬件系统设计和学习算法的共同匹配。**
- 它说明低成本机器人并非只能做粗粒度 pick-and-place；如果遥操作接口、控制频率、动作表示和训练目标设计合理，低成本系统也能完成相当复杂的精细双手任务。
- 对机器人学习研究很有启发：相比只堆更大的模型，**高质量示范采集 + 合适的动作建模**可能更关键。

### Method

#### 1. ALOHA 硬件系统

- 使用两套低成本机械臂：
  - 小臂作为 leader，供人手直接 backdrive；
  - 大臂作为 follower，镜像执行动作。
- 采用**关节空间映射**，而不是 task-space mapping。
- 原因：
  1. 精细操作常靠近奇异位形，IK 不稳定；
  2. 关节空间控制延迟更低、带宽更高；
  3. leader 机械臂本身的阻尼有助于抑制手抖。
- 感知输入：
  4 个 RGB 相机（top / front / 左右 wrist）。
- 遥操作和数据记录频率：
  **50Hz**。

#### 2. ACT 的核心思想

- 标准 BC 学的是：
  $\pi(a_t \mid s_t)$
- ACT 学的是：
  $\pi(a_{t:t+k} \mid s_t)$

也就是给定当前观测，直接预测未来 **k 步动作序列**。

#### 3. 为什么 action chunking 有用

- 它把长时序任务的有效 horizon 缩短了；
- 减轻误差逐步积累的问题；
- 对人类示范中的“停顿”“节奏差异”等 temporally correlated confounders 更鲁棒。

#### 4. Temporal Ensembling

- 如果每 k 步才重新规划一次，会有动作切换不连续的问题；
- 作者因此在**每个时间步都查询策略**；
- 同一时刻会收到多个 chunk 给出的候选动作；
- 再用指数加权平均融合这些预测，使轨迹更平滑。

#### 5. CVAE 的作用

- 同一个状态下，人类可能采取不同但都合理的动作；
- 尤其在不那么关键的阶段，示范更随机；
- 因此作者不把动作视为单一 deterministic label，而是用 **CVAE** 建模动作分布；
- 训练时编码 action chunk + proprioception 到 latent z；
- 测试时把 z 设成 0，做确定性解码。

#### 6. 模型结构

- 4 路图像先经 ResNet18 编码；
- 再与 joint positions 和 latent z 一起送入 Transformer encoder；
- Transformer decoder 输出长度为 k 的动作序列；
- 动作是两只机械臂的**绝对关节目标位置**，总共 14 维。

### Experiments

#### 1. 任务设置

- 2 个仿真任务：
  - Cube Transfer
  - Bimanual Insertion

- 6 个真实任务：
  - Slide Ziploc
  - Slot Battery
  - Open Cup
  - Thread Velcro
  - Prep Tape
  - Put On Shoe

这些任务都不是简单抓取，而是多个子步骤串联而成，强调双手协作、视觉闭环和接触精度。

#### 2. 数据量

- 真实任务一般收集 **50 条示范**；
- Thread Velcro 收集 **100 条**；
- 每个任务大约 **10–20 分钟示范数据**。

#### 3. 对比方法

- BC-ConvMLP
- BeT
- RT-1
- VINN

#### 4. 主要结果

- Slide Ziploc：最终成功率 **88%**
- Slot Battery：最终成功率 **96%**
- Open Cup：最终成功率 **84%**
- Prep Tape：最终成功率 **64%**
- Put On Shoe：最终成功率 **92%**
- Thread Velcro：最终成功率 **20%**，是最难任务之一

总体上，ACT 明显优于所有基线，尤其在真实高精度任务上优势很大。

### Innovation / contributions

- **系统贡献**：
  提出了一个低成本、可复现、开源的双臂遥操作平台 ALOHA。

- **算法贡献**：
  提出 ACT，把动作 chunking、temporal ensembling 和 CVAE 结合到视觉模仿学习里。

- **实验贡献**：
  证明少量真实示范就足以让低成本双臂系统学会多个精细任务。

- **研究视角贡献**：
  强调 fine manipulation 不是单纯靠更强模型，而是要把数据采集、控制频率、动作表示和学习目标一起设计。

### Useful details

- 作者特别强调：
  用 **leader joint positions** 而不是 follower joints 作为动作标签，因为前者更能反映操作者真正施加的控制意图。
- 训练时使用 **L1 loss** 重建动作序列，而不是更常见的 L2。
- 论文观察到：
  用 **绝对关节位置** 比用 delta joint position 更好。
- 模型参数量大约 **80M**；
- 单任务从头训练，大约 **5 小时**；
- 推理约 **0.01 秒**。

### Limitations

- **硬件限制**：
  ALOHA 只有平行夹爪，不是多指灵巧手，因此对需要复杂手指协同的任务能力有限。
- **力矩限制**：
  低成本电机输出力不足，重物操作、紧瓶盖、强力旋拧任务较难。
- **感知限制**：
  对低对比、透明、细长、易形变物体仍然困难。
- **任务泛化限制**：
  论文是单任务训练，不是一个可泛化到多任务、多场景的大模型系统。
- **Thread Velcro 成功率较低**：
  表明在超高精度插入和小目标感知方面仍有明显瓶颈。

### Potential relation to my work (AI-generated)

- 如果我的研究关注：
  - imitation learning
  - robot manipulation
  - bimanual coordination
  - low-cost embodied systems
  - vision-based control

  那这篇论文非常值得作为相关工作引用。

- 对我最有价值的启发：
  1. 可以考虑把单步 action prediction 改成 chunk prediction；
  2. 设计数据采集系统时，控制频率和示范质量很关键；
  3. 对 noisy human demonstrations，需要显式考虑多模态建模。

### AI Take

这篇论文最值得学的不是某个单独模块，而是它的整体研究方法：
**从“真实任务难点”倒推数据采集系统，再倒推动作表示和学习目标。**
这是很强的 systems + learning 论文范式。

### AI Questions to Verify

- 论文里的 chunk 长度 `k` 在不同实验里具体取多少，结果对 `k` 有多敏感？
- temporal ensembling 的指数加权公式具体是什么，论文做了哪些 ablation？
- 为什么 leader joint positions 比 follower joints 更适合作为动作标签？
- 真实效果的提升，究竟主要来自 ACT 本身，还是 ALOHA 数据采集系统与示范质量？
- 当前 LeRobot 代码里的 migration / processor / normalization 逻辑，哪些属于论文算法本体，哪些属于后续工程封装？

## Part B — My own reading notes

> Fill this part after your own paper reading, figure/table checking, and code tracing. This is the part that should gradually replace Part A.


### My summary

- **Problem:** 想要做比较精细的任务，之前的方法大多需要昂贵且设置复杂的设备。所以希望可以通过低成本的系统、借助learning的方法去完成比较精细的操作任务。
- **Method:** Action Chunking，以小段动作（动作序列）为单位去预测。
- **Main result:** 实机实验有效且需要的数据量相对较少（应该是较少的意思，说是10min演示）

### Why it matters

-

### What I now understand

-
### Questions, clarifications, and current understanding

- **Trigger:** “actively compensating for errors”
  - **My question:** 这里的“主动补偿误差”是什么意思？
  - **Current understanding(AI):** 更像是闭环策略根据新观测持续修正前面动作造成的偏差，而不是显式建模一个误差控制器。**系统并不假设自己每一步都做得完全准确，而是在执行过程中持续观察结果，并根据偏差立刻修正后续动作。** 作者是在拿人类做类比：人做精细操作时，也不是靠一次性算准全部轨迹，而是边看边调。论文紧接着就提出用闭环视觉反馈、直接从图像到动作来学策略。
  - **Why it matters(AI):** 这有助于理解本文为什么强调 closed-loop visual feedback。

- **Trigger:** “learning the manipulation policy is much simpler than modeling the whole environment”
  - **My question:** 这算是体现了一种系统/模型设计思想？类似于diffusion model学习噪声也是觉得噪声相比整个图片分布更容易学习？
  - **Current understanding(AI):** 是的。作者是在做问题重表述：不先追求完整世界建模，而是选择一个更直接、更贴近任务接口的学习目标。
```markdown
在这篇论文里，作者的判断是：
- “整个环境”包含复杂接触、摩擦、形变、透明物体视觉、物体间相互作用……
- 如果你想先把这些都建模准确，再拿去规划，会非常难，工程量很大。
相比之下，直接学一个闭环操作策略“看到这种状态就怎么动”，反而更直接。
所以这确实是一种**问题重表述 / 目标重选型**的思想。
你拿 diffusion 做类比，方向是对的，但要小心不要完全等同。
相似点在于：
- diffusion 不是直接拟合“整张图的复杂分布”，而是转成逐步去噪这个更容易学习的过程；
- 这篇论文不是先建“整个物理世界模型”，而是直接学“给定观测该怎么动作”。
两者都体现了一个共同思想：
**把原问题变成一个更容易优化、更贴近决策接口的学习目标。**
但差异也很大：
- diffusion 里的“学噪声”本质上还是在做生成建模，只是换了参数化方式；
- 这里作者是在比较两条完全不同的路线：  
    **世界建模 + 规划** vs **直接策略学习**。
- 所以它更像“任务接口设计”和“系统分解选择”，不只是损失函数或参数化技巧的变化。
  
换句话说，你可以把它们放在同一个“设计哲学”下理解，但不要把两者看成同一种技术操作。
```
  - **Why it matters(AI):** 这帮助我把本文理解为 systems + learning 的共同设计，而不只是一个网络结构创新。

- **Trigger:** “a closed-loop policy can react ... rather than precisely anticipating ...”
  - **My question:** 相比复杂物理建模，这种做法是不是拿可解释性、泛化性、鲁棒性做了交换？
  - **Current understanding(AI):** 通常会有这种 trade-off.
```markdown
#### 可解释性

这个肯定会弱一些。

- 显式物理建模里，你知道接触模型、状态变量、规划目标是什么；
- 端到端策略里，输入图像、输出动作，中间很多决策依据是隐式的。

所以从“为什么它这样动”这个角度，确实通常没有物理模型那么透明。

#### 泛化性

这个要分情况。

- 如果换的是**相近分布内的小变化**，闭环策略有时反而很强，因为它会实时纠偏，不需要把每个细节都算准。
- 但如果换到**任务机制变了、物理规律变了、对象类别变了很多**，只靠 imitation policy 往往就容易掉性能。

这篇论文本身也更偏向**单任务、少量示范、高闭环精度**，不是在强调大范围跨任务泛化。

#### 鲁棒性

这里也不能一概而论。

- 对**小扰动、小偏差**，闭环策略常常比开环计划更鲁棒，因为它会看着改。
- 但对**分布外情况**、视觉遮挡、物体属性明显变化，端到端策略可能又不如有强先验的模型方法稳。

所以更准确的说法不是“它一定更不鲁棒”，而是：

> **它把鲁棒性的来源，从‘模型先验正确’换成了‘数据覆盖 + 闭环反馈 + 学到的反应能力’。**

```
  - **Status(AI):** 这是当前判断，还需要结合实验与后续工作进一步验证。
### Useful details

- Definitions / notation:
- Key hyperparameters / settings:
- Important implementation details:
- Figures / tables worth revisiting:

### Relation to my work

-

### Doubts / disagreements

- 我还没有完全想清楚 LeRobot 里为什么需要做 `migration`；这更像框架与模型格式演化的问题，需要和论文本身的方法贡献分开理解。

### Open questions

-

### My take

-

### Next actions

- 读清论文里 ACT 的 chunk 长度、loss、temporal ensembling 定义。
- 对照 LeRobot 代码，区分论文算法本体和后续工程封装。
- 单独弄明白 `migrate_policy_normalization.py` 和 processor / normalization 文件的作用。


## Publication

- Set `publish: github` to publish this note on `github.io`
- Or add `github` to `tags`
