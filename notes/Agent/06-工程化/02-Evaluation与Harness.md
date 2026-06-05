# Evaluation与Harness

## 本笔记的学习目标
- 理解如何为 Agent、RAG 和工具调用系统建立可重复的评估体系。

## 核心内容
- Evaluation 是判断系统是否变好的机制，Harness 是让评估可重复运行的测试框架。
- Agent 评估不能只看最终答案，还要评估计划质量、工具选择、参数正确性、检索质量、执行成功率和安全边界。
- Hugging Face 课程最终项目涉及 GAIA，Datawhale 课程覆盖 BFCL、GAIA、LLM Judge、Win Rate，适合迁移到本知识库的评估体系。

## 评估对象
- Prompt：是否稳定遵守格式、边界和风格。
- Tool Calling：是否选对工具、参数是否正确、错误处理是否合理。
- RAG：是否召回正确资料、答案是否忠于引用。
- Planning：计划是否可执行、步骤是否完整、是否有验收条件。
- Safety：是否拒绝越权请求、是否触发人工确认。
- Product：用户任务是否完成、成本和延迟是否可接受。

## Harness 设计
- 固定测试集：覆盖正常、边界、恶意、长上下文、工具失败等场景。
- 可重复执行：固定模型版本、Prompt 版本、工具模拟结果。
- 自动评分：规则校验、精确匹配、Schema 校验、LLM Judge。
- 人工复核：对高风险或主观任务抽样审核。
- 回归对比：Prompt、模型、工具或检索策略变更后自动比较。

## 工程化理解
- 没有评估集的 Prompt 优化基本是在凭感觉调参。
- Agent 的每个关键模块都应该能单独评估。
- 评估结果要和 Trace 关联，才能定位失败原因。

## 后续需要补充的知识点清单
- BFCL、GAIA、LLM Judge 的使用方式
- Agent 评估集模板
- 回归评估报告格式

## 相关笔记链接
- [[05-RAG评估与工程化|RAG评估与工程化]]
- [[02-Reasoning与Reflection|Reasoning与Reflection]]
- [[04-模型选择与模型路由|模型选择与模型路由]]
- [[03-Observability与Tracing|Observability与Tracing]]

## TODO
- [ ] 建立 Agent 评估用例模板
- [ ] 补充 Harness 目录结构

