# Agent知识地图

## 本笔记的学习目标
- 用一张概念地图理解 Agent 系统中模型、工具、记忆、状态、RAG、编排、评估和安全之间的关系。

## 核心内容
- LLM 是 Agent 的推理核心，但 Agent 的能力来自系统组合：模型负责判断，工具负责行动，状态负责连续执行，记忆负责跨轮次保留信息，RAG 负责连接外部知识。
- Agent 的基本运行关系可以理解为：用户目标进入系统，经过上下文构造和 Prompt 约束后交给模型，模型在思考、工具调用、观察反馈之间循环，直到达到停止条件。
- RAG 不是 Agent 的必备组件，但当任务依赖私有知识、长文档或可追溯引用时，RAG 通常会成为 Agent 的知识入口。
- Workflow 和 Graph 编排负责把不稳定的自由决策收束到明确流程中，适合生产场景中的多步骤任务。
- Evaluation、Tracing、安全权限不是附加项，而是 Agent 从 Demo 走向可用系统的基础设施。

## 知识关系
- 基础层：[[01-LLM应用基本架构|LLM应用基本架构]]、[[02-Prompt Engineering|Prompt Engineering]]、[[03-上下文管理与结构化输出|上下文管理与结构化输出]]
- Agent 层：[[03-Agent核心组成与运行循环|Agent核心组成与运行循环]]、[[01-Planning任务规划|Planning任务规划]]、[[04-Tool Calling与外部系统|Tool Calling与外部系统]]
- 知识层：[[01-RAG整体架构|RAG整体架构]]、[[03-Memory记忆机制|Memory记忆机制]]
- 编排层：[[02-LangGraph|LangGraph]]、[[03-Workflow与Graph编排|Workflow与Graph编排]]、[[04-Agent通信协议与MCP|Agent通信协议与MCP]]
- 工程层：[[02-Evaluation与Harness|Evaluation与Harness]]、[[03-Observability与Tracing|Observability与Tracing]]、[[07-Agent安全与治理|Agent安全与治理]]

## 后续需要补充的知识点清单
- Agent 核心组成关系图
- RAG、Memory、Context Engineering 的边界
- MCP、A2A、工具协议与多智能体通信关系
- 工程化、安全治理、可观测性与项目实战的交叉点

## 相关笔记链接
- [[03-Agent核心组成与运行循环|Agent核心组成与运行循环]]
- [[01-RAG整体架构|RAG整体架构]]
- [[04-Tool Calling与外部系统|Tool Calling与外部系统]]
- [[04-Agent通信协议与MCP|Agent通信协议与MCP]]
- [[01-Agent项目架构|Agent项目架构]]
- [[07-Agent安全与治理|Agent安全与治理]]

## TODO
- [ ] 用 Mermaid 画出知识地图
- [ ] 标记每个节点对应的项目实践

