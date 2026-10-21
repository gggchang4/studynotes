---
id: "AI-03-02"
type: topic
status: framework
layer: "主干"
kind: "算法"
sources: ["T01","T07","T09"]
code_status: not-added
diagram_status: planned
---

# Logistic回归、Softmax与广义线性模型

> [!info] 框架，待扩写
> 已确定范围、提纲和资料入口。正文推导、代码、论文精读与配图尚未展开。

[[AI/00-知识库总览|总览]] · [[AI/01-笔记编写约束|编写约束]] · [[AI/02-学习资料与论文索引|资料与论文]] · [[AI/03-经典机器学习算法/00-模块索引|模块索引]]

## 本篇范围

线性打分怎样转化为类别概率，决策边界与损失怎样对应？

**前置知识：** [[AI/03-经典机器学习算法/01-线性回归与正则化|线性回归与正则化]]、[[AI/01-数学与编程基础/06-信息论与概率损失|信息论与概率损失]]

## 内容提纲

- **分类线性模型**：Logistic 回归、Sigmoid、决策边界、二元交叉熵；Softmax 回归、多分类交叉熵；感知机与线性可分性。
- **广义线性模型**：广义线性模型的基本思想。

## 后续正文重点

- 推导二元交叉熵的梯度，并检查 logits 与概率的区别。
- 连接感知机、Softmax、多分类损失与 GLM；明确多项式特征并不使参数模型失去线性。

## 学习资料与论文

| 类型 | 入口 | 具体阅读内容 |
| --- | --- | --- |
| 主教材/教程 | [T01 · 吴恩达机器学习专项](https://www.coursera.org/specializations/machine-learning-introduction) | 课程1：Logistic Regression；课程2：多分类 |
| 补充/实现 | [T07 · CS229](https://cs229.stanford.edu/syllabus-autumn2018.html) | Logistic Regression、Perceptron、GLM |
| 补充/实现 | [T09 · scikit-learn 用户指南](https://scikit-learn.org/stable/user_guide.html) | Linear Models |

本篇以教材与官方资料为主，暂不强配原始论文。教程当前核对公开目录或页面入口；详细书目、版次和证据范围见 [[AI/02-学习资料与论文索引|资料与论文索引]]。

## 教学图示设计

拟配：决策边界、Sigmoid 与 Softmax 的输入输出。

当前为图示设计，尚未生成本篇配图；扩写时按 [[AI/01-笔记编写约束#8. 教学配图|配图约束]] 选择素材或制作、插入并验证。
