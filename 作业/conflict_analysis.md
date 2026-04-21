# 依赖冲突分析
## 系统信息
OS: Ubuntu 22.04 LTS
Python: 3.8 (conda环境)
硬件: CPU only / NVIDIA GPU

## 4个核心冲突
### 1. sklearn==0.0 无效包冲突
根因：sklearn 不是真实包，是 scikit-learn 的别名，PyPI 没有 0.0 版本，直接安装失败。
类型：包名错误 + 无效版本。

### 2. torch + torchvision CUDA/版本不匹配
根因：torch=2.0.0+cu117 搭配 torchvision=0.15.1+cu118，CUDA 版本不一致，且版本强绑定不兼容。
类型：包间依赖冲突。

### 3. Python 版本冲突
根因：conda 环境是 Python3.8，文件里写 python==3.10，pip 无法修改 conda 的核心 Python 版本。
类型：Python 版本不兼容。

### 4. conda 与 pip 解析差异
根因：conda 管理系统依赖（CUDA/Python），pip 只管理 Python 包；混装带 CUDA 后缀的 torch 会导致依赖解析失败。
类型：工具解析机制冲突。
