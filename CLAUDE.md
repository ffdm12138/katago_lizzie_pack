# katago_lizzie_pack — 项目说明

## 仓库地址
- **GitHub**: `https://github.com/ffdm12138/katago_lizzie_pack.git`
- **本地路径**: `c:\1\katago_win64`

## 项目概述

Lizzie YZY v2.5.3 + KataGo 围棋 AI Windows 整合包。
解压即用，包含多引擎（CUDA/TensorRT/OpenCL/Eigen）、棋盘识别、主题、音效等完整组件。

## 环境说明

- **Shell**: 本机使用 Git Bash（POSIX），而非 cmd.exe 或 PowerShell
- **PowerShell 7**: 已安装，位于 `pwsh`，必要时优先使用 PowerShell 7
- **Python**: 可用 `python` 命令
- **GitHub CLI**: `gh` 已登录授权

## 目录结构

```
katago_win64/
├── config.txt              # Lizzie YZY 主配置（引擎路径、UI、分析参数）
├── persist                 # 界面布局持久化状态
├── dignostic.bat           # 引擎诊断脚本
├── test_commands.txt       # GTP 测试命令
├── .gitignore              # 排除大型二进制文件
├── README.md               # 项目说明
│
├── scripts/                # 工具脚本
│   ├── pack_git.py         #   打包 git 跟踪文件 → katago_lizzie_pack_git.zip
│   └── pack_full.py        #   打包全部文件（含引擎）→ katago_lizzie_pack_full.zip
│
├── katago_configs/         # KataGo 核心配置
│   ├── default_gtp.cfg     #   对弈模式配置（6线程，中国规则）
│   ├── analysis.cfg        #   分析模式配置（6×6线程）
│   └── estimate.cfg        #   形势判断配置（1线程）
│
├── katago_cuda/            # KataGo v1.16.4 CUDA 后端
├── katago_tensorRT/        # KataGo v1.16.4 TensorRT 后端（默认引擎）
├── katago_opencl/          # KataGo v1.16.4 OpenCL 后端
├── katago_eigen/           # KataGo 纯 CPU 版
├── katago_eigen_avx2/      # KataGo CPU AVX2 版
│
├── weights/                # 神经网络权重（gitignored，需自行下载）
│   ├── kata1-zhizi-b28c512nbt-muonfd2.bin.gz    # 28B 259MB
│   └── kata1-zhizi-b40c768nbt-fdx6d.bin.gz      # 40B 824MB
│
├── readboard/              # 棋盘识别工具（OpenCV .NET）
├── readboard_java/         # 棋盘识别工具（Java BoofCV 版）
├── readboard_boofcv_config.txt
│
├── theme/                  # 6 套棋盘/棋子/背景主题
├── sound/                  # 落子/提子音效
├── 说明文档/               # 中文说明与更新日志
│
├── jre/                    # Java 17 运行时（gitignored）
├── jcef-bundle/            # 内置浏览器（gitignored）
├── ZenEstimate/            # 形势判断（Python 2.7 旧版）
├── clockHelper/            # 对局计时辅助
├── KataGoData/             # 引擎缓存（gitignored）
├── gtp_logs/               # 通信日志（gitignored）
├── save/                   # 存档（gitignored）
│
├── Lizzieyzy-2.5.3-win64.exe
├── Lizzieyzy(仅在显示异常时尝试)-win64.exe
├── lizzie-yzy2.5.3-shaded.jar
└── 两个 bat 启动器
```

## 打包脚本

```bash
# 轻量包 — 仅 git 跟踪的文件（配置/文档/主题/音效）
python scripts/pack_git.py

# 完整包 — 项目全部文件（补上权重即可解压即用）
python scripts/pack_full.py
```

## 引擎预设（config.txt）

6 组预设，默认引擎索引 2（28B TensorRT）：

| 索引 | 名称 | 权重 | 后端 |
|------|------|------|------|
| 0 | KataGo-2026-03-22-28B(OpenCL) | 28B | OpenCL |
| 1 | KataGo-2026-03-22-28B(CUDA) | 28B | CUDA |
| **2** | **KataGo-2026-03-22-28B(TensorRT)** | **28B** | **TensorRT（默认）** |
| 3 | KataGo-2026-05-02-40B(OpenCL) | 40B | OpenCL |
| 4 | KataGo-2026-05-02-40B(CUDA) | 40B | CUDA |
| 5 | KataGo-2026-05-02-40B(TensorRT) | 40B | TensorRT |

## 硬件信息

- GPU: NVIDIA GeForce RTX 4070 Laptop GPU
- CPU: 6+ 搜索线程
- 已有 OpenCL 调优和 TensorRT 缓存

## 许可证

| 组件 | 许可证 |
|------|--------|
| yzyray/lizzieyzy | GPL-3.0 |
| featurecat/lizzie | GPL-3.0 |
| lightvector/KataGo | MIT |

## 维护习惯

- 大型二进制（权重/引擎 DLL/JRE/JAR）通过 .gitignore 排除
- 配置文件、主题、音效、文档都在版本控制中
- 更新引擎或权重后记得记录变更
