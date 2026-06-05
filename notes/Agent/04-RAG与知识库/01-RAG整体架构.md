# RAG整体架构

## 本笔记的学习目标
- 理解 RAG 从文档入库、检索到生成答案的完整流程，以及它和 Agent 的关系。

## 核心内容
- RAG 是 Retrieval-Augmented Generation，通过检索外部知识来增强模型生成，解决私有知识、时效知识和可追溯引用问题。
- 一个标准 RAG 系统包含文档解析、清洗、Chunk 切分、Embedding、索引、检索、重排、上下文构造、生成和评估。
- Agentic RAG 是让 Agent 把检索作为工具使用，能根据任务动态决定查什么、查几次、是否改写 Query、是否调用其他工具。
- Hugging Face 课程有 Agentic RAG 实战，Microsoft 课程也把 Agentic RAG 作为独立主题。

## 基本流程
- Ingestion：读取文档、网页、数据库或业务知识。
- Parsing：解析 PDF、Markdown、HTML、表格、代码等格式。
- Chunking：按语义、标题、段落或固定窗口切分。
- Indexing：生成 Embedding，写入向量库或混合检索索引。
- Retrieval：根据用户问题召回候选片段。
- Rerank：对候选片段重新排序，保留最相关内容。
- Generation：把检索结果与问题一起交给模型生成答案。
- Evaluation：评估检索质量、答案质量、引用质量和幻觉率。

## 工程化理解
- RAG 的质量很大程度取决于数据处理，而不是只取决于向量数据库。
- 检索结果必须进入上下文预算，不能召回越多越好。
- 生产 RAG 要处理权限过滤、数据更新、索引重建、缓存、引用溯源和评估集。

## 后续需要补充的知识点清单
- Agentic RAG 与普通 RAG 的区别
- RAG 数据流架构图
- RAG 的最小实现方案

## 相关笔记链接
- [[02-文档解析与Chunk切分|文档解析与Chunk切分]]
- [[03-Embedding与向量数据库|Embedding与向量数据库]]
- [[04-Retriever、Rerank与Query Rewrite|Retriever、Rerank与Query Rewrite]]
- [[05-RAG评估与工程化|RAG评估与工程化]]
- [[02-RAG知识库问答Agent|RAG知识库问答Agent]]

## TODO
- [ ] 绘制 RAG 总体架构图
- [ ] 补充最小 RAG 项目流程

