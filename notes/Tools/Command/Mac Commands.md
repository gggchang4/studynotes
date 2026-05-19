---
title: macOS 常用命令
aliases:
  - Mac Commands
  - macOS 命令速查
  - zsh 常用命令
tags:
  - tools/command
  - macos
  - zsh
  - shell
  - cheatsheet
created: 2026-05-20
updated: 2026-05-20
---

# macOS 常用命令

> [!info] 使用场景
> macOS 的命令行和 Linux 很像，但很多基础工具来自 BSD，参数细节会和 GNU/Linux 不完全一样。这篇笔记以 **Terminal / iTerm2 + zsh + Homebrew** 的日常使用为主。

相关笔记：[[Windows Commands]] | [[Linux Commands]] | [[Termimal & Shell Tools]] | [[SSH]]

## macOS 终端与 Shell 选择

> [!note] 终端和 Shell
> 终端是窗口，Shell 是命令解释器。macOS 默认 Shell 是 `zsh`，但你可以在 Terminal.app、iTerm2、Warp、Ghostty、WezTerm 等终端里运行同一个 `zsh`。

### 流行终端工具

| 工具 | 适合谁 | 特点 | 优点 | 不足 |
| --- | --- | --- | --- | --- |
| Terminal.app | 大多数轻量用户 | macOS 自带终端 | 稳定、无需安装、系统集成好 | 分屏、配置和搜索体验较基础 |
| iTerm2 | macOS 重度终端用户 | 标签页、分屏、Profiles、触发器、热键窗口 | 功能成熟，资料多 | 只适合 macOS，配置项多 |
| Warp | 想要现代交互和 AI 辅助的人 | 命令块、历史搜索、补全、AI | 交互体验友好，适合学习和回看命令 | 部分能力依赖账号或云服务 |
| Ghostty | 喜欢现代高性能终端的人 | 原生、高性能、配置简洁 | 轻快，视觉效果好 | 生态和资料仍在增长中 |
| WezTerm | 跨平台配置党 | Lua 配置、GPU 渲染、跨平台 | 一套配置可同步多系统 | 配置门槛高于 iTerm2 |
| Kitty | 高性能终端用户 | GPU 渲染、丰富扩展、键盘驱动 | 快、功能强 | 配置和快捷键需要适应 |
| Alacritty | 极简用户 | 高性能、配置文件驱动 | 轻量、专注终端本身 | 默认不带标签页和分屏 |

### 常用 Shell

| Shell | 适合场景 | 优点 | 不足 |
| --- | --- | --- | --- |
| zsh | macOS 默认 Shell、日常开发 | 兼容性好，插件主题生态成熟 | 插件过多会拖慢启动 |
| bash | 服务器兼容、老脚本 | 资料最多，Linux 服务器常见 | macOS 自带版本偏旧 |
| fish | 交互式命令行 | 自动补全和提示体验好 | 语法和 POSIX Shell 不完全兼容 |
| nushell | 结构化数据处理 | 表格/JSON/对象处理舒服 | 生态和脚本兼容性还不如 bash/zsh |

### 安装与切换

```bash
brew install --cask iterm2
brew install --cask warp
brew install --cask ghostty
brew install wezterm
brew install fish nushell starship
```

切换默认 Shell：

```bash
chsh -s /bin/zsh
chsh -s /opt/homebrew/bin/fish
```

> [!warning] 切换 Shell 前
> 如果 `fish` 或 `nu` 不是系统已认可的登录 Shell，需要先确认它们在 `/etc/shells` 中。否则可能导致登录 Shell 异常。

### VSCode 集成

常用入口：

- `Cmd + Shift + P` -> `Terminal: Select Default Profile`
- `` Ctrl + ` `` 打开/关闭内置终端
- `Shell Command: Install 'code' command in PATH` 后可在终端中用 `code .`

`settings.json` 示例：

```json
{
  "terminal.integrated.defaultProfile.osx": "zsh",
  "terminal.integrated.profiles.osx": {
    "zsh": {
      "path": "/bin/zsh",
      "args": ["-l"]
    },
    "fish": {
      "path": "/opt/homebrew/bin/fish"
    }
  }
}
```

常见搭配：

| 任务 | VSCode 里推荐用法 |
| --- | --- |
| 本机开发 | 默认 `zsh`，按项目需要切换 `fish` |
| Homebrew / Node / Python | 确保 VSCode 终端加载正确的 `PATH` |
| 远程 Linux 开发 | 使用 `Remote - SSH` 打开远程目录 |
| 临时传文件 | 优先用 `scp` / `rsync` / `sftp`，需要图形同步再用 SFTP 扩展 |

## 快速索引

| 我想做什么 | 命令 |
| --- | --- |
| 查看当前位置 | `pwd` |
| 列出文件 | `ls -lah` |
| 切换目录 | `cd <目录>` |
| 用 Finder 打开当前目录 | `open .` |
| 打开文件或 App | `open <文件或应用>` |
| 复制命令输出到剪贴板 | `<命令> \| pbcopy` |
| 查看剪贴板文本 | `pbpaste` |
| 查看系统版本 | `sw_vers` |
| 安装软件包 | `brew install <包>` |
| 查看端口占用 | `lsof -i :<端口>` |

> [!tip] macOS 记忆方式
> 通用 Unix 命令负责“文件、文本、进程、网络”，macOS 专属命令负责“Finder、剪贴板、系统信息、应用、磁盘镜像、Homebrew”。

## 目录与文件

### 导航与 Finder 联动

```bash
pwd
ls -lah
cd ~/Documents
cd ..
cd -
open .
open ~/Downloads
open -R README.md
```

| 命令 | 说明 |
| --- | --- |
| `pwd` | 查看当前目录 |
| `ls -lah` | 显示全部文件和可读大小 |
| `cd -` | 回到上一个目录 |
| `open .` | 用 Finder 打开当前目录 |
| `open <文件>` | 用默认 App 打开文件 |
| `open -R <文件>` | 在 Finder 中定位文件 |

### 创建、复制、移动、删除

```bash
mkdir notes
mkdir -p projects/demo/src
touch README.md
cp a.txt b.txt
cp -R src backup
mv old.txt new.txt
rm file.txt
rm -r old_dir
```

| 命令 | 说明 |
| --- | --- |
| `mkdir` | 创建目录 |
| `mkdir -p` | 创建多级目录 |
| `touch` | 创建空文件或更新修改时间 |
| `cp` | 复制文件 |
| `cp -R` | 复制目录 |
| `mv` | 移动或重命名 |
| `rm` | 删除文件或目录 |

> [!warning] 删除提醒
> 终端里的 `rm` 不经过废纸篓。删除目录前先执行 `pwd`、`ls`，确认自己所在位置。

### 文件大小与信息

```bash
file app
stat README.md
du -sh .
du -h -d 1
df -h
mdls README.md
```

| 命令 | 说明 |
| --- | --- |
| `file <文件>` | 判断文件类型 |
| `stat <文件>` | 查看文件元数据 |
| `du -sh <目录>` | 查看目录总大小 |
| `du -h -d 1` | 查看下一级目录大小 |
| `df -h` | 查看磁盘空间 |
| `mdls <文件>` | 查看 Spotlight 元数据 |

## 查看、搜索与文本处理

### 查看文件

```bash
cat README.md
less README.md
head -n 20 app.log
tail -n 50 app.log
tail -f app.log
nano config.txt
vim config.txt
```

| 命令 | 说明 |
| --- | --- |
| `cat` | 输出文件内容 |
| `less` | 分页查看 |
| `head` | 查看开头 |
| `tail` | 查看末尾 |
| `tail -f` | 追踪日志 |
| `nano` / `vim` | 终端编辑器 |

### 搜索文件与内容

```bash
find . -name "*.md"
find . -type f -size +100M
grep -R "TODO" .
grep -n "error" app.log
mdfind "Obsidian"
```

| 命令 | 说明 |
| --- | --- |
| `find` | 按名称、类型、大小等查找文件 |
| `grep` | 搜索文本内容 |
| `mdfind` | 使用 Spotlight 索引搜索 |
| `rg` | 更快的文本搜索工具，需安装 |

### sed 在 macOS 上的写法

```bash
sed 's/old/new/g' file.txt
sed -i '' 's/old/new/g' file.txt
```

> [!note] BSD sed 差异
> Linux 常见写法是 `sed -i 's/old/new/g' file.txt`，macOS 自带 BSD sed 需要给 `-i` 一个备份后缀；不需要备份时写成 `-i ''`。

## 剪贴板与系统小工具

```bash
echo "hello" | pbcopy
pbpaste
date
cal
caffeinate
say "build finished"
screencapture ~/Desktop/screen.png
sips -Z 1024 image.png
textutil -convert txt document.docx
```

| 命令 | 说明 |
| --- | --- |
| `pbcopy` | 把标准输入写入剪贴板 |
| `pbpaste` | 输出剪贴板文本 |
| `caffeinate` | 防止系统睡眠 |
| `say` | 文字转语音 |
| `screencapture` | 截图 |
| `sips` | 图片处理 |
| `textutil` | 文档格式转换 |

## 系统信息与进程

### 系统信息

```bash
sw_vers
uname -a
uname -m
system_profiler SPHardwareDataType
sysctl -n machdep.cpu.brand_string
whoami
```

| 命令 | 说明 |
| --- | --- |
| `sw_vers` | 查看 macOS 版本 |
| `uname -m` | 查看架构，常见为 `arm64` 或 `x86_64` |
| `system_profiler` | 查看系统硬件和软件信息 |
| `sysctl` | 查询内核参数和硬件信息 |
| `whoami` | 查看当前用户 |

### 进程管理

```bash
ps aux
ps aux | grep nginx
top
pgrep nginx
kill <PID>
kill -9 <PID>
killall Finder
```

| 命令 | 说明 |
| --- | --- |
| `ps aux` | 查看进程 |
| `top` | 实时资源占用 |
| `pgrep` | 按名称查 PID |
| `kill` | 结束进程 |
| `killall <名称>` | 按名称结束进程 |

## 网络与远程

### 网络诊断

```bash
ifconfig
ipconfig getifaddr en0
networksetup -listallhardwareports
scutil --dns
ping github.com
traceroute github.com
dig github.com
curl -I https://example.com
```

| 命令 | 说明 |
| --- | --- |
| `ifconfig` | 查看网络接口 |
| `ipconfig getifaddr en0` | 查看 Wi-Fi 常见接口 IP |
| `networksetup -listallhardwareports` | 查看网卡设备名 |
| `scutil --dns` | 查看 DNS 配置 |
| `ping` | 测试连通 |
| `traceroute` | 查看路由路径 |
| `dig` | DNS 查询 |
| `curl` | HTTP 请求 |

### 端口占用

```bash
lsof -i :3000
lsof -iTCP:3000 -sTCP:LISTEN
nc -vz example.com 443
```

结束占用端口的进程：

```bash
lsof -i :3000
kill <PID>
```

### SSH 与文件传输

```bash
ssh user@example.com
ssh -p 2222 user@example.com
scp file.txt user@example.com:/home/user/
rsync -avz ./dist/ user@example.com:/var/www/app/
```

更多内容见：[[SSH]]

## Homebrew 包管理

```bash
brew update
brew search node
brew info node
brew install node
brew list
brew upgrade
brew uninstall node
brew cleanup
brew doctor
```

| 命令 | 说明 |
| --- | --- |
| `brew update` | 更新 Homebrew 索引 |
| `brew search <包>` | 搜索软件包 |
| `brew info <包>` | 查看软件包信息 |
| `brew install <包>` | 安装软件包 |
| `brew list` | 查看已安装包 |
| `brew upgrade` | 更新已安装包 |
| `brew uninstall <包>` | 卸载软件包 |
| `brew cleanup` | 清理旧版本缓存 |
| `brew doctor` | 检查 Homebrew 环境 |

### Brew services

```bash
brew services list
brew services start <服务名>
brew services stop <服务名>
brew services restart <服务名>
```

## App、系统设置与 Finder

### 打开应用

```bash
open -a "Visual Studio Code"
open -a "Google Chrome" https://example.com
open /Applications
```

### 显示或隐藏 Finder 隐藏文件

```bash
defaults write com.apple.finder AppleShowAllFiles -bool true
killall Finder
```

恢复隐藏：

```bash
defaults write com.apple.finder AppleShowAllFiles -bool false
killall Finder
```

### 隔离属性与安全提示

```bash
xattr -l app.dmg
xattr -dr com.apple.quarantine SomeApp.app
spctl --assess --verbose SomeApp.app
```

> [!warning] Gatekeeper 相关命令
> `xattr -dr com.apple.quarantine` 会移除下载文件的隔离属性。只对你确认来源可信的软件使用。

## 磁盘与镜像

```bash
diskutil list
diskutil info disk3
diskutil eject disk3
hdiutil attach image.dmg
hdiutil detach /Volumes/AppName
tmutil listlocalsnapshots /
```

| 命令 | 说明 |
| --- | --- |
| `diskutil list` | 查看磁盘和分区 |
| `diskutil info <磁盘>` | 查看磁盘详情 |
| `diskutil eject <磁盘>` | 弹出磁盘 |
| `hdiutil attach` | 挂载 dmg 镜像 |
| `hdiutil detach` | 卸载镜像 |
| `tmutil` | Time Machine 相关操作 |

## zsh 环境变量与配置

```bash
echo $SHELL
echo $PATH
which python3
type brew
code ~/.zshrc
source ~/.zshrc
export PATH="/opt/homebrew/bin:$PATH"
alias ll='ls -lah'
```

| 文件 | 用途 |
| --- | --- |
| `~/.zshrc` | zsh 交互 shell 配置 |
| `~/.zprofile` | zsh 登录 shell 配置 |
| `~/.ssh/config` | SSH 主机别名配置 |
| `/etc/paths` | 系统 PATH 配置之一 |

> [!note] Apple Silicon Homebrew 路径
> Apple Silicon 常见 Homebrew 路径是 `/opt/homebrew/bin`；Intel Mac 常见路径是 `/usr/local/bin`。

## 常见任务配方

### 把 SSH 公钥复制到剪贴板

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

### 查看当前目录下的大文件

```bash
find . -type f -size +100M
```

### 查看一级目录大小

```bash
du -h -d 1 | sort -h
```

### 检查本机服务端口

```bash
lsof -iTCP:3000 -sTCP:LISTEN
```

### 让电脑临时不睡眠

```bash
caffeinate
```

### 下载文件并查看响应头

```bash
curl -I https://example.com
curl -L -o file.zip https://example.com/file.zip
```

## 与 Linux 容易混淆的地方

| 主题 | macOS | Linux 常见写法 |
| --- | --- | --- |
| sed 原地替换 | `sed -i '' 's/a/b/g' file` | `sed -i 's/a/b/g' file` |
| du 一级深度 | `du -h -d 1` | `du -h --max-depth=1` |
| 复制目录 | `cp -R src dst` | `cp -r src dst` |
| 查看 IP | `ifconfig` / `ipconfig getifaddr en0` | `ip addr` |
| 包管理 | `brew install <包>` | `apt` / `dnf` / `pacman` |

## 高风险命令

> [!warning] 执行前先确认
> 谨慎使用：`rm -rf`、`diskutil eraseDisk`、`diskutil partitionDisk`、`sudo chmod -R`、`sudo chown -R`、`xattr -dr com.apple.quarantine`、覆盖重定向 `>`。

建议先确认：

```bash
pwd
ls -lah
diskutil list
echo "$变量名"
```
