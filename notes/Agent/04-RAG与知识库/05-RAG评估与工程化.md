# RAG评估与工程化

## 本笔记的学习目标
- 掌握 RAG 系统从效果评估到生产落地的关键问题和优化路径。

## 核心内容
- RAG 评估要拆成检索评估和生成评估，不要只看最终答案是否“像对的”。
- 检索评估关注是否召回正确片段、正确片段排第几、无关片段是否过多。
- 生成评估关注答案是否忠于上下文、是否有引用、是否遗漏、是否幻觉。
- Hugging Face 和 Datawhale 课程都涉及 GAIA、BFCL、LLM Judge、Win Rate 等评估思路，可迁移到 RAG 质量评估。

## 评估指标
- Recall@K：正确资料是否在前 K 个候选中。
- MRR / NDCG：正确资料排序是否靠前。
- Context Precision：上下文中无关内容比例。
- Faithfulness：答案是否被检索上下文支持。
- Answer Relevance：答案是否回答了用户问题。
- Citation Accuracy：引用是否指向正确来源。

## 工程化问题
- 数据更新：新增、修改、删除文档后索引如何同步。
- 权限过滤：不同用户只能检索有权限的资料。
- 索引重建：Embedding 模型、切分策略或元数据变化后如何重建。
- 缓存：常见查询、检索结果和生成结果如何缓存。
- 引用溯源：答案中必须保留来源、页码、段落或 URL。
- 监控：检索延迟、召回失败、空答案、用户反馈和成本。

## 优化路径
- 先检查文档解析和 Chunk，再检查 Embedding 和检索。
- 如果召回不到，优化切分、Query Rewrite、Hybrid Search。
- 如果召回到了但答案错，优化上下文构造、Prompt、引用规则和模型。
- 如果答案不稳定，建立固定评估集和回归测试。

## 后续需要补充的知识点清单
- RAG 评估集构建
- RAG 排障流程
- 权限过滤和数据同步方案

## 相关笔记链接
- [[01-RAG整体架构|RAG整体架构]]
- [[04-Retriever、Rerank与Query Rewrite|Retriever、Rerank与Query Rewrite]]
- [[02-Evaluation与Harness|Evaluation与Harness]]
- [[03-Observability与Tracing|Observability与Tracing]]

## TODO
- [ ] 建立 RAG 优化 Checklist
- [ ] 补充 RAG 回归评估模板

