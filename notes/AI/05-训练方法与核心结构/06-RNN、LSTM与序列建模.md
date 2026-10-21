---
id: "AI-05-06"
type: topic
status: framework
layer: "主干"
kind: "架构"
sources: ["T03","T02","T06"]
code_status: not-added
diagram_status: planned
---

# RNN、LSTM与序列建模

> [!info] 框架，待扩写
> 已确定范围、提纲和资料入口。正文推导、代码、论文精读与配图尚未展开。

[[AI/00-知识库总览|总览]] · [[AI/01-笔记编写约束|编写约束]] · [[AI/02-学习资料与论文索引|资料与论文]] · [[AI/05-训练方法与核心结构/00-模块索引|模块索引]]

## 本篇范围

序列依赖如何被状态递推表示，门控结构缓解了哪些问题？

**前置知识：** [[AI/04-神经网络与PyTorch/02-损失函数、反向传播与梯度检验|损失函数、反向传播与梯度检验]]、[[AI/04-神经网络与PyTorch/03-初始化与梯度问题|初始化与梯度问题]]

## 内容提纲

- **序列模型**：序列表示、变长输入、Padding、Mask；RNN、BPTT、长期依赖问题；LSTM、GRU、双向循环网络；Encoder–Decoder、Seq2Seq、Teacher Forcing。

## 后续正文重点

- 展开 RNN 与 BPTT，再说明 LSTM/GRU 的门与状态。
- 比较双向网络、Seq2Seq、Teacher Forcing、Padding/Mask 及因果限制。

## 学习资料与论文

| 类型 | 入口 | 具体阅读内容 |
| --- | --- | --- |
| 主教材/教程 | [T03 · 动手学深度学习](https://d2l.ai/) | 第9–10章：RNN 与现代循环网络 |
| 补充/实现 | [T02 · 吴恩达深度学习专项](https://www.coursera.org/specializations/deep-learning) | 课程5：Sequence Models |
| 补充/实现 | [T06 · 深度学习教材](https://www.deeplearningbook.org/) | 第10章：Sequence Modeling |

本篇以教材与官方资料为主，暂不强配原始论文。教程当前核对公开目录或页面入口；详细书目、版次和证据范围见 [[AI/02-学习资料与论文索引|资料与论文索引]]。

## 教学图示设计

拟配：时间展开、门控单元与编码器—解码器。

当前为图示设计，尚未生成本篇配图；扩写时按 [[AI/01-笔记编写约束#8. 教学配图|配图约束]] 选择素材或制作、插入并验证。
