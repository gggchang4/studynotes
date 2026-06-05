# Prompt Engineering

## 本笔记的学习目标
- 掌握 Prompt 在 LLM 应用和 Agent 系统中的作用，并理解如何设计可维护、可评估的 Prompt。

## 核心内容
- Prompt 是模型执行任务的运行说明书，通常包含角色、目标、约束、输入信息、工具说明、输出格式和错误处理要求。
- System Prompt 负责长期稳定约束，User Prompt 负责当前任务，Developer/业务配置负责组织规则和策略。
- 好的 Prompt 不只是“说得清楚”，还要能被版本化、测试、复盘和迭代。
- 在 Agent 中，Prompt 还要说明工具使用规则、停止条件、反思策略、安全边界和失败时如何恢复。

## 设计原则
- 明确任务边界：说明 Agent 应该做什么，也说明不应该做什么。
- 分离稳定规则和动态上下文：长期规则放在固定 Prompt，临时信息放在上下文构造层。
- 使用结构化输出：重要任务尽量要求 JSON、Schema 或明确字段。
- 少用含糊形容词：把“详细”“准确”“专业”转成可检查标准。
- 用示例压缩歧义：复杂输出格式最好提供少量 Few-shot。
- 为失败设计 Prompt：说明工具失败、信息不足、冲突和低置信度时如何处理。

## 常见问题
- Prompt 太长导致核心指令被稀释。
- 把不可信网页、文档内容直接当成系统指令。
- 工具说明不清楚，导致参数生成错误。
- 输出格式只靠自然语言约束，没有校验和修复。
- 修改 Prompt 后没有评估，靠感觉判断效果。

## 后续需要补充的知识点清单
- Prompt 模板管理
- Few-shot 设计
- Prompt 版本评估
- Prompt Injection 防护

## 相关笔记链接
- [[03-上下文管理与结构化输出|上下文管理与结构化输出]]
- [[04-Tool Calling与外部系统|Tool Calling与外部系统]]
- [[02-Evaluation与Harness|Evaluation与Harness]]
- [[07-Agent安全与治理|Agent安全与治理]]

## TODO
- [ ] 建立 Agent System Prompt 模板
- [ ] 增加 Prompt 改动评估流程

