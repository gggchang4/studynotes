---
id: "AI-05-07"
type: topic
status: framework
layer: "主干"
kind: "架构"
sources: ["T03","T16","P06"]
code_status: not-added
diagram_status: planned
---

# 注意力机制与Transformer

> [!info] 框架，待扩写
> 已确定范围、提纲和资料入口。正文推导、代码、论文精读与配图尚未展开。

[[AI/00-知识库总览|总览]] · [[AI/01-笔记编写约束|编写约束]] · [[AI/02-学习资料与论文索引|资料与论文]] · [[AI/05-训练方法与核心结构/00-模块索引|模块索引]]

## 本篇范围

模型怎样通过注意力选择信息，多头结构与掩码如何约束计算？

**前置知识：** [[AI/04-神经网络与PyTorch/05-PyTorch模型、数据与训练循环|PyTorch模型、数据与训练循环]]、[[AI/01-数学与编程基础/02-线性代数与矩阵分解|线性代数与矩阵分解]]

**关联阅读：** [[AI/05-训练方法与核心结构/06-RNN、LSTM与序列建模|RNN、LSTM与序列建模]]（辅助理解，不作为严格前置）。

## 内容提纲

- **注意力机制**：Query、Key、Value 与加权聚合；点积注意力、缩放点积注意力；Self-attention、Cross-attention、Multi-head Attention；Padding Mask、Causal Mask 与信息可见范围。
- **Transformer 结构**：Token Embedding、位置编码、前馈网络；注意力、残差连接与归一化的组合；Encoder-only、Decoder-only、Encoder–Decoder 结构。
- **序列生成与复杂度**：注意力的计算与显存复杂度、长序列问题；自回归生成与训练、推理过程的差异。

## 后续正文重点

- 逐步计算一个小型 Q/K/V 例子，说明缩放、Softmax 与多头形状。
- 对照三类 Transformer、位置编码、残差/归一化，以及训练、自回归推理和复杂度。

## 学习资料与论文

| 类型 | 入口 | 具体阅读内容 |
| --- | --- | --- |
| 主教材/教程 | [T03 · 动手学深度学习](https://d2l.ai/) | 第11章：Attention Mechanisms and Transformers |
| 补充/实现 | [T16 · CS224N](https://web.stanford.edu/class/cs224n/) | Attention、Transformer 与语言建模相关讲义 |
| 原始论文 | [P06 · Transformer](https://arxiv.org/abs/1706.03762) | 多头注意力与编码器、解码器结构 |

论文当前仅核对书目信息与摘要/出版社页面，全文待结合本篇阅读。教程当前核对公开目录或页面入口；详细书目、版次和证据范围见 [[AI/02-学习资料与论文索引|资料与论文索引]]。

## 教学图示设计

拟配：带 B/H/N/D 维度的注意力数据流、两类 Mask 与三种结构。

当前为图示设计，尚未生成本篇配图；扩写时按 [[AI/01-笔记编写约束#8. 教学配图|配图约束]] 选择素材或制作、插入并验证。
