---
title: Linux 常用命令
aliases:
  - Linux Commands
  - Linux 命令速查
  - Bash 常用命令
tags:
  - tools/command
  - linux
  - bash
  - shell
  - cheatsheet
created: 2026-05-20
updated: 2026-05-20
---

# Linux 常用命令

> [!info] 使用场景
> 这篇笔记适合日常 Linux 服务器、WSL、开发环境和命令行排错。命令以 Bash / zsh 通用写法为主，不同发行版的包管理器会单独列出。

相关笔记：[[Windows Commands]] | [[Mac Commands]] | [[Termimal & Shell Tools]] | [[WSL]] | [[SSH]]

## Linux 终端与 Shell 选择

> [!note] Linux 上的三层
> 桌面终端负责显示窗口，Shell 负责解释命令，`tmux` / `zellij` 负责在远程会话里保持窗口和分屏。服务器上最值得学的是 Shell + tmux，而不是某个桌面终端。

### 流行终端工具

| 工具 | 适合谁 | 特点 | 优点 | 不足 |
| --- | --- | --- | --- | --- |
| GNOME Terminal | Ubuntu / GNOME 用户 | 桌面默认终端 | 稳定、简单、系统集成好 | 高级配置较少 |
| Konsole | KDE 用户 | KDE 默认终端 | 配置丰富，分屏体验好 | 主要面向 KDE 生态 |
| Kitty | 高性能终端用户 | GPU 渲染、扩展能力强 | 快、功能强、键盘驱动 | 配置需要学习 |
| WezTerm | 跨平台用户 | Lua 配置、GPU 渲染、SSH/mux 能力 | 配置可复用到 Windows/macOS | 初始配置成本较高 |
| Alacritty | 极简用户 | 高性能、少内置功能 | 轻量、稳定 | 不自带标签页和分屏 |
| Ghostty | 现代终端体验 | 高性能、配置简洁 | 体验现代，跨平台趋势明显 | Linux 发行版打包情况可能不一致 |
| Terminator / Tilix | 喜欢图形分屏的人 | 多面板终端 | 分屏直观 | 外观和维护活跃度因发行版而异 |
| Guake | 快速下拉终端 | 类似游戏控制台下拉 | 临时执行命令很快 | 不适合作为唯一终端 |

### 常用 Shell

| Shell | 适合场景 | 优点 | 不足 |
| --- | --- | --- | --- |
| bash | Linux 默认、服务器脚本 | 兼容性最好，资料最多 | 交互体验较朴素 |
| zsh | 日常开发、主题插件 | 插件生态强，和 macOS 体验一致 | 插件过多会影响启动 |
| fish | 命令行交互体验 | 自动补全、语法提示非常舒服 | 脚本语法不完全兼容 POSIX |
| nushell | 数据处理和现代 Shell 实验 | 结构化管道适合表格/JSON | 服务器默认环境少见 |

### 安装与切换

Debian / Ubuntu：

```bash
sudo apt update
sudo apt install zsh fish tmux ripgrep fd-find bat btop
```

Fedora：

```bash
sudo dnf install zsh fish tmux ripgrep fd-find bat btop
```

Arch：

```bash
sudo pacman -S zsh fish tmux ripgrep fd bat btop
```

切换默认 Shell：

```bash
chsh -s "$(which zsh)"
chsh -s "$(which fish)"
```

### VSCode 集成

常用入口：

- `Ctrl + Shift + P` -> `Terminal: Select Default Profile`
- `` Ctrl + ` `` 打开/关闭内置终端
- Remote 场景下，VSCode 终端运行在远程 Linux 主机内

`settings.json` 示例：

```json
{
  "terminal.integrated.defaultProfile.linux": "zsh",
  "terminal.integrated.profiles.linux": {
    "bash": {
      "path": "bash",
      "args": ["-l"]
    },
    "zsh": {
      "path": "zsh",
      "args": ["-l"]
    },
    "fish": {
      "path": "fish"
    }
  }
}
```

常见搭配：

| 任务 | VSCode 里推荐用法 |
| --- | --- |
| 本机 Linux 开发 | 内置终端默认 `zsh` 或 `bash` |
| 服务器开发 | 使用 `Remote - SSH`，让 VSCode 直接打开远程目录 |
| 长时间运行任务 | 在 VSCode 远程终端里启动 `tmux`，断线后还能恢复 |
| 搜索大项目 | 安装 `ripgrep`，VSCode 搜索和终端 `rg` 都会更顺 |

## 快速索引

| 我想做什么 | 命令 |
| --- | --- |
| 查看当前位置 | `pwd` |
| 列出文件 | `ls -lah` |
| 切换目录 | `cd <目录>` |
| 创建目录 | `mkdir -p <目录>` |
| 创建空文件 | `touch <文件>` |
| 查看文件 | `cat <文件>` / `less <文件>` |
| 复制 | `cp <源> <目标>` |
| 移动或重命名 | `mv <源> <目标>` |
| 删除 | `rm <文件>` |
| 搜索文件 | `find <目录> -name "<模式>"` |
| 搜索内容 | `grep -R "关键字" <目录>` |
| 查看帮助 | `man <命令>` / `<命令> --help` |

> [!tip] 学命令的顺序
> 先把“目录、文件、查看、搜索、进程、网络、权限”练熟，再记包管理和服务管理。大多数服务器排错其实都围绕这几类命令转。

## 基础操作

### 帮助与历史

```bash
man ls
ls --help
type cd
which python
history
clear
```

| 命令 | 说明 |
| --- | --- |
| `man <命令>` | 查看手册 |
| `<命令> --help` | 查看简短帮助 |
| `type <命令>` | 判断命令是内建、别名还是可执行文件 |
| `which <命令>` | 查找可执行文件位置 |
| `history` | 查看历史命令 |
| `clear` | 清屏 |

### 常用快捷键

| 快捷键 | 作用 |
| --- | --- |
| `Tab` | 自动补全 |
| `Ctrl + C` | 中断当前命令 |
| `Ctrl + D` | 退出当前 shell / 输入 EOF |
| `Ctrl + Z` | 挂起前台任务 |
| `Ctrl + A` | 光标到行首 |
| `Ctrl + E` | 光标到行尾 |
| `Ctrl + R` | 反向搜索历史命令 |

## 目录与文件

### 导航与列出

```bash
pwd
ls
ls -lah
ls -lt
cd /var/log
cd ..
cd ~
```

| 命令 | 说明 |
| --- | --- |
| `pwd` | 查看当前目录 |
| `ls -lah` | 以可读大小显示所有文件 |
| `ls -lt` | 按修改时间排序 |
| `cd ..` | 返回上一级 |
| `cd -` | 回到上一次所在目录 |
| `tree` | 树状显示目录，可能需要安装 |

### 创建、复制、移动、删除

```bash
mkdir notes
mkdir -p projects/demo/src
touch README.md
cp a.txt b.txt
cp -r src backup
mv old.txt new.txt
rm file.txt
rm -r old_dir
```

| 命令 | 说明 |
| --- | --- |
| `mkdir <目录>` | 创建目录 |
| `mkdir -p a/b/c` | 创建多级目录 |
| `touch <文件>` | 创建空文件或更新修改时间 |
| `cp <源> <目标>` | 复制文件 |
| `cp -r <目录> <目标>` | 递归复制目录 |
| `mv <源> <目标>` | 移动或重命名 |
| `rm <文件>` | 删除文件 |
| `rm -r <目录>` | 删除目录 |

> [!warning] 删除命令
> `rm -rf` 没有回收站。执行前用 `pwd` 和 `ls` 确认位置，变量为空时尤其危险。

### 文件信息与大小

```bash
file app
stat README.md
du -sh .
du -h --max-depth=1
df -h
wc -l README.md
```

| 命令 | 说明 |
| --- | --- |
| `file <文件>` | 判断文件类型 |
| `stat <文件>` | 查看文件详细元数据 |
| `du -sh <目录>` | 查看目录总大小 |
| `du -h --max-depth=1` | 查看当前目录下一级大小 |
| `df -h` | 查看磁盘分区使用情况 |
| `wc -l <文件>` | 统计行数 |

## 查看与编辑文本

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
| `cat` | 一次性输出文件内容 |
| `less` | 分页查看大文件 |
| `head` | 查看文件开头 |
| `tail` | 查看文件末尾 |
| `tail -f` | 持续跟踪日志 |
| `nano` | 轻量命令行编辑器 |
| `vim` | 常用终端编辑器 |

## 搜索、筛选与管道

### 搜索文件

```bash
find . -name "*.md"
find /var/log -type f -name "*.log"
find . -type f -size +100M
find . -type f -mtime -7
```

| 条件 | 说明 |
| --- | --- |
| `-name "*.md"` | 按文件名匹配 |
| `-type f` | 只找文件 |
| `-type d` | 只找目录 |
| `-size +100M` | 大于 100MB |
| `-mtime -7` | 7 天内修改过 |

### 搜索内容

```bash
grep "error" app.log
grep -n "error" app.log
grep -R "TODO" .
grep -Ri "warning" .
```

| 命令 | 说明 |
| --- | --- |
| `grep "词" 文件` | 搜索文本 |
| `grep -n` | 显示行号 |
| `grep -R` | 递归搜索目录 |
| `grep -i` | 忽略大小写 |
| `rg "词"` | 使用 ripgrep，速度更快，需安装 |

### 管道组合

```bash
ps aux | grep nginx
cat access.log | grep "404" | wc -l
du -h --max-depth=1 | sort -h
history | grep ssh
```

| 命令 | 说明 |
| --- | --- |
| `|` | 把前一个命令输出交给后一个命令 |
| `sort` | 排序 |
| `uniq` | 去重，通常配合 `sort` |
| `cut` | 按列截取 |
| `awk` | 文本按列处理 |
| `sed` | 流式文本替换 |
| `tee` | 输出到屏幕同时写入文件 |

## 权限与用户

```bash
whoami
id
groups
ls -l
chmod +x script.sh
chmod 644 file.txt
chmod 755 script.sh
chown user:user file.txt
sudo <命令>
```

| 命令 | 说明 |
| --- | --- |
| `whoami` | 当前用户名 |
| `id` | 用户 ID 和组信息 |
| `groups` | 当前用户所在组 |
| `chmod` | 修改权限 |
| `chown` | 修改所有者 |
| `sudo` | 以管理员权限执行 |
| `su -` | 切换用户或 root 登录 shell |

### 权限数字速记

| 数字 | 权限 | 含义 |
| --- | --- | --- |
| `4` | `r` | 读 |
| `2` | `w` | 写 |
| `1` | `x` | 执行 |
| `644` | `rw-r--r--` | 普通文件常用权限 |
| `755` | `rwxr-xr-x` | 脚本或目录常用权限 |

## 进程、任务与服务

### 进程管理

```bash
ps aux
ps aux | grep nginx
top
htop
pgrep nginx
kill <PID>
kill -9 <PID>
killall nginx
```

| 命令 | 说明 |
| --- | --- |
| `ps aux` | 查看全部进程 |
| `top` | 实时查看资源占用 |
| `htop` | 更友好的 top，需安装 |
| `pgrep <名称>` | 按名称找 PID |
| `kill <PID>` | 结束进程 |
| `kill -9 <PID>` | 强制结束进程 |

### 前后台任务

```bash
command &
jobs
fg %1
bg %1
nohup command > app.log 2>&1 &
```

| 命令 | 说明 |
| --- | --- |
| `command &` | 后台运行 |
| `jobs` | 查看当前 shell 的后台任务 |
| `fg` | 放回前台 |
| `bg` | 在后台继续运行 |
| `nohup` | 退出终端后继续运行 |

### systemd 服务

```bash
systemctl status nginx
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl enable nginx
sudo systemctl disable nginx
journalctl -u nginx -f
```

| 命令 | 说明 |
| --- | --- |
| `systemctl status <服务>` | 查看服务状态 |
| `start` / `stop` / `restart` | 启动、停止、重启 |
| `enable` / `disable` | 开机自启或取消 |
| `journalctl -u <服务>` | 查看服务日志 |

## 网络与远程连接

### 网络诊断

```bash
ip addr
ip route
ping github.com
traceroute github.com
dig github.com
nslookup github.com
curl -I https://example.com
wget https://example.com/file.zip
```

| 命令 | 说明 |
| --- | --- |
| `ip addr` | 查看网卡和 IP |
| `ip route` | 查看路由 |
| `ping` | 测试连通性 |
| `traceroute` | 查看路由路径，可能需要安装 |
| `dig` | DNS 查询，常用于排错 |
| `curl` | HTTP 请求、接口测试 |
| `wget` | 下载文件 |

### 端口与连接

```bash
ss -tulpen
ss -tulpen | grep :3000
lsof -i :3000
nc -vz example.com 443
```

| 命令 | 说明 |
| --- | --- |
| `ss -tulpen` | 查看监听端口和连接 |
| `lsof -i :端口` | 查看端口占用进程 |
| `nc -vz <主机> <端口>` | 测试 TCP 端口 |

### SSH 与传输

```bash
ssh user@example.com
ssh -p 2222 user@example.com
scp file.txt user@example.com:/home/user/
rsync -avz ./dist/ user@example.com:/var/www/app/
```

更多内容见：[[SSH]]

## 包管理器

| 发行版 | 更新索引 | 安装软件 | 升级系统 | 删除软件 |
| --- | --- | --- | --- | --- |
| Debian / Ubuntu | `sudo apt update` | `sudo apt install <包>` | `sudo apt upgrade` | `sudo apt remove <包>` |
| Fedora | `sudo dnf check-update` | `sudo dnf install <包>` | `sudo dnf upgrade` | `sudo dnf remove <包>` |
| Arch | `sudo pacman -Sy` | `sudo pacman -S <包>` | `sudo pacman -Syu` | `sudo pacman -R <包>` |
| openSUSE | `sudo zypper refresh` | `sudo zypper install <包>` | `sudo zypper update` | `sudo zypper remove <包>` |

常用查询：

```bash
apt search nginx
apt show nginx
dpkg -l | grep nginx
dnf search nginx
pacman -Ss nginx
```

## 磁盘、内存与硬件

```bash
df -h
du -sh /var/log
lsblk
blkid
mount
free -h
uptime
uname -a
lscpu
```

| 命令 | 说明 |
| --- | --- |
| `df -h` | 查看磁盘空间 |
| `du -sh` | 查看目录大小 |
| `lsblk` | 查看磁盘块设备 |
| `mount` | 查看挂载情况 |
| `free -h` | 查看内存 |
| `uptime` | 查看运行时间和负载 |
| `uname -a` | 查看内核与系统信息 |

## 压缩与解压

```bash
tar -czf archive.tar.gz folder
tar -xzf archive.tar.gz
tar -cjf archive.tar.bz2 folder
tar -xjf archive.tar.bz2
zip -r archive.zip folder
unzip archive.zip
gzip file.log
gunzip file.log.gz
```

| 格式 | 压缩 | 解压 |
| --- | --- | --- |
| `.tar.gz` | `tar -czf a.tar.gz dir` | `tar -xzf a.tar.gz` |
| `.tar.bz2` | `tar -cjf a.tar.bz2 dir` | `tar -xjf a.tar.bz2` |
| `.zip` | `zip -r a.zip dir` | `unzip a.zip` |
| `.gz` | `gzip file` | `gunzip file.gz` |

## 环境变量与 Shell 配置

```bash
echo $SHELL
echo $PATH
env
export NODE_ENV=development
source ~/.bashrc
source ~/.zshrc
alias ll='ls -lah'
```

| 文件 | 常见用途 |
| --- | --- |
| `~/.bashrc` | Bash 交互 shell 配置 |
| `~/.zshrc` | zsh 配置 |
| `~/.profile` | 登录 shell 配置 |
| `/etc/environment` | 系统级环境变量 |
| `/etc/profile` | 系统级 shell 配置 |

## 定时任务

```bash
crontab -l
crontab -e
systemctl list-timers
```

cron 示例：

```cron
# 每天凌晨 2 点执行脚本
0 2 * * * /home/user/backup.sh
```

## 常见任务配方

### 找出大目录

```bash
du -h --max-depth=1 | sort -h
```

### 查找最近 7 天修改过的文件

```bash
find . -type f -mtime -7
```

### 查看某个端口被谁占用

```bash
ss -tulpen | grep :3000
lsof -i :3000
```

### 实时查看服务日志

```bash
journalctl -u nginx -f
```

### 给脚本添加执行权限并运行

```bash
chmod +x deploy.sh
./deploy.sh
```

### 后台运行任务并保存日志

```bash
nohup python app.py > app.log 2>&1 &
tail -f app.log
```

## 高风险命令

> [!warning] 执行前先确认
> 这些命令会删除、覆盖、格式化或修改系统关键状态：`rm -rf`、`dd`、`mkfs`、`fdisk`、`parted`、`chmod -R`、`chown -R`、`kill -9`、`systemctl disable`、重定向覆盖 `>`。

建议先用这些命令做确认：

```bash
pwd
ls -lah
echo "$变量名"
find . -name "<目标>" -print
```
