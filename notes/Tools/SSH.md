---
title: SSH 使用笔记
aliases:
  - SSH
  - Secure Shell
  - SSH 远程登录
  - SSH 端口转发
tags:
  - tools/network
  - tools/ssh
  - linux
  - server
  - cheatsheet
created: 2026-05-20
updated: 2026-05-20
---

# SSH 使用笔记

> [!info] 使用场景
> SSH 是日常连接 Linux 服务器、管理云主机、远程执行命令、端口转发、传输文件的基础工具。它更像是一条安全的远程通道，`ssh` 负责登录，`scp` / `sftp` / `rsync` 负责传文件。

相关笔记：[[Linux Commands]] | [[Windows Commands]] | [[Mac Commands]] | [[FTP]] | [[WSL]] | [[Termimal & Shell Tools]]

## 快速索引

| 我想做什么 | 命令 |
| --- | --- |
| 登录服务器 | `ssh user@example.com` |
| 指定端口登录 | `ssh -p 2222 user@example.com` |
| 使用指定密钥 | `ssh -i ~/.ssh/id_ed25519 user@example.com` |
| 远程执行命令 | `ssh user@example.com "uptime"` |
| 复制文件到服务器 | `scp file.txt user@example.com:/home/user/` |
| 从服务器下载文件 | `scp user@example.com:/home/user/file.txt .` |
| 交互式传文件 | `sftp user@example.com` |
| 同步目录 | `rsync -avz ./dist/ user@example.com:/var/www/app/` |
| 本地端口转发 | `ssh -L 8080:127.0.0.1:80 user@example.com` |
| 查看详细日志 | `ssh -v user@example.com` |

## SSH 是什么

SSH，全称 Secure Shell，是一种安全远程登录协议。它常用于：

- 登录远程 Linux 服务器
- 在远程服务器上执行命令
- 通过加密通道传输文件
- 做本地端口转发、远程端口转发和跳板机连接
- 配合 GitHub / GitLab 使用 SSH Key 推拉代码

> [!tip] 记忆方式
> `ssh` 管登录，`scp` 管简单复制，`sftp` 管交互式文件管理，`rsync` 管高效同步。

## 基本登录

```bash
ssh user@example.com
ssh user@192.168.1.10
ssh -p 2222 user@example.com
ssh user@example.com "hostname && uptime"
```

| 命令 | 说明 |
| --- | --- |
| `ssh user@host` | 使用指定用户登录主机 |
| `ssh -p <端口>` | 指定 SSH 服务端口，默认是 `22` |
| `ssh user@host "命令"` | 在远程服务器执行一次命令 |
| `exit` | 退出远程会话 |

第一次连接时通常会看到主机指纹确认：

```text
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

确认主机可信后输入 `yes`，客户端会把服务器指纹写入 `~/.ssh/known_hosts`。

> [!warning] 主机指纹变化
> 如果之前能连接，后来突然提示 `REMOTE HOST IDENTIFICATION HAS CHANGED`，不要直接忽略。可能是服务器重装，也可能是中间人攻击。先确认服务器是否变更过。

## 密码登录与密钥登录

### 密码登录

```bash
ssh user@example.com
```

输入用户密码即可登录。优点是简单，缺点是容易被暴力破解，正式服务器建议关闭密码登录，改用密钥登录。

### 生成 SSH Key

推荐使用 `ed25519`：

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

常见文件：

| 文件 | 说明 |
| --- | --- |
| `~/.ssh/id_ed25519` | 私钥，只能自己保存 |
| `~/.ssh/id_ed25519.pub` | 公钥，可以放到服务器或 Git 平台 |
| `~/.ssh/known_hosts` | 记录连接过的服务器指纹 |
| `~/.ssh/config` | SSH 客户端配置 |

> [!warning] 私钥不要外传
> `.pub` 结尾的是公钥，可以复制给服务器；没有 `.pub` 的是私钥，不要发给别人，也不要提交到 Git 仓库。

### 把公钥放到服务器

Linux / macOS：

```bash
ssh-copy-id user@example.com
```

如果没有 `ssh-copy-id`，可以手动追加：

```bash
cat ~/.ssh/id_ed25519.pub | ssh user@example.com "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

在 Windows PowerShell 中：

```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh user@example.com "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

服务器端权限建议：

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

## SSH 配置文件

配置文件位置：

| 系统 | 用户配置路径 |
| --- | --- |
| Linux / macOS | `~/.ssh/config` |
| Windows | `C:\Users\<用户名>\.ssh\config` |

示例：

```sshconfig
Host myserver
    HostName example.com
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 60
```

之后可以直接：

```bash
ssh myserver
scp file.txt myserver:/home/ubuntu/
rsync -avz ./dist/ myserver:/var/www/app/
```

常用配置项：

| 配置项 | 说明 |
| --- | --- |
| `Host` | 自定义别名 |
| `HostName` | 真实主机名或 IP |
| `User` | 默认登录用户 |
| `Port` | 默认端口 |
| `IdentityFile` | 指定私钥 |
| `ServerAliveInterval` | 定期发送保活包 |
| `ProxyJump` | 跳板机配置 |

## 流行 SSH 工具

| 工具 | 平台 | 适合场景 | 优点 | 不足 |
| --- | --- | --- | --- | --- |
| OpenSSH `ssh` | Windows / macOS / Linux | 标准远程登录、脚本、服务器管理 | 跨平台、最通用、和 VSCode/Git 集成最好 | 纯命令行，需要自己管理配置 |
| Windows Terminal | Windows | 本地 Shell + SSH 命令入口 | 和 PowerShell/WSL 集成好 | 不负责图形化 SSH 主机管理 |
| Tabby | Windows / macOS / Linux | 多服务器连接管理 | GUI 配置 SSH/SFTP，分组直观 | 相比原生命令行更重 |
| Termius | Windows / macOS / Linux / Mobile | 多设备 SSH 连接管理 | 跨设备同步、移动端友好 | 高级同步能力通常依赖账号 |
| PuTTY | Windows | 老牌 SSH 客户端、旧环境 | 兼容性强，资料多 | 配置方式偏老，和 OpenSSH 配置不完全通用 |
| MobaXterm | Windows | Windows 上的远程运维套件 | SSH、SFTP、X11、会话管理集中 | 商业功能较多，工具较重 |
| WinSCP | Windows | SFTP/SCP 文件管理 | 图形化传文件很方便 | 不是完整终端环境 |
| iTerm2 Profiles | macOS | macOS 上保存 SSH 会话 | 和日常终端融为一体 | 只在 macOS 上好用 |
| tmux / zellij | 服务器端 | 远程会话保持、分屏 | 断线不丢任务，非常适合服务器 | 需要先学快捷键 |
| mosh | Linux / macOS / 部分 Windows 环境 | 网络不稳定的远程终端 | 漫游和弱网体验好 | 需要服务端安装，不能完全替代 SSH |

> [!tip] 选择建议
> 如果你主要写代码，优先学 OpenSSH + `~/.ssh/config` + VSCode Remote-SSH；如果你主要管理很多服务器，再加 Tabby / Termius / MobaXterm 这类会话管理工具。

## VSCode Remote-SSH 集成

VSCode 的 `Remote - SSH` 可以让编辑器直接运行在远程服务器环境里：文件浏览、终端、Git、调试、扩展都可以面向远程主机。

### 基本流程

1. 安装 VSCode 扩展：`Remote - SSH`
2. 本机先确认命令行能连上：

```bash
ssh myserver
```

3. 配置 `~/.ssh/config`：

```sshconfig
Host myserver
    HostName example.com
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```

4. VSCode 中执行：

```text
Remote-SSH: Connect to Host...
```

5. 选择 `myserver`，连接后打开远程目录。

### Remote-SSH 常见能力

| 能力 | 用法 |
| --- | --- |
| 打开远程文件夹 | `Remote-SSH: Connect to Host...` 后选择目录 |
| 远程终端 | VSCode 内置终端会直接运行在远程服务器 |
| 远程安装扩展 | 扩展面板会区分 Local 和 SSH: Host |
| 端口转发 | `Ports` 面板里转发远程服务端口到本地 |
| 使用 SSH 配置 | 直接复用 `~/.ssh/config` |
| 跳板机 | 在 SSH config 中使用 `ProxyJump` |

端口转发示例：远程服务器运行了 `localhost:3000`，VSCode `Ports` 面板可以把它转发成本地 `http://localhost:3000`。

也可以写在 SSH config 里：

```sshconfig
Host myserver
    HostName example.com
    User ubuntu
    LocalForward 3000 127.0.0.1:3000
```

### 推荐设置

```json
{
  "remote.SSH.configFile": "~/.ssh/config",
  "remote.SSH.defaultExtensions": [
    "eamodio.gitlens",
    "ms-python.python"
  ],
  "remote.restoreForwardedPorts": true
}
```

> [!warning] Remote-SSH 的边界
> Remote-SSH 不是简单“同步文件”，而是让 VSCode Server 在远程主机上运行。远程机器 CPU、内存、磁盘、网络质量都会影响体验。

### 常见问题

| 问题 | 排查方向 |
| --- | --- |
| VSCode 能力和命令行不一致 | 先在本机终端跑通 `ssh myserver` |
| 私钥权限错误 | Linux/macOS 用 `chmod 600 ~/.ssh/id_ed25519` |
| 远程扩展不可用 | 确认扩展是否支持 Remote 环境 |
| 连接卡在安装 VSCode Server | 检查远程磁盘空间、Shell 输出、代理、防火墙 |
| 端口打不开 | 检查远程服务监听地址和 VSCode Ports 转发 |

## 文件传输

### scp：简单复制

本地上传到服务器：

```bash
scp file.txt user@example.com:/home/user/
scp -P 2222 file.txt user@example.com:/home/user/
scp -r ./dist user@example.com:/var/www/app/
```

服务器下载到本地：

```bash
scp user@example.com:/home/user/file.txt .
scp -r user@example.com:/var/log/nginx ./nginx-logs
```

> [!note] 端口参数大小写
> `ssh` 指定端口是 `-p`，`scp` 指定端口是 `-P`。

### sftp：交互式文件管理

```bash
sftp user@example.com
```

进入后常用命令：

| 命令 | 说明 |
| --- | --- |
| `pwd` | 查看远程目录 |
| `lpwd` | 查看本地目录 |
| `ls` | 列出远程文件 |
| `lls` | 列出本地文件 |
| `cd <目录>` | 切换远程目录 |
| `lcd <目录>` | 切换本地目录 |
| `put file.txt` | 上传文件 |
| `get file.txt` | 下载文件 |
| `put -r dir` | 上传目录 |
| `get -r dir` | 下载目录 |
| `exit` | 退出 |

### rsync：高效同步目录

上传目录：

```bash
rsync -avz ./dist/ user@example.com:/var/www/app/
```

下载目录：

```bash
rsync -avz user@example.com:/var/www/app/ ./app-backup/
```

删除远端多余文件，使两边保持一致：

```bash
rsync -avz --delete ./dist/ user@example.com:/var/www/app/
```

> [!warning] `--delete`
> `rsync --delete` 会删除目标端多余文件。执行前先用 `--dry-run` 预演。

```bash
rsync -avz --delete --dry-run ./dist/ user@example.com:/var/www/app/
```

## 端口转发

### 本地端口转发

把本地 `8080` 转发到远程服务器能访问的 `127.0.0.1:80`：

```bash
ssh -L 8080:127.0.0.1:80 user@example.com
```

访问：

```text
http://127.0.0.1:8080
```

常见用途：

- 访问服务器内网 Web 服务
- 临时访问远程数据库管理后台
- 调试只监听 `127.0.0.1` 的远程服务

### 远程端口转发

把远程服务器的 `8080` 转发到本机的 `3000`：

```bash
ssh -R 8080:127.0.0.1:3000 user@example.com
```

常见用途：

- 临时把本机开发服务暴露给远程服务器访问
- 远程回连调试

### 动态端口转发

创建 SOCKS 代理：

```bash
ssh -D 1080 user@example.com
```

然后在浏览器或系统代理里设置 SOCKS5：

```text
127.0.0.1:1080
```

> [!note] 保持后台转发
> `-N` 表示不执行远程命令，`-f` 表示进入后台。

```bash
ssh -N -f -L 8080:127.0.0.1:80 user@example.com
```

## 跳板机

命令行写法：

```bash
ssh -J jumpuser@jump.example.com user@internal.example.com
```

配置文件写法：

```sshconfig
Host jump
    HostName jump.example.com
    User jumpuser

Host internal
    HostName 10.0.0.10
    User ubuntu
    ProxyJump jump
```

使用：

```bash
ssh internal
```

## SSH Agent

SSH Agent 可以缓存私钥密码，避免每次输入。

Linux / macOS：

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l
```

Windows PowerShell：

```powershell
Get-Service ssh-agent
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
ssh-add -l
```

## 服务端配置

OpenSSH 服务端配置文件通常在：

```text
/etc/ssh/sshd_config
```

常见配置：

```sshconfig
Port 22
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AllowUsers ubuntu
```

重启服务：

```bash
sudo systemctl restart ssh
sudo systemctl restart sshd
```

查看状态：

```bash
sudo systemctl status ssh
sudo systemctl status sshd
```

> [!warning] 改 SSH 配置前
> 修改 `sshd_config` 前先保留一个已登录的终端，不要立刻关闭。改错配置可能导致新连接进不去。

## Git 使用 SSH

测试 GitHub SSH：

```bash
ssh -T git@github.com
```

仓库地址示例：

```bash
git clone git@github.com:username/repo.git
git remote set-url origin git@github.com:username/repo.git
```

如果有多个 Git 平台账号，可以用 `~/.ssh/config` 区分：

```sshconfig
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal

Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
```

使用：

```bash
git clone git@github-personal:username/repo.git
```

## 常见报错排查

### Permission denied publickey

可能原因：

- 公钥没有加入远程服务器的 `~/.ssh/authorized_keys`
- 使用了错误的私钥
- 远程用户名写错
- 服务器端 `.ssh` 或 `authorized_keys` 权限不正确

排查：

```bash
ssh -v user@example.com
ssh -i ~/.ssh/id_ed25519 user@example.com
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

### Connection timed out

可能原因：

- IP 或域名错误
- SSH 端口没有开放
- 防火墙或安全组拦截
- 服务器 SSH 服务未启动

排查：

```bash
ping example.com
nc -vz example.com 22
ssh -p 2222 user@example.com
```

Windows 可用：

```powershell
Test-NetConnection example.com -Port 22
```

### Host key verification failed

可能原因：

- 服务器重装导致指纹变化
- DNS 或 IP 指向了另一台机器
- `known_hosts` 中记录过旧

确认安全后再清理：

```bash
ssh-keygen -R example.com
ssh-keygen -R 192.168.1.10
```

### Too many authentication failures

客户端尝试了太多私钥。指定正确私钥：

```bash
ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes user@example.com
```

配置文件：

```sshconfig
Host myserver
    HostName example.com
    User ubuntu
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
```

## 安全建议

> [!tip] SSH 安全基线
> 正式服务器建议：使用密钥登录、关闭 root 登录、关闭密码登录、限制登录用户、开启防火墙和云安全组、定期检查登录日志。

常用检查：

```bash
last
lastb
journalctl -u ssh -n 100
sudo tail -n 100 /var/log/auth.log
```

高风险操作：

> [!warning] 谨慎操作
> 修改 `sshd_config`、删除 `~/.ssh/authorized_keys`、覆盖私钥、关闭防火墙规则、关闭 SSH 服务，都可能让你失去远程访问权限。
