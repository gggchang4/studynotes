# Workflow与Graph编排

## 本笔记的学习目标
- 理解确定性 Workflow、状态图和 Agent 自主决策之间的关系。

## 核心内容
- Workflow 是由开发者定义步骤、分支、重试和依赖关系的流程。
- Graph 编排用节点和边表示任务流转，适合有循环、有状态、有条件分支的 Agent 系统。
- Agent 自主决策适合开放性子任务，但生产系统通常需要 Workflow 或 Graph 限制其自由度。
- 最可靠的工程形态往往是 Workflow 控制主流程，Agent 处理局部智能决策。

## 编排模式
- Sequential：线性步骤，例如检索 -> 生成 -> 校验。
- Router：根据输入类型进入不同流程。
- Loop：执行、观察、反思、重试。
- Parallel：并行执行多个检索或子任务。
- Human-in-the-loop：关键节点等待人工确认。
- Supervisor：主管节点调度多个子 Agent。

## 工程化要点
- 每个节点应有明确输入、输出、失败处理和日志。
- 工作流要有超时、重试、降级和终止条件。
- 图编排中的状态不能完全依赖自然语言历史。
- 高风险业务流程要用确定性规则包住 Agent。

## 后续需要补充的知识点清单
- Workflow 与 Agent 混合架构
- 图编排节点设计
- 工作流失败恢复策略
- 人工审核节点设计

## 相关笔记链接
- [[02-Agent与Chatbot、Workflow的区别|Agent与Chatbot、Workflow的区别]]
- [[02-LangGraph|LangGraph]]
- [[05-State状态管理|State状态管理]]
- [[04-多步骤任务Agent|多步骤任务Agent]]

## TODO
- [ ] 补充一个 Agent Workflow 图
- [ ] 增加多步骤任务编排模板

