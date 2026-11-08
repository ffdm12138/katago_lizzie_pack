# KataGo 权重更新规范

## 已验证基线

| 项目 | 值 |
| --- | --- |
| 模型文件 | `kata1-tf3-b11c768-s11003M-d5973M-7gres.bin.gz` |
| 文件大小 | `262,039,869` 字节 |
| SHA-256 | `93bdb63a3bfae4a70db0cb5265287495ecfc10b1ba1cc6814feeba1cdf055871` |
| 验证环境 | Windows x64，RTX 4070 Laptop GPU，KataGo `v1.18.2` CUDA |
| 验证结果 | 19×19 GTP 加载成功，`genmove` 返回合法落点 |

[KataGo 官方模型列表](https://katagotraining.org/networks/) · [下载基线模型](https://media.katagotraining.org/uploaded/networks/models/kata1/kata1-tf3-b11c768-s11003M-d5973M-7gres.bin.gz)

## 下载并验证

从官方模型列表选择 **Network File**，把 `.bin.gz` 下载到独立目录，保留原名。对压缩文件本身校验字节数和 SHA-256。下面以基线模型为例。

```powershell
$weight = Get-Item -LiteralPath 'C:\Downloads\kata1-tf3-b11c768-s11003M-d5973M-7gres.bin.gz' -ErrorAction Stop
$expected = '93bdb63a3bfae4a70db0cb5265287495ecfc10b1ba1cc6814feeba1cdf055871'
$hash = Get-FileHash -LiteralPath $weight.FullName -Algorithm SHA256 -ErrorAction Stop
if ($weight.Length -ne 262039869 -or $hash.Hash -ne $expected) {
    throw '权重校验失败，请检查文件名并重新下载。'
}
```

在同一 PowerShell 会话中进入便携根目录，再用内置 CUDA 引擎试跑。测试在临时目录内执行，使用 19 路、单线程和 8 次访问，便于确认模型能加载并完成推理。

```powershell
$engine = (Resolve-Path -LiteralPath '.\app\engines\katago\windows-x64\katago.exe').Path
$config = Join-Path (Split-Path -Parent $engine) 'default_gtp.cfg'
$scratch = New-Item -ItemType Directory -Path (Join-Path ([IO.Path]::GetTempPath()) "katago-gtp-$([guid]::NewGuid())")
$commands = '1 protocol_version', '2 boardsize 19', '3 clear_board', '4 play B D4', '5 genmove W', '6 quit'
Push-Location -LiteralPath $scratch.FullName
try {
    $commands | & $engine gtp -config $config -model $weight.FullName `
        -override-config 'homeDataDir=.,logDir=gtp_logs,numSearchThreads=1,maxVisits=8'
    if ($LASTEXITCODE -ne 0) { throw 'KataGo 试跑失败。' }
} finally {
    Pop-Location
}
```

通过条件为 `=1` 至 `=6` 都有成功响应，`=5` 后有合法坐标或 `pass`，进程正常退出。试跑日志位于 `$scratch.FullName` 下的 `gtp_logs/`，可在其中核对模型名和 CUDA 后端。

## 切换和回滚

1. 记录当前引擎和权重，保留旧模型。需要备份时先关闭程序，复制便携目录内的 `user-data/`。
2. 在 **KataGo 一键设置** 的权重管理中导入已验证的本地文件，选中该模型并应用到当前 CUDA 引擎。
3. 用同一盘 SGF 检查分析、落点和访问数，重启后确认仍在使用所选模型。出现加载失败、显存不足或分析异常时，选回原权重并重启引擎。程序无法打开时可退出后恢复 `user-data/` 备份。

维护者更新基线时，在同一次提交里记录官方文件名、下载地址、字节数、SHA-256、实际验证的 KataGo 版本与后端，以及试跑结果。以固定模型版本为准。评估搜索速度时，用相同后端、棋谱、访问预算和线程数对照旧模型。
