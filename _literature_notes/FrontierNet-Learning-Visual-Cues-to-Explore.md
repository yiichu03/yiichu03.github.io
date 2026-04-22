---
title: "FrontierNet: Learning Visual Cues to Explore"
slug: "FrontierNet-Learning-Visual-Cues-to-Explore"
date: 2026-04-09 14:40:42 +0000
published_at: 2026-04-09 14:40:42 +0000
updated_at: 2026-04-20 12:04:08 +0000
source_path: "10 Literature Notes/FrontierNet Learning Visual Cues to Explore.md"
---

> Published: 2026-04-09
> Updated: 2026-04-20 12:04 UTC

## Citation

- Authors: Boyang Sun, Hanzhi Chen, Stefan Leutenegger, Cesar Cadena, Marc Pollefeys, Hermann Blum
- Year: 2025
- Venue: IEEE Robotics and Automation Letters
- Citekey: sun2025frontiernet

## Reading Context

- Why I read this paper:
- Reading goal: quick scan / focused understanding / reproduction / related work
- My current stage: unread / skimming / deep reading / revisiting

## Part A — AI-generated scaffold

> Use this part to quickly build structure, but verify every important claim against the paper.

### AI Summary

- Problem: Existing exploration methods usually extract exploration goals from dense 3D maps, so they depend heavily on map quality and often underuse RGB visual cues.
现有 autonomous exploration 方法大多还是先建 3D map，再从 map 里提 frontier / goal pose，因此很依赖地图质量，而且没有直接利用 RGB image 里的 appearance cues。 
- Core idea: Predict frontier regions and their information gain directly from posed RGB images augmented with monocular depth priors, then convert these 2D predictions into sparse 3D exploration targets.
这篇论文的核心想法是：**不要先在 3D occupancy map 里找 frontier**，而是直接从 **RGB + monocular depth prior** 里预测 2D frontier 和 info gain，再==把它们 lifting 成 sparse 3D frontiers 给 planner 用==。
- Method: A two-head UNet-like model, FrontierNet, predicts a frontier distance field and a discretized info-gain map; these are post-processed through viewpoint generation, clustering, 3D lifting, frontier update, and utility-based planning.
方法上，FrontierNet 是一个 **two-head UNet-like network**：一个 head 预测 frontier distance field，另一个 head 预测 discretized info-gain map。后面再接 viewpoint generation、2D clustering、3D lifting、frontier update 和 utility-based planning。
- Main result: On 10 HM3D validation scenes, the method achieves the best overall exploration efficiency and success rate among the compared baselines, with especially strong gains in early and mid-stage exploration; it also runs in real time on a Spot robot.
实验上，在 10 个 HM3D validation scenes 上，这个方法整体 exploration efficiency 和 success rate 都最好，尤其在 early-stage / mid-stage exploration 更强；并且作者还在 Spot robot 上做了 real-world validation。
- One-sentence takeaway: This paper argues that exploration goal proposal does not need to start from dense 3D geometryl visual cues can directly predict where a robot should go next and how valuable that move is.
 **exploration goal proposal 不一定非要从 dense 3D geometry 出发，visual cues 本身就可以直接预测“该往哪去”以及“去了值不值”。

### Abstract-style reading note

- Paper goal: Build an efficient autonomous exploration system that visual cues from individual camera images to propose frontiers and rank them by expected exploration value.
论文目标是做一个 efficient exploration system，直接利用单张相机图像中的 visual cues 来 propose frontier，并估计它们的 exploration value。
- Core challenge: Frontier extraction is usually done in 3D maps, but map quality is fragile and appearance information from RGB is typically not used directly at the goal-proposal stage.传统frontier extraction 通常在3D map上完成，但3D map质量容易受传感器、重建误差、表示方式影响；同时RGB中的texture / color / semantic context往往没有被直接用于goal proposal.
- Authors' claim: A learning-based visual frontier proposal system can improve exploration efficiency, especially early on, while remaining robust robust even when using monocular depth priors instead of perfect depth. 一个learning-based visual frontier proposal system能显著提升exploration efficiency，尤其是前期探索效率；而且就算用monocular depth prior而不是perfect depth, 也依然有较强鲁棒性。

### Method

- Inputs / observations: Posed RGB images plus a monocular depth prior; the system may also maintain an optional 3D occupancy map for safer planning and frontier updates. 输入主要是posed RGB images + monocular depth prior. 此外，系统可以选择维护一个3D occupancy map， 用于safer planning和frontier update，但这不是proposal 阶段的核心依赖
- Outputs / targets: FrontierNet predicts a 2D frontier distance field and a discretized 2D info-gain map; after post-processing, the system outputs sparse 3D frontiers with position, viewing direction, and utility-related gain. 网络输出是两个2D prediction，经过后处理得到sparse 3D frontiers.
- Main modules:
	- FrontierNet with two heads: frontier proposal head and info-gain prediction head
	- Ground-truth generation from HM3D vocelized scenes.
	- Anchoring in 3D via viewpoint generation, HDBSCAN clustering, and 3D lifting.
	- Frontier update and utility-based path planning
从system view来看，主要模块包括：FrontierNet -> GT generation pipeline -> 3D anchoring -> frontier update -> planner. 其中3D anchoring 又分成viewpoint generation、HDBSCAN clustering 和 3D lifting.
- Training objective: A weighted sum of L1 loss for the normalized distance field and cross-entropy plus multi-class Dice loss for the discretized info-gain prediction.训练目标是多任务loss，distance filed这边用L1 loss, info gain classification这边用cross entropy + multi-class Dice loss, 最后做weighted sum.
- Inference / rollout: Predict 2D frontier pixels and gain, recover candidate frontier pixels by thresholding the distance field, estimate viewing directions from depth gradients, cluster pixels, lift clusters to 3D, update frontier list, and select the next goal using info-gain-over-distance utility. inference时的pipeline很清楚：predict 2D frontier + gain -> threshold distance field 得到frontier pixels -> 用depth gradient 推 viewing direction -> clustering -> lifting to 3D -> frontier update -> planner选下一目标
- Key assumptions: 
	- Visual appearance and monocular depth cues are sufficient to infer useful exploration frontiers.（所以可不可以是输入图片序列呢？？）
	- Information gain can be learned from single-image context using lables generated with privileged 3D scene knowledge.
	- Projected frontier pixels aligh with depth discontinuities strongly enough to support robust proposal and lifting
	- 单张图像中的appearance+depth cues足以推断有用的frontier；
	- info gain可以通过带privileged 3D supervision的方式学出来
	- frontier pixels 和 depth discontinuity之间存在较稳定对应关系

### Experiments

- Tasks / datasets: Simulated exploration on unseen HM3D validation scenes, plus real-world deployment on a Boston Dynamics Spot robot in a large indoor environment.
实验包括两部分：一部分是在HM3D unseen validation scenes上面做simulation，另一部分是在Boston Dynamics Spot上做real-world validation。
- Baselines: Classic frontier-based exploration, NBVP，SEER, and a re-implemented SEER frontier proposal paired with the authors’ planner for fairer comparison.  
  baseline 包括 classic frontier-based method、NBVP、SEER，以及作者自己 re-implement 的一个 SEER 版本。
- Main metrics: Vox@25, Vox@50, Vox@100, and success rate. These measure mapped volume at matched exploration stages and final success.  
  主要指标是 **Vox@25 / Vox@50 / Vox@100 / Success rate**。  
  你可以把它们理解成：在 exploration 不同阶段，已经覆盖了多少 scene volume。
- Best numbers worth remembering:
	- With simulator depth, their method reaches mean Vox@25 = 32.7, Vox@50 = 58.6, Vox@100 = 71.5, success = 88.6%.
	  - With monocular depth, it still reaches mean Vox@25 = 32.7, Vox@50 = 55.5, Vox@100 = 70.6, success = 86.5%.
	  - The paper highlights about a 15% improvement over the second-best method at Vox@50 overall.  
	  最值得记的数字是：  
	  - perfect/simulator depth 下：**32.7 / 58.6 / 71.5 / 88.6%**  
	  - monocular depth 下：**32.7 / 55.5 / 70.6 / 86.5%**  
	  - 作者特别强调：在 **Vox@50** 上，相比 second-best method 大约高 **15%**。
- Strongest evidence:
	- The method outperforms baselines across 10 diverse scenes, especially at early and mid exploration stages.
	  - Ablations show both learned distance-field prediction and info-gain prediction matter.
	  - A map-free version still performs competitively, supporting the claim that dense maps are not essential for goal proposal.
	  - Real-world Spot experiments show sim-to-real robustness and real-time inference around 5 Hz.  
	  strongest evidence 主要有四个：  
	  1. 在 10 个 diverse scenes 上 consistently 优于 baselines；  
	  2. ablation 说明 distance field 和 info gain 两部分都重要；  
	  3. map-free setup 仍然能 work，支撑了 visual-first proposal 的主张；  
	  4. real-world Spot experiment 显示有一定 sim-to-real robustness，推理速度大约 **5 Hz**。

### Innovation / contributions

- System contribution: An exploration system that uses visual cues in individual camera images to propose and rank frontiers instead of extracting exploration goals from dense 3D maps.  把 exploration goal proposal 从 dense 3D map operation 转成了 visual-cue-driven proposal。
- Algorithm contribution: FrontierNet, a two-head learning model for joint frontier proposal and information-gain prediction from RGB plus monocular depth prior.   FrontierNet 本身：jointly 做 frontier proposal 和 info-gain prediction。
- Experimental contribution:  Extensive validation in simulation across 10 HM3D scenes and real-world deployment on a Spot robot.  benchmark 相对比较全面，不只是在少数两个场景里展示结果。
- Research perspective contribution:  The paper reframes exploration goal extraction as something that can be inferred directly from visual observations, not only from dense 3D geometry.  这篇论文的意义在于：它把“frontier extraction 必须依赖 3D map”这个默认前提挑战掉了。

### Limitations

- The training supervision depends on privileged 3D scene information and a fairly elaborate label-generation pipeline, which may make the approach conceptually elegant at inference but expensive to prepare.
- Although the proposal stage is visual-first, the full system still benefits from an occupancy map for safer planning and frontier updating, so it is not purely map-free in its strongest setting.
- The 3D lifting and planning stages still depend on depth quality; monocular depth errors can plausibly affect robustness even though the method is more tolerant than baselines.
- Real-world validation is promising but limited in scope compared with the simulation benchmark.  
  局限性也比较明确：  
  第一，training label 的生成依赖完整 3D scene knowledge；  
  第二，最强 setting 下依然会利用 occupancy map；  
  第三，3D lifting 和 planning 还是受 depth quality 影响；  
  第四，real-world validation 目前规模还不算大。

### AI Questions to Verify

- Which claims should I check in the figures/tables?
	- Table I: Is the 15% Vox@50 advantage the most convincing main result?
	  - Table II: Does RGB mainly help info-gain estimation while depth mainly helps frontier detection?
	  - Figure 9: How much do distance-field prediction and info-gain prediction each contribute?
	  - Table III / Figure 10: How competitive is the map-free setup really?  
	  建议重点核查 Table I、Table II、Figure 9、Table III / Figure 10，这几个地方基本决定了这篇论文的说服力。
- Which design choices seem most important?
	- Predicting a distance field instead of a binary frontier mask.
	  - Discretizing info gain into 11 classes instead of regressing it directly.
	  - Refining projected frontier labels using a depth discontinuity mask.
	  - Estimating viewing direction from local depth gradients and then clustering in 2D before 3D lifting.  
	  最关键的 design choices 包括：  
	  用 **distance field** 替代 binary mask；  
	  用 **classification** 替代 direct regression；  
	  用 **depth discontinuity** refine labels；  
	  先在 2D clustering，再做 3D lifting。
- Which details are still vague after only reading the abstract/introduction?
	- Exactly how the ground-truth info gain is approximated from 3D frontier voxels.
	  - How robust the 3D lifting is when depth priors are noisy or mis-scaled.
	  - How sensitive the planner is to thresholds for frontier merging, invalidation, and utility ranking.
	  - Whether the gains come mostly from visual proposal quality or partly from stronger overall engineering and benchmarking.  
	  如果只看 abstract / intro，最容易还不清楚的是：  
	  1. GT info gain 到底怎么近似生成；  
	  2. noisy monocular depth 对 lifting 的影响有多大；  
	  3. planner 对阈值是否敏感；  
	  4. improvement 究竟主要来自 model，还是部分来自更好的系统工程。





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

1. GPT说**FrontierNet**主张**不在 3D 稠密地图上提 frontier proposal，而是直接从 posed RGB 图像提出 frontier pixels 并预测 info gain**，然后再把这些 2D frontier 锚定到 3D 并用于规划。
我想知道这里说的==“锚定”==具体是什么过程？怎么做到的？

==摘要==
#### 1. posed RGB images里面的相机位姿是从哪里来的呢？
如SLAM/VIO提供位姿估计（机器人本体的or某个传感器的），然后结合相机相对于机器人机体/某传感器的外参，得到真正的相机位姿
==[[2026-04-20#^t8mtka]]==
#### 2. achieve a 15% improvement in a early-stage exploration efficiency，强调了是early-stage，所以是不是完整阶段来看的时候，效率并没有提升呢？还是有其他含义？这个应该是要看实验部分？
GPT： 不是。**强调 early-stage，不等于后期没提升。**  
从实验结果看，作者的方法在完整比较里并不只是早期更强，而是**在 Vox@25、Vox@50、Vox@100 以及 success rate 上整体都更好**；作者自己在结果部分也明确写了：在 10 个场景上，使用 simulator depth 时，他们的方法在 25%、50%、100% steps 处都取得了最高 overall efficiency 和最高 success rate。==那为什么摘要还专门强调 early-stage？原因更像是：==**（我的理解是，把效果好进行归因分析的一种分析/写作手法？）**
- 这篇论文的关键创新之一，是**预测 info gain 并优先选更“值钱”的 frontier**；
- 这种能力最容易在**探索前期**体现出来，因为前几步选得好不好，会明显影响后面覆盖速度；
- 结果里作者特别指出：在 **Vox@50** 上，他们比第二名整体高大约 **15%**，并把这解释为系统能够在 early exploration 阶段更有效地优先访问高 info-gain 区域。
你可以这样理解：
- **摘要里的“15% improvement”主要对应的是中早期阶段的优势表达**；
- **但不是说最终阶段没有提升**。实际上 Table I 里他们在 Vox@100 的 mean 也是最高：
    - Ours（sim depth）= **71.5**
    - NBVP = **67.0**
    - Classic = **53.6**
    - SEER = **51.8 / 55.1**（原版 / 重实现）  
        所以完整阶段也还是更强。
所以这句话更准确的读法是：
**作者最想突出的是“前期决策质量提升非常明显”，不是“只有前期提升”。**
#### 3. 引言里面说了现有exploration方法可以分为两大类：一是frontier-based：从 map boundary 里直接找 frontier, 二是**sampling-based / NBV-like**：在地图里采样 viewpoint 或 path，再评估哪一个更好。==所以这两类方法的区别到底是什么？==
GPT：
这是个非常核心的问题。你可以先记最短版本：
- **frontier-based**：先找“已知自由区域”和“未知区域”的边界，再围绕这些边界选目标。
- **sampling-based / NBV-like**：不先限定必须是 frontier 边界，而是在地图里采样 candidate viewpoints / paths，再根据某种指标评估哪个最好。
更细一点说：
> [!A. frontier-based 方法]
这类方法的出发点是：
**未知空间最有可能从 frontier 附近被看到。**
所以流程通常是：
1. 先有一个 occupancy map / voxel map；
2. 在 map 里找 frontier，也就是 known-free 和 unknown 的边界；
3. 再从这些 frontier 里挑下一个要去的目标。
它的特点是：
- 候选点来源比较明确；
- 搜索空间相对小；
- 通常比较直接、计算也可能更省；
- 但很依赖 frontier 提取得准不准，也强依赖地图边界质量。
> [!B. sampling-based / NBV-like 方法]
这类方法的思路是：
**先提出很多候选 viewpoint / path，再评估哪一个信息收益最高。**
所以流程通常是：
1. 在当前 map 中采样一些 viewpoint 或 path；
2. 对每个 candidate 计算一个评价分数，比如 map entropy、uncertainty、information gain；
3. 选分数最高的 next-best-view / next-best-path。
它的特点是：
- 候选不局限于 frontier 边界本身；
- flexibility 更高；
- 可以直接把“信息收益”“不确定性”“路径代价”等统一进评分里；
- ==但一般采样和评估开销更大。==
==我的疑问：所以 sampling based / nbv like 方法它是怎么选点的呢？？？ 是用均匀采样这种吗？==
C. 这两类方法的本质差别
你可以把差别总结成一句：
**frontier-based 是“先找边界，再选目标”；sampling-based 是“先撒候选，再算哪个目标最好”。**
或者更学术一点：
- frontier-based 的 candidate generation 是 **boundary-driven**
- sampling-based 的 candidate generation 是 **proposal/evaluation-driven**
论文 introduction 里那句
> one derives poses from the 3D map by calculating optimal poses directly, the other samples poses and evaluates them against the map  
> 其实就是在讲这个差别。前者是**从 map 边界直接导出 pose**，后者是**采样 pose 再回到 map 上打分**。

D. 这篇论文为什么会抓住这个差别？
因为作者认为：虽然 frontier-based 和 sampling-based 看起来不一样，**但两者有一个共同点——都高度依赖 3D map 来指导 exploration**。
所以 FrontierNet 想改的不是“只打败 frontier-based”，而是更上层地挑战这个共性：
**goal proposal 这一步，能不能不从 dense 3D map 出发，而是直接从视觉里学？**

#### 4. Unlike existing methods, it avoids operations on dense 3D maps at the proposal stage, which are sensitive to map quality, and often discard rich appearance information. 什么是proposal阶段？
这里的 **proposal stage**，你可以先直接理解成：
**“提出候选探索目标”的阶段**，也就是系统先决定  
**哪些 frontier / 哪些 candidate poses 值得后续考虑**。
放到这篇论文里具体是什么意思
这篇论文的系统大致可以拆成：
1. **proposal**：先从输入里提出 frontier candidates，并估计它们的 info gain
2. **3D anchoring**：把 2D 结果变成 sparse 3D frontiers
3. **planning**：再从这些候选里选 next best goal，并规划路径去那里
所以这里的 **proposal stage** 不是“真正去走路径”的阶段，  
而是更前面的：
**先找出“可以去哪里”和“哪里更值得去”** 的阶段。
==[[2026-04-20#^9bt9ty]]==
为什么作者要特别说这个阶段？
因为传统方法通常在这个阶段会做很多 **dense 3D map operations**，比如：
- 在 occupancy map / voxel map 里找 frontier boundary
- 在 3D map 里采样 viewpoints
- 根据 3D map 计算 candidate 的信息收益

而作者说他们的方法在 **proposal stage** 避免了这种 dense 3D map 上的操作，转而直接从图像里预测：
- frontier 在哪里
- 它的 info gain 大概多大
结合 Fig. 3 来理解
Fig. 3 里其实已经把流程画出来了：
- posed RGB image
- depth prediction
- **FrontierNet predicts 2D frontier regions and info gain**
- transform into sparse 3D frontiers
- planning module selects next goal and plans path
所以在这张图里：
**FrontierNet 输出 2D frontier regions + info gain 的这部分，就是 proposal stage 的核心。**
后面的 tracking、next-best-goal selection、path planning，就已经不属于 proposal 本身了。

#### 5. 如何制作数据集用于训练？？如何有ground truth，它再method里面说会在III-D里面讲解
---
#### 6. Fig. 4: Ground Truth Generation. For a sampled camera pose in the voxelized scene, 3D frontier voxels are calculated and projected onto the camera frame using ground truth 3D occupancy grid. Merging the projection with the depth discontinuity mask produces a refined and less noisy frontier pixels mask F, which is used to calculate the distance field map D. Additionally, projecting the info gain of each frontier voxel onto the camera frame generates the info gain map G.
==我不是很理解，如果ground truth是通过3D信息去打标签的话，那么也没有利用到前面作者一直说的图片的appearance 信息阿？？？==(我的意思是，ground truth是去引导模型学习的对吗？如果ground truth是基于几何信息得到的，那么它如何有效引导模型去利用图片的appearance信息呢？我的意思是，比如图片的appearance提供的信息应该是除了几何还有语义信息，但是现在的实验设计是偏向于让模型从图片里面可以得到和3D信息提供的类似的输出，类似于去锻炼了模型的模仿传统方法的潜力？但是并没有充分针对或者利用图片的信息？我不知道我有没有表达清楚)
chatGPT的回答
> [!关于这篇论文里 appearance information 的一个当前理解]
> 我目前的理解是，这篇论文虽然一直强调 visual cues / appearance information，但它在训练时使用的 ground truth 其实仍然主要是由 **3D 几何信息**定义出来的：frontier 来自 3D occupancy / frontier voxel 的投影，info gain 也来自额外可观测体积这一几何量的估计。也就是说，作者先用完整 3D 场景生成监督信号，再让模型从图像中学习去预测这些标签。
> 所以我现在更倾向于把这篇论文理解为：**它是在学习如何从视觉输入中预测一个由几何定义出来的 frontier / info gain 目标**。从这个角度看，appearance information 的作用更像是帮助模型完成 prediction，而不是直接参与定义 exploration objective 本身。换句话说，这篇论文证明的更像是：**图像中的 appearance cues 可以帮助预测 geometry-defined frontier 和 info gain**。
> 这也让我产生一个阅读上的提醒：论文里提到“利用 appearance information”，更准确地理解，可能不是说它建立了一个“由 appearance 原生定义”的探索目标，而是说它让模型有机会从 RGB 中学习那些对 frontier / gain prediction 有帮助的线索。这样理解的话，这篇论文的重点更像是 **visual prediction of geometry-defined targets**，而不是完全跳出传统几何定义。
> 我觉得这样看之后，这篇论文的贡献会更清楚：它不是在重新定义 frontier，而是在尝试回答——**是否可以不用在 test time 显式操作 dense 3D map，而直接从图像中预测传统几何意义下有用的 frontier 和 info gain。** 至于图像里更高层的语义信息是否被充分利用，我感觉这篇论文有涉及这个方向，但可能还不是它最核心、最彻底展开的部分。
> 


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

### useful sentences

1. 感觉摘要可以帮助我更好地理解exploration这个任务本身的意义
2. 说了之前方法的问题：一是依赖3D map, 二是没有利用到视觉线索（RGB）
3. 引言里面说了现有exploration方法可以分为两大类：一是frontier-based：从 map boundary 里直接找 frontier, 二是**sampling-based / NBV-like**：在地图里采样 viewpoint 或 path，再评估哪一个更好。==所以这两类方法的区别到底是什么？==
4. 作者在引言里面把explortion的问题，通过人类的直觉类比，认为2D视觉输入可以得到explicite boundary，认为类似于3D地图中的boundary(边界)，我感觉这一点他们是把问题再次聚焦起来，从而起到理论上觉得可以替换的可行性？
5. 在Method里面有两个设计，一是frontier使用的是distance field而不是二分法（是frontier或者不是frontier, bool) ，二是对于 info gain value预测头，==因为预测高方差的回归任务难度较高，所以作者设计的是分为K bins的多分类任务预测头。==
6. If both the distance of the positions and the angle between the orientations of the new frontier and an existing frontier are below a threshold, the two are merged, ^syzsjk
[[2026-04-20#^p28o39]]


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
