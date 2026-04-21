# dl-2026-01

## 题目名称

Conda 深度学习环境排障：定位依赖冲突并构建可复现环境

## 这是一道什么题

这道题主要考查：

- Miniconda / Anaconda 基础使用
- conda 环境创建、激活、导出与复现
- pip 与 conda 混装依赖的风险判断
- CUDA / PyTorch 版本匹配意识
- Python 版本与包版本兼容性判断
- 依赖冲突排查、修复与复盘能力

你需要根据故意写坏的 `requirements_broken.txt`部署环境，要求你找出冲突、解释原因、修复环境，并给出可复现方案。

## 任务背景

请你创建一个名为姓名简写（如张三的环境名为ZS）的独立 conda 环境。严禁使用 `venv`、`virtualenv`、系统 Python 全局环境完成本题。

本目录已提供故障文件：

- [requirements_broken.txt](./requirements_broken.txt)

该文件包含4类冲突，禁止删除所有版本号后无脑安装。你需要解释每个冲突为什么发生，并给出最小合理修复。

## 你的任务

### 1. 创建 conda 环境并复现失败，20 分

要求：

- 使用 conda 创建 环境
- 禁止使用 `venv`或全局python
- 尝试安装题目给出的 `requirements_broken.txt`
- 保存完整失败日志到 `logs/install_failed.log`
- 在报告中说明你的操作系统、Python 版本、是否有 GPU

评分：

- 正确使用 conda 创建隔离环境，5 分
- 明确没有使用 `venv` 或全局 Python，3 分
- 真实复现安装失败并截图，4 分
- 将失败输出记录日志，5 分
- 硬件与系统信息记录清楚，3 分

### 2. 逐条定位至少 4 个依赖问题，20 分

请编写 `conflict_analysis.md`，至少分析 4 个问题

评分：

- 至少定位 4 个真实问题，8 分
- 每个问题能解释根因，不只复制报错，6 分
- 能区分包名问题、Python 版本问题、包间依赖问题，4 分
- 能说明 conda 与 pip 解析差异，2 分

### 3. 设计并实现修复后的环境，20 分

你需要提交：

- `environment_fixed.yml`
- `requirements_fixed.txt`
- `check_env.py`

修复后的环境至少需要满足：

- 可以成功导入 `torch`、`torchvision`、`numpy`、`pandas`、`cv2`、`matplotlib`
- 可以运行 `check_env.py`
- `check_env.py` 输出 Python 版本、conda 环境名、PyTorch 版本、torchvision 版本、CUDA 可用性、GPU 名称或 `CPU only`
- 环境文件中不得包含个人绝对路径、大量无关包、完整本机环境快照

评分：

- 修复方案能成功安装，6 分
- `check_env.py` 输出完整，5 分
- conda 与 pip 分工合理，5 分
- 环境文件干净可迁移，4 分

### 4. 压轴：写出“最小修复”和“工程修复”两套方案，25 分

请提交 `fix_strategy.md`，同时给出两套方案：

- 最小修复：尽量少改动原始 `requirements_broken.txt`，让环境能装上并跑通，环境名为姓名简写-mini（如：ZS-mini）
- 工程修复：面向后续 YOLO / PyTorch 项目训练，整理一个更合理、更稳定的环境方案，环境名称为姓名简写-project

报告必须包含：

- 原始文件中每一处修改的理由
- 哪些包应该用 conda 安装，哪些包可以用 pip 安装
- 为什么不能使用 `sklearn==0.0`
- 为什么不能随意混用不匹配的 `torch` / `torchvision`
- 如果有 GPU，如何选择 CUDA 版本；如果没有 GPU，如何选择 CPU 版本

评分：

- 两套方案边界清楚，5 分
- 修改理由逐条具体，10 分
- conda / pip 分工合理，4 分
- GPU / CPU 选择逻辑正确，4 分
- 能总结避免同类问题的原则，2 分

### 5. 提交与 README，15 分

你需要提交：

- `check_env.py`
- `requirements_broken.txt`
- `requirements_fixed.txt`
- `environment_fixed.yml`
- `logs/install_failed.log`
- `conflict_analysis.md`
- `fix_strategy.md`
- `README.md`

评分：

- 文件齐全，5 分
- README 能让他人按步骤复现，5 分
- 命令、截图、日志组织清楚，5 分
