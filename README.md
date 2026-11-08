# LizzieYzy Next + KataGo 部署手册

用 LizzieYzy Next 上游整合包部署 Windows NVIDIA 围棋分析环境。这里公开部署步骤、权重更新规范和可复制的 PowerShell 验证命令。整合包、引擎、运行库和权重均从上游获取。

1. [部署 Windows NVIDIA 便携版](docs/deployment.md)。按固定版本下载、校验、解压并启动。
2. [更新与回滚 KataGo 权重](docs/weight-updates.md)。按模型原名校验文件，试跑成功后在 LizzieYzy Next 切换。

复现基线为 LizzieYzy Next `next-2026-10-24.2` 的 NVIDIA CUDA 便携版，内置 KataGo `v1.18.2`。权重规范记录了经 CUDA 推理验证的 B11 Transformer 模型。

本仓库原创文档和命令采用 [MIT 许可](LICENSE)。上游组件和模型适用各自许可。[LizzieYzy Next](https://github.com/wimi321/lizzieyzy-next) · [KataGo](https://github.com/lightvector/KataGo) · [KataGo 权重许可](https://katagotraining.org/network_license/)
