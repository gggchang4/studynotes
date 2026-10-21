---
id: "AI-02-06"
type: topic
status: framework
layer: "主干"
kind: "框架"
sources: ["T09","T01"]
code_status: not-added
diagram_status: planned
---

# scikit-learn与Pipeline

> [!info] 框架，待扩写
> 已确定范围、提纲和资料入口。正文推导、代码、论文精读与配图尚未展开。

[[AI/00-知识库总览|总览]] · [[AI/01-笔记编写约束|编写约束]] · [[AI/02-学习资料与论文索引|资料与论文]] · [[AI/02-数据与机器学习基础/00-模块索引|模块索引]]

## 本篇范围

如何把预处理、模型训练与评估组织成一致且避免泄漏的流水线？

**前置知识：** [[AI/01-数学与编程基础/08-科学计算与可视化|科学计算与可视化]]、[[AI/02-数据与机器学习基础/01-数据理解与特征工程|数据理解与特征工程]]、[[AI/02-数据与机器学习基础/02-数据划分与数据泄漏|数据划分与数据泄漏]]

## 内容提纲

- **scikit-learn**：scikit-learn 的 Estimator、fit、predict、transform 接口；Pipeline、ColumnTransformer、交叉验证与参数搜索；模型保存、加载与预处理对象保存。

## 后续正文重点

- 对应 fit、transform、predict 的职责展示完整调用路径。
- 说明 ColumnTransformer、交叉验证与保存预处理器的关系。

## 学习资料与论文

| 类型 | 入口 | 具体阅读内容 |
| --- | --- | --- |
| 主教材/教程 | [T09 · scikit-learn 用户指南](https://scikit-learn.org/stable/user_guide.html) | Pipelines and composite estimators；Model persistence |
| 补充/实现 | [T01 · 吴恩达机器学习专项](https://www.coursera.org/specializations/machine-learning-introduction) | 课程1：NumPy 与 scikit-learn 实现入口 |

本篇以教材与官方资料为主，暂不强配原始论文。教程当前核对公开目录或页面入口；详细书目、版次和证据范围见 [[AI/02-学习资料与论文索引|资料与论文索引]]。

## 教学图示设计

拟配：训练时 fit 与推理时 transform/predict 的双路径。

当前为图示设计，尚未生成本篇配图；扩写时按 [[AI/01-笔记编写约束#8. 教学配图|配图约束]] 选择素材或制作、插入并验证。
