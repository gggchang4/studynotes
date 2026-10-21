---
id: "AI-08-01"
type: topic
status: framework
layer: "分支"
kind: "原理"
sources: ["T20","T03","T07"]
code_status: not-added
diagram_status: planned
---

# MDP、价值函数与基本决策方法

> [!info] 框架，待扩写
> 已确定范围、提纲和资料入口。正文推导、代码、论文精读与配图尚未展开。

[[AI/00-知识库总览|总览]] · [[AI/01-笔记编写约束|编写约束]] · [[AI/02-学习资料与论文索引|资料与论文]] · [[AI/08-强化学习/00-模块索引|模块索引]]

## 本篇范围

长期回报、策略与价值怎样描述智能体在环境中的连续决策？

**前置知识：** [[AI/01-数学与编程基础/04-概率统计与参数估计|概率统计与参数估计]]、[[AI/01-数学与编程基础/05-优化与数值计算基础|优化与数值计算基础]]、[[AI/01-数学与编程基础/01-机器学习概念与任务|机器学习概念与任务]]

## 内容提纲

- **基本对象与价值**：Agent、环境、状态、动作、奖励、轨迹；Markov 决策过程（MDP）、策略、回报、折扣因子；状态价值函数、动作价值函数、Bellman 方程。
- **学习与决策**：动态规划、Monte Carlo、时序差分（TD）；探索与利用、On-policy 与 Off-policy；价值迭代与策略迭代。

## 后续正文重点

- 从小型状态转移表定义 MDP，展开 Bellman 期望与最优关系。
- 比较价值/策略迭代、MC/TD、探索利用和 On/Off-policy。

## 学习资料与论文

| 类型 | 入口 | 具体阅读内容 |
| --- | --- | --- |
| 主教材/教程 | [T20 · 强化学习导论](https://mitpress.mit.edu/9780262039246/reinforcement-learning/) | MDP、Dynamic Programming、Monte Carlo、Temporal-Difference 相关章 |
| 补充/实现 | [T03 · 动手学深度学习](https://d2l.ai/) | 第17章：Reinforcement Learning |
| 补充/实现 | [T07 · CS229](https://cs229.stanford.edu/syllabus-autumn2018.html) | MDPs 与 Bellman Equations |

本篇以教材与官方资料为主，暂不强配原始论文。教程当前核对公开目录或页面入口；详细书目、版次和证据范围见 [[AI/02-学习资料与论文索引|资料与论文索引]]。

## 教学图示设计

拟配：Agent—环境闭环、MDP 小图与价值备份。

当前为图示设计，尚未生成本篇配图；扩写时按 [[AI/01-笔记编写约束#8. 教学配图|配图约束]] 选择素材或制作、插入并验证。
