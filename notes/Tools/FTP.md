---
title: FTP 使用笔记
aliases:
  - FTP
  - FTPS
  - SFTP
  - FTP 文件传输
tags:
  - tools/network
  - tools/ftp
  - file-transfer
  - server
  - cheatsheet
created: 2026-05-20
updated: 2026-05-20
---

# FTP 使用笔记

> [!info] 使用场景
> FTP 常用于服务器文件上传下载、站点部署、老系统文件交换。新项目优先考虑 **SFTP** 或 **FTPS**，避免使用明文 FTP 传输账号密码。

相关笔记：[[SSH]] | [[Linux Commands]] | [[Windows Commands]] | [[Mac Commands]] | [[Termimal & Shell Tools]]

## 快速索引

| 我想做什么 | 命令或工具 |
| --- | --- |
| 连接 FTP | `ftp example.com` |
| 连接 SFTP | `sftp user@example.com` |
| 下载文件 | `get remote.txt` |
| 上传文件 | `put local.txt` |
| 下载目录 | `mget *` / `mirror` |
| 上传目录 | `mput *` / `mirror -R` |
| 使用 curl 下载 | `curl -O ftp://user:pass@example.com/file.txt` |
| 使用 lftp | `lftp -u user,password ftp://example.com` |
| 图形客户端 | FileZilla / WinSCP / Cyberduck |

## FTP、FTPS、SFTP 的区别

| 协议 | 默认端口 | 是否加密 | 关系 | 适合场景 |
| --- | --- | --- | --- | --- |
| FTP | `21` | 不加密 | 传统文件传输协议 | 内网、旧系统兼容 |
| FTPS | `21` 或 `990` | 加密 | FTP + TLS | 需要兼容 FTP 生态并加密 |
| SFTP | `22` | 加密 | SSH File Transfer Protocol | 现代服务器文件传输，推荐 |

> [!warning] SFTP 不是 FTP
> SFTP 走 SSH 协议，通常端口是 `22`；FTP/FTPS 走 FTP 协议，控制端口通常是 `21`。两者命令体验相似，但协议完全不同。

## 常用客户端

| 工具 | 平台 | 说明 |
| --- | --- | --- |
| FileZilla | Windows / macOS / Linux | 常见图形化 FTP/FTPS/SFTP 客户端 |
| WinSCP | Windows | Windows 上很好用的 SFTP/FTP 客户端 |
| Cyberduck | macOS / Windows | 图形化文件传输工具 |
| `ftp` | 多平台 | 基础命令行 FTP 客户端 |
| `sftp` | 多平台 | OpenSSH 自带的 SFTP 客户端 |
| `lftp` | Linux / macOS | 强大的命令行 FTP/FTPS/SFTP 客户端 |
| `curl` | 多平台 | 适合脚本化下载上传 |

> [!tip] 选择建议
> 临时传文件用图形客户端最省心；服务器之间同步目录用 `rsync` 或 `lftp mirror`；如果服务器支持 SSH，优先用 [[SSH]] 里的 `sftp` / `scp` / `rsync`。

## 流行 FTP / SFTP 工具对比

| 工具 | 协议 | 平台 | 适合场景 | 优点 | 不足 |
| --- | --- | --- | --- | --- | --- |
| FileZilla | FTP / FTPS / SFTP | Windows / macOS / Linux | 通用图形化传文件 | 免费、跨平台、上手快 | 不是代码编辑环境 |
| WinSCP | SFTP / SCP / FTP / FTPS | Windows | Windows 服务器文件管理 | 双栏界面、和 PuTTY/编辑器配合好 | 主要面向 Windows |
| Cyberduck | FTP / FTPS / SFTP / 云存储 | macOS / Windows | 图形化文件传输、云存储 | 界面友好，协议多 | 批量自动化不如命令行 |
| Transmit | FTP / SFTP / 云存储 | macOS | macOS 高质量图形客户端 | 体验精致、稳定 | 付费，跨平台不足 |
| ForkLift | FTP / SFTP / SMB / 云存储 | macOS | 文件管理器 + 传输 | 适合日常文件整理 | 付费 |
| lftp | FTP / FTPS / SFTP | Linux / macOS | 自动化同步、镜像目录 | `mirror` 强大，适合脚本 | 命令行学习成本 |
| rclone | SFTP / FTP / 云存储 | 多平台 | 云存储和远程目录同步 | 后端很多，脚本友好 | 配置项较多 |
| curl / wget | FTP / FTPS 等 | 多平台 | 单文件下载上传、脚本 | 系统常见，适合自动化 | 不适合交互式管理 |
| VSCode SFTP 扩展 | SFTP / FTP | VSCode | 编辑器内同步文件 | 保存即上传、项目级配置 | 不等于远程开发，误同步风险高 |

> [!warning] 工具选择原则
> 写代码优先 `VSCode Remote-SSH`；传文件优先 SFTP/FTPS；需要同步目录用 `rsync` 或 `lftp mirror`；明文 FTP 只适合可信内网或旧系统兼容。

## VSCode 中使用 FTP / SFTP

VSCode 里有三种常见方式：

| 方式 | 适合场景 | 特点 |
| --- | --- | --- |
| Remote-SSH | 远程服务器开发 | 推荐。直接打开远程目录，终端和扩展都在远程运行 |
| SFTP/FTP 扩展 | 本地编辑，保存后同步到服务器 | 适合静态站点、小项目、旧 FTP 主机 |
| VSCode Tasks 调用命令行 | 可重复部署流程 | 用 `rsync`、`lftp`、`scp` 写成任务，更可控 |

### 推荐：Remote-SSH 替代手工 SFTP

如果服务器支持 SSH，不建议把远程开发做成“本地编辑 + FTP 上传”。更稳的方式是：

1. 配好 `~/.ssh/config`
2. VSCode 安装 `Remote - SSH`
3. `Remote-SSH: Connect to Host...`
4. 直接打开远程项目目录

这样 Git、终端、调试、依赖安装都在远程环境中完成，少了同步错文件的问题。

### 使用 SFTP 扩展同步文件

常见流程：

1. 安装 SFTP 类扩展
2. 在项目中执行 `SFTP: Config`
3. 生成 `.vscode/sftp.json`
4. 配置远程路径和认证方式
5. 按需执行上传、下载、同步，谨慎开启保存自动上传

示例配置：

```json
{
  "name": "prod-server",
  "host": "example.com",
  "protocol": "sftp",
  "port": 22,
  "username": "ubuntu",
  "remotePath": "/var/www/app",
  "privateKeyPath": "~/.ssh/id_ed25519",
  "uploadOnSave": false,
  "ignore": [
    ".vscode",
    ".git",
    "node_modules",
    "dist"
  ]
}
```

FTP 示例：

```json
{
  "name": "legacy-ftp",
  "host": "example.com",
  "protocol": "ftp",
  "port": 21,
  "username": "user",
  "remotePath": "/public_html",
  "uploadOnSave": false
}
```

> [!warning] 不要把密码提交进仓库
> `.vscode/sftp.json` 可能包含服务器地址、用户名、密钥路径甚至密码。建议把敏感信息放到本机配置或环境变量，并把含密配置加入 `.gitignore`。

### 用 VSCode Tasks 调用 lftp

`.vscode/tasks.json` 示例：

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "deploy:lftp",
      "type": "shell",
      "command": "lftp -u $FTP_USER,$FTP_PASSWORD ftp://example.com -e \"mirror -R --delete ./dist /public_html; exit\"",
      "problemMatcher": []
    }
  ]
}
```

> [!tip] 自动化部署
> 如果项目有构建流程，可以把 `npm run build` 和 `lftp mirror` 拆成两个 task，或者交给 GitHub Actions / CI 去部署，减少手动上传出错。

## FTP 基本命令

连接：

```bash
ftp example.com
ftp 192.168.1.10
```

登录后常用命令：

| 命令 | 说明 |
| --- | --- |
| `open <主机>` | 连接服务器 |
| `user <用户名>` | 输入用户名登录 |
| `pwd` | 查看远程当前目录 |
| `lpwd` | 查看本地当前目录，部分客户端支持 |
| `ls` | 列出远程文件 |
| `cd <目录>` | 切换远程目录 |
| `lcd <目录>` | 切换本地目录 |
| `get <文件>` | 下载单个文件 |
| `put <文件>` | 上传单个文件 |
| `mget <模式>` | 批量下载 |
| `mput <模式>` | 批量上传 |
| `delete <文件>` | 删除远程文件 |
| `mkdir <目录>` | 创建远程目录 |
| `rmdir <目录>` | 删除远程目录 |
| `binary` | 二进制模式 |
| `ascii` | 文本模式 |
| `passive` | 切换被动模式，具体支持看客户端 |
| `bye` / `quit` | 退出 |

### 下载与上传

```ftp
ftp example.com
cd /public_html
lcd ~/Downloads
binary
get index.html
put style.css
bye
```

批量下载：

```ftp
prompt
mget *.log
```

批量上传：

```ftp
prompt
mput *.html
```

> [!note] `prompt`
> 在很多 FTP 客户端中，`mget` / `mput` 会逐个询问是否确认。执行 `prompt` 可以切换交互确认开关。

## SFTP 常用命令

SFTP 通过 SSH 加密传输：

```bash
sftp user@example.com
sftp -P 2222 user@example.com
sftp -i ~/.ssh/id_ed25519 user@example.com
```

登录后：

| 命令 | 说明 |
| --- | --- |
| `pwd` | 远程当前目录 |
| `lpwd` | 本地当前目录 |
| `ls` | 远程列表 |
| `lls` | 本地列表 |
| `cd <目录>` | 切换远程目录 |
| `lcd <目录>` | 切换本地目录 |
| `get file.txt` | 下载文件 |
| `put file.txt` | 上传文件 |
| `get -r dir` | 下载目录 |
| `put -r dir` | 上传目录 |
| `mkdir <目录>` | 创建远程目录 |
| `rm <文件>` | 删除远程文件 |
| `exit` | 退出 |

示例：

```bash
sftp user@example.com
```

```sftp
cd /var/www/app
lcd ./dist
put -r .
exit
```

## lftp 高级用法

安装：

```bash
sudo apt install lftp
brew install lftp
```

连接：

```bash
lftp -u user,password ftp://example.com
lftp sftp://user@example.com
```

常用命令：

| 命令 | 说明 |
| --- | --- |
| `ls` | 查看远程文件 |
| `lcd <目录>` | 切换本地目录 |
| `mirror <远程> <本地>` | 下载目录 |
| `mirror -R <本地> <远程>` | 上传目录 |
| `mirror --delete` | 同步删除目标端多余文件 |
| `pget -n 4 <文件>` | 多线程下载 |
| `set ftp:ssl-force true` | 强制 FTPS |
| `exit` | 退出 |

下载整个目录：

```bash
lftp -u user,password ftp://example.com -e "mirror /remote/path ./local/path; exit"
```

上传整个目录：

```bash
lftp -u user,password ftp://example.com -e "mirror -R ./dist /public_html; exit"
```

预演同步：

```bash
lftp -u user,password ftp://example.com -e "mirror -R --dry-run ./dist /public_html; exit"
```

> [!warning] `mirror --delete`
> `--delete` 会删除目标端多余文件。部署站点前建议先用 `--dry-run` 查看会发生什么。

## curl 与 wget

### curl 下载

```bash
curl -O ftp://user:password@example.com/file.txt
curl -u user:password -O ftp://example.com/file.txt
curl --ssl-reqd -u user:password -O ftp://example.com/file.txt
```

### curl 上传

```bash
curl -T local.txt ftp://user:password@example.com/path/
curl -u user:password -T local.txt ftp://example.com/path/
```

### wget 下载

```bash
wget ftp://user:password@example.com/file.txt
wget -r ftp://user:password@example.com/path/
```

> [!warning] 密码出现在命令历史里
> `ftp://user:password@host` 很方便，但密码会留在 shell 历史、进程列表或脚本中。重要账号尽量用交互输入、配置文件、环境变量或密钥方式。

## FTP 主动模式与被动模式

FTP 有两个连接：

- 控制连接：发送命令，默认端口 `21`
- 数据连接：传输文件和目录列表

| 模式 | 数据连接方向 | 常见问题 |
| --- | --- | --- |
| 主动模式 Active | 服务器主动连客户端 | 客户端在 NAT 或防火墙后容易失败 |
| 被动模式 Passive | 客户端主动连服务器开放的数据端口 | 服务器防火墙或被动端口范围没放行会失败 |

> [!tip] 实战建议
> 现代网络环境大多优先使用被动模式。若能登录但 `ls` 卡住、目录列表失败、文件传输失败，优先检查被动模式和防火墙端口。

## 服务器端常见配置点

常见 FTP 服务端：

| 服务端 | 说明 |
| --- | --- |
| vsftpd | Linux 上常见、轻量 |
| ProFTPD | 功能丰富 |
| Pure-FTPd | 配置相对简单 |
| FileZilla Server | Windows 上常见 |

以 vsftpd 为例，配置文件常见位置：

```text
/etc/vsftpd.conf
```

常见配置项：

```ini
listen=YES
anonymous_enable=NO
local_enable=YES
write_enable=YES
chroot_local_user=YES
pasv_enable=YES
pasv_min_port=40000
pasv_max_port=40100
```

重启：

```bash
sudo systemctl restart vsftpd
sudo systemctl status vsftpd
```

> [!warning] 防火墙
> FTP 除了控制端口 `21`，还需要开放被动模式端口范围，比如 `40000-40100`。云服务器还要检查安全组。

## 权限与路径

FTP 上传失败常见原因：

- 账号没有目标目录写权限
- 目录所有者不是当前用户
- 服务端开启了 chroot，用户被限制在家目录
- 磁盘满了
- 文件名或编码不兼容

Linux 服务端排查：

```bash
pwd
ls -lah
df -h
id
sudo chown -R user:user /path/to/upload
sudo chmod -R 755 /path/to/upload
```

> [!note] 权限不要一把梭
> 不建议为了省事直接 `chmod -R 777`。先确认服务运行用户、目录所有者和最小需要权限。

## 常见任务配方

### 用图形客户端连接

连接信息通常需要：

| 字段 | 示例 |
| --- | --- |
| 协议 | FTP / FTPS / SFTP |
| 主机 | `example.com` |
| 端口 | FTP `21`，SFTP `22`，FTPS 可能是 `21` 或 `990` |
| 用户名 | `user` |
| 密码或密钥 | 账号密码 / SSH 私钥 |
| 远程目录 | `/public_html` |

### 用 SFTP 上传站点目录

```bash
sftp user@example.com
```

```sftp
cd /var/www/app
lcd ./dist
put -r .
exit
```

### 用 lftp 部署静态站点

```bash
lftp -u user,password ftp://example.com -e "mirror -R --delete ./dist /public_html; exit"
```

先预演：

```bash
lftp -u user,password ftp://example.com -e "mirror -R --delete --dry-run ./dist /public_html; exit"
```

### 用 curl 上传单个文件

```bash
curl -u user:password -T ./index.html ftp://example.com/public_html/
```

### 下载远程日志

```bash
ftp example.com
```

```ftp
cd /logs
binary
mget *.log
bye
```

## 常见报错排查

### 能登录，但 `ls` 或传输卡住

优先检查：

- FTP 被动模式是否开启
- 服务器被动端口范围是否配置
- 防火墙和云安全组是否放行被动端口
- 客户端是否强制主动模式

### 530 Login incorrect

可能原因：

- 用户名或密码错误
- 账号被禁用
- 服务端禁止本地用户登录
- FTP 服务器要求 FTPS，但客户端使用了明文 FTP

### 550 Permission denied

可能原因：

- 目标目录没有写权限
- 用户被 chroot 到其他目录
- 文件已存在且不可覆盖
- 服务端配置禁止写入

### Connection refused

可能原因：

- FTP 服务没启动
- 端口不是 `21`
- 防火墙或安全组没有放行
- 服务器只支持 SFTP，不支持 FTP

排查：

```bash
nc -vz example.com 21
nc -vz example.com 22
```

Windows：

```powershell
Test-NetConnection example.com -Port 21
Test-NetConnection example.com -Port 22
```

## 安全建议

> [!tip] 文件传输安全基线
> 能用 SFTP 就优先用 SFTP；必须用 FTP 时，尽量改用 FTPS，关闭匿名登录，限制用户目录，使用强密码，并限制来源 IP。

高风险点：

> [!warning] 谨慎操作
> 明文 FTP 会暴露账号密码；`mirror --delete` 会删除目标端文件；`chmod -R 777` 会扩大权限；把密码写在脚本或命令历史里会留下泄露风险。
