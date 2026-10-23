---
id: "AI-02-06"
type: topic
status: reviewed
layer: "主干"
kind: "框架"
sources: ["T09"]
code_status: syntax-checked-not-run
diagram_status: rendered-checked
updated: 2026-10-23
reviewed: 2026-10-23
---

# scikit-learn与Pipeline

[[AI/00-知识库总览|总览]] · [[AI/02-数据与机器学习基础/00-模块索引|模块索引]] · [[AI/02-学习资料与论文索引|资料索引]]

> [!abstract] 先抓住主线
> scikit-learn 用统一接口表达“学习状态”和“应用状态”。Pipeline 将需要拟合的预处理与最终模型连接成一个估计器，使交叉验证能够在每一折内重新拟合整个方案；ColumnTransformer 让不同类型的列采用不同变换。它们解决的是计算组织与拟合边界，不能自动判断特征是否偷看未来。

**前置：** [[AI/01-数学与编程基础/08-科学计算与可视化|数组和表格]]、[[AI/02-数据与机器学习基础/01-数据理解与特征工程|特征工程]]、[[AI/02-数据与机器学习基础/02-数据划分与数据泄漏|数据边界]]。

## 1. Estimator、Transformer、Predictor

Estimator（估计器）是具有 `fit` 等学习接口的对象，构造参数通常是超参数，拟合后属性常以 `_` 结尾。不是每个估计器都能预测，也不是每个变换都需要标签。

| 接口 | 输入与输出 | 状态含义 |
| --- | --- | --- |
| `fit(X, y)` | 从训练数据学习，通常返回自身 | 会建立或更新统计量、类别集合、模型参数 |
| `transform(X)` | 将输入映射到新表示 | 复用已学习状态；适用于 transformer |
| `fit_transform(X, y)` | 组合拟合与训练数据变换 | 不能用于独立验证/测试数据的重新拟合 |
| `predict(X)` | 输出数值或类别 | 复用最终模型状态 |
| `predict_proba(X)` | 输出各类概率估计 | 不是所有模型都支持；有概率不代表已校准 |
| `decision_function(X)` | 输出决策分数 | 不应直接解释成概率 |
| `score(X, y)` | 返回估计器约定的默认分数 | 不同模型默认含义可能不同 |

通常 $X$ 为 `(n_samples, n_features)`，单输出 $y$ 为 `(n_samples,)`；多输出和文本等有各自约定。`classes_` 等属性决定输出概率列与类别的对应关系，不能想当然把最后一列当“正类”而不检查标签定义。

`fit_transform` 对某些估计器可能有专门的交叉拟合语义，不能假设它总等于逐字执行一次 `fit` 再一次 `transform`。特别是目标编码，需要分别理解训练表示和推理表示。

## 2. Pipeline 的训练与推理两条路径

一个典型链条是“填补 → 标准化 → 分类”。调用 `pipe.fit(X_train,y_train)` 时，前面各阶段在训练输入上拟合并产生下一阶段的训练表示，最后一阶段拟合模型；调用 `pipe.predict(X_new)` 时，前面各阶段只 `transform`，最后一阶段 `predict`。

![整个预测方案的拟合、选择与应用边界](../assets/figures/learning-data-flow.svg)

这张原创图从更高层说明职责；Pipeline 封装的是其中“预处理与模型”的完整状态。具体接口语义见 [scikit-learn Pipelines §8.1.1](https://scikit-learn.org/stable/modules/compose.html)。

例如训练均值为 2，新输入 9 在标准差为 1 的坐标系中变成 7。Pipeline 要复用这个状态，而不是对新输入单独计算均值变成 0。模型系数是在训练坐标系下学到的；改变预处理也就是改变了模型输入。

> [!warning] 将预处理放进 CV 内部才形成完整边界
> 若先在全部开发数据 `scaler.fit_transform(X)`，再只对分类器做 CV，验证折已经影响标准化。应把包含 scaler 的整个 Pipeline 交给 CV。若输入中已包含签收后字段、重复记录跨组，Pipeline 本身无法修复。

## 3. ColumnTransformer 处理混合列

假设输入列为距离 `distance`、重量 `weight` 和运输方式 `mode`，目标为是否超时。数值列可填补后标准化，类别列可填补后 one-hot；变换后再沿特征轴拼接。

以下代码仅构造估计器，帮助对照对象结构。按 **scikit-learn 1.9.1 在线文档接口**核对，已作 Python 语法检查；当前环境没有安装 scikit-learn，**未执行导入、拟合或预测**。

```python
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

numeric = Pipeline([
    ("impute", SimpleImputer(strategy="median")),
    ("scale", StandardScaler()),
])
categorical = Pipeline([
    ("impute", SimpleImputer(strategy="most_frequent")),
    ("encode", OneHotEncoder(handle_unknown="ignore")),
])
features = ColumnTransformer([
    ("num", numeric, ["distance", "weight"]),
    ("cat", categorical, ["mode"]),
], remainder="drop")
classifier = Pipeline([
    ("features", features),
    ("model", LogisticRegression(C=1.0, max_iter=1000)),
])
```

`remainder='drop'` 明确丢弃未指定列，避免 ID 或标签意外进入输入。训练集有几个类别，编码器据此建立几个坐标；`handle_unknown='ignore'` 使新类别在相应编码块中变为全零，允许计算继续，但并不表示模型已学会该新类别。缺失类别处理与未知类别处理也不是同一问题。

输出可能是稀疏矩阵。稀疏表示保存非零项，适合 one-hot 和词袋；对稀疏矩阵减去均值可能使大量零变为非零，因此不能在未知数据结构上随意套用普通中心化。ColumnTransformer 的列选择、拼接与输出规则见 [官方 §8.1.4](https://scikit-learn.org/stable/modules/compose.html#columntransformer-for-heterogeneous-data)。

## 4. 参数搜索为什么需要克隆完整方案

嵌套参数名用 `步骤名__参数名` 表达，例如 `model__C` 控制 Logistic 模型的正则化参数，`features__num__impute__strategy` 控制数值填补策略。构造参数用于配置；已拟合的 `statistics_`、`mean_`、`coef_` 等则是数据学到的状态，不能混淆。

交叉验证与参数搜索会为各个候选/折建立独立的估计器副本，再在相应训练部分拟合。需要学习的中位数、均值、类别词表和模型参数因此都属于本折状态。使用相同的数据划分比较候选，有助于减少仅由划分差异造成的噪声。

下面是**流程伪代码**，并非可直接运行的数据实验：

```text
搜索器 = 指定 Pipeline、候选参数、评分函数、合理的 CV 划分
搜索器.fit(开发集输入, 开发集标签)
  每个候选、每折：克隆 Pipeline → 在训练折 fit → 在验证折评价
选择配置；按设定在全部开发数据 refit
最终方案.predict(独立测试输入)；最后才计算测试指标
```

`GridSearchCV` 的最佳 CV 分数来自选择过程，不是独立测试分数。`refit=True` 一般会用选中配置对传入的全部开发数据重新拟合；有些调用只返回分数或拟合后的折模型，不能假设任意 CV 函数都会自动给出一个最终全数据模型。详见 [[AI/02-数据与机器学习基础/05-验证、模型选择与实验可信度|嵌套验证与选择偏差]]。

## 5. 评分、类别顺序与预测输出

scikit-learn 的评分接口常使用“越大越好”的方向，因此某些损失的 scorer 名称带 `neg_`。负均方误差更接近 0 表示原始 MSE 更小；不能把负号直接当作程序错误。

离散预测、分数和概率要与指标要求匹配：Accuracy/F1 使用类别或阈值后的决策，ROC-AUC 使用连续分数，log loss 需要概率及明确的类别顺序。阈值是一个另外需要确定的决策层，不应以为 `predict_proba` 已替你完成所有代价权衡。

分组与时间划分要由调用者选对并提供必要的组/时间信息；仅指定一个整数 `cv` 不会自动理解样本的真实独立性。自定义转换器也应把可学习统计放在 `fit` 中，并在 `transform` 中复用；不能从全局变量或外部缓存偷读其他折。

## 6. 保存的是完整的预测含义

只保存线性模型系数而丢掉填补值、标准化均值、类别编码顺序与特征名单，会使恢复后的输入含义改变。通常需要保存整个已拟合 Pipeline，以及标签定义、输入 schema、依赖版本与数据处理约定。版本之间不保证任意序列化对象都兼容。

`pickle`/基于它的 `joblib` 等对象格式在加载时可能执行代码，只能用于可信来源；ONNX 等导出方式又受算子与估计器支持范围约束。这里的重点是模型表示与运行时的契约，不提供或加载外来模型文件。相关边界见 [scikit-learn Model persistence](https://scikit-learn.org/stable/model_persistence.html)。

**知识连接：** 本篇把数据边界和模型选择原则映射到接口。下一模块的 [[AI/03-经典机器学习算法/00-模块索引|经典算法]]会分别解释每种最终估计器内部在优化什么；部署时再由 [[AI/12-工程与部署/02-模型导出、量化、剪枝与蒸馏|导出与模型压缩]]补足跨运行时问题。

## 资料与验证范围

- **T09 · scikit-learn 用户指南，2026-10-23 stable 快照（页示 1.9.1）**：[Pipelines and composite estimators](https://scikit-learn.org/stable/modules/compose.html) 的 §8.1.1、§8.1.4；[Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) 的拟合边界；[Parameter search](https://scikit-learn.org/stable/modules/grid_search.html) 的搜索/refit；[Model persistence](https://scikit-learn.org/stable/model_persistence.html) 的保存与加载约束。相关正文已核对。

本篇 Python 块只通过语法检查；没有可报告的 scikit-learn 运行结果。以概念和对象状态讲解为主，没有为接口演示新增脚本、模型文件或实验目录。
