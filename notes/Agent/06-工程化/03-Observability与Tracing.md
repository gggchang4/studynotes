# Observability与Tracing

## 本笔记的学习目标
- 理解 Agent 系统为什么必须可观测，以及如何通过日志、Trace 和指标定位问题。

## 核心内容
- Observability 是让 Agent 从黑盒变成可复盘系统的能力。
- Tracing 记录一次请求中模型调用、工具调用、检索、状态变更、错误和输出的完整链路。
- Hugging Face Bonus Unit 和 Datawhale 工程经验都强调评估与观测；没有 Trace，很难知道 Agent 是 Prompt 问题、工具问题、检索问题还是模型问题。

## 需要记录什么
- 用户输入和任务 ID。
- Prompt 版本、模型名称、模型参数。
- 检索 Query、召回片段、Rerank 结果。
- 工具名称、参数、结果、错误、耗时。
- Agent 状态、计划步骤、反思和停止原因。
- Token、成本、延迟、重试次数。
- 最终输出、用户反馈和评估结果。

## 指标体系
- 质量指标：任务成功率、答案准确率、工具调用正确率、RAG Faithfulness。
- 性能指标：总延迟、模型延迟、工具延迟、检索延迟。
- 成本指标：Token、调用次数、单任务成本、缓存命中率。
- 稳定性指标：错误率、重试率、超时率、降级率。
- 安全指标：拒绝率、人工确认率、越权拦截率。

## 工程化理解
- Trace 要结构化，不能只保存一大段自然语言日志。
- 失败样本比成功样本更有价值，不能清洗掉。
- 可观测性要同时服务开发者和业务人员：技术细节用于排障，摘要用于复核。

## 后续需要补充的知识点清单
- Trace 数据结构
- OpenTelemetry / LangSmith / Arize Phoenix 等工具调研
- 线上监控面板

## 相关笔记链接
- [[02-Evaluation与Harness|Evaluation与Harness]]
- [[04-错误处理、重试与降级|错误处理、重试与降级]]
- [[07-Agent安全与治理|Agent安全与治理]]
- [[05-RAG评估与工程化|RAG工程化问题]]

## TODO
- [ ] 设计 Agent Trace Schema
- [ ] 补充一次失败任务的 Trace 示例

