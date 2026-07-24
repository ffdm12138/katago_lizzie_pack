# Lizzie YZY + KataGo Windows 整合包

[Lizzie YZY](https://github.com/yzyray/lizzieyzy) 是 [Lizzie](https://github.com/featurecat/lizzie) 的中文增强分支，集成了 [KataGo](https://github.com/lightvector/KataGo) 围棋 AI 引擎。
本仓库为 Windows 整合包发布仓库，**不包含源码改动**——所有组件均直接使用上游官方发布版，解压即用。

## 目录结构

| 目录/文件 | 说明 |
|-----------|------|
| [config.txt](config.txt) | Lizzie YZY 配置文件（引擎路径、UI 等） |
| [persist](persist) | 界面布局持久化状态 |
| [scripts/](scripts/) | 工具脚本（打包等） |
| [katago_configs/](katago_configs/) | KataGo 配置文件（对弈/分析/估计） |
| [katago_cuda/](katago_cuda/) | KataGo v1.16.5 CUDA 版引擎 |
| [katago_tensorRT/](katago_tensorRT/) | KataGo v1.16.5 TensorRT 版引擎 |
| [katago_opencl/](katago_opencl/) | KataGo v1.16.5 OpenCL 版引擎 |
| [katago_eigen/](katago_eigen/) | KataGo CPU 版引擎 |
| [katago_eigen_avx2/](katago_eigen_avx2/) | KataGo CPU+AVX2 版引擎 |
| [weights/](weights/) | 神经网络权重（需自行下载，已 gitignore） |
| [readboard/](readboard/) | 棋盘识别工具（OpenCV .NET 版） |
| [readboard_java/](readboard_java/) | 棋盘识别工具（Java BoofCV 版） |
| [theme/](theme/) | 棋盘/棋子/背景主题 |
| [sound/](sound/) | 落子音效 |
| [说明文档/](说明文档/) | 中文文档与更新日志 |

## 快速开始

1. 下载权重文件放入 `weights/` 目录：
   - [katagotraining.org/networks/](https://katagotraining.org/networks/)（官方权重列表）
   - 或 [KataGo Releases](https://github.com/lightvector/KataGo/releases)（随版本发布的权重）
2. 双击 `Lizzieyzy-2.5.3-win64.exe` 启动
3. 如无法打开，尝试 `bat启动器(exe无法打开时使用).bat`

## 打包发行

```bash
# 轻量包 — 仅 git 跟踪的文件（配置/文档/主题/音效）
python scripts/pack_git.py

# 完整包 — 全部文件（含引擎 DLL 和权重，解压即用）
python scripts/pack_full.py
```

## 引擎配置

[config.txt](config.txt) 中预置了 6 组引擎配置（28B/40B 权重 × OpenCL/CUDA/TensorRT），默认使用 **28B TensorRT**。

### 引擎选择指南

| 引擎 | 推荐显卡 | 说明 |
|------|---------|------|
| **TensorRT** | NVIDIA RTX 20系以上 | **性能最优**，NVIDIA 官方推理优化，对 RTX 30/40/50 系支持最好。默认引擎 |
| **CUDA** | NVIDIA 任意显卡（GTX 7系以上） | 兼容性最广，支持所有支持 CUDA 的 NVIDIA 显卡 |
| **OpenCL** | 任意品牌显卡（N/A/I 均可） | 跨平台通用，NVIDIA/AMD/Intel 显卡均可用，性能相对较低 |
| **Eigen / Eigen AVX2** | 无独立显卡 | 纯 CPU 运算，AVX2 版需要支持 AVX2 指令集的 CPU（Intel Haswell / AMD Excavator 以上） |

实测环境：**NVIDIA GeForce RTX 4070 Laptop GPU（8 GB VRAM）**，TensorRT 和 CUDA 表现最佳。

## 开源许可

本项目是以下开源组件的整合包，请遵守各自的许可证条款：

| 组件 | 仓库 | 许可证 | 说明 |
|------|------|--------|------|
| **Lizzie YZY** | [github.com/yzyray/lizzieyzy](https://github.com/yzyray/lizzieyzy) | **GPL-3.0** | GUI 前端（Lizzie 的中文增强分支） |
| **Lizzie**（上游） | [github.com/featurecat/lizzie](https://github.com/featurecat/lizzie) | **GPL-3.0** | Lizzie YZY 的上游项目 |
| **KataGo** | [github.com/lightvector/KataGo](https://github.com/lightvector/KataGo) | **MIT License** | AI 引擎（Copyright David J Wu） |

- **GPL-3.0**: 使用、修改、分发须保留版权声明和许可证文本，修改后的代码也必须以 GPL-3.0 发布。
- **MIT License**: 更宽松的许可，允许商业使用、修改和再分发，仅须保留版权声明。

## 维护说明

- **GUI**: Lizzie YZY v2.5.3（最后更新 2023-06-15，原作者 yzyray 已停止维护）
- **引擎**: KataGo v1.16.5（可手动升级至更新版本）
- **权重**: 需从社区下载最新权重自行替换

本仓库仅跟踪配置文件、文档和资源文件。大型二进制文件（引擎、DLL、权重、JRE、JAR）通过 [.gitignore](.gitignore) 排除。

> **安全提醒**：`config.txt` 不包含任何敏感凭据。贡献功能（KataGo 分布式训练）的用户名和密码已清空，使用前请自行注册并填写。

### 更新 KataGo 引擎

KataGo 作为外部引擎被 Lizzie YZY 调用，不建议克隆源码编译，推荐使用官方预编译版。

1. **下载**：去 [KataGo Releases](https://github.com/lightvector/KataGo/releases) 下载对应版本的预编译包（CUDA / TensorRT / OpenCL / Eigen）

2. **替换**：解压后覆盖对应 `katago_*/` 目录中的 `katago.exe` 和 DLL 文件

3. **更新配置**：检查新版 KataGo 参数变化，相应调整 `katago_configs/` 下的三个 `.cfg` 文件

4. **测试**：运行 `dignostic.bat` 或 `katago.exe benchmark` 验证

5. **提交**：记录变更并推送
