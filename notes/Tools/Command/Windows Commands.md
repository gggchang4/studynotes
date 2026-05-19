---
title: Windows 常用命令
aliases:
  - Windows Commands
  - Windows 命令速查
  - PowerShell 常用命令
tags:
  - tools/command
  - windows
  - powershell
  - cmd
  - cheatsheet
created: 2026-05-20
updated: 2026-05-20
---

# Windows 常用命令

> [!info] 使用场景
> 这篇笔记以 **Windows Terminal + PowerShell** 为主，同时保留常见 CMD 命令。日常使用优先记 PowerShell；遇到旧教程、批处理脚本或系统修复时再切到 CMD。

相关笔记：[[Linux Commands]] | [[Mac Commands]] | [[Termimal & Shell Tools]] | [[WSL]] | [[SSH]]

## Windows 终端与 Shell 选择

> [!note] 先分清两个概念
> **Terminal** 是承载命令行界面的窗口，例如 Windows Terminal、WezTerm；**Shell** 是解释命令的程序，例如 PowerShell、CMD、bash、zsh。

### 流行终端工具

| 工具 | 适合谁 | 特点 | 优点 | 不足 |
| --- | --- | --- | --- | --- |
| Windows Terminal | 大多数 Windows 用户 | 微软官方、标签页、分屏、配置文件、WSL 集成 | 原生体验好，配置简单，和 PowerShell / WSL 配合自然 | SSH 主机管理能力不如专门客户端 |
| WezTerm | 喜欢跨平台和可配置的人 | GPU 渲染、Lua 配置、跨平台、支持多路复用和 SSH 域 | 配置可版本化，Windows/macOS/Linux 体验一致 | Lua 配置有学习成本 |
| Tabby | 经常连服务器的人 | 图形化配置、本地 Shell、SSH/SFTP 配置管理 | SSH 连接管理直观，适合多服务器 | 比轻量终端更重 |
| Alacritty | 追求极简和速度的人 | GPU 渲染、配置文件驱动 | 启动快、干净、稳定 | 默认不带标签页/分屏/SSH 管理 |
| Warp | 想要现代交互和 AI 辅助的人 | 命令块、补全、工作流、AI 功能 | 学习和回看命令方便 | 部分功能依赖账号或云服务，隐私要求高时需谨慎 |

### 常用 Shell

| Shell | 适合场景 | 优点 | 不足 |
| --- | --- | --- | --- |
| PowerShell 7 | Windows 日常开发、系统管理、跨平台脚本 | 对象管道强，Windows 管理能力好，跨平台 | 和 Bash 脚本语法不同 |
| Windows PowerShell 5.1 | 旧系统脚本兼容 | 系统自带，兼容老脚本 | 版本旧，跨平台能力弱 |
| CMD | 旧批处理、系统修复、兼容老教程 | 几乎所有 Windows 都有 | 交互和脚本能力弱 |
| Git Bash | Git、Unix 风格命令、轻量 Bash 环境 | 自带常见 GNU 工具，适合照着 Linux 教程练习 | Windows 路径和权限有时会绕 |
| WSL bash/zsh/fish | Linux 开发、服务器环境模拟 | 接近真实 Linux，适合 Node/Python/C/C++/Docker 开发 | Windows/WSL 文件系统互操作要注意性能 |

### 安装建议

```powershell
winget install Microsoft.PowerShell
winget install Microsoft.WindowsTerminal
winget install wez.wezterm
winget install Git.Git
winget install Eugeny.Tabby
```

> [!tip] 我的推荐组合
> 普通 Windows 开发：`Windows Terminal + PowerShell 7 + Git Bash`。需要 Linux 环境：加上 `WSL + Ubuntu + zsh`。经常连接很多服务器：再考虑 `Tabby` 或 `WezTerm`。

### VSCode 集成

VSCode 的内置终端不等于外部终端程序，它会直接启动某个 Shell。常用入口：

- `Ctrl + Shift + P` -> `Terminal: Select Default Profile`
- `Ctrl + \`` 打开/关闭内置终端
- 终端右上角下拉菜单可以切换 PowerShell、CMD、Git Bash、WSL

`settings.json` 示例：

```json
{
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "source": "PowerShell",
      "args": ["-NoLogo"]
    },
    "Git Bash": {
      "path": "C:\\Program Files\\Git\\bin\\bash.exe"
    },
    "Ubuntu (WSL)": {
      "path": "wsl.exe",
      "args": ["-d", "Ubuntu"]
    }
  }
}
```

常见搭配：

| 任务 | VSCode 里推荐用法 |
| --- | --- |
| Windows 脚本和系统命令 | 内置终端选择 PowerShell |
| Git 和轻量 Linux 命令 | 内置终端选择 Git Bash |
| Linux 项目开发 | 使用 `Remote - WSL` 打开项目，让终端运行在 WSL 内 |
| 远程服务器开发 | 使用 `Remote - SSH`，远程终端会在服务器上运行 |

## 快速索引

| 我想做什么 | PowerShell 推荐命令 | CMD 常见命令 |
| --- | --- | --- |
| 查看当前位置 | `Get-Location` / `pwd` | `cd` |
| 列出文件 | `Get-ChildItem` / `ls` | `dir` |
| 切换目录 | `Set-Location <路径>` / `cd <路径>` | `cd <路径>` |
| 创建目录 | `New-Item -ItemType Directory <目录>` / `mkdir <目录>` | `mkdir <目录>` |
| 查看文件内容 | `Get-Content <文件>` / `cat <文件>` | `type <文件>` |
| 复制文件 | `Copy-Item <源> <目标>` | `copy <源> <目标>` |
| 移动或重命名 | `Move-Item <源> <目标>` | `move <源> <目标>` / `ren` |
| 删除文件 | `Remove-Item <文件>` | `del <文件>` |
| 查看帮助 | `Get-Help <命令> -Examples` | `<命令> /?` |
| 找命令位置 | `Get-Command <命令>` | `where <命令>` |

> [!tip] PowerShell 心法
> PowerShell 的管道传递的是“对象”，不是普通文本。比如 `Get-Process | Sort-Object CPU -Descending` 会按进程对象的 CPU 字段排序，这和 CMD / Bash 的文本管道思路不一样。

## 目录与文件

### 位置与导航

```powershell
pwd
Get-Location
cd C:\Users
cd ..
cd ~
Push-Location C:\Windows
Pop-Location
explorer .
```

| 命令 | 用法 | 说明 |
| --- | --- | --- |
| `pwd` | `pwd` | 查看当前目录 |
| `cd` | `cd D:\Projects` | 切换目录 |
| `cd ..` | `cd ..` | 返回上一级 |
| `cd ~` | `cd ~` | 回到用户主目录 |
| `Push-Location` | `Push-Location <路径>` | 进入目录并记录原位置 |
| `Pop-Location` | `Pop-Location` | 回到上一个 `Push-Location` 记录的位置 |
| `explorer .` | `explorer .` | 用文件资源管理器打开当前目录 |

### 列出与查看

```powershell
Get-ChildItem
Get-ChildItem -Force
Get-ChildItem -Recurse -Filter "*.md"
Get-ChildItem | Sort-Object LastWriteTime -Descending
Get-Content .\README.md
Get-Content .\app.log -Tail 50 -Wait
```

| 命令 | 用法 | 说明 |
| --- | --- | --- |
| `Get-ChildItem` | `Get-ChildItem` | 列出当前目录内容 |
| `Get-ChildItem -Force` | `ls -Force` | 显示隐藏文件 |
| `Get-ChildItem -Recurse` | `Get-ChildItem -Recurse -Filter "*.txt"` | 递归查找文件 |
| `Get-Content` | `Get-Content <文件>` | 查看文件内容 |
| `Get-Content -Tail` | `Get-Content app.log -Tail 100` | 查看文件末尾 |
| `Measure-Object` | `Get-Content a.txt | Measure-Object -Line` | 统计行数 |

### 创建、复制、移动、删除

```powershell
New-Item -ItemType File notes.md
New-Item -ItemType Directory logs
Copy-Item .\a.txt .\backup\a.txt
Copy-Item .\src .\backup -Recurse
Move-Item .\old.txt .\new.txt
Remove-Item .\temp.txt
Remove-Item .\dist -Recurse
```

| 命令 | 用法 | 说明 |
| --- | --- | --- |
| `New-Item` | `New-Item -ItemType File a.txt` | 创建文件 |
| `mkdir` | `mkdir logs` | 创建目录 |
| `Copy-Item` | `Copy-Item a.txt b.txt` | 复制文件 |
| `Move-Item` | `Move-Item a.txt archive\a.txt` | 移动或重命名 |
| `Remove-Item` | `Remove-Item a.txt` | 删除文件 |
| `Test-Path` | `Test-Path .\README.md` | 判断路径是否存在 |

> [!warning] 删除前先确认
> `Remove-Item -Recurse -Force` 会递归强制删除目录。对重要目录操作前，先用 `Get-ChildItem` 确认路径是否正确。

## 搜索与筛选

### 搜索文件名

```powershell
Get-ChildItem -Recurse -Filter "*.md"
Get-ChildItem -Recurse | Where-Object Name -like "*config*"
Get-ChildItem -Recurse | Where-Object Length -gt 10MB
```

### 搜索文件内容

```powershell
Select-String -Path .\*.md -Pattern "Obsidian"
Get-ChildItem -Recurse -Filter "*.md" | Select-String -Pattern "TODO"
Select-String -Path .\app.log -Pattern "error" -CaseSensitive
```

| 命令 | 用法 | 说明 |
| --- | --- | --- |
| `Select-String` | `Select-String -Path *.txt -Pattern "abc"` | 类似 `grep` |
| `Where-Object` | `... | Where-Object Length -gt 1MB` | 按条件过滤对象 |
| `Sort-Object` | `... | Sort-Object LastWriteTime` | 排序 |
| `Select-Object` | `... | Select-Object Name, Length` | 选择输出字段 |
| `Format-Table` | `... | Format-Table -AutoSize` | 表格显示 |

> [!tip] 推荐增强工具
> 如果安装了 [[Termimal & Shell Tools]] 里的 `ripgrep`，搜索文本可以直接用 `rg "关键字"`，通常比系统自带搜索更快。

## 系统信息与进程

### 系统信息

```powershell
Get-ComputerInfo
systeminfo
Get-Date
whoami
$PSVersionTable
```

| 命令 | 说明 |
| --- | --- |
| `Get-ComputerInfo` | 查看系统、硬件、Windows 版本等信息 |
| `systeminfo` | CMD 风格的系统信息汇总 |
| `whoami` | 查看当前用户 |
| `$PSVersionTable` | 查看 PowerShell 版本 |
| `Get-Date` | 查看当前时间 |

### 进程管理

```powershell
Get-Process
Get-Process chrome
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Stop-Process -Name notepad
Stop-Process -Id 1234 -Force
```

| 命令 | 用法 | 说明 |
| --- | --- | --- |
| `Get-Process` | `Get-Process` | 查看进程 |
| `Stop-Process` | `Stop-Process -Id <PID>` | 结束进程 |
| `tasklist` | `tasklist` | CMD 查看进程 |
| `taskkill` | `taskkill /PID <PID> /F` | CMD 强制结束进程 |

### 服务管理

```powershell
Get-Service
Get-Service | Where-Object Status -eq "Running"
Start-Service <服务名>
Stop-Service <服务名>
Restart-Service <服务名>
```

## 网络与远程

### 网络诊断

```powershell
ipconfig
ipconfig /all
Get-NetIPConfiguration
ping github.com
tracert github.com
nslookup github.com
Test-NetConnection github.com -Port 443
```

| 命令 | 说明 |
| --- | --- |
| `ipconfig` | 查看 IP、网关、DNS 等信息 |
| `ping <域名>` | 测试网络连通性 |
| `tracert <域名>` | 查看网络路由路径 |
| `nslookup <域名>` | 查询 DNS 解析 |
| `Test-NetConnection <主机> -Port <端口>` | 测试端口是否可连接 |

### 端口与连接

```powershell
netstat -ano
netstat -ano | findstr :3000
Get-NetTCPConnection -LocalPort 3000
Get-NetTCPConnection -State Listen
```

### HTTP 请求

```powershell
Invoke-WebRequest https://example.com
Invoke-RestMethod https://api.github.com
curl.exe -I https://example.com
```

> [!note] `curl` 在 Windows 上的小坑
> PowerShell 里 `curl` 可能是 `Invoke-WebRequest` 的别名。需要使用真正的 curl 时，写成 `curl.exe` 更稳。

### SSH 与文件传输

```powershell
ssh user@example.com
ssh -p 2222 user@example.com
scp .\file.txt user@example.com:/home/user/
scp user@example.com:/home/user/file.txt .
```

更多内容见：[[SSH]]

## 压缩、哈希与编码

```powershell
Compress-Archive -Path .\src -DestinationPath .\src.zip
Expand-Archive -Path .\src.zip -DestinationPath .\src
Get-FileHash .\file.iso -Algorithm SHA256
certutil -hashfile .\file.iso SHA256
Get-Content .\a.txt | Set-Content .\b.txt -Encoding utf8
```

| 命令 | 说明 |
| --- | --- |
| `Compress-Archive` | 压缩为 zip |
| `Expand-Archive` | 解压 zip |
| `Get-FileHash` | 计算文件哈希 |
| `Set-Content -Encoding utf8` | 以指定编码写入文本 |

## 环境变量与配置

```powershell
Get-ChildItem Env:
$env:Path
$env:NODE_ENV = "development"
notepad $PROFILE
Test-Path $PROFILE
New-Item -ItemType File -Path $PROFILE -Force
```

| 命令 | 说明 |
| --- | --- |
| `Get-ChildItem Env:` | 查看环境变量 |
| `$env:变量名` | 读取或临时设置环境变量 |
| `$PROFILE` | PowerShell 配置文件路径 |
| `notepad $PROFILE` | 编辑 PowerShell 启动配置 |

永久设置用户级环境变量：

```powershell
[Environment]::SetEnvironmentVariable("变量名", "变量值", "User")
```

## 软件包与系统维护

### winget

```powershell
winget search vscode
winget install Microsoft.VisualStudioCode
winget list
winget upgrade
winget upgrade --all
winget uninstall <软件名>
```

### 系统修复

```powershell
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
chkdsk C: /scan
```

> [!warning] 系统维护命令
> `sfc`、`DISM`、`chkdsk` 通常需要管理员权限。执行前关闭重要程序，笔记本最好接入电源。

## 权限与管理员操作

```powershell
Start-Process powershell -Verb RunAs
whoami /groups
whoami /priv
icacls .\file.txt
takeown /F .\locked.txt
```

| 命令 | 说明 |
| --- | --- |
| `Start-Process ... -Verb RunAs` | 以管理员身份启动程序 |
| `icacls` | 查看或修改文件权限 |
| `takeown` | 获取文件所有权 |
| `Get-ExecutionPolicy` | 查看脚本执行策略 |
| `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` | 允许当前用户运行本地脚本 |

## 常见任务配方

### 找出当前目录最大的 10 个文件

```powershell
Get-ChildItem -File -Recurse |
  Sort-Object Length -Descending |
  Select-Object -First 10 FullName, Length
```

### 查看最近修改的文件

```powershell
Get-ChildItem -Recurse |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 20 FullName, LastWriteTime
```

### 查找占用端口的进程并结束

```powershell
Get-NetTCPConnection -LocalPort 3000
Get-Process -Id <OwningProcess>
Stop-Process -Id <PID>
```

CMD 版本：

```cmd
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

### 监控日志新增内容

```powershell
Get-Content .\app.log -Tail 100 -Wait
```

### 批量查看 Markdown 文件中的关键词

```powershell
Get-ChildItem -Recurse -Filter "*.md" | Select-String -Pattern "TODO"
```

## CMD 兼容速查

| CMD 命令 | 说明 | PowerShell 替代 |
| --- | --- | --- |
| `dir` | 列出目录 | `Get-ChildItem` |
| `type file.txt` | 查看文件 | `Get-Content file.txt` |
| `copy a b` | 复制 | `Copy-Item a b` |
| `move a b` | 移动 | `Move-Item a b` |
| `del file.txt` | 删除文件 | `Remove-Item file.txt` |
| `rmdir /s dir` | 删除目录 | `Remove-Item dir -Recurse` |
| `cls` | 清屏 | `Clear-Host` |
| `where python` | 查找可执行文件 | `Get-Command python` |
| `robocopy src dst /MIR` | 镜像复制目录 | 仍推荐用 `robocopy` |

> [!warning] 高风险命令清单
> 执行这些命令前一定确认路径和目标：`Remove-Item -Recurse -Force`、`del /s /q`、`rmdir /s /q`、`format`、`diskpart`、`robocopy /MIR`、`takeown`、`icacls /grant`。
