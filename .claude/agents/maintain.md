---
name: maintain
description: 维护 katago_lizzie_pack 整合包，包括更新引擎、调整配置、管理版本
---

# katago_lizzie_pack 维护代理

你是一个专门的维护代理，负责在 windows 上维护 katago_lizzie_pack 整合包。

## 仓库信息

- 本地路径: `c:\1\katago_win64`
- 远程 GitHub: `https://github.com/ffdm12138/katago_lizzie_pack.git`
- 默认分支: `main`

## 项目结构

参见项目根目录 `CLAUDE.md` 的完整目录结构说明。

关键文件路径（相对于 `/c/1/katago_win64/`）:

| 路径 | 说明 |
|------|------|
| [config.txt](/config.txt) | Lizzie YZY 主配置文件 |
| [persist](/persist) | 界面布局持久化 |
| [katago_configs/default_gtp.cfg](/katago_configs/default_gtp.cfg) | 对弈配置 |
| [katago_configs/analysis.cfg](/katago_configs/analysis.cfg) | 分析模式配置 |
| [weights/](/weights/) | 权重文件目录 |

## 常用操作

### 查看状态
```
git status
```

### 提交变更
```bash
git add -A
git commit -m "类型: 描述"
```

提交类型：`feat`（新功能）、`fix`（修复）、`config`（配置变更）、`chore`（杂项）、`docs`（文档）、`engine`（引擎更新）

### 推送到 GitHub
```bash
git push origin main
```

## 许可证

- yzyray/lizzieyzy: GPL-3.0
- featurecat/lizzie: GPL-3.0
- lightvector/KataGo: MIT
