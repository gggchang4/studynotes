---
title: Terminal & Shell Tools
aliases:
  - Terminal Tools
  - Shell Tools
  - Termimal & Shell Tools
  - 终端工具
  - Shell 工具
tags:
  - tools/terminal
  - tools/shell
  - tools/network
  - vscode
  - cheatsheet
created: 2026-05-20
updated: 2026-05-20
---

# Terminal & Shell Tools

> [!info] 这篇笔记的定位
> 这里是终端、Shell、SSH、FTP/SFTP、VSCode 集成的总览入口。具体命令速查见 [[Windows Commands]]、[[Mac Commands]]、[[Linux Commands]]；远程连接和传输见 [[SSH]]、[[FTP]]。

## 概念速记

| 概念 | 是什么 | 例子 |
| --- | --- | --- |
| Terminal Emulator | 显示命令行界面的窗口程序 | Windows Terminal、iTerm2、WezTerm、Kitty |
| Shell | 解释命令的程序 | PowerShell、bash、zsh、fish、nushell |
| Prompt | 命令提示符样式和上下文信息 | Starship、Oh My Posh、Powerlevel10k |
| Multiplexer | 终端会话复用、分屏、断线恢复 | tmux、zellij |
| Remote Tool | 远程登录和文件传输 | OpenSSH、Remote-SSH、FileZilla、WinSCP |

> [!tip] 最实用的理解
> 终端像“窗口”，Shell 像“语言”，Prompt 像“仪表盘”，tmux/zellij 像“会话管理器”，SSH/SFTP 像“远程通道”。

## 一页推荐组合

| 平台 | 轻量稳定 | 现代增强 | 远程开发 |
| --- | --- | --- | --- |
| Windows | Windows Terminal + PowerShell 7 | WezTerm / Tabby + Git Bash | WSL + VSCode Remote-WSL + Remote-SSH |
| macOS | Terminal.app + zsh | iTerm2 / Ghostty / Warp + zsh | VSCode Remote-SSH + iTerm2 Profiles |
| Linux 桌面 | GNOME Terminal / Konsole + bash | Kitty / WezTerm / Ghostty + zsh/fish | VSCode Remote-SSH + tmux |
| Linux 服务器 | OpenSSH + bash | zsh/fish + starship | tmux / zellij + Remote-SSH |

## 终端工具对比

| 工具 | 平台 | 特点 | 优点 | 不足 |
| --- | --- | --- | --- | --- |
| Windows Terminal | Windows | 官方终端、标签页、分屏、配置 Profiles | 原生、稳定、WSL 集成好 | SSH 管理不是重点 |
| Terminal.app | macOS | 系统自带 | 简单可靠，无需安装 | 高级配置较少 |
| iTerm2 | macOS | Profiles、分屏、热键窗口、触发器 | macOS 终端重度用户首选之一 | 只适合 macOS |
| GNOME Terminal | Linux | GNOME 默认终端 | 稳定、简单 | 高级能力一般 |
| Konsole | Linux | KDE 默认终端 | 配置丰富，分屏好用 | KDE 生态体验最好 |
| WezTerm | Windows / macOS / Linux | Lua 配置、GPU 渲染、SSH/mux | 跨平台一致，配置可版本化 | 配置门槛稍高 |
| Kitty | macOS / Linux | GPU 渲染、键盘驱动、扩展强 | 快、功能强 | Windows 支持不是重点 |
| Alacritty | Windows / macOS / Linux | 极简高性能终端 | 轻量、快、干净 | 默认无标签页/分屏 |
| Ghostty | macOS / Linux 等 | 现代高性能终端 | 原生体验好，配置简洁 | 不同平台生态仍在发展 |
| Tabby | Windows / macOS / Linux | 图形化终端和 SSH 管理 | 多服务器连接直观 | 相对更重 |
| Warp | Windows / macOS / Linux | 命令块、AI、工作流 | 学习和回看命令舒服 | 部分能力依赖账号/云功能 |

## Shell 对比

| Shell | 平台 | 适合场景 | 优点 | 不足 |
| --- | --- | --- | --- | --- |
| PowerShell 7 | Windows / macOS / Linux | Windows 管理、跨平台脚本 | 对象管道强，系统管理舒服 | Bash 脚本不能直接照搬 |
| CMD | Windows | 旧脚本和系统兼容 | 到处都有 | 能力较弱 |
| bash | Linux / macOS / WSL | 服务器和通用脚本 | 兼容性最好，资料最多 | 交互体验较朴素 |
| zsh | macOS / Linux / WSL | 日常开发、主题插件 | 补全和插件生态成熟 | 插件过多会拖慢 |
| fish | Windows / macOS / Linux | 交互式命令行 | 自动补全和提示很舒服 | 脚本语法不完全 POSIX |
| nushell | Windows / macOS / Linux | 结构化数据处理 | 表格、JSON、对象管道自然 | 生态和兼容性仍在成长 |

## 终端增强工具

### 会话管理

| 工具 | 用途 | 适合场景 |
| --- | --- | --- |
| tmux | 终端复用、分屏、会话保持 | 服务器长期任务、远程开发 |
| zellij | tmux 的现代替代 | 想要更友好的布局和提示 |

常用 tmux：

```bash
tmux new -s dev
tmux ls
tmux attach -t dev
```

### 提示符美化

| 工具 | 用途 | 适合 Shell |
| --- | --- | --- |
| starship | 跨平台提示符 | bash / zsh / fish / PowerShell |
| Oh My Posh | 提示符主题 | PowerShell / zsh / bash |
| Oh My Zsh | zsh 插件和主题管理 | zsh |
| Powerlevel10k | zsh 高性能主题 | zsh |

### 搜索与跳转

| 工具 | 替代对象 | 特点 |
| --- | --- | --- |
| ripgrep / `rg` | `grep` | 搜索速度快，适合代码库 |
| fd | `find` | 更现代、默认忽略 `.gitignore` |
| fzf | 手工选择 | 模糊搜索文件、历史、分支 |
| zoxide | `cd` | 按使用频率智能跳转目录 |
| atuin | Shell history | 可搜索、可同步的历史记录 |

### 文件与监控

| 工具 | 替代对象 | 特点 |
| --- | --- | --- |
| bat | `cat` | 语法高亮、行号 |
| eza | `ls` | 彩色、图标、Git 状态 |
| btop | `top` | 现代系统监控 |
| lazygit | Git 命令 | 终端 Git UI |
| neovim | Vim / 编辑器 | 高度可配置终端编辑器 |

## SSH 工具

| 工具 | 平台 | 适合场景 | 备注 |
| --- | --- | --- | --- |
| OpenSSH | 全平台 | 标准 SSH 登录、脚本、VSCode Remote-SSH | 最推荐先学 |
| VSCode Remote-SSH | VSCode | 远程开发 | 直接打开远程目录 |
| Tabby | 全平台 | 多服务器管理 | 带图形化 SSH/SFTP 配置 |
| Termius | 全平台 + 移动端 | 多设备连接管理 | 适合移动端和同步 |
| PuTTY | Windows | 老环境兼容 | 经典但配置体系偏旧 |
| MobaXterm | Windows | 运维工具箱 | SSH、SFTP、X11 集中 |
| WinSCP | Windows | SFTP/SCP 文件管理 | 适合图形化传文件 |
| tmux / zellij | 服务器端 | 会话保持 | 断线不丢任务 |

更多见：[[SSH]]

## FTP / SFTP 工具

| 工具 | 协议 | 平台 | 适合场景 |
| --- | --- | --- | --- |
| FileZilla | FTP / FTPS / SFTP | Windows / macOS / Linux | 通用图形客户端 |
| WinSCP | SFTP / SCP / FTP / FTPS | Windows | Windows 文件传输 |
| Cyberduck | FTP / FTPS / SFTP / 云存储 | macOS / Windows | 图形化传输和云存储 |
| Transmit | FTP / SFTP / 云存储 | macOS | 高质量付费客户端 |
| lftp | FTP / FTPS / SFTP | Linux / macOS | 自动化 mirror 同步 |
| rclone | SFTP / FTP / 云存储 | 全平台 | 多后端同步 |
| curl / wget | FTP / FTPS 等 | 全平台 | 脚本化下载上传 |
| VSCode SFTP 扩展 | SFTP / FTP | VSCode | 编辑器内同步 |

更多见：[[FTP]]

## VSCode 集成

### 内置终端

VSCode 内置终端会启动 Shell，而不是替代 Windows Terminal、iTerm2、WezTerm 这些外部终端。常用命令：

```text
Terminal: Select Default Profile
Terminal: Create New Terminal
Terminal: Split Terminal
```

Windows 示例：

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

macOS / Linux 示例：

```json
{
  "terminal.integrated.defaultProfile.osx": "zsh",
  "terminal.integrated.defaultProfile.linux": "zsh",
  "terminal.integrated.profiles.osx": {
    "zsh": {
      "path": "/bin/zsh",
      "args": ["-l"]
    }
  },
  "terminal.integrated.profiles.linux": {
    "zsh": {
      "path": "zsh",
      "args": ["-l"]
    },
    "bash": {
      "path": "bash",
      "args": ["-l"]
    }
  }
}
```

### 外部终端

如果想从 VSCode 打开系统外部终端，可以使用命令：

```text
Terminal: Open New External Terminal
```

常见设置：

```json
{
  "terminal.external.windowsExec": "C:\\Program Files\\WezTerm\\wezterm-gui.exe",
  "terminal.external.osxExec": "iTerm.app",
  "terminal.external.linuxExec": "x-terminal-emulator"
}
```

> [!note] 内置终端 vs 外部终端
> 日常项目命令、任务、调试更适合 VSCode 内置终端；需要完整终端工作区、长期会话、复杂 SSH 管理时，再打开 Windows Terminal、iTerm2、WezTerm、Tabby 这类外部终端。

### Remote Development

| 扩展 | 用途 | 适合场景 |
| --- | --- | --- |
| Remote - SSH | 通过 SSH 打开远程服务器 | Linux 服务器开发 |
| WSL | 在 Windows 上打开 WSL 项目 | Windows + Linux 开发环境 |
| Dev Containers | 在容器中开发 | 团队统一依赖环境 |
| Remote Tunnels | 通过隧道访问远程机器 | 不能直接 SSH 的场景 |

### 文件传输集成

| 方式 | 推荐度 | 说明 |
| --- | --- | --- |
| Remote-SSH | 高 | 直接远程开发，避免同步错文件 |
| `scp` / `rsync` / `lftp` Task | 高 | 可重复、可审计，适合部署 |
| SFTP 扩展 | 中 | 适合静态站点和旧主机 |
| 明文 FTP 扩展 | 低 | 只适合可信内网或旧系统 |

VSCode Task 调用 `rsync` 示例：

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "deploy:rsync",
      "type": "shell",
      "command": "rsync -avz --delete ./dist/ myserver:/var/www/app/",
      "problemMatcher": []
    }
  ]
}
```

> [!warning] VSCode 同步类扩展
> 自动上传很方便，也很容易把错误文件推到服务器。正式环境建议关闭 `uploadOnSave`，改成手动同步或 CI 部署。

## 学习路线

1. 先熟悉系统自带终端和默认 Shell。
2. 再安装一个现代终端：Windows Terminal / iTerm2 / WezTerm / Kitty。
3. 给 Shell 配置 `starship`、`rg`、`fd`、`fzf`、`zoxide`。
4. 学会 `ssh`、`scp`、`sftp`、`rsync`。
5. 在 VSCode 中配置默认终端、Remote-SSH、Remote-WSL。
6. 服务器长期任务使用 `tmux` 或 `zellij`。
