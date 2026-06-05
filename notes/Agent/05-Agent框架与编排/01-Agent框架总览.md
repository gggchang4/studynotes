# Agent框架总览

## 本笔记的学习目标
- 理解主流 Agent 框架的定位、适用场景和选型维度。

## 核心内容
- Agent 框架的价值在于降低模型调用、工具管理、状态编排、RAG 集成、可观测性和部署的复杂度。
- Hugging Face 课程重点覆盖 smolagents、LlamaIndex、LangGraph；Microsoft 课程使用 Microsoft Agent Framework 与 Azure AI Foundry；Datawhale 课程既讲框架实践，也讲自建 Agent 框架。
- 框架不是越重越好。学习阶段可以用轻量框架理解原理，生产阶段要关注可维护性、可观测性、权限、安全和团队熟悉度。

## 框架分类
- 轻量 Agent 框架：适合快速理解工具调用和 Agent 循环，例如 smolagents。
- RAG / 数据框架：适合文档连接、索引、检索和知识库问答，例如 LlamaIndex。
- 图编排框架：适合有状态、多步骤、可恢复流程，例如 LangGraph。
- 企业平台：适合托管运行、权限、观测和部署，例如 Azure AI Foundry Agent Service。
- 低代码编排平台：适合业务流程和快速搭建，例如 Dify、n8n。
- 多智能体框架：适合角色协作和任务分工，例如 AutoGen、CrewAI。

## 选型维度
- 是否需要复杂状态和循环控制。
- 是否以 RAG 为核心。
- 是否需要生产级可观测性和部署。
- 是否需要多智能体协作。
- 是否允许供应商锁定。
- 团队是否能维护框架抽象背后的底层逻辑。

## 工程化理解
- 框架能加速开发，但不能替代架构设计。
- 不理解 Agent 核心循环时直接上框架，容易把问题藏在抽象层里。
- 生产项目要优先评估框架的调试能力、日志结构、扩展性和失败恢复能力。

## 后续需要补充的知识点清单
- smolagents、LlamaIndex、LangGraph、Microsoft Agent Framework 对比
- LangChain、AutoGen、CrewAI、Dify、n8n 的调研要点
- 自研框架与现成框架的取舍

## 相关笔记链接
- [[03-参考课程映射|参考课程映射]]
- [[02-LangGraph|LangGraph]]
- [[03-Workflow与Graph编排|Workflow与Graph编排]]
- [[04-Agent通信协议与MCP|Agent通信协议与MCP]]
- [[01-Agent项目架构|Agent项目架构]]

## TODO
- [ ] 建立框架选型矩阵
- [ ] 补充每个框架的最小示例项目

