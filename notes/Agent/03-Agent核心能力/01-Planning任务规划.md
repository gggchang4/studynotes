# Planning任务规划

## 本笔记的学习目标
- 理解 Agent 如何把复杂目标拆解成可执行步骤，并在执行过程中动态调整计划。

## 核心内容
- Planning 是 Agent 面对复杂任务时的执行管理能力，目标是把高层目标转成步骤、依赖、工具调用和验收条件。
- Microsoft 课程把 Planning 作为重要设计模式，强调任务拆解、迭代计划和 Planner/Executor 分工。
- Datawhale 框架实践中常见 Plan-and-Solve、ReAct、Reflection 等范式，它们都在不同程度上解决“下一步做什么”的问题。
- 计划可以是自然语言列表，也可以是 JSON、状态图、任务队列或可执行工作流。

## 常见模式
- ReAct：每一步交替进行推理、行动和观察，适合探索型任务。
- Plan-and-Execute：先生成完整计划，再逐步执行，适合目标明确的多步骤任务。
- Dynamic Replanning：执行过程中根据工具结果或失败情况更新计划。
- Hierarchical Planning：大任务拆成子任务，子任务再交给子 Agent 或工具完成。

## 工程化要点
- 计划必须有验收条件，否则 Agent 容易“看似完成但实际没完成”。
- 计划步骤不宜过细，否则模型会被流程拖慢；也不宜过粗，否则无法执行和评估。
- 每一步应记录输入、输出、工具、状态变更和失败原因。
- 高风险步骤应插入人工确认节点。

## 后续需要补充的知识点清单
- Planning Prompt 模板
- 计划 JSON Schema
- Planner / Executor 架构
- 计划质量评估指标

## 相关笔记链接
- [[03-Agent核心组成与运行循环|Agent核心组成与运行循环]]
- [[02-Reasoning与Reflection|Reasoning与Reflection]]
- [[05-State状态管理|State状态管理]]
- [[04-多步骤任务Agent|多步骤任务Agent]]

## TODO
- [ ] 补充一个旅行规划 Agent 的计划样例
- [ ] 增加计划失败的排查清单

