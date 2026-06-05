# Multi-Agent多智能体

## 本笔记的学习目标
- 理解多智能体系统的角色划分、协作模式、通信方式和工程风险。

## 核心内容
- Multi-Agent 是把一个复杂任务拆给多个角色或多个 Agent 协作完成的模式。
- Microsoft 课程把 Multi-Agent 作为设计模式，Datawhale 项目案例中也有多角色 NPC、深度研究和综合毕业项目。
- 多智能体可以提升模块化和角色专业性，但也会增加成本、延迟、协调复杂度和不可控性。
- 多智能体不是越多越好，很多任务用单 Agent + Workflow 已经足够。

## 常见协作模式
- Supervisor-Worker：主管 Agent 分配任务，工作 Agent 执行。
- Planner-Executor：规划 Agent 生成计划，执行 Agent 调用工具。
- Debate / Critic：多个 Agent 提出方案，评审 Agent 选择或纠错。
- Role-based Team：研究员、写作者、审查者、工具执行者等角色协作。
- Swarm：大量轻量 Agent 共享任务状态，适合模拟和探索，但难以控制。

## 工程化要点
- 每个 Agent 应有明确职责、输入输出和权限。
- Agent 间通信要结构化，避免互相传递长篇自然语言噪音。
- 需要全局状态和全局停止条件。
- 成本和延迟要被单独评估，因为多智能体会放大调用次数。
- 高风险决策不能用“多个 Agent 都同意”替代人工复核。

## 后续需要补充的知识点清单
- 多智能体角色模板
- Supervisor 架构
- Agent 通信协议
- 多智能体评估方法

## 相关笔记链接
- [[01-Agent框架总览|Agent框架总览]]
- [[04-Agent通信协议与MCP|Agent通信协议与MCP]]
- [[02-Evaluation与Harness|Evaluation与Harness]]
- [[07-Agent安全与治理|Agent安全与治理]]

## TODO
- [ ] 设计一个研究型多智能体架构
- [ ] 补充多智能体失败案例

