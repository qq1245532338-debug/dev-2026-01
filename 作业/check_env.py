import sys, os, torch, torchvision, numpy, pandas, cv2, matplotlib

def check():
    print("===== 环境检查完成 =====")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Conda环境: {os.environ.get('CONDA_DEFAULT_ENV')}")
    print(f"PyTorch: {torch.__version__}")
    print(f"TorchVision: {torchvision.__version__}")
    print(f"CUDA: 可用" if torch.cuda.is_available() else "CUDA: 不可用(CPU)")
    print("所有包导入成功！")

if __name__ == "__main__":
    check()
