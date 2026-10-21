---
id: "AI-08-03"
type: topic
status: framework
layer: "分支"
kind: "算法"
sources: ["T20","T07","T19","P16"]
code_status: not-added
diagram_status: planned
---

# 策略梯度、Actor-Critic与PPO

> [!info] 框架，待扩写
> 已确定范围、提纲和资料入口。正文推导、代码、论文精读与配图尚未展开。

[[AI/00-知识库总览|总览]] · [[AI/01-笔记编写约束|编写约束]] · [[AI/02-学习资料与论文索引|资料与论文]] · [[AI/08-强化学习/00-模块索引|模块索引]]

## 本篇范围

如何直接优化策略，价值估计和更新约束分别起什么作用？

**前置知识：** [[AI/08-强化学习/01-MDP、价值函数与基本决策方法|MDP、价值函数与基本决策方法]]、[[AI/04-神经网络与PyTorch/02-损失函数、反向传播与梯度检验|损失函数、反向传播与梯度检验]]、[[AI/08-强化学习/02-Q-learning与DQN|Q-learning与DQN]]

## 内容提纲

- **策略方法**：策略梯度、REINFORCE、Actor–Critic、PPO。
- **拓展与评价**：模型式与无模型强化学习、离线强化学习的基本概念；奖励设计、样本效率、训练稳定性与评价方法。

## 后续正文重点

- 解释 REINFORCE、基线、优势与 Actor-Critic，再进入 PPO。
- 区分在线/离线、模型式/无模型，说明奖励、样本效率、稳定性和评价；离线 RL 不沿用在线评估假设。

## 学习资料与论文

| 类型 | 入口 | 具体阅读内容 |
| --- | --- | --- |
| 主教材/教程 | [T20 · 强化学习导论](https://mitpress.mit.edu/9780262039246/reinforcement-learning/) | Policy Gradient Methods 与 Actor-Critic 相关章 |
| 补充/实现 | [T07 · CS229](https://cs229.stanford.edu/syllabus-autumn2018.html) | Policy Search 与 REINFORCE |
| 补充/实现 | [T19 · CS336](https://cs336.stanford.edu/spring2025/) | Alignment 与 reasoning RL 相关讲义 |
| 原始论文 | [P16 · PPO](https://arxiv.org/abs/1707.06347) | 策略更新约束与代理目标 |

论文当前仅核对书目信息与摘要/出版社页面，全文待结合本篇阅读。教程当前核对公开目录或页面入口；详细书目、版次和证据范围见 [[AI/02-学习资料与论文索引|资料与论文索引]]。

## 教学图示设计

拟配：Actor/Critic 双网络与采样—更新闭环。

当前为图示设计，尚未生成本篇配图；扩写时按 [[AI/01-笔记编写约束#8. 教学配图|配图约束]] 选择素材或制作、插入并验证。
