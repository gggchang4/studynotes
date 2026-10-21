---
id: "AI-08-02"
type: topic
status: framework
layer: "分支"
kind: "算法"
sources: ["T20","T03","T08","P15"]
code_status: not-added
diagram_status: planned
---

# Q-learning与DQN

> [!info] 框架，待扩写
> 已确定范围、提纲和资料入口。正文推导、代码、论文精读与配图尚未展开。

[[AI/00-知识库总览|总览]] · [[AI/01-笔记编写约束|编写约束]] · [[AI/02-学习资料与论文索引|资料与论文]] · [[AI/08-强化学习/00-模块索引|模块索引]]

## 本篇范围

动作价值怎样从表格更新扩展为神经网络近似？

**前置知识：** [[AI/08-强化学习/01-MDP、价值函数与基本决策方法|MDP、价值函数与基本决策方法]]、[[AI/04-神经网络与PyTorch/05-PyTorch模型、数据与训练循环|PyTorch模型、数据与训练循环]]

## 内容提纲

- **价值方法**：Q-learning、SARSA、DQN、经验回放、目标网络。

## 后续正文重点

- 用一次转移手算 TD 目标与 Q 更新。
- 以 2015 DQN 为基准解释经验回放与目标网络，不与 2013 初版混写。

## 学习资料与论文

| 类型 | 入口 | 具体阅读内容 |
| --- | --- | --- |
| 主教材/教程 | [T20 · 强化学习导论](https://mitpress.mit.edu/9780262039246/reinforcement-learning/) | TD 与函数近似相关章 |
| 补充/实现 | [T03 · 动手学深度学习](https://d2l.ai/) | 17.3 Q-Learning |
| 补充/实现 | [T08 · PyTorch 入门](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | 由官方教程索引进入 DQN 专题 |
| 原始论文 | [P15 · DQN](https://www.nature.com/articles/nature14236) | 深度 Q 学习、经验回放与目标网络 |

论文当前仅核对书目信息与摘要/出版社页面，全文待结合本篇阅读。教程当前核对公开目录或页面入口；详细书目、版次和证据范围见 [[AI/02-学习资料与论文索引|资料与论文索引]]。

## 教学图示设计

拟配：Q 表更新与在线网络/目标网络训练流。

当前为图示设计，尚未生成本篇配图；扩写时按 [[AI/01-笔记编写约束#8. 教学配图|配图约束]] 选择素材或制作、插入并验证。
