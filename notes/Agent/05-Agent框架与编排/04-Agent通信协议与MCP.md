# Agent通信协议与MCP

## 本笔记的学习目标
- 理解 Agent 与工具、外部服务、资源和其他 Agent 通信时的协议化设计。

## 核心内容
- MCP 是 Model Context Protocol，用于把外部工具、资源和上下文以标准方式暴露给模型应用。
- Microsoft 课程把 MCP、A2A、NLWeb 等 Agentic Protocols 放在独立章节，说明协议层会成为 Agent 工程的重要基础设施。
- 协议化的价值是降低工具接入成本、提升互操作性，并让权限、审计和资源管理更清晰。
- Agent 通信协议不能只看功能，也要看安全边界：能暴露什么资源、能执行什么动作、谁来授权、如何记录。

## 关键问题
- 资源暴露：外部系统向 Agent 暴露哪些文件、数据库、API 或上下文。
- 工具调用：工具 Schema、参数校验、返回格式和错误处理。
- 上下文注入：如何避免不可信资源污染系统指令。
- Agent 间通信：任务委派、结果回传、状态同步和冲突处理。
- 权限控制：按用户、会话、工具、资源和操作级别授权。

## 工程化理解
- MCP 可以看作工具和上下文的标准化接口，但它不是安全机制本身。
- 协议层越开放，越需要最小权限、审计日志和人工确认。
- 多智能体或跨系统 Agent 项目，应尽早设计通信契约和错误语义。

## 后续需要补充的知识点清单
- MCP 基本架构
- A2A 与 NLWeb 适用场景
- Tool Calling 与 MCP 的边界
- 协议安全与审计

## 相关笔记链接
- [[04-Tool Calling与外部系统|Tool Calling与外部系统]]
- [[06-Multi-Agent多智能体|Multi-Agent多智能体]]
- [[03-Workflow与Graph编排|Workflow与Graph编排]]
- [[07-Agent安全与治理|Agent安全与治理]]
- [[03-Observability与Tracing|Observability与Tracing]]

## TODO
- [ ] 补充一个 MCP Server 最小示例
- [ ] 建立协议权限检查表

