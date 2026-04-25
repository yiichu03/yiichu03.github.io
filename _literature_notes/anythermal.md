---
title: "AnyThermal: Towards Learning Universal Representations for Thermal Perception"
slug: "anythermal"
date: 2026-04-24 15:19:15 +0000
published_at: 2026-04-24 15:19:15 +0000
updated_at: 2026-04-24 15:18:56 +0000
source_path: "10 Literature Notes/AnyThermal.md"
---

> Published: 2026-04-24
> Updated: 2026-04-24 15:18 UTC

## Citation

- Authors: Parv Maheshwari, Jay Karhade, Yogesh Chawla, Isaiah Adu, Florian Heisen, Andrew Porco, Andrew Jong, Yifei Liu, Santosh Pitla, Sebastian Scherer, Wenshan Wang
- Year: 2026
- Venue: arXiv preprint
- Citekey: Maheshwari2026AnyThermal

## Reading Context

- Why I read this paper: 我正在关注 thermal camera 在移动机器人导航与探索中的作用，尤其是希望理解 thermal 是否能作为 RGB/RGB-D/LiDAR perception module 的替代或补充。
- Reading goal: focused understanding / related work
- My current stage: skimming

## Part A — AI-generated scaffold

> Use this part to quickly build structure, but verify every important claim against the paper.

### AI Summary

- Problem:
  现有 thermal perception 方法通常是 task-specific 的，也就是针对某一个具体任务训练，例如 thermal segmentation、thermal depth estimation 或 thermal place recognition。由于 thermal 数据集规模小、环境覆盖窄，这类模型往往只能在特定任务或特定环境中表现较好，难以作为通用 thermal backbone 使用。本文要解决的问题是：能否学习一个 task-agnostic thermal encoder，使它能够迁移到多种 thermal perception 任务和多类环境中。

- Core idea:
  核心思路是把 RGB foundation model 的表征能力蒸馏到 thermal encoder 中。具体来说，作者使用 frozen DINOv2 作为 RGB teacher，用 trainable DINOv2 作为 thermal student，通过 RGB-T paired data 进行 cross-modal feature distillation。这样 thermal encoder 不需要从零开始学习语义表征，而是从强 RGB foundation model 中继承语义结构，同时通过 thermal image 训练适配 thermal modality。

- Method:
  AnyThermal 使用两个 DINOv2 ViT-B/14 encoder。RGB teacher 处理 RGB image，并保持 frozen；thermal student 处理 thermal image，并参与训练。thermal image 原本是 grayscale，会被转成 3-channel 输入。训练时，作者使用 RGB-T pair 的 CLS token features 做 contrastive learning，使对应 RGB 和 thermal 图像的全局语义特征靠近。训练完成后，thermal student 就成为 AnyThermal backbone。下游任务只需要在这个 backbone 上接 task-specific head。

- Main result:
  AnyThermal 在三个 downstream tasks 上展示了效果：
  - cross-modal place recognition；
  - thermal semantic segmentation；
  - monocular thermal depth estimation。

  在 cross-modal place recognition 中，AnyThermal-VPR 在 MS2、CART、OdomBeyondVision 三个数据集上都取得表中最好的 Recall@1。在 thermal segmentation 中，AnyThermal-SEG 在 MF-Net 上达到 53.47% mIoU，并且在 ORIN AGX 上达到 6.79 FPS。在 monocular thermal depth estimation 中，AnyThermal 在 MS2 上 AbsRel 为 0.0883，优于 EfficientLite3 和 frozen DINOv2 backbone。

- One-sentence takeaway:
  AnyThermal 本身不是导航或探索算法，而是一个通用 thermal perception backbone；它的价值在于为 thermal-based navigation、place recognition、semantic mapping、frontier scoring、recovery cue 等后续机器人任务提供更强的 thermal representation。

### Abstract-style reading note

- Paper goal:
  本文目标是构建一个通用 thermal feature extractor，使其不依赖单一任务训练，也能迁移到不同环境和不同 downstream thermal perception 任务中。

- Core challenge:
  Thermal image 在弱光、恶劣天气、退化视觉条件下对机器人感知很有用，但 thermal 数据远少于 RGB 数据，也缺少类似 ImageNet / Internet-scale RGB data 那样的大规模资源。因此，thermal backbone 很难像 RGB backbone 一样通过大规模预训练获得通用表征能力。

- Authors' claim:
  作者认为，通过多环境 RGB-T 数据，把 DINOv2 这类 RGB foundation model 的 feature representations 蒸馏到 thermal encoder 中，可以得到一个泛化性更强的 task-agnostic thermal backbone。同时，作者提出 TartanRGBT platform 和 TartanRGBT dataset，用来缓解现有 RGB-T 数据集环境单一、采集平台不统一、同步和配准不足的问题。

### Method

- Inputs / observations:
  方法训练时使用 paired RGB and thermal images。训练数据来自多个 RGB-T 数据集，覆盖 urban、aerial、indoor、off-road 等环境。作者使用的数据包括 ViVID++、STheReO、Freiburg、Boson Nighttime 和 TartanRGBT。MS2、CART、OdomBeyondVision 被保留用于 zero-shot downstream evaluation。

- Outputs / targets:
  输出不是 robot action、pose、map 或 trajectory，而是一个 thermal feature-extraction backbone。这个 backbone 可以作为通用特征提取器，被不同任务的 head 使用。

- Main modules:
  - Frozen RGB teacher:
    使用 pretrained DINOv2 ViT-B/14，输入 RGB image，参数冻结。
  - Trainable thermal student:
    使用同样结构的 DINOv2 ViT-B/14，输入 thermal image，参数可训练。
  - RGB-T feature distillation:
    使用 RGB-T pair 的 CLS token feature 做 contrastive alignment。
  - Task-specific heads:
    不同任务接不同 head。例如 VPR 使用 SALAD head，segmentation 使用 two-layer non-linear MLP head，depth estimation 使用 MiDaS framework。
  - TartanRGBT platform:
    一个同步采集 RGB-T 数据的平台，包括 stereo RGB、stereo thermal、IMU 和 hardware synchronization。
  - TartanRGBT dataset:
    作者用该平台采集的多环境 RGB-T 数据集，覆盖 indoor、off-road、urban driving、park/trail 等场景。

- Training objective:
  Backbone training 使用 task-agnostic knowledge distillation，不依赖人工语义标签。主要目标是在 RGB teacher 和 thermal student 的 CLS token features 之间做 contrastive alignment，使 thermal image 的全局语义表征接近对应 RGB image 的语义表征。

  下游任务训练方式不同：
  - VPR head:
    使用 triplet margin loss。
  - Segmentation head:
    backbone frozen，只训练 segmentation head，loss 使用 Dice loss。
  - Depth estimation:
    采用 MiDaS 框架，将原有 backbone 替换为 DINOv2 或 AnyThermal。

- Inference / rollout:
  本文没有 closed-loop robot navigation 或 exploration rollout。Inference 取决于下游任务：
  - Cross-modal VPR:
    thermal query image → AnyThermal feature / SALAD head → 在 RGB database 中检索 matching place。
  - Thermal segmentation:
    thermal image → AnyThermal backbone → segmentation head → semantic mask。
  - Mono-thermal depth estimation:
    thermal image → AnyThermal-backed MiDaS → depth map。

- Key assumptions:
  - RGB foundation model 中的语义结构可以迁移到 thermal modality。
  - RGB-T paired data 提供了足够的跨模态对应关系。
  - 使用 CLS token 做全局语义对齐，比 patch-level loss 更不依赖严格的 pixel-level alignment 和同步。
  - 对 thermal representation 来说，数据多样性比单纯增加同质数据量更重要。
  - Thermal perception 可以通过 foundation-model-style representation learning 获得跨任务泛化能力。

### Experiments

- Tasks / datasets:
  - Cross-modal place recognition:
    在 MS2、CART、OdomBeyondVision 上评估。
  - Thermal semantic segmentation:
    在 MF-Net 上评估。
  - Monocular thermal depth estimation:
    在 MS2 上评估。
  - Data scaling / diversity ablation:
    比较不同 pretraining dataset 组合对 downstream performance 的影响。

- Baselines:
  - Cross-modal VPR:
    DINOv2、SALAD、ImageBind、SGM。
  - Thermal segmentation:
    RTFNet-152、MCNet、RGB DINO-SEG。
  - Thermal depth estimation:
    EfficientLite3、frozen DINOv2 ViT-B/14、AnyThermal。

- Main metrics:
  - VPR:
    Recall@1。
  - Segmentation:
    mIoU 和 FPS。
  - Depth estimation:
    AbsRel、SqRel、RMSE、RMSElog。
  - Data scaling:
    Recall、mIoU、AbsRel。

- Best numbers worth remembering:
  - Cross-modal VPR:
    AnyThermal-VPR 在 MS2 / CART / OdomBeyondVision 上的 Recall@1 分别为 81.11 / 56.00 / 53.17。
  - Thermal segmentation:
    AnyThermal-SEG 在 MF-Net 上达到 53.47% mIoU，在 NVIDIA ORIN AGX 64GB 上达到 6.79 FPS。
  - Monocular thermal depth estimation:
    AnyThermal 在 MS2 上达到 AbsRel = 0.0883，优于 frozen DINOv2 和 EfficientLite3。

- Strongest evidence:
  最强证据不是某一个任务上的单点 SOTA，而是同一个 AnyThermal backbone 在 VPR、segmentation、depth estimation 三个不同任务上都能带来提升。尤其是 VPR 中，frozen RGB-DINOv2 与 AnyThermal 的差距说明，直接把 RGB foundation model 用在 thermal image 上是不够的，thermal-specific distillation 是有必要的。

### Innovation / contributions

- System contribution:
  作者提出 TartanRGBT platform，这是一个用于采集 RGB-T 数据的开放平台，包含 synchronized stereo RGB 和 stereo thermal cameras。这个平台的意义在于降低 community 采集多样化 RGB-T 数据的门槛。

- Algorithm contribution:
  作者提出 AnyThermal，一个通过 RGB-T knowledge distillation 得到的 task-agnostic thermal backbone。关键算法设计是使用 DINOv2 作为 teacher/student backbone，并在 CLS token feature 上做 contrastive alignment。

- Experimental contribution:
  作者在多个 downstream tasks 和多个环境中验证同一个 thermal backbone 的泛化能力，并通过 data scaling experiment 说明：增加数据有帮助，但跨 domain 的数据多样性比单纯增加相似数据更重要。

- Research perspective contribution:
  这篇论文把 thermal robotics perception 从 task-specific model 推向 reusable thermal representation learning。对我的机器人导航/探索方向来说，它可以作为 thermal-only 或 thermal-dominant navigation stack 的 perception backbone 候选，尤其适合进一步探索：
  - thermal place recognition / relocalization cue；
  - thermal semantic mapping；
  - frontier utility prediction；
  - traversability estimation；
  - localization degradation 下的 recovery cue。

### Limitations

- This is not a navigation or exploration paper:
  这篇论文没有提出 planner、exploration policy、localization uncertainty monitor 或 recovery mechanism。它主要解决的是 thermal representation learning 问题。

- No closed-loop autonomy evaluation:
  实验主要是 downstream perception tasks，没有展示 AnyThermal 是否能直接提升 closed-loop navigation、exploration efficiency 或 real-robot recovery performance。

- Still depends on RGB supervision:
  AnyThermal 是通过 RGB teacher 蒸馏得到的，因此训练质量依赖 RGB teacher 的表征质量。如果 RGB 图像本身质量差，teacher feature 可能也不可靠。

- TartanRGBT cannot yet serve as a ground-truth benchmark for some tasks:
  作者说明 TartanRGBT 中的 dense depth 和 odometry 来自 stereo-RGB algorithms，精度不足以作为 odometry 或 depth estimation benchmark 的 ground truth。

- Depth improvement is relatively modest:
  在 monocular thermal depth estimation 上，AnyThermal 相比 frozen DINOv2 有提升，但数值提升不如 VPR 和 segmentation 明显。因此 depth task 上的结论需要谨慎看待。

- The representation is promising but not yet proven for planner-level decisions:
  AnyThermal 是否能直接改善 frontier selection、semantic exploration、localization recovery、uncertainty-aware planning，目前还没有被本文验证。

### AI Questions to Verify

- Which claims should I check in the figures/tables?
  - Table I:
    检查 TartanRGBT 是否确实在 environment diversity、synchronization、registration 上比现有 RGB-T 数据集更全面。
  - Table II:
    检查 cross-modal VPR 结果，确认 AnyThermal-VPR 是否在 MS2、CART、OdomBeyondVision 上都优于 baseline。
  - Table III:
    检查 MF-Net segmentation 的 mIoU 和 FPS，尤其是 “3.6× faster than closest baseline” 的依据。
  - Table IV:
    检查 depth estimation 的提升幅度，判断它是否足够支撑 strong claim。
  - Fig. 8:
    重点看 data scaling / diversity ablation，判断 “diversity matters more than scale” 是否被充分支持。

- Which design choices seem most important?
  - 使用 DINOv2 作为 RGB teacher 和 thermal student 的初始化。
  - 使用 CLS token feature 做 contrastive distillation，而不是强依赖 RGB-T pixel-level alignment 的 patch loss。
  - 使用多个 domain 的 RGB-T 数据进行蒸馏。
  - 将 MS2、CART、OdomBeyondVision 等数据集保留为 downstream zero-shot evaluation。
  - 不只在单一任务上评估，而是在 VPR、segmentation、depth estimation 上共同验证 backbone 的通用性。

- Which details are still vague after only reading the abstract/introduction?
  - Contrastive loss 的具体形式，例如 temperature、negative sample 构造、batch sampling 策略。
  - RGB-T 同步误差和配准误差对蒸馏效果的影响。
  - Thermal student 到底学到了多少 thermal-specific cues，而不是简单继承 RGB semantic prior。
  - AnyThermal feature 是否适合 planner-level decision，例如 frontier ranking、semantic exploration、localization confidence estimation。
  - 模型、代码、TartanRGBT dataset 是否已经 release，还是只是在 acceptance 后计划 release。
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
