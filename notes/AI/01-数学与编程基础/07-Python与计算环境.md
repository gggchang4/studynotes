---
id: "AI-01-07"
type: topic
status: reviewed
layer: "主干"
kind: "工具"
sources: ["T10","T03"]
code_status: executed-cpu
command_status: illustrative-not-run
diagram_status: not-needed
updated: 2026-10-23
reviewed: 2026-10-23
---

# Python与计算环境

[[AI/00-知识库总览|总览]] · [[AI/01-数学与编程基础/00-模块索引|模块索引]] · [[AI/02-学习资料与论文索引|资料索引]]

> [!abstract] 先抓住主线
> 阅读机器学习代码时，先看数据怎样流动、状态保存在哪里、函数返回什么，再看语法。解释器决定运行哪一种 Python，环境决定可导入哪些依赖，设备决定计算与存储发生在哪里。随机种子只控制部分随机源，不能单独保证结果完全可复现。

**前置：** 无专题前置。本篇只覆盖理解后续 NumPy、scikit-learn、PyTorch 代码所需的 Python 知识；通用语法细节留给官方教程。

## 1. 用容器表示数据与配置

Python 是动态类型语言：名字绑定到对象，类型属于对象。`n = 3` 后再写 `n = '3'` 会把名字绑定到另一个对象，不会自动把字符串当数值。机器学习中还需区分 Python 整数、浮点数与数组库的 dtype，后者决定批量数据的存储与运算精度。

| 对象 | 典型用途 | 容易忽略的性质 |
| --- | --- | --- |
| `list` | 样本路径、变长记录、配置序列 | 可变；`b = a` 共享同一对象 |
| `tuple` | 一个样本的 `(x, y)`、形状 | 元组结构不可变，但其中可放可变对象 |
| `dict` | 名称到参数/指标/类别的映射 | 根据键访问，不应靠偶然顺序解释特征语义 |
| `set` | 去重后的 ID 集合 | 不保留样本重复次数，不是稳定的排序接口 |
| `str`、`Path` | 文本、文件路径 | 字符串不是文件内容，路径存在也不代表格式正确 |

列表推导式适合简短转换，如 `[float(v) for v in values]`。数值批量计算通常交给数组库；对每个元素写 Python 循环虽容易理解，但可能增加开销。先确保语义正确，再考虑向量化。

**共享状态例子：** `a = [1, 2]; b = a` 后执行 `b.append(3)`，`a` 也变成 `[1, 2, 3]`。`a.copy()` 只做浅拷贝，嵌套列表仍可能共享内部对象。数据预处理函数若悄悄原地修改输入，就会影响后续比较。

## 2. 函数定义计算，类保存需要复用的状态

函数通过参数接收输入，通过 `return` 输出结果；只 `print` 不返回的函数，返回值是 `None`。参数默认值在函数定义时求值，因此不要用 `cache=[]` 这样的可变默认参数积累样本；常用 `cache=None`，进入函数后再建立列表。

类（class）把状态和相关操作放在一起。实例方法的 `self` 指向当前对象；`__init__` 初始化状态。机器学习中的模型对象、优化器和预处理器都是这种组织方式。Python 的函数与类说明可对照 [官方教程第 4 章](https://docs.python.org/3.12/tutorial/controlflow.html) 与 [第 9 章](https://docs.python.org/3.12/tutorial/classes.html)。

下面用“减去训练均值”的一维预处理器说明为什么有些操作必须分为学习与应用两个阶段：

```python
# Python 3.12；仅标准库，无外部数据或文件写入
class Centerer:
    def __init__(self):
        self.mean_ = None

    def fit(self, values):
        if len(values) == 0:
            raise ValueError("training values must be non-empty")
        self.mean_ = sum(values) / len(values)
        return self

    def transform(self, values):
        if self.mean_ is None:
            raise RuntimeError("fit must be called first")
        return [float(v) - self.mean_ for v in values]

processor = Centerer().fit([1.0, 2.0, 6.0])
result = processor.transform([5.0])
print(result)  # [2.0]
```

训练输入均值是 3；新输入 5 减的是训练均值，所以输出 2。`transform` 没有根据新输入重新学习均值；否则模型的输入坐标系会随每批数据改变。返回 `self` 支持链式写法，名称末尾 `_` 只是这里沿用的已拟合属性约定，Python 不会强制它的含义。

> [!note] 先理解状态，再理解框架名字
> `fit`、`transform`、`predict` 是常见接口约定，不是 Python 语言关键字。神经网络的 `forward` 描述计算，`backward` 由自动微分构建的依赖执行，优化器再改参数；“调用了模型”不代表已经训练。见 [[AI/02-数据与机器学习基础/06-scikit-learn与Pipeline|Pipeline]] 与 [[AI/04-神经网络与PyTorch/05-PyTorch模型、数据与训练循环|PyTorch 训练循环]]。

## 3. 迭代器、生成器、模块与异常

`for batch in loader` 的核心是迭代协议：每次取得下一个元素，直到结束；数据不一定事先全部放在内存中。带 `yield` 的函数可以逐次产生数据，这有助于理解批量读取和数据流。生成器通常会消耗，不能假设重复遍历还能获得相同内容。

`import numpy as np` 把模块名绑定到当前命名空间。项目文件若叫 `numpy.py`、`torch.py` 或 `random.py`，可能遮蔽同名库。一个模块中顶层语句在导入时也会执行；脚本常用 `if __name__ == '__main__':` 区分直接运行与导入。

异常应帮助暴露输入、路径、维度与状态错误。`try/except` 应捕获预期的具体异常；把所有错误吞掉并继续输出零分，会把程序失败伪装成模型效果差。日志要说明发生在哪一步，但不要输出原始敏感数据。

文件读取还依赖当前工作目录和编码。`Path('data.csv')` 是相对工作目录，不一定相对脚本所在位置；读写中文 Markdown 或配置时显式指定 UTF-8。数据路径、模型路径与环境路径是三种对象，不能混作“Python 找不到文件”的同一个原因。

## 4. 解释器、环境、依赖与 Notebook 内核

同一台机器可以安装多个 Python。终端输入 `python`，由路径与当前环境决定调用哪一个；`pip` 也可能指向另一个安装。用 `python -m pip` 能明确让当前解释器执行其对应的 pip。虚拟环境主要隔离 Python 包，不会自动替你隔离操作系统驱动或 GPU 硬件。

下面是 **PowerShell 用法说明，未在本轮执行安装或创建环境**：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip --version
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"
```

这展示的是从指定解释器调用环境的方式。实际工程应在自己的代码目录创建环境，不把环境与数据集放进本笔记库。环境机制见 [Python 3.12 官方教程 §12](https://docs.python.org/3.12/tutorial/venv.html)。

Notebook 由内核执行 Python；终端激活某个环境，并不保证已经打开的 Notebook 使用同一内核。单元格还能保留过去的变量，重新排列代码却不重启内核可能隐藏依赖。理解实验时，要能辨认哪些变量由当前代码产生，哪些来自历史状态。

实验配置应区分可重复声明的设置与拟合后的状态：特征名单、模型种类、超参数、种子、数据版本和路径是配置；训练均值、类别词表、学得权重是结果状态。把二者明确记录，才能判断恢复运行时究竟重用了什么。调试时先定位第一次异常的输入、类型和形状，再检查数值范围；记录阶段与上下文通常比打印全部数组更有用。

## 5. CPU/GPU、内存与显存

CPU 与 GPU 是计算设备，系统内存与显存是数据存储位置。数据在 CPU 上不代表 GPU 能零成本直接计算；从 CPU 复制到 GPU 要付出传输时间，部分操作还需要同步。GPU 是否更快取决于计算规模、并行性、传输、内核开销和所用算子的支持。

数组的 dtype 决定单个元素大小。仅考虑数据本身，$B\times d$ 的 float32 输入需要 $4Bd$ 字节；训练还要保存参数、梯度、中间激活和优化器状态，因此不能只用模型权重大小估计所需显存。

安装某个 CUDA 相关包不自动证明驱动兼容、设备可访问或训练已实际使用 GPU。本笔记的数值示例只验证 CPU，设备和自动微分的细节放到 [[AI/04-神经网络与PyTorch/04-PyTorch张量与自动微分|PyTorch 张量与自动微分]]。

## 6. 随机性与可复现的含义

随机数通常来自伪随机数生成器。相同生成器、算法与状态在相同执行条件下可产生相同序列；Python `random`、NumPy 和深度学习框架可能分别维护随机状态。设置其中一个种子不会自动覆盖其余来源。

可复现还取决于数据版本、划分索引、预处理状态、依赖版本、设备、并行调度和确定性算法。多线程、GPU 归约及浮点运算顺序都可能改变末位数值。应区分“代码能够重新运行”“指标在合理波动范围内一致”“逐位相同”这三个不同目标。

**知识连接：** 本篇的状态、接口与环境概念支撑 [[AI/01-数学与编程基础/08-科学计算与可视化|科学计算]]；数据拟合范围连接 [[AI/02-数据与机器学习基础/02-数据划分与数据泄漏|数据泄漏]]；实验信息保存进入 [[AI/12-工程与部署/01-数据版本、实验管理与漂移|实验管理]]。

## 资料与验证范围

- **T10 · Python 官方教程，3.12 文档线**：[函数与控制流](https://docs.python.org/3.12/tutorial/controlflow.html)、[类](https://docs.python.org/3.12/tutorial/classes.html)、[虚拟环境](https://docs.python.org/3.12/tutorial/venv.html)，已读与本篇接口和环境说明直接相关的部分。
- **T03 · D2L 1.0.3**：[Installation](https://d2l.ai/chapter_installation/index.html) 与工具附录为补充入口；不据安装教程推断读者机器已有 GPU 环境。

上面的 `Centerer` 示例在 Python **3.12.14 / CPU** 实际运行，输出 `[2.0]`；环境安装命令仅作说明，未执行。没有新增环境目录或实验项目。
