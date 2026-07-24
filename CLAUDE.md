# katago_lizzie_pack — 项目说明

## 仓库地址
- **GitHub**: `https://github.com/ffdm12138/katago_lizzie_pack.git`
- **Gitee**:  `https://gitee.com/adam121389/katago_lizzie_pack.git`
- **本地路径**: `c:\1\katago_win64`

## 项目概述

Lizzie YZY v2.5.3 + KataGo 围棋 AI Windows 整合包。
**本仓库为整合包发布仓库，不包含源码改动**——所有组件均直接使用上游官方发布版。
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
├── katago_cuda/            # KataGo v1.16.5 CUDA 后端
├── katago_tensorRT/        # KataGo v1.16.5 TensorRT 后端（某些显卡可能因 DLL 版本问题初始化失败，备选）
├── katago_opencl/          # KataGo v1.16.5 OpenCL 后端
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

# 完整包 — 全部文件（含引擎 DLL 和权重，解压即用）
python scripts/pack_full.py
```

## 引擎预设（config.txt）

6 组预设，默认引擎索引 1（28B CUDA）：

| 索引 | 名称 | 权重 | 后端 |
|------|------|------|------|
| 0 | KataGo-v1.16.5-28B(OpenCL) | 28B | OpenCL |
| 1 | KataGo-v1.16.5-28B(CUDA) | 28B | CUDA |
| 2 | KataGo-v1.16.5-28B(TensorRT) | 28B | TensorRT |
| 3 | KataGo-v1.16.5-40B(OpenCL) | 40B | OpenCL |
| 4 | KataGo-v1.16.5-40B(CUDA) | 40B | CUDA |
| 5 | KataGo-v1.16.5-40B(TensorRT) | 40B | TensorRT |

## 硬件信息

- GPU: NVIDIA GeForce RTX 4070 Laptop GPU（8 GB VRAM）
- CPU: 6+ 搜索线程
- 已有 OpenCL 调优和 TensorRT 缓存

## 引擎选择参考

| 引擎 | 推荐显卡 | 说明 |
|------|---------|------|
| **CUDA** | NVIDIA 任意显卡（GTX 7系+） | 兼容性最广，**默认引擎** |
| **TensorRT** | NVIDIA RTX 20系以上 | 性能最优，但需匹配 TRT DLL 版本 |
| **OpenCL** | 任意品牌显卡 | 跨平台通用 |
| **Eigen / AVX2** | 无独立显卡 | 纯 CPU 运算 |

### TensorRT DLL 匹配

KataGo 官方 Release zip 不含 `nvinfer*.dll`，这些 DLL 来自系统 NVIDIA 驱动或旧版 TensorRT SDK。
必须选择与当前 DLL 版本匹配的 Katago 构建：

| TRT DLL 版本 | Katago zip 文件名 |
|-------------|-------------------|
| TRT 8.x (`nvinfer.dll`) | `katago-v*-trt8.6.1-cuda12.1-*.zip` |
| TRT 10.2 (`nvinfer_10.dll`) | `katago-v*-trt10.2.0-cuda12.5-*.zip` |
| TRT 10.9 (`nvinfer_10.dll`) | `katago-v*-trt10.9.0-cuda12.8-*.zip` |

> **本机环境**：`nvinfer_10.dll` 为 TRT 10.2，使用 `v1.16.5-trt10.2.0-cuda12.5` 构建。
> 版本不对 → 静默崩溃无错误日志，用 `katago.exe version` 可以看到 "Using TensorRT backend" 确认成功。

## 权重下载

[katagotraining.org/networks/](https://katagotraining.org/networks/) — 官方权重列表

## 许可证

| 组件 | 许可证 |
|------|--------|
| yzyray/lizzieyzy | GPL-3.0 |
| featurecat/lizzie | GPL-3.0 |
| lightvector/KataGo | MIT |

## 维护习惯

- 大型二进制（权重/引擎 DLL/JRE/JAR）通过 .gitignore 排除
- 配置文件、主题、音效、文档都在版本控制中
- `config.txt` 不包含敏感凭据（贡献密码已清空）
- 更新引擎或权重后记得记录变更

## 更新 KataGo 引擎

KataGo 作为外部引擎被 Lizzie YZY 调用，本整合包不做源码级二次开发。
不建议克隆 KataGo 源码自行编译，推荐使用官方预编译版。

### 更新要点

> **每次更新引擎后必须清理缓存**，否则旧缓存与新引擎不兼容会导致初始化卡死或报错。

**清理缓存：** 删除 `KataGoData/` 目录（引擎会在下次启动时自动重建）。

**首次启动较慢：** TensorRT 和 OpenCL 引擎首次加载模型时需要编译优化内核（TensorRT 可能需要 **5-15 分钟**）。之后会生成缓存，后续启动就快了。

### 步骤

1. **下载**：去 [KataGo Releases](https://github.com/lightvector/KataGo/releases) 下载对应版本的预编译包（权重从 [katagotraining.org/networks/](https://katagotraining.org/networks/) 获取）：
   - `kamata-go-vX.Y.Z-cuda12.8-cudnn9.8-windows-x64.zip` → CUDA 版
   - `kamata-go-vX.Y.Z-trt10.8-cuda12.8-windows-x64.zip` → TensorRT 版
   - `kamata-go-vX.Y.Z-opencl-windows-x64.zip` → OpenCL 版
   - `kamata-go-vX.Y.Z-eigen-windows-x64.zip` → Eigen/CPU 版

2. **替换**：解压后覆盖对应 `katago_*/` 目录中的 `katago.exe` 和 DLL 文件

3. **清理缓存**：删除 `KataGoData/` 目录

4. **更新配置**：检查新版 KataGo 是否有新增/移除的配置参数，相应调整：
   - `katago_configs/default_gtp.cfg` — 对弈配置
   - `katago_configs/analysis.cfg` — 分析模式配置
   - `katago_configs/estimate.cfg` — 形势判断配置

5. **测试**：运行 `dignostic.bat` 或手动执行 `katago.exe benchmark` 验证

6. **提交**：更新 `.gitignore` 中引擎文件规则，提交变更记录
