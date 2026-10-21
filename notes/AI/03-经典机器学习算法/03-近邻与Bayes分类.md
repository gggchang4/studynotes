---
id: "AI-03-03"
type: topic
status: framework
layer: "主干"
kind: "算法"
sources: ["T04","T07","T09"]
code_status: not-added
diagram_status: planned
---

# 近邻与Bayes分类

> [!info] 框架，待扩写
> 已确定范围、提纲和资料入口。正文推导、代码、论文精读与配图尚未展开。

[[AI/00-知识库总览|总览]] · [[AI/01-笔记编写约束|编写约束]] · [[AI/02-学习资料与论文索引|资料与论文]] · [[AI/03-经典机器学习算法/00-模块索引|模块索引]]

## 本篇范围

相似性投票与概率推断如何形成不同类型的分类器？

**前置知识：** [[AI/01-数学与编程基础/04-概率统计与参数估计|概率统计与参数估计]]、[[AI/02-数据与机器学习基础/01-数据理解与特征工程|数据理解与特征工程]]

## 内容提纲

- **近邻方法**：K 近邻（KNN）、距离度量、维度灾难。
- **概率分类**：Bayes 决策、朴素 Bayes、条件独立假设；线性判别分析（LDA）与二次判别分析（QDA）；朴素 Bayes 的 Laplace 平滑。

## 后续正文重点

- 用小数据手算 KNN 与朴素 Bayes 的预测。
- 比较距离尺度、条件独立、LDA/QDA 假设与高维问题。

## 学习资料与论文

| 类型 | 入口 | 具体阅读内容 |
| --- | --- | --- |
| 主教材/教程 | [T04 · 统计学习导论 Python 版](https://www.statlearning.com/) | Classification |
| 补充/实现 | [T07 · CS229](https://cs229.stanford.edu/syllabus-autumn2018.html) | Gaussian Discriminant Analysis；Naive Bayes；Laplace Smoothing |
| 补充/实现 | [T09 · scikit-learn 用户指南](https://scikit-learn.org/stable/user_guide.html) | Nearest Neighbors；Naive Bayes；Discriminant Analysis |

本篇以教材与官方资料为主，暂不强配原始论文。教程当前核对公开目录或页面入口；详细书目、版次和证据范围见 [[AI/02-学习资料与论文索引|资料与论文索引]]。

## 教学图示设计

拟配：邻域分类、生成式分类分布与判别边界。

当前为图示设计，尚未生成本篇配图；扩写时按 [[AI/01-笔记编写约束#8. 教学配图|配图约束]] 选择素材或制作、插入并验证。
