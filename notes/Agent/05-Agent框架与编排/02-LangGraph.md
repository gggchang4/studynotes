# LangGraph

## 本笔记的学习目标
- 理解 LangGraph 在有状态 Agent、循环控制和多步骤图编排中的作用。

## 核心内容
- LangGraph 是面向有状态 Agent Workflow 的图编排框架，适合把 Agent 的多步骤执行建模为节点、边和状态流转。
- Hugging Face 课程中 LangGraph 单元包含基本概念、构建块、首个图和文档分析 Agent。
- LangGraph 的核心价值是把 Agent 的动态循环变得更可控：每个节点做什么、什么时候进入下一节点、如何结束都可以显式建模。

## 核心概念
- State：图执行过程中共享和更新的结构化状态。
- Node：执行一个具体步骤，例如调用模型、调用工具、检索、判断。
- Edge：节点之间的流转关系。
- Conditional Edge：根据状态决定走哪条分支。
- Checkpoint：保存执行进度，支持恢复和人工介入。
- Human-in-the-loop：在关键节点暂停，等待人工确认或补充。

## 适用场景
- 多步骤任务需要明确状态和可恢复执行。
- Agent 需要在工具调用、反思、重规划之间循环。
- 需要人工审核节点。
- 需要把 RAG、工具、计划和输出组合成可观测流程。

## 工程化理解
- LangGraph 适合生产化 Agent，但前提是先设计好 State Schema。
- 图越复杂，越需要可视化和 Trace，否则维护难度会快速上升。
- 不是所有 Agent 都需要 LangGraph，简单工具调用任务可以用更轻的结构。

## 后续需要补充的知识点清单
- LangGraph 基本图示例
- State Schema 设计
- Checkpoint 与恢复
- Human-in-the-loop 实践

## 相关笔记链接
- [[05-State状态管理|State状态管理]]
- [[03-Workflow与Graph编排|Workflow与Graph编排]]
- [[01-Planning任务规划|Planning任务规划]]
- [[04-多步骤任务Agent|多步骤任务Agent]]

## TODO
- [ ] 补充 LangGraph 最小图代码
- [ ] 增加文档分析 Agent 图结构

