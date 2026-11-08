# 部署 Windows NVIDIA 便携版

## 下载与校验

本方案面向 Windows x64 和 NVIDIA RTX 20/30/40/50 系列。使用兼容的 NVIDIA 驱动。完整便携包自带 Java 运行时、KataGo 和 CUDA/cuDNN 运行库。其他显卡与纯 CPU 的选包说明见上游。[LizzieYzy Next 安装指南](https://github.com/wimi321/lizzieyzy-next/blob/next-2026-10-24.2/docs/INSTALL.md)

从上游下载 `2026-10-24-windows64.nvidia.portable.zip`（`1,970,961,581` 字节）。以下 SHA-256 来自该发布资产的 GitHub 摘要。命令中的路径按实际位置替换。[固定版本 Release](https://github.com/wimi321/lizzieyzy-next/releases/tag/next-2026-10-24.2) · [NVIDIA 便携包下载](https://github.com/wimi321/lizzieyzy-next/releases/download/next-2026-10-24.2/2026-10-24-windows64.nvidia.portable.zip)

```powershell
$archive = Get-Item -LiteralPath 'C:\Downloads\2026-10-24-windows64.nvidia.portable.zip' -ErrorAction Stop
$expected = '31d5192cfe9bf788c15d215512f9580f80859653a57764fd1e6ecdeb5d66b3fd'
$hash = Get-FileHash -LiteralPath $archive.FullName -Algorithm SHA256 -ErrorAction Stop
if ($archive.Length -ne 1970961581 -or $hash.Hash -ne $expected) {
    throw '便携包校验失败，请重新下载。'
}
```

## 解压与启动

1. 把校验通过的 ZIP 解压到一个新的可写目录。进入同时包含 `.lizzie-portable` 和 `LizzieYzy Next NVIDIA.exe` 的目录，保留 `app/`、`runtime/` 与启动器的相对位置。
2. 启动 `LizzieYzy Next NVIDIA.exe`。在 **KataGo 一键设置** 中选择内置 CUDA 引擎。打开一盘 SGF，启用分析，确认能看到候选落点、访问数和胜率。
3. 需要复现本仓库验证过的模型时，按[权重规范](weight-updates.md)导入并切换。上游便携包会用随包默认模型完成初始配置。

可在便携根目录检查引擎。预期输出 `KataGo v1.18.2` 和 `Using CUDA backend`，该上游整合包的引擎构建来自 KataGo 提交 `47aadc08518b3e121f22539796c911002f699584`。[KataGo 源码](https://github.com/lightvector/KataGo/commit/47aadc08518b3e121f22539796c911002f699584)

```powershell
& '.\app\engines\katago\windows-x64\katago.exe' version
```

## 迁移与回退

- 从旧 Lizzie YZY 整合包迁移时，保留旧目录，按需导入 SGF，在 Next 中重新选择引擎与权重。
- 已使用 Next 便携版时，退出程序后备份原目录的 `user-data/`。在独立目录试用新版本，需要迁移设置时再复制备份，并检查引擎和权重的路径。回退时从原目录启动。
