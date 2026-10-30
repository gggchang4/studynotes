---
title: Linux 常用命令
aliases:
  - Linux Commands
  - Linux 命令速查
  - Linux命令大全
  - Bash 常用命令
tags:
  - tools/command
  - linux
  - bash
  - shell
  - cheatsheet
created: 2026-05-20
updated: 2026-10-26
---

# Linux 常用命令

> [!info] 范围与查阅方式
> 面向 Linux 桌面、服务器、开发环境和 WSL 的日常参考。先用下面的任务表定位，再查看对应命令的**语法、参数、示例和易错点**。主要采用 **Bash + GNU 工具**；systemd、包管理器及部分可选工具另标适用条件。这里只解释高频参数，完整选项以目标机器上的 `man`、`help`、`--help` 为准。
> 在 Obsidian 中可通过大纲折叠分类，也可用 `Ctrl+F` 直接搜索命令名。
>
> 示例中的 `app.log`、`src/`、`nginx`、`user@server.example.com` 都是场景名称，需要替换为实际对象；各代码块用于独立查阅，不要把整篇当作脚本连续执行。标有“修改”的命令会改变文件或系统状态。

相关笔记：[[Linux基础]] | [[服务器使用基础]] | [[Windows Commands]] | [[Mac Commands]] | [[Termimal & Shell Tools]] | [[WSL]] | [[SSH]]

## 00 任务速查与目录

| 我现在要做什么 | 常用入口 | 详细说明 |
| --- | --- | --- |
| 看不懂命令、参数或报错 | `man ls`、`help cd`、`type -a python` | [[#01 命令基础与帮助\|命令基础与帮助]] |
| 切目录、列文件、复制和删除 | `pwd`、`ls -lah`、`cp -a`、`rm -I` | [[#02 文件与目录\|文件与目录]] |
| 看文件、追日志、临时编辑 | `less`、`tail -F`、`nano`、`vim` | [[#03 文件查看与编辑\|文件查看与编辑]] |
| 找文件名、查代码或日志内容 | `find`、`grep`、`rg` | [[#04 文件查找与内容搜索\|查找与搜索]] |
| 统计、排序、替换、处理 JSON | `sort`、`uniq`、`sed`、`awk`、`jq` | [[#05 管道重定向与文本处理\|管道与文本]] |
| 解决权限或所有者问题 | `id`、`chmod`、`chown`、`sudo` | [[#06 用户身份与权限\|身份与权限]] |
| 找进程、结束任务、断线后继续工作 | `ps`、`pgrep`、`kill`、`tmux` | [[#07 进程与前后台任务\|进程与任务]] |
| 查服务状态和日志 | `systemctl`、`journalctl`、`dmesg` | [[#08 服务日志与关机\|服务与日志]] |
| 磁盘满、inode 满、挂载失败 | `df`、`du`、`lsblk`、`findmnt` | [[#09 磁盘空间与挂载\|磁盘与挂载]] |
| 看 CPU、内存、负载和 I/O | `uptime`、`free`、`vmstat`、`iostat` | [[#10 系统信息与资源观察\|系统与资源]] |
| 网络不通、DNS 异常、端口占用 | `ip`、`dig`、`ss`、`curl` | [[#11 网络诊断与下载\|网络与下载]] |
| 登录服务器、传文件、同步目录 | `ssh`、`scp`、`rsync` | [[#12 SSH 与文件传输\|远程与传输]] |
| 安装、查询、更新或删除软件 | `apt`、`dnf`、`pacman`、`zypper` | [[#13 软件包管理\|包管理]] |
| 打包、解压、校验下载文件 | `tar`、`zip`、`gzip`、`sha256sum` | [[#14 打包压缩与校验\|归档与校验]] |
| 配 PATH、环境变量和别名 | `export`、`env`、`source`、`alias` | [[#15 环境变量与 Shell 配置\|环境与配置]] |
| 定时运行脚本 | `crontab`、`systemctl list-timers` | [[#16 定时任务\|定时任务]] |
| 按现象逐步排错 | 磁盘满、服务失败、权限不足等 | [[#17 常见任务与排错配方\|任务配方]] |
| 选择终端、Shell 或配置 VS Code | 终端 / Shell / tmux 的分工 | [[#18 附录终端与开发环境\|终端附录]] |
| 核对来源和本笔记的验证范围 | 官方手册与本机帮助 | [[#19 参考资料与验证边界\|参考资料]] |

## 01 命令基础与帮助

### 1.1 命令由什么组成

一般形式：`命令 [选项] 参数...`。手册中的方括号表示“可选”，省略号表示“可以重复”，尖括号通常表示占位符；这些符号通常不需要照着输入。

```bash
ls -lh /var/log
cp -iv -- report.txt backup.txt
```

- `ls` 是命令；`-l` 和 `-h` 是选项，可合写为 `-lh`；`/var/log` 是操作对象。
- `cp` 中 `report.txt` 是源文件，`backup.txt` 是目标；`-i` 在覆盖前询问，`-v` 显示操作。
- `--` 表示选项结束：之后即使文件名以 `-` 开头，也作为操作对象处理。它是许多工具的约定，并非所有命令都支持。
- **大小写与上下文都重要**：`ssh -p` 指端口，`scp -P` 才指端口；`ls -h` 表示可读大小，其他命令的 `-h` 可能表示帮助。
- 短选项不总能直接拆开：`find -name` 是一个完整选项，`ps aux` 又采用 BSD 风格，不能简单套用 `ls -lah` 的规则。

### 1.2 路径、引号与通配符

| 写法 | 含义 | 例子或注意事项 |
| --- | --- | --- |
| `/etc/hosts` | 以 `/` 开始的绝对路径 | 不依赖当前目录 |
| `./app`、`../data` | 相对当前目录的路径 | `.` 为当前目录，`..` 为父目录 |
| `~`、`~/bin` | 当前用户的家目录 | `~` 需要处于可展开的位置；`"~/bin"` 不会做波浪号展开 |
| `"$HOME/bin"` | 展开变量，并保持为一个参数 | 路径包含空格时仍能正确传递 |
| `'文本'` | 单引号内保持字面内容 | `'$HOME'` 就是五个字符的变量名写法，不会展开 |
| `"文本 $变量"` | 双引号内允许变量和命令替换 | 通常给路径变量加双引号 |
| `*.log` | Shell 的文件名通配符 | 匹配当前目录相应文件，默认不含点开头文件 |
| `'*.log'` | 将模式原样交给命令 | `find . -name '*.log'` 由 find 匹配文件名 |
| `$(命令)` | 用命令输出替换这一部分 | `today=$(date +%F)`；尾部换行会被移除 |

```bash
cd "$HOME"
ls -l -- "My Notes.txt"
printf '%s\n' "$HOME"
find . -name '*.log'
```

**通配符与正则表达式是两套规则**：Shell 中 `*.log` 匹配文件名；`grep -E '.*\.log$'` 中 `.*` 才表示任意长度字符。不要把 `grep '*.log'` 当成搜索“以 .log 结尾”。

### 1.3 查帮助、定位命令与历史

| 命令与语法 | 用法说明 |
| --- | --- |
| `man [章节] 命令` | 本机手册；`man 1 printf` 查用户命令，`man 5 crontab` 查配置格式；`/关键词` 搜索，`n` 下一个，`q` 退出 |
| `命令 --help` | 常见外部命令的参数摘要；并非所有程序都接受此选项 |
| `help 内建命令` | Bash 内建命令帮助，例如 `help cd`、`help export` |
| `type -a 名称` | 列出名称可能解析到的别名、函数、内建命令和可执行文件 |
| `command -v 名称` | 查看当前 Shell 如何解析这个名称；适合检查工具是否存在 |
| `which 名称` | 通常从 PATH 查找外部程序；不同实现对别名、函数的支持不一，优先用前两种方式 |
| `history [数量]` | Bash 交互历史；`history 20` 看最近 20 条 |
| `clear` / `reset` | 前者清屏；后者用于终端显示异常时重新初始化终端 |

```bash
man 1 ls
help cd
type -a python
command -v curl
history 20
```

### 1.4 退出码与条件执行

命令结束后，`$?` 是**紧邻的上一条命令**的退出码。通常 `0` 表示成功、非 `0` 表示其他结果；具体含义由命令规定。`grep` 的 `1` 表示没有匹配，`diff` 的 `1` 表示有差异，都不等于程序崩溃。[GNU grep 退出码](https://www.gnu.org/software/grep/manual/html_node/Exit-Status.html)

```bash
grep -q 'ERROR' app.log
status=$?
printf 'grep exit status: %s\n' "$status"

mkdir -p backup && cp -iv -- report.txt backup/
```

- `A && B`：A 成功才运行 B。
- `A || B`：A 不成功才运行 B。
- `A; B`：A 结束后运行 B，不论 A 的结果。
- `A &`：异步运行 A；这不代表任务已经成功完成。
- 管道默认返回最后一个命令的退出码；Bash 的 `set -o pipefail` 可让管道在某一环失败时返回最右侧非零状态。`grep` 没匹配、`head` 提前关闭管道等也可能产生非零结果，需要按业务判断。[Bash 管道说明](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html)

### 1.5 交互快捷键

以下主要对应 Bash 默认的 Emacs 按键模式；终端和 Shell 配置可能覆盖它们。

| 按键 | 作用 |
| --- | --- |
| `Tab` / 连按两次 `Tab` | 补全 / 列出候选 |
| `Ctrl+C` | 通常向前台进程组发送 SIGINT；程序可以处理或忽略 |
| `Ctrl+D` | 在空输入处表示 EOF；空命令行上通常退出 Shell，不是通用的“结束进程” |
| `Ctrl+Z` | 通常挂起前台任务，之后可用 `jobs`、`fg`、`bg` 管理 |
| `Ctrl+A` / `Ctrl+E` | 到行首 / 行尾 |
| `Ctrl+U` / `Ctrl+K` | 删除光标前 / 后的行内容 |
| `Ctrl+W` / `Ctrl+Y` | 删除前一个词 / 粘回最近剪切内容 |
| `Ctrl+R` | 反向搜索历史；继续按可找更早的匹配 |
| `Ctrl+L` | 重绘并清屏 |

## 02 文件与目录

### 2.1 pwd、cd：定位与切换

**语法**：`pwd [-L|-P]`；`cd [目录]`。

| 写法 | 含义 |
| --- | --- |
| `pwd` / `pwd -L` | 显示逻辑路径，可能保留符号链接中的路径名 |
| `pwd -P` | 显示解析符号链接后的物理路径 |
| `cd /var/log` | 进入绝对路径 |
| `cd ..` | 进入父目录 |
| `cd` / `cd ~` | 回家目录 |
| `cd -` | 回到上次工作目录，并显示路径 |

`cd` 是 Shell 内建命令，因为它要改变当前 Shell 的工作目录。脚本中需要先切目录再操作时，用 `cd "$dir" || exit 1` 明确处理切换失败，避免在错误目录继续执行。

### 2.2 ls、tree：列出内容

**语法**：`ls [选项] [路径...]`；`tree [选项] [目录]`。`tree` 通常需安装。

| 参数 | 含义 |
| --- | --- |
| `ls -l` | 长格式：权限、链接数、所有者、组、大小、时间、文件名 |
| `-a` / `-A` | 包括点开头的隐藏文件；`-A` 排除 `.` 和 `..` |
| `-h` | 配合 `-l` / `-s` 用 K、M、G 等可读单位，通常按 1024 进位 |
| `-t` / `-r` | 按修改时间由新到旧 / 反转排序 |
| `-S` | 按文件大小由大到小排序 |
| `-d` | 显示目录本身，不展开目录内容 |
| `-R` | 递归列子目录，大目录输出可能非常多 |
| `tree -L 2` | 最多显示两层 |
| `tree -a -d` | 包括隐藏目录，只列目录 |

```bash
ls -lah
ls -lt /var/log
ls -ld /var/log
tree -L 2 .
```

长格式示例 `-rw-r--r-- 1 alice dev 1200 ... report.txt`：开头的 `-` 表示普通文件，`d` 表示目录，`l` 表示符号链接；后面九位是三组权限。`ls -lh` 的目录大小通常是目录自身的数据结构大小，**不是目录内所有文件的总大小**；总量用 `du`。脚本不要解析 `ls` 输出处理文件名，使用 `find -exec` 或 NUL 分隔。

### 2.3 mkdir、touch：创建目录与更新时间

**语法**：`mkdir [选项] 目录...`；`touch [选项] 文件...`。

| 参数 | 含义 |
| --- | --- |
| `mkdir -p` | 自动创建缺失的父目录，目标目录已存在时不报错 |
| `mkdir -m 700` | 指定新建目标目录权限；`-p` 创建的中间目录不由此参数统一设为 700 |
| `touch 文件` | 不存在则创建空文件；已存在则更新访问和修改时间，不清空内容 |
| `touch -c` | 不创建不存在的文件 |
| `touch -r 参考文件 文件` | 复制参考文件的访问和修改时间 |
| `touch -t 202610261430.00 文件` | 指定本地时间，格式为 `[[CC]YY]MMDDhhmm[.ss]` |

```bash
mkdir -p projects/demo/src
mkdir -m 700 private
touch notes.txt
touch -r notes.txt notes-copy.txt
```

### 2.4 cp：复制文件或目录【修改】

**语法**：`cp [选项] 源 目标`；多个源时，最后一个参数必须是目标目录。

| 参数 | 含义 |
| --- | --- |
| `-R` / `-r` | 递归复制目录；GNU 下二者均可，跨实现优先核对 `-R` 行为 |
| `-a` | 归档复制，相当于 GNU 的 `-dR --preserve=all`；保留链接并尽可能保留元数据 |
| `-p` | 保留权限、所有者和时间等指定基础属性，受执行权限和文件系统限制 |
| `-i` | 覆盖已有文件前询问 |
| `-v` | 显示复制操作 |
| `-L` / `-P` | 跟随源符号链接 / 保留源符号链接本身 |

```bash
cp -iv -- report.txt report.bak
cp -a -- src backup/
mkdir -p backup
cp -a -- src/. backup/
```

目标 `backup/` 已存在时，第二条生成 `backup/src/`；最后一条把 `src/` **里面的内容**复制到 `backup/`，也包括隐藏文件。目标不存在时，`cp -a src backup` 会直接创建名为 `backup` 的副本。复制前确认目标是否存在，默认覆盖不经过回收站。[GNU cp 手册](https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html)

### 2.5 mv：移动与重命名【修改】

**语法**：`mv [选项] 源 目标`。

| 参数 | 含义 |
| --- | --- |
| `-i` | 覆盖前询问 |
| `-v` | 显示移动过程 |
| `-T` | GNU 扩展：把目标当作精确目标路径，不按“放进目标目录”处理 |

```bash
mv -iv -- old.txt new.txt
mv -iv -- report.txt archive/
```

同一文件系统内通常只是目录项变化；跨文件系统通常需要复制再删除源文件，耗时和失败方式不同，不能一概当作瞬间或原子的操作。

### 2.6 rm、rmdir：删除【修改】

**语法**：`rm [选项] 文件...`；`rmdir [选项] 空目录...`。

| 参数 | 含义 |
| --- | --- |
| `rm -r` / `-R` | 递归删除目录及内容 |
| `rm -i` | 对每个删除对象询问 |
| `rm -I` | GNU 扩展：删除超过三个文件或递归删除时，先统一询问一次 |
| `rm -f` | 不询问，忽略不存在的对象；不会绕过文件系统权限 |
| `rm -v` | 输出删除的名称 |
| `rmdir -p a/b` | 删除空目录 b，并继续尝试删除变空的父目录 a |

```bash
rm -i -- old.txt
rm -rI -- old-output/
rmdir empty-dir
rm -- ./-strange-name
```

> [!warning] 删除前确认对象
> `rm` 通常没有回收站。先用 `pwd`、`ls -ld -- 路径`、`find ... -print` 确认范围。`rm -rf` 不适合当作日常默认写法。删除文件主要取决于父目录的写入和搜索权限，也受 sticky bit、ACL、只读挂载等限制；文件自身只读不等于不能被删除。

### 2.7 ln、readlink、realpath：链接与路径解析

**语法**：`ln [选项] 目标 链接名`；`readlink [选项] 链接`；`realpath [选项] 路径`。

| 命令 | 含义 |
| --- | --- |
| `ln file.txt hard-link.txt` | 创建硬链接：同一 inode 的另一个名称，通常不能跨文件系统，普通用户不能硬链接目录 |
| `ln -s target link` | 创建符号链接：保存目标路径，可以跨文件系统，也可以指向暂不存在的对象 |
| `readlink link` | 输出符号链接内保存的目标路径 |
| `readlink -f link` | GNU 下递归解析并输出规范绝对路径，除最终分量外的路径分量需存在 |
| `realpath -e 路径` | 解析规范绝对路径，要求所有路径分量存在 |

```bash
ln -s /opt/myapp/releases/v1 current
readlink current
realpath -e current
```

相对符号链接的目标是相对于**链接所在目录**解析，不是相对于执行命令时的当前目录。删除符号链接名称一般不会删除它所指向的目标。

### 2.8 file、stat：类型与元数据

| 命令 | 作用与参数 |
| --- | --- |
| `file 路径` | 根据内容等信息识别文件类型，扩展名不能可靠代表真实类型 |
| `file -L 链接` | 跟随符号链接，查看目标类型 |
| `stat 文件` | 查看大小、inode、权限、所有者和各时间戳 |
| `stat -c '%s %n' 文件` | GNU 格式化输出；`%s` 为字节数，`%n` 为名称 |
| `stat -L 链接` | 查看符号链接目标的元数据 |

```bash
file ./app
stat README.md
stat -c 'size=%s bytes; mode=%a; name=%n' README.md
```

`mtime` 是内容修改时间，`ctime` 是 inode 状态变化时间，`atime` 是访问时间；`ctime` **不是创建时间**。创建时间是否存在、是否能显示取决于文件系统和工具支持。

## 03 文件查看与编辑

### 3.1 cat、less：一次输出与分页阅读

**语法**：`cat [选项] [文件...]`；`less [选项] 文件`。

| 命令或参数 | 含义 |
| --- | --- |
| `cat a.txt b.txt` | 依次输出两个文件的内容；没有文件参数时读标准输入 |
| `cat -n` / `-b` | 对所有行 / 仅非空行编号 |
| `cat -A` | GNU 下显示制表符、行尾等不可见标记，适合检查 CRLF 等问题 |
| `less -N` | 分页时显示行号 |
| `less -S` | 长行不折行，可横向滚动 |
| `less +G` | 打开后直接到末尾 |

```bash
cat -n README.md
less -NS app.log
```

`less` 内：空格下一页，`b` 上一页，`g` 开头，`G` 末尾，`/词` 向后搜索，`?词` 向前搜索，`n` 下一个，`N` 反向，`q` 退出。大文件优先分页，不要用 `cat` 把整个日志刷满终端；二进制文件优先 `file`，再选择专门的查看器。

### 3.2 head、tail：首尾与持续追踪

| 命令或参数 | 含义 |
| --- | --- |
| `head -n 20 文件` | 前 20 行；不指定 `-n` 时默认 10 行 |
| `tail -n 50 文件` | 后 50 行；默认 10 行 |
| `tail -n +20 文件` | 从第 20 行开始一直输出到末尾 |
| `head -c 100 文件` | 前 100 字节，可能截断多字节字符 |
| `tail -f 文件` | 跟踪打开的文件描述符；适合仍写入同一个文件的日志 |
| `tail -F 文件` | GNU 下按文件名跟踪并重试，适合日志轮转后同名文件被重建的情况 |

```bash
head -n 20 app.log
tail -n 50 app.log
tail -n 100 -F app.log
```

追踪时按 `Ctrl+C` 停止。需要实时过滤时可用 `tail -F app.log | grep --line-buffered -i 'error'`，其中 `--line-buffered` 减少 grep 输出缓冲造成的延迟。

### 3.3 wc：行数、字数与字节数

**语法**：`wc [选项] [文件...]`。

| 参数 | 含义 |
| --- | --- |
| `-l` | 换行符数量；最后一行没有换行时，与直观“行数”可能差 1 |
| `-w` | 按空白分隔的词数，不是中文分词结果 |
| `-c` | 字节数 |
| `-m` | 字符数，依赖当前 locale 和字符编码 |

```bash
wc -l app.log
wc -cm README.md
```

### 3.4 nano、vim：临时编辑【修改】

**语法**：`nano 文件`；`vim 文件`。不同系统可能只有其中一个，精简环境常见 `vi`。

| 编辑器 | 最少需要掌握的操作 |
| --- | --- |
| nano | 直接输入；`Ctrl+O` 写入，再按 Enter 确认名称；`Ctrl+X` 退出；`Ctrl+W` 搜索。底部 `^` 表示 Ctrl |
| vim | `i` 进入插入；`Esc` 回普通模式；`:w` 保存；`:q` 退出；`:wq` 保存退出；`:q!` 放弃未保存修改；`/词` 搜索，`n` 下一处 |

```bash
nano config.txt
vim +20 config.txt
```

`vim +20` 打开后定位第 20 行。编辑配置前先备份，完成后运行相应程序的配置检查；需要权限时，可在 sudo 策略允许的情况下用 `sudoedit /etc/hosts` 编辑。

## 04 文件查找与内容搜索

### 4.1 find：按名称、类型、大小和时间找文件

**语法**：`find [起始路径...] [条件与动作]`。先给起始目录，后给筛选条件；GNU find 缺省路径为 `.`，缺省动作通常为 `-print`。

| 条件 / 动作 | 含义 |
| --- | --- |
| `-name '*.log'` / `-iname '*.log'` | 按基本文件名匹配 / 忽略大小写；模式加引号，避免 Shell 预先展开 |
| `-path '*/build/*'` | 按从起始路径形成的整条路径匹配 |
| `-type f` / `-type d` / `-type l` | 普通文件 / 目录 / 符号链接 |
| `-maxdepth 2` / `-mindepth 1` | GNU 下最多向下两层 / 不匹配起始目录本身 |
| `-size +100M` | 大于 100 MiB；GNU find 的 M 为 1024² 字节，按单位向上取整后比较 |
| `-size +104857600c` | 以字节为单位比较，明确表达大于 100 MiB |
| `-mtime -7` | 内容修改距现在不足 7 个 24 小时，不是“本周” |
| `-mmin -60` | 最近不足 60 分钟修改过 |
| `-newermt '2026-10-20'` | GNU 扩展：内容修改时间晚于给定时间，时区按本机设置 |
| `-empty` | 空文件或空目录 |
| `-print` / `-print0` | 换行 / NUL 分隔输出文件名 |
| `-exec 命令 {} +` | 把匹配对象分批作为参数传给命令；`{}` 表示文件名 |
| `-delete` | 直接删除匹配对象；这是写操作，会隐含 `-depth`，不能随便与 `-prune` 组合 |

```bash
find . -type f -name '*.md' -print
find /var/log -type f -name '*.log' -mtime -7 -print
find . -type f -size +100M -print
find . -type f \( -name '*.log' -o -name '*.txt' \) -print
find . -type d -name .git -prune -o -type f -name '*.py' -print
find . -type f -name '*.log' -exec wc -l -- {} +
```

相邻条件默认是 AND，`-o` 表示 OR；AND 优先于 OR，因此“log 或 txt，且都是文件”要加括号，并用 `\(`、`\)` 防止 Shell 解释括号。`-prune` 跳过子树，上例排除 `.git`。

时间的 `n`、`+n`、`-n` 是对取整后的时间单位比较：`-mtime 1` 为距现在约 24～48 小时，`-mtime +7` 为至少 8 个 24 小时；若需要明确时间边界，使用 `-newermt` 更直观。[GNU find 时间规则](https://www.gnu.org/software/findutils/manual/html_node/find_html/Age-Ranges.html)

### 4.2 grep：在文本中筛选匹配行

**语法**：`grep [选项] 模式 [文件...]`。

| 参数 | 含义 |
| --- | --- |
| `-n` / `-H` | 显示行号 / 即使只有一个文件也显示文件名 |
| `-i` | 忽略大小写 |
| `-v` | 反选：输出不匹配的行 |
| `-E` | 使用扩展正则，例如 `error\|warning`；默认是基本正则 |
| `-F` | 把模式作为固定字符串，句点等不作正则解释 |
| `-w` / `-x` | 匹配完整词 / 完整行；词边界按工具和 locale 定义 |
| `-r` / `-R` | 递归目录；GNU `-r` 不跟随递归遇到的符号链接，`-R` 会跟随 |
| `-l` / `-c` | 只输出有匹配的文件名 / 每个输入文件的匹配行数 |
| `-A 3` / `-B 3` / `-C 3` | 显示匹配行之后 / 之前 / 前后 3 行 |
| `-q` | 不输出，主要用退出码判断是否存在匹配 |
| `-e 模式` | 指定模式，可重复；模式以 `-` 开头时也适用 |
| `--include='*.py'` / `--exclude-dir=.git` | GNU 下按文件名筛选 / 排除目录 |

```bash
grep -nF '127.0.0.1' access.log
grep -nEi 'error|warning' app.log
grep -nC 3 -e 'timeout' app.log
grep -rn --include='*.py' --exclude-dir=.git -e 'TODO' .
grep -c 'ERROR' app.log
```

`grep -c` 数的是**匹配行数**，一行中出现三次仍只算 1 行。返回码通常为 `0` 匹配、`1` 无匹配、`2` 出错；不要用 `2>/dev/null` 把“读不了文件”悄悄当成“没找到”。

### 4.3 rg：搜索项目内容【可选安装】

**语法**：`rg [选项] 模式 [路径...]`。默认递归搜索，通常尊重 `.gitignore` 等忽略规则，并跳过隐藏对象和二进制文件；这与 `grep -r` 的默认范围不同。

| 参数 | 含义 |
| --- | --- |
| `-n` / `-i` / `-F` | 行号 / 忽略大小写 / 固定字符串 |
| `-g '*.py'` / `-g '!vendor/**'` | 包含或排除匹配路径；glob 用引号保护 |
| `--hidden` | 允许搜索隐藏文件和目录，但仍会应用忽略规则 |
| `--no-ignore` | 不应用忽略文件规则，但不会自动包含隐藏文件 |
| `--files` | 列出将被搜索的文件，不搜索内容 |
| `-l` / `-c` | 仅匹配文件名 / 每文件匹配行数 |
| `-C 3` | 前后各带 3 行上下文 |

```bash
rg -n 'TODO' src/
rg -nF '127.0.0.1' .
rg -n -g '*.py' -g '!vendor/**' 'import ' .
rg --hidden --no-ignore -g '!.git/**' 'timeout' .
rg --files -g '*.md'
```

“搜不到”时先确认文件是否被忽略、是否隐藏、是否位于当前路径内。[ripgrep 使用指南](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md)

### 4.4 xargs：把输入变成命令参数

**语法**：`上游命令 | xargs [选项] 下游命令`。普通管道传递的是字节流；xargs 负责把流转换成一个或多个命令的参数。

| 参数 | 含义 |
| --- | --- |
| `-0` | 输入使用 NUL 分隔；与 `find -print0` 配合处理含空格、引号、换行的文件名 |
| `-r` | GNU 扩展：输入为空时不执行下游命令 |
| `-n 20` | 每批最多传 20 个输入参数 |
| `-P 4` | 最多同时执行 4 个进程；仅适合彼此独立且允许并发的任务 |
| `-I {}` | 在命令中用 `{}` 替换输入项；改变输入分组方式，通常逐项执行 |

```bash
find ./logs -type f -name '*.log' -print0 | xargs -0 -r sha256sum --
find ./logs -type f -name '*.log' -exec sha256sum -- {} +
```

上面两种写法都能避免按空白拆坏文件名；只需对 find 结果执行命令时，`-exec ... {} +` 通常更直接。不要使用 `for f in $(find ...)` 或 `ls | xargs ...` 处理任意文件名。[GNU Findutils 文件名处理](https://www.gnu.org/software/findutils/manual/html_node/find_html/Safe-File-Name-Handling.html)

## 05 管道重定向与文本处理

### 5.1 标准输入输出与重定向

进程通常有三个标准文件描述符：`0` 标准输入 stdin，`1` 标准输出 stdout，`2` 标准错误 stderr。**重定向由 Shell 在启动命令前处理**。[Bash 重定向](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)

| 写法 | 含义 |
| --- | --- |
| `命令 < input.txt` | 从文件读取标准输入 |
| `命令 > out.log` | 标准输出写文件，文件存在则先截断；即使命令随后失败，也可能已经截断 |
| `命令 >> out.log` | 标准输出追加到文件 |
| `命令 2> err.log` | 只重定向标准错误 |
| `命令 > all.log 2>&1` | 先让 stdout 指向文件，再让 stderr 指向 stdout 的同一去处 |
| `命令 2>&1 > out.log` | 顺序不同：stderr 仍指向原 stdout，只有 stdout 写文件 |
| `命令 &> all.log` | Bash 中合并 stdout 与 stderr 后写文件 |
| `/dev/null` | 丢弃输出的特殊设备；排错时不要过早丢掉 stderr |

管道 `A | B` 把 A 的标准输出接到 B 的标准输入，不自动包含 A 的标准错误；Bash 的 `A |& B` 会同时传递两者。

```bash
grep -i 'error' app.log | wc -l
my_program > stdout.log 2> stderr.log
my_program > combined.log 2>&1
```

`sudo echo ... > /etc/某文件` 不能解决重定向权限问题，因为 `>` 仍由当前 Shell 执行。需要以管理员权限写文件时，用 `sudoedit`，或审查内容后用 `printf ... | sudo tee ...`；`tee` 默认也会覆盖文件。

### 5.2 tee：一边显示一边保存【写文件】

**语法**：`命令 | tee [选项] 文件...`。输入既输出到屏幕，也写入指定文件。

```bash
printf '%s\n' 'build started' | tee build.log
printf '%s\n' 'build finished' | tee -a build.log
```

`-a` 表示追加；不加则覆盖。要同时记录标准错误，使用 `命令 2>&1 | tee 文件`。注意管道的退出码规则，不能仅因 tee 成功就断定上游成功。

### 5.3 sort、uniq：排序与相邻去重

**语法**：`sort [选项] [文件...]`；`uniq [选项] [输入 [输出]]`。

| 参数 | 含义 |
| --- | --- |
| `sort -n` | 按数值排序，避免 `10` 排在 `2` 前面 |
| `sort -h` | GNU 下识别 K、M、G 等可读大小 |
| `sort -r` | 反向排序 |
| `sort -k 2,2n` | 仅以第 2 个字段作数值排序键；默认字段按空白划分 |
| `sort -t ':'` | 指定字段分隔符 |
| `sort -u` | 排序并按排序比较规则去重 |
| `uniq -c` | 对相邻重复行计数 |
| `uniq -d` / `-u` | 只显示重复过的行 / 只显示未重复的行 |

```bash
sort names.txt | uniq -c | sort -nr
du -h --max-depth=1 . | sort -hr
LC_ALL=C sort names.txt
```

`uniq` 只合并**相邻**相同行，所以无序输入通常先 sort。排序受 locale 影响；`LC_ALL=C` 只对这一条命令设置确定的字节排序环境。[GNU sort](https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html)、[GNU uniq](https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html)

### 5.4 cut、tr、paste：字段、字符与行的组合

| 命令与语法 | 参数含义与用途 |
| --- | --- |
| `cut -d ':' -f 1 /etc/passwd` | `-d` 指定单字符分隔符，`-f` 选字段，从 1 开始；`-f 1,3` 选两列，`-f 2-4` 选范围 |
| `cut -b 1-10 文件` | `-b` 按字节位置选择，可能截断 UTF-8 字符，不等于按字符数或终端显示宽度裁剪 |
| `tr '[:lower:]' '[:upper:]'` | 转换大小写，从标准输入读取；不是直接接收文件名参数 |
| `tr -d '\r'` | 删除回车字符；常用于确认是 CRLF 的文本转换，不用于任意二进制数据 |
| `tr -s ' '` | 将连续重复的空格压缩成一个，不会自动去除行首空格 |
| `paste -d ',' a.txt b.txt` | 把两个文件对应行并排连接，用逗号分隔；不会自动生成规范 CSV 转义 |

```bash
cut -d ':' -f 1,3 /etc/passwd
printf '%s\n' 'hello linux' | tr '[:lower:]' '[:upper:]'
tr -d '\r' < windows.txt > unix.txt
```

`cut -d ' ' -f 2` 不会把连续空格当成一个分隔符；对齐的命令输出更适合 awk。含引号、转义逗号或跨行字段的 CSV 需要专门的 CSV 解析器。

### 5.5 sed：按行筛选与替换

**语法**：`sed [选项] '程序' [文件...]`。默认把处理后的内容输出到 stdout，原文件不变。

| 写法 | 含义 |
| --- | --- |
| `sed -n '10,20p' 文件` | `-n` 关闭默认输出；`10,20` 指行范围，`p` 打印 |
| `sed 's/old/new/' 文件` | 每行仅替换第一个匹配 |
| `sed 's/old/new/g' 文件` | `g` 替换每行所有匹配 |
| `sed '/^#/d' 文件` | 删除以 `#` 开头的行，仅影响输出 |
| `sed -E '正则' 文件` | 使用扩展正则 |
| `sed -i.bak 's/old/new/g' 文件` | 原地修改，并把原内容备份到 `.bak`；GNU 与 BSD 的 `-i` 细节有差异 |

```bash
sed -n '10,20p' app.log
sed 's/debug=false/debug=true/g' app.conf
# 确认预览无误后，才原地修改并留备份
sed -i.bak 's/debug=false/debug=true/g' app.conf
```

替换式左侧是正则，右侧的 `&` 代表整个匹配内容；含 `/` 的路径可换分隔符，例如 `s|/old/path|/new/path|g`。不要写 `sed '...' file > file`，因为 Shell 会在 sed 读取前清空 file。[GNU sed 参数](https://www.gnu.org/software/sed/manual/html_node/Command_002dLine-Options.html)

### 5.6 awk：按字段筛选与计算

**语法**：`awk [选项] '条件 { 动作 }' 文件`。默认按行处理，以连续空白分字段。

| 写法 | 含义 |
| --- | --- |
| `$0` / `$1` / `$2` | 整行 / 第一字段 / 第二字段；单引号保护程序，避免被 Shell 展开 |
| `NR` / `NF` | 已读记录数量 / 当前记录字段数 |
| `-F ':'` | 指定输入字段分隔符 |
| `-v name=value` | 从命令行给 awk 变量赋值 |
| `BEGIN { ... }` / `END { ... }` | 处理任何行前 / 所有行后执行 |

```bash
awk -F ':' '{print $1, $3}' /etc/passwd
awk '$3 > 80 {print $1, $3}' scores.txt
awk '{sum += $2} END {print sum}' data.txt
awk -v limit=100 '$2 > limit {print $0}' data.txt
```

第二条假设输入的第三字段是分数，第三、四条假设第二字段是数字。逗号分隔的 `print` 参数默认用空格连接。awk 很适合规则文本；JSON 用 jq，复杂 CSV 用相应解析库。[GNU awk 用户手册](https://www.gnu.org/software/gawk/manual/gawk.html)

### 5.7 jq：查询 JSON【可选安装】

**语法**：`jq [选项] '过滤表达式' [文件...]`。

| 写法 | 含义 |
| --- | --- |
| `jq '.' 文件` | 解析并格式化 JSON，也可用来发现格式错误 |
| `jq '.name' 文件` | 取对象的 name 字段 |
| `jq -r '.name' 文件` | 字符串输出不带 JSON 引号 |
| `jq '.items[]' 文件` | 遍历 items 数组的元素 |
| `jq '.items[] \| select(.enabled == true)' 文件` | 只输出 enabled 为 true 的元素 |
| `jq --arg name "$name" '.name == $name' 文件` | 安全传入字符串变量，不手工拼接 jq 程序 |

```bash
jq '.' response.json
jq -r '.items[] | select(.enabled == true) | .name' response.json
```

JSON 中的字符串、布尔值、数字是不同类型，`.enabled == "true"` 与 `.enabled == true` 不等价。[jq 手册](https://jqlang.org/manual/)

### 5.8 diff、cmp：比较内容

| 命令 | 用法与结果 |
| --- | --- |
| `diff -u old.conf new.conf` | `-u` 输出统一格式差异，`-` 为旧内容、`+` 为新内容 |
| `diff -r dir-a dir-b` | 递归比较目录内容 |
| `diff -q a b` | 只报告是否不同 |
| `cmp a.bin b.bin` | 逐字节比较，适合二进制文件；默认报告第一个差异 |
| `cmp -s a.bin b.bin` | 静默比较，仅看退出码 |

`diff` 通常以 `0` 表示相同、`1` 表示存在差异、`2` 表示出错；不要在自动脚本中把“发现差异”直接混同于“命令执行失败”。

## 06 用户身份与权限

### 6.1 whoami、id、groups：确认当前身份

| 命令 | 含义 |
| --- | --- |
| `whoami` | 当前有效用户的名称，sudo 后可能与登录用户不同 |
| `id [用户]` | 用户的 UID、主 GID 和附加组；不指定用户则查询当前进程身份 |
| `id -u` / `id -g` | 只显示有效 UID / 有效主 GID |
| `id -un` / `id -Gn` | 当前用户名 / 当前组名列表 |
| `groups [用户]` | 查看组成员关系 |

```bash
whoami
id
id -Gn
```

用户被加入新组后，已有会话通常不会自动取得新的附加组；重新登录再用 `id` 检查。

### 6.2 先理解文件和目录的 rwx

权限分为所有者 `u`、所属组 `g`、其他人 `o` 三组；`a` 表示所有类别。普通访问控制会根据身份选择相应类别，并非把三组权限简单叠加。

| 权限 | 对普通文件 | 对目录 |
| --- | --- | --- |
| `r = 4` | 读取内容 | 列出目录项名称 |
| `w = 2` | 修改文件内容 | 配合 `x`，创建、删除或重命名目录项 |
| `x = 1` | 允许执行，还需文件格式、解释器和挂载选项等支持 | 搜索、穿过目录，访问里面已知名称的对象 |

访问 `/a/b/file` 需要对沿途目录具有搜索权限。删除一个文件通常取决于其父目录的权限，而非只看文件的 `w`。ACL、SELinux/AppArmor、sticky bit、只读或 `noexec` 挂载也可能影响结果。

### 6.3 chmod：修改权限【修改】

**语法**：`chmod [选项] 模式 文件...`。

| 写法 | 含义 |
| --- | --- |
| `chmod u+x script.sh` | 只给所有者增加执行权限 |
| `chmod go-w file.txt` | 撤销组和其他人的写权限 |
| `chmod u=rw,g=r,o= file.txt` | 显式指定三类权限，未列出的位会被清除 |
| `chmod 644 file.txt` | `rw-r--r--`：所有者可读写，其余只读 |
| `chmod 755 script.sh` | `rwxr-xr-x`：所有者可读写执行，其余可读执行 |
| `chmod 700 private-dir` | 仅所有者可访问目录 |
| `chmod -R u+rwX project/` | 递归设置；大写 `X` 只给目录或已有任一执行位的文件增加执行位 |

```bash
chmod u+x deploy.sh
./deploy.sh
chmod 600 "$HOME/.ssh/id_ed25519"
```

数字中每位为 `r+w+x` 的和，例如 `6 = 4+2`。`chmod -R 755` 会把普通数据文件也设成可执行；不要把 `chmod -R 777` 当作权限问题的通用修复。特殊权限位如 setuid、setgid 和 sticky bit 需另看 `man chmod`。[GNU chmod](https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html)

### 6.4 chown、chgrp、umask：归属与新文件默认权限

| 命令与语法 | 作用与参数 |
| --- | --- |
| `chown 用户:组 文件` | 修改所有者和组；修改所有者通常需要 root |
| `chown -R 用户:组 目录` | 递归修改归属，先确认根路径和链接策略 |
| `chgrp 组 文件` | 仅修改组；普通用户只能在有相应权限时改到自己所属的组 |
| `umask` / `umask -S` | 查看当前 Shell 的创建权限屏蔽值 / 符号形式 |
| `umask 027` | 为当前 Shell 及后代新建对象屏蔽相应权限位，不修改已有对象 |

```bash
sudo chown alice:developers report.txt
chgrp developers report.txt
umask 027
```

新权限等于程序请求的基础权限再屏蔽 umask 对应位。常见程序以文件 `666`、目录 `777` 为基础：umask `022` 通常得到文件 `644`、目录 `755`；umask `027` 通常得到文件 `640`、目录 `750`。程序可请求更小权限，默认 ACL 也会改变计算，不能理解为固定的十进制减法。

### 6.5 sudo、sudoedit、su：以其他身份执行【可能修改系统】

| 写法 | 含义 |
| --- | --- |
| `sudo 命令 参数...` | 按 sudo 策略以目标身份执行，默认通常为 root |
| `sudo -u alice 命令` | 指定目标用户 |
| `sudo -l` | 查询当前用户获准执行的命令 |
| `sudo -k` | 使缓存的认证时间戳失效；下次是否重新认证仍由策略决定 |
| `sudo -i` | 启动目标用户的登录式 Shell，默认通常是 root |
| `sudoedit /etc/hosts` | 按策略用编辑器修改受保护文件 |
| `su - alice` | 切换为 alice 并建立登录环境；通常需要目标用户密码，认证取决于系统策略 |

```bash
sudo -l
sudo -u alice id
sudoedit /etc/hosts
```

`su alice` 与 `su - alice` 的环境初始化方式不同。sudo 是否存在、能执行哪些操作、是否保留环境变量，都由系统配置决定；不要直接把所有权限报错都升级为 root 执行。

## 07 进程与前后台任务

### 7.1 ps：进程快照

**语法**：`ps [选项]`。下面以 Linux 的 procps-ng 实现为基准。

| 写法 | 含义 |
| --- | --- |
| `ps aux` | BSD 风格：`a` 扩展到其他用户有终端的进程，`x` 包括无终端进程，`u` 采用面向用户的输出格式 |
| `ps -ef` | Unix 风格：`-e` 选全部进程，`-f` 显示完整格式，包括父进程 PPID |
| `ps -p 1234 -o pid,ppid,user,stat,%cpu,%mem,args` | 只选 PID 1234，并用 `-o` 指定输出字段 |
| `ps -eo pid,ppid,stat,%cpu,%mem,args --sort=-%cpu` | 自选全体进程字段，按 CPU 占用降序，GNU/procps-ng 选项 |
| `ps -L -p 1234` | 显示指定进程的线程 |

```bash
ps aux
ps -ef
ps -eo pid,ppid,stat,%cpu,%mem,args --sort=-%cpu | head -n 11
```

常看 `PID`、`PPID`、`STAT`、`%CPU`、`%MEM`、`RSS`、`COMMAND/ARGS`。`RSS` 是驻留内存，通常按 KiB 显示；ps 的 `%CPU` 通常按进程生命周期内 CPU 时间比例计算，与 top 的刷新周期观察不等价。`STAT` 中 `R` 可运行、`S` 可中断睡眠、`D` 不可中断睡眠、`T` 停止、`Z` 僵尸；僵尸需要父进程回收，继续给僵尸发 kill 无法解决。[procps-ng ps 手册](https://man7.org/linux/man-pages/man1/ps.1.html)

### 7.2 pgrep、pkill、kill、killall：定位与发信号【可结束进程】

| 命令与参数 | 含义 |
| --- | --- |
| `pgrep -a 名称` | 按进程名正则查找，并显示 PID 与完整命令行 |
| `pgrep -x 名称` | 完整匹配进程名，减少误匹配 |
| `pgrep -f 模式` | 改为匹配完整命令行；范围可能明显扩大 |
| `pgrep -u alice -a 模式` | 限定有效用户；实际匹配仍需检查 |
| `kill -TERM 1234` | 向指定 PID 发 SIGTERM，请求有序退出；省略信号时通常也是 TERM |
| `kill -KILL 1234` / `kill -9 1234` | SIGKILL，不能由目标捕获处理；仅在确认对象且正常退出无效时使用 |
| `kill -STOP 1234` / `kill -CONT 1234` | 停止执行 / 继续执行 |
| `kill -l` | 列出支持的信号名称 |
| `pkill -TERM -x my_worker` | 按名称匹配后发信号，可能一次影响多个进程 |
| `killall -TERM my_worker` | Linux 常见 psmisc 实现按进程名发信号；其他 Unix 的 killall 行为可能不同 |

```bash
pgrep -a -x nginx
ps -p 1234 -o pid,ppid,user,stat,args
# 仅在确认 1234 确实是目标进程后执行
kill -TERM 1234
```

kill 是“发信号”，不是“保证立即消失”。进程可能处理 TERM、卡在不可中断等待中，或者被服务管理器自动重启。由 systemd 管理的服务优先用 `systemctl stop`，避免与自动重启策略相互干扰。

### 7.3 top、htop：持续观察资源

| 命令 | 常用参数或交互 |
| --- | --- |
| `top` | 默认交互；`P` 按 CPU、`M` 按内存、`1` 切换各 CPU、`H` 切换线程、`q` 退出 |
| `top -p 1234` | 关注指定进程 |
| `top -b -n 1` | `-b` 批处理输出，`-n 1` 采样一次，适合保存快照 |
| `htop` | 可选安装；F6 选择排序字段，F10 或 q 退出，按键依配置而异 |

```bash
top -p 1234
top -b -n 1 > top-snapshot.txt
```

多核系统中，多线程进程在常用显示模式下 `%CPU` 可能超过 100%。单次快照不能代表长期负载，注意观察时间窗口。

### 7.4 jobs、fg、bg、wait：当前 Shell 的作业

| 写法 | 含义 |
| --- | --- |
| `命令 &` | 在后台启动任务；仍可能继承终端输入输出 |
| `jobs -l` | 列出当前 Shell 管理的作业，并显示 PID |
| `fg %1` | 把编号 1 的作业放到前台 |
| `bg %1` | 让挂起的编号 1 作业在后台继续 |
| `$!` | 最近一个异步启动任务的 PID，需要及时保存 |
| `wait "$pid"` | 等待当前 Shell 的相应子进程，返回其退出状态 |

```bash
sleep 60 &
pid=$!
jobs -l
wait "$pid"
```

`%1` 是 Shell 作业号，不是 PID 1。`jobs` 不会列出其他 SSH 会话或其他 Shell 创建的后台任务。后台任务若尝试读取终端，可能再次被挂起。

### 7.5 nohup、tmux：长任务与会话保持

**nohup 语法**：`nohup 命令 参数... > 日志 2>&1 &`。

```bash
nohup python3 app.py > app.log 2>&1 < /dev/null &
printf 'pid=%s\n' "$!"
tail -F app.log
```

nohup 让启动的命令忽略 SIGHUP，并处理仍指向终端的标准流；**它本身不负责后台化**，末尾的 `&` 才负责。它不提供重启后恢复、失败自动重启或交互界面；系统的会话清理策略仍可能结束任务。长期服务使用 systemd 等服务管理器。

**tmux 语法**：`tmux 子命令 [选项]`，需要安装。

| 命令 / 按键 | 含义 |
| --- | --- |
| `tmux new -s work` | 创建名为 work 的会话并进入 |
| `tmux ls` | 列出当前用户的会话 |
| `tmux attach -t work` | 重新接入已有会话 |
| `tmux new -As work` | 已有则接入，没有则创建 |
| `Ctrl+b`，松开，再按 `d` | detach，离开界面并保留会话 |
| `Ctrl+b` 后按 `c` / `n` / `p` | 新建窗口 / 下一个 / 上一个窗口 |
| `Ctrl+b` 后按 `%` / `"` | 左右分屏 / 上下分屏 |

```bash
tmux new -s work
# 断线重连后，在新的 Shell 中接回
tmux attach -t work
```

tmux 的会话依赖其服务进程存活；主机重启、管理员回收会话或进程退出后，不能靠 attach 续跑。关闭 pane 中的 Shell 与 detach 的含义也不同。[tmux 官方入门](https://github.com/tmux/tmux/wiki/Getting-Started)

### 7.6 watch、timeout、time：重复观察与运行时间

| 命令 | 参数与用途 |
| --- | --- |
| `watch -n 2 'df -h /'` | 每 2 秒刷新一次输出；`-n` 指定秒数，Ctrl+C 停止 |
| `watch -d 'free -h'` | 高亮相邻刷新之间的差异 |
| `timeout 30s 命令` | GNU 工具：超时后默认发 TERM；`s/m/h` 为秒/分钟/小时 |
| `timeout -k 5s 30s 命令` | 30 秒时发 TERM，再过 5 秒仍未退出则发 KILL |
| `time 命令` | Bash 关键字：统计 real 墙钟时间、user 用户态 CPU 时间、sys 内核态 CPU 时间 |

```bash
watch -n 2 'df -h /'
time sha256sum large-file.bin
```

timeout 发生超时时通常返回 `124`，具体还受参数和信号情况影响。`/usr/bin/time` 若已安装，则是另一种外部程序，支持与 Bash `time` 不同的选项。

## 08 服务日志与关机

### 8.1 systemctl：管理 systemd 单元【部分命令修改系统】

**适用条件**：系统实际以 systemd 作为相应实例的服务管理器。容器、某些 WSL 配置和其他 init 系统不一定满足；可用 `ps -p 1 -o comm=` 查看 PID 1。安装了 systemctl 并不意味着 systemd 正在运行。

**语法**：`systemctl [选项] 子命令 [单元...]`。下面以已安装的 `nginx.service` 为例，实际名称需核对。

| 子命令 / 参数 | 作用 |
| --- | --- |
| `status nginx` | 状态、主进程和最近日志；有时需 sudo 才能看到完整日志 |
| `is-active nginx` / `is-enabled nginx` | 查询是否活动 / 是否启用，可供脚本检查退出码 |
| `start nginx` / `stop nginx` | 现在启动 / 停止 |
| `restart nginx` | 停止后重新启动，可能中断连接 |
| `reload nginx` | 要求服务重读自身配置，前提是服务支持 reload |
| `enable nginx` / `disable nginx` | 配置 / 撤销启用关系；通常对应开机拉起，不自动改变当前运行状态 |
| `enable --now nginx` | 同时启用并立即启动 |
| `disable --now nginx` | 同时禁用并立即停止 |
| `daemon-reload` | 重读 systemd 单元定义；修改 `.service` 等单元文件后使用，不等同于服务的 reload |
| `list-units --type=service --all` | 列出已加载服务，包括不活动项 |
| `list-unit-files --type=service` | 查看已安装服务单元的启用状态 |
| `--user` | 操作当前用户的服务管理器；通常不与 sudo 混用 |
| `--no-pager` / `--full` | 不使用分页器 / 不截短字段 |

```bash
systemctl status nginx --no-pager --full
systemctl --failed
sudo systemctl start nginx
sudo systemctl enable --now nginx
```

`active` 和 `enabled` 是不同维度；`static` 通常表示没有直接 enable 所需的安装配置，不等于服务损坏。服务管理器报告活动，也不保证业务接口一定可用，还需检查日志和实际请求。[systemctl 官方手册](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)

### 8.2 journalctl：查看 systemd 日志

**语法**：`journalctl [选项] [匹配条件...]`。

| 参数 | 含义 |
| --- | --- |
| `-u nginx.service` | 按服务单元过滤，可重复指定 |
| `-n 100` | 最近 100 条记录 |
| `-f` | 持续跟踪新增日志 |
| `-b` / `-b -1` | 本次启动 / 上一次启动，历史是否存在取决于持久化配置 |
| `-k` | 内核日志，通常限于本次启动 |
| `--since '1 hour ago'` / `--until '2026-10-26 12:00:00'` | 设置时间下界 / 上界，按本机时间环境解释 |
| `-p warning` | warning 及更严重的级别，不是只选 warning |
| `-o short-iso` | 用带日期和时区的较明确格式显示 |
| `--no-pager` | 直接输出 |
| `--disk-usage` | 查看 journal 文件占用 |

```bash
journalctl -u nginx.service -n 100 --no-pager
journalctl -u nginx.service --since '1 hour ago' -f
journalctl -b -p warning
journalctl --disk-usage
```

普通用户的可见范围取决于权限。`-f` 只说明正在跟踪日志，不代表服务无故障。需要清理 journal 时先确认保留要求；`--vacuum-time` 等清理选项会删除旧的**归档日志**，不应与只读查询混用。[journalctl 官方手册](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html)

### 8.3 dmesg：内核环形缓冲区

| 命令 | 含义 |
| --- | --- |
| `sudo dmesg` | 显示内核消息；是否必须 sudo 取决于 `dmesg_restrict` 等配置 |
| `sudo dmesg -T` | 转成人类可读的墙钟时间，休眠/时钟调整等情况下时间换算可能不精确 |
| `sudo dmesg -w` | 跟踪新增内核消息 |

```bash
sudo dmesg -T | tail -n 50
journalctl -k -b --no-pager
```

常用于设备识别、驱动、文件系统错误、OOM 等线索。dmesg 不是全部系统日志，环形缓冲区中的旧消息可能已被覆盖。

### 8.4 reboot、shutdown：重启与关机【影响整机】

以下是常见 systemd 系统的用法，其他实现需看本机帮助。

| 命令 | 含义 |
| --- | --- |
| `sudo systemctl reboot` / `sudo reboot` | 重启主机 |
| `sudo shutdown -h now` | 立即关机，常见 Linux 实现中 `-h` 默认进入关机流程 |
| `sudo shutdown -r +10` | 10 分钟后重启 |
| `sudo shutdown -c` | 取消尚未执行的计划关机/重启 |

远程执行前确认主机、未完成任务和维护窗口；这些操作会断开当前连接。

## 09 磁盘空间与挂载

### 9.1 df、du：文件系统容量与目录占用

**语法**：`df [选项] [路径...]`；`du [选项] [路径...]`。

| 参数 | 含义 |
| --- | --- |
| `df -h` | 以可读单位显示已挂载文件系统容量、已用和可用空间 |
| `df -T` | 同时显示文件系统类型 |
| `df -i` | 查看 inode 数量及使用率，大量小文件可能耗尽 inode |
| `df -h /var/log` | 查看该路径所在文件系统，而非该目录本身占多少 |
| `du -s` | 每个给定对象只显示汇总 |
| `du -h` | 可读单位，默认主要统计已分配磁盘块 |
| `du -d 1` / `--max-depth=1` | GNU 下显示到一层子目录，并保留总计 |
| `du -x` | 不跨入其他文件系统，适合定位某个分区内部占用 |
| `du -a` | 除目录外也输出文件 |
| `du --apparent-size` | GNU 下统计逻辑大小；稀疏文件可能与实际占用差很大 |

```bash
df -hT /
df -i /
du -sh -- ./data
du -xh --max-depth=1 /var | sort -hr
```

`df` 看文件系统，`du` 遍历可访问的目录项，因此数值可能不同：权限不足导致漏统计、已删除但仍打开的文件、快照、文件系统元数据、保留块、稀疏文件、其他挂载点等都可能产生差异。出现 `Permission denied` 时不能把不完整的 du 结果当成总量。[GNU du](https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html)

### 9.2 lsblk、blkid、findmnt：设备与文件系统的对应关系

| 命令 | 参数与用途 |
| --- | --- |
| `lsblk` | 树状显示块设备、分区及挂载关系，不等于文件系统空间统计 |
| `lsblk -f` | 显示文件系统类型、标签、UUID 等 |
| `lsblk -o NAME,SIZE,FSTYPE,UUID,MOUNTPOINTS` | `-o` 明确指定输出列；老版本可能只有 `MOUNTPOINT` |
| `sudo blkid` | 查询设备的文件系统标识；普通用户可能只能读到缓存或部分信息 |
| `findmnt` | 查看挂载树 |
| `findmnt -T /var/log` | `-T` 查询包含给定路径的文件系统 |
| `findmnt -o SOURCE,TARGET,FSTYPE,OPTIONS` | 查看设备、挂载点、类型及挂载选项 |

```bash
lsblk -f
findmnt -T /var/log
findmnt -o SOURCE,TARGET,FSTYPE,OPTIONS
```

硬盘、分区、文件系统、挂载点是不同层次。例如 `/dev/sdb1` 是分区设备，ext4 是文件系统类型，`/mnt/data` 是挂载入口。容器、网络文件系统、LVM 等布局可能更复杂。

### 9.3 mount、umount：挂载与卸载【修改挂载状态】

**语法**：`mount [选项] 设备 挂载点`；`umount 设备或挂载点`。以下 `/dev/sdX1` 只是设备占位名称，必须先用 lsblk 确认真实目标。

| 参数 | 含义 |
| --- | --- |
| `mount -t ext4` | 显式指定文件系统类型；许多常见格式可以自动识别 |
| `mount -o ro` | 申请只读挂载；需严格保证设备不被写入的取证场景还需考虑文件系统日志回放等行为 |
| `mount -o rw` | 申请可读写挂载，还受设备和文件系统状态限制 |
| `mount -a` | 按 `/etc/fstab` 处理可自动挂载项；会影响多个挂载，不是只做检查 |
| `umount /mnt/data` | 卸载挂载点；注意命令拼写是 umount |

```bash
sudo mkdir -p /mnt/data
sudo mount -o ro /dev/sdX1 /mnt/data
findmnt -T /mnt/data
# 确保无进程使用，且当前目录不在挂载点内，再卸载
cd "$HOME"
sudo umount /mnt/data
```

`target is busy` 时先确认当前目录、打开文件及子挂载；可用 `sudo lsof +f -- /mnt/data` 查询使用该文件系统的进程。挂载会暂时遮住挂载点原来的内容，不等于删除它。`mkfs`、`fdisk`、`parted`、向块设备写入的 `dd` 会改动数据布局，本参考不提供可直接误执行的格式化配方。

### 9.4 lsof：打开文件与已删除文件

**语法**：`lsof [选项] [文件...]`，通常需要安装；查看其他用户进程可能需要 sudo。

| 写法 | 含义 |
| --- | --- |
| `lsof /path/to/file` | 哪些进程打开了该文件 |
| `lsof -p 1234` | 哪个 PID 打开了哪些文件；`-p` 是进程，不是端口 |
| `sudo lsof +L1` | 筛选链接数小于 1 的打开文件，定位“已删除但仍占空间” |
| `sudo lsof -nP -iTCP:3000 -sTCP:LISTEN` | 查监听 TCP 3000 的进程；`-n` 不反查主机名，`-P` 不把端口转为服务名 |

```bash
sudo lsof +L1
sudo lsof -nP -iTCP:3000 -sTCP:LISTEN
```

看 `COMMAND`、`PID`、`FD`、`SIZE/OFF`、`NAME`，再决定如何让相关进程有序关闭或重开文件；不要只为释放空间就直接杀掉关键服务。[lsof 上游项目](https://github.com/lsof-org/lsof)

## 10 系统信息与资源观察

### 10.1 uname、hostnamectl、lscpu、date：机器与时间

| 命令 | 参数与含义 |
| --- | --- |
| `uname -r` / `-m` / `-a` | 内核发行号 / 机器架构 / 多项内核信息；不等于发行版版本 |
| `cat /etc/os-release` | 发行版名称、版本和 ID，具体字段可能有所不同 |
| `hostname` | 当前主机名 |
| `hostnamectl` | systemd 环境中查询主机、操作系统等信息；修改主机名需子命令和权限 |
| `lscpu` | CPU 架构、逻辑 CPU、核心和拓扑；虚拟机展示的是虚拟化后的信息 |
| `date -Is` | ISO 8601 风格日期时间，带时区偏移 |
| `date -u` | 以 UTC 显示时间，不会修改系统时间 |
| `date '+%F %T %Z'` | `%F` 为年月日，`%T` 为时分秒，`%Z` 为时区名称 |
| `timedatectl` | systemd 环境下查看时区、时间同步状态 |

```bash
uname -r
cat /etc/os-release
lscpu
date -Is
```

### 10.2 uptime：负载与运行时间

**语法**：`uptime`；`uptime -p` 用更直观的格式显示已运行时长。

输出常含当前时间、运行时长、登录用户数，以及最近 **1、5、15 分钟的 load average**。Linux 的负载包含可运行任务及不可中断等待任务，**不是 CPU 使用率**。应结合可用 CPU 数、I/O 和等待状态判断；容器内看到的值也不一定严格对应其 CPU 配额。

### 10.3 free：内存与交换区

**语法**：`free [选项]`。

| 参数 / 字段 | 含义 |
| --- | --- |
| `-h` | 可读单位 |
| `-m` / `-g` | 按 MiB / GiB 显示；整数取整可能掩盖小量变化 |
| `-s 2` | 每 2 秒刷新 |
| `total` | 系统可用物理内存总量 |
| `free` | 完全未使用的内存，通常不是判断应用还能分配多少的最佳指标 |
| `buff/cache` | 缓冲与缓存，部分可以回收 |
| `available` | 估计无需交换即可供新应用使用的内存，更适合初步判断余量 |
| `Swap` 行 | 交换区总量、已用和空闲；已用不为 0 本身不能证明此刻正在频繁换页 |

```bash
free -h
free -h -s 2
```

`used` 的具体计算方式在 procps 版本间可能变化，不要拿不同版本的列值机械对比。`available` 也不是某个容器一定还能使用的额度，需要结合 cgroup 限制。[procps-ng free 手册](https://man7.org/linux/man-pages/man1/free.1.html)

### 10.4 vmstat、iostat：持续采样

| 命令 | 参数与重点 |
| --- | --- |
| `vmstat 1 5` | 每 1 秒输出一次，共 5 次；首行的许多速率统计是开机以来平均，后续才是区间采样 |
| `vmstat -w 1 5` | 宽格式，减少字段挤在一起 |
| `iostat -xz 1 5` | sysstat 工具；`-x` 扩展设备指标，`-z` 隐藏空闲设备，按 1 秒间隔输出 |
| `iostat -y -xz 1 5` | `-y` 在区间采样时跳过开机以来的首份报告，需本机版本支持 |

```bash
vmstat 1 5
iostat -y -xz 1 5
```

vmstat 重点看 `r`（等待运行）、`b`（阻塞）、`si/so`（交换流入/流出速率）、`us/sy/id/wa`（CPU 时间分类）。iostat 重点看读写量、`await`（包含排队的平均完成延迟）、队列和 `%util`；现代并行存储设备的 `%util=100%` 不一定等价于已达到全部吞吐能力。首轮排错先看多次采样，再判断 CPU、内存或 I/O 方向。

## 11 网络诊断与下载

### 11.1 ip：地址、链路与路由

**语法**：`ip [选项] 对象 子命令`，属于 iproute2。下面均为查询；`ip addr add`、`ip route del` 等是配置修改，不要混淆。

| 命令 | 含义与输出重点 |
| --- | --- |
| `ip -br addr` | `-br` 简略格式；接口状态及 IPv4/IPv6 地址 |
| `ip addr show dev eth0` | `dev` 限定网卡；实际名称也可能是 ens33、enp3s0 等 |
| `ip link show` | 链路信息、MTU、MAC 地址；链路 UP 不等于已有可用 IP |
| `ip route` | IPv4 路由；看 `default via`、出口 `dev`、源地址 `src` |
| `ip -6 route` | IPv6 路由 |
| `ip route get 1.1.1.1` | 查询内核将如何路由到该地址，不会因此实际发送探测包 |
| `ip neigh` | IPv4 ARP / IPv6 邻居缓存 |

```bash
ip -br addr
ip route
ip route get 1.1.1.1
```

### 11.2 ping、tracepath、traceroute：连通性与路径

| 命令 | 参数与意义 |
| --- | --- |
| `ping -c 4 -W 2 example.com` | Linux iputils：`-c` 发 4 次，`-W` 设置等待响应超时秒数；不是整个命令只运行 2 秒 |
| `ping -4 example.com` / `ping -6 example.com` | 限定 IPv4 / IPv6 |
| `tracepath example.com` | 观察路径和路径 MTU，通常不需 root，可能需安装 |
| `traceroute -n example.com` | 逐跳探测；`-n` 不做地址反向解析，通常需安装 |

看 ping 的丢包率、往返延迟，以及是域名解析失败还是请求无响应。**ping 不通不能直接判定主机或 HTTPS 服务不可达**：ICMP 可能被过滤。traceroute 中某跳 `*` 也可能只是中间设备不回复探测，不足以断言该跳断网；还需测试目标协议和端口。

### 11.3 dig、nslookup、getent：DNS 与系统名称解析

| 命令 | 参数与用途 |
| --- | --- |
| `dig example.com A` | 查询 IPv4 地址；看 status、ANSWER、SERVER 和查询时间 |
| `dig example.com AAAA` / `dig example.com MX` | 查询 IPv6 / 邮件交换记录 |
| `dig +short example.com` | 简洁结果，但省略了排错所需的许多状态信息 |
| `dig @1.1.1.1 example.com A` | 指定 DNS 服务器；只在网络和组织策略允许时使用，结果未必与内部 DNS 相同 |
| `nslookup example.com` | 另一种 DNS 查询工具，交互与参数随实现有所区别 |
| `getent ahosts example.com` | 按系统 NSS 配置解析，可能包含 `/etc/hosts`、DNS 等来源，更接近许多应用的解析路径 |

```bash
dig example.com A
getent ahosts example.com
cat /etc/resolv.conf
```

dig 查到记录而应用仍解析异常时，要检查 NSS、hosts、缓存、容器和代理环境；`/etc/resolv.conf` 也可能由 systemd-resolved、NetworkManager 等管理，不宜直接覆盖。

### 11.4 ss：监听端口与连接

**语法**：`ss [选项] [过滤表达式]`。优先使用内置端口过滤，避免 `grep :3000` 把 `:30001` 也匹配出来。

| 参数 | 含义 |
| --- | --- |
| `-t` / `-u` / `-x` | TCP / UDP / Unix domain socket |
| `-l` | 只看监听类 socket；不会同时列出所有已建立连接 |
| `-a` | 同时列监听与非监听对象 |
| `-n` | 用数字显示地址和端口，不转换服务名 |
| `-p` | 显示关联进程，完整查看通常需要相应权限 |
| `-e` | 扩展信息，如 UID、inode |
| `-s` | 汇总统计 |
| `'sport = :3000'` | 筛选本地源端口 3000；引号保护表达式 |

```bash
ss -lnt
sudo ss -lntp 'sport = :3000'
sudo ss -lunp
ss -tn state established
ss -s
```

`ss -tulpen` 可拆成 TCP、UDP、监听、进程、扩展、数字输出。`127.0.0.1:3000` 通常只允许本机 IPv4 访问，`0.0.0.0:3000` 绑定所有本机 IPv4 地址；IPv6 的 `[::]` 是否同时接收 IPv4 取决于应用和系统设置。监听成功仍不代表防火墙、云安全组和外部路由均已放行。[ss 手册](https://man7.org/linux/man-pages/man8/ss.8.html)

### 11.5 nc、lsof：测试 TCP 与查占用

| 命令 | 参数与用途 |
| --- | --- |
| `nc -vz -w 3 example.com 443` | 常见 OpenBSD netcat：`-v` 详细，`-z` 只探测连接，`-w 3` 设置连接/空闲超时；其他 nc 实现需核对帮助 |
| `sudo lsof -nP -iTCP:3000 -sTCP:LISTEN` | 查询监听 3000 的进程；`-nP` 保持数字地址/端口 |
| `sudo lsof -nP -i :3000` | 范围更宽，可能包括 TCP/UDP、监听与非监听连接 |

TCP 建连成功只证明相应链路与端口可建立连接，不证明 TLS 证书、HTTP 路径、认证和业务响应正确。UDP 无握手，不能照搬 TCP 探测结论。

### 11.6 curl：HTTP 请求与下载

**语法**：`curl [选项] URL`。默认通常把响应体输出到 stdout，不自动按 URL 文件名保存。[curl 官方手册](https://curl.se/docs/manpage.html)

| 参数 | 含义 |
| --- | --- |
| `-I` | 发 HEAD 请求，只取响应头；服务可能对 HEAD 与 GET 处理不同 |
| `-i` | 输出时包含响应头，仍会请求响应体 |
| `-L` | 跟随 HTTP 重定向 |
| `-o 文件` / `-O` | 保存为指定文件名 / 使用 URL 中的远端文件名 |
| `-f` | 通常让 HTTP 4xx/5xx 返回失败状态，并不输出错误响应体 |
| `-sS` | 隐藏进度与普通提示，但仍显示错误 |
| `-v` | 输出连接、TLS 和协议调试信息到 stderr；分享前留意其中的认证和请求信息 |
| `--connect-timeout 5` / `--max-time 15` | 连接阶段最多 5 秒 / 整次操作最多 15 秒 |
| `-H '名称: 值'` | 添加请求头，可重复 |
| `-d 'a=1'` | 发送表单风格数据，HTTP 下通常隐含 POST |
| `--data-binary @文件` | 原样读取文件作为请求体；配合 Content-Type 指定格式 |
| `-X 方法` | 显式指定方法字符串，和请求体处理是不同概念 |
| `--retry 3` | 对符合重试条件的失败重试，不能保证对所有错误都重试 |
| `-C -` | 按已有输出文件长度尝试断点续传，需要服务端支持 |

```bash
curl -I --max-time 15 https://example.com/
curl -sS -o /dev/null -w 'HTTP %{http_code}\n' https://example.com/
curl -fL --connect-timeout 5 --max-time 60 -o archive.tar.gz https://example.com/archive.tar.gz
# 向你有权操作的接口发送 JSON；这类请求可能修改远端数据
curl -sS -H 'Content-Type: application/json' --data-binary @request.json https://api.example.com/items
```

`-w` 指定传输结束时的输出格式，`%{http_code}` 为 HTTP 状态码。不加 `-f` 时，curl 成功收到 404 页面也可能返回退出码 0；curl 退出码与 HTTP 状态码是两套概念。证书错误应排查域名、系统时间、证书链或 CA，`-k` 跳过验证不适合作为长期解决方式。

### 11.7 wget：以下载为主

**语法**：`wget [选项] URL...`。

| 参数 | 含义 |
| --- | --- |
| `-O 文件` | 将下载内容写入指定文件，注意是大写 O，可能覆盖原文件 |
| `-c` | 在服务端支持的情况下继续已有下载；要确认远端内容未换版本 |
| `-P 目录` | 指定保存目录 |
| `-S` | 显示服务器响应头，便于排错 |

```bash
wget -O archive.tar.gz https://example.com/archive.tar.gz
wget -c https://example.com/large-file.bin
```

下载完成后可用 `file` 检查类型，防止下载到错误页，再用可信发布方提供的校验值或签名核验。

## 12 SSH 与文件传输

### 12.1 ssh：远程登录与端口转发

**语法**：`ssh [选项] [用户@]主机 [远程命令]`。

| 参数 | 含义 |
| --- | --- |
| `-p 2222` | 远端 SSH 端口，默认通常为 22 |
| `-i ~/.ssh/id_ed25519` | 指定私钥文件 |
| `-v` / `-vvv` | 逐步增加调试信息，定位认证、连接和配置问题 |
| `-J jumpuser@jump.example.com` | 通过跳板机连接 |
| `-o ConnectTimeout=5` | 设置连接阶段超时 |
| `-o ServerAliveInterval=30` | 每 30 秒通过 SSH 协议探测响应；与 TCP keepalive 不同 |
| `-L 本地地址:本地端口:目标地址:目标端口` | 本地端口转发；目标地址从 SSH 服务端一侧访问 |
| `-N` | 不执行远程命令，常与纯转发结合 |

```bash
ssh -p 2222 -i "$HOME/.ssh/id_ed25519" user@server.example.com
ssh user@server.example.com 'uname -r; uptime'
ssh -N -L 127.0.0.1:8888:127.0.0.1:8888 user@server.example.com
```

最后一条把本地 `127.0.0.1:8888` 转发到远端一侧的 `127.0.0.1:8888`；命令持续运行时转发才保持。首次连接应核对主机指纹；主机密钥变化时先确认服务器是否重装或更换密钥。[OpenSSH ssh 手册](https://man.openbsd.org/ssh)

### 12.2 ssh-keygen、ssh-copy-id：密钥初始化

| 命令 | 参数与用途 |
| --- | --- |
| `ssh-keygen -t ed25519 -C 'my-laptop'` | `-t` 指密钥类型，`-C` 添加便于识别的注释；生成时可设置私钥口令 |
| `ssh-keygen -lf ~/.ssh/id_ed25519.pub` | `-l` 显示指纹，`-f` 指定文件 |
| `ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server.example.com` | 将指定公钥追加部署到远端账户；需要工具已安装，并且已有可用认证方式；非默认端口加 `-p 2222` |

私钥 `id_ed25519` 留在本机，公钥 `.pub` 才用于部署。生成时遇到同名现有私钥，应保留或改用新文件名；不要为了套用示例覆盖正在使用的密钥。[ssh-keygen 手册](https://man.openbsd.org/ssh-keygen)

### 12.3 scp：简单复制

**语法**：`scp [选项] 源... 目标`；远端路径通常写作 `用户@主机:路径`。

| 参数 | 含义 |
| --- | --- |
| `-P 2222` | SSH 端口，注意大写 P |
| `-p` | 保留修改时间、访问时间和文件权限位，不是端口 |
| `-r` | 递归复制目录；会跟随遍历中遇到的符号链接 |
| `-i 私钥` | 指定 SSH 私钥 |

```bash
scp -P 2222 report.txt user@server.example.com:/home/user/
scp user@server.example.com:/home/user/report.txt ./
scp -r ./src user@server.example.com:/home/user/project/
```

现代 OpenSSH 的 scp 默认通过 SFTP 传输；旧版本和兼容选项可能使用不同协议。大量目录同步、预览变更或重跑传输时可选 rsync。[OpenSSH scp 手册](https://man.openbsd.org/scp)

### 12.4 rsync：可预览的增量同步【修改目标】

**语法**：`rsync [选项] 源... 目标`。通过 SSH 同步时通常要求两端都安装 rsync。

| 参数 | 含义 |
| --- | --- |
| `-a` | 归档模式，约等于 `-rlptgoD`；并不自动包含硬链接、ACL、扩展属性 |
| `-v` / `-h` | 显示过程 / 可读数字 |
| `-z` | 传输时压缩；已压缩文件和高速局域网不一定受益 |
| `-n` / `--dry-run` | 预览，不实际修改同步目标 |
| `--itemize-changes` | 逐项列出预计变化 |
| `--progress` | 显示文件传输进度 |
| `--exclude='模式'` | 排除对象，规则相对同步根路径理解 |
| `-e 'ssh -p 2222'` | 指定远程 Shell 及端口 |
| `--delete` | 删除目标中源端没有的对象；会把备份行为变成镜像式同步，必须先预览 |

```bash
# 先预览：同步 src 里面的内容到 backup
rsync -avhn --itemize-changes ./src/ ./backup/
# 确认后执行
rsync -avh ./src/ ./backup/
# 经 SSH 上传
rsync -avz -e 'ssh -p 2222' ./dist/ user@server.example.com:/home/user/app/
# 仅预览镜像删除的范围
rsync -avhn --delete --itemize-changes ./src/ ./backup/
```

**源目录末尾斜杠很重要**：`src/` 表示复制其中内容，`src` 通常表示连目录名一起复制。默认的快速变化判断主要看大小和修改时间，并非每次都完整比对内容。普通用户保留所有者等元数据受权限限制；`-a` 也不等于备份了所有文件系统属性。[rsync 官方手册](https://download.samba.org/pub/rsync/rsync.1)

更多 SSH 配置和认证细节见 [[SSH]]。

## 13 软件包管理

先用 `cat /etc/os-release` 确认发行版。下表按各自仓库查询和升级；软件包名称与版本受发行版、发行版版本和启用仓库影响，不能直接跨列照搬。安装、升级和删除会修改系统，确认事务清单后再继续。

### 13.1 按发行版查操作

| 任务 | Debian / Ubuntu | Fedora 等 DNF 系 | Arch Linux | openSUSE |
| --- | --- | --- | --- | --- |
| 刷新元数据 / 检查更新 | `sudo apt update` | DNF5：`dnf check-upgrade`；DNF4：`dnf check-update` | `sudo pacman -Syu` 同时完整升级 | `sudo zypper refresh` |
| 搜索包 | `apt search nginx` | `dnf search nginx` | `pacman -Ss nginx` | `zypper search nginx` |
| 查看仓库包详情 | `apt show nginx` | `dnf info nginx` | `pacman -Si nginx` | `zypper info nginx` |
| 安装 | `sudo apt install nginx` | `sudo dnf install nginx` | `sudo pacman -S nginx` | `sudo zypper install nginx` |
| 更新已安装包 | `sudo apt upgrade` | `sudo dnf upgrade` | `sudo pacman -Syu` | Leap 常见 `sudo zypper update`；Tumbleweed 通常 `sudo zypper dup` |
| 删除包 | `sudo apt remove nginx` | `sudo dnf remove nginx` | `sudo pacman -R nginx` | `sudo zypper remove nginx` |
| 查本地已安装包 | `dpkg -l nginx` | `rpm -q nginx` | `pacman -Qi nginx` | `rpm -q nginx` |
| 包装了哪些文件 | `dpkg -L nginx` | `rpm -ql nginx` | `pacman -Ql nginx` | `rpm -ql nginx` |
| 文件归属哪个包 | `dpkg -S /usr/bin/ls` | `rpm -qf /usr/bin/ls` | `pacman -Qo /usr/bin/ls` | `rpm -qf /usr/bin/ls` |

### 13.2 参数和行为区别

- **apt**：`update` 更新索引，不升级已安装软件；`upgrade` 升级且不移除已有包；`full-upgrade` 必要时可以移除包，先审查清单。`remove` 通常保留包的系统配置文件，`purge` 进一步清除该类配置，但并不自动删除用户家目录数据。`autoremove` 清理不再需要的自动安装依赖，也应先审查。日常交互用 apt，自动脚本优先参考 apt-get/apt-cache 的稳定接口。[APT 手册](https://manpages.debian.org/stable/apt/apt.8.en.html)
- **dnf**：本机的 `dnf --version` 可区分实现；DNF5 文档使用 `check-upgrade`，DNF4 常见 `check-update`。检查更新发现可升级包时，退出码可能为 **100**，这是“有更新”，不是一般执行失败。`-y` 表示自动确认，初次手工操作可先不加。[DNF5 检查更新](https://dnf5.readthedocs.io/en/latest/commands/check-upgrade.8.html)、[DNF4 参考](https://dnf.readthedocs.io/en/stable/command_ref.html)
- **pacman**：`-S` 操作仓库包，`-Q` 查本地，`-R` 删除；在 `-Syu` 中，`-y` 刷新数据库，`-u` 升级全部可升级包。`-Ss` 搜仓库、`-Si` 查仓库详情、`-Qi` 查已安装包。Arch 不支持局部升级：不要执行 `pacman -Sy` 后只安装个别软件；应完成 `pacman -Syu`，也可用 `pacman -Syu 包名` 完整升级并安装。[pacman 手册](https://man.archlinux.org/man/pacman.8.en)、[Arch 完整升级说明](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported)
- **zypper**：`refresh/ref` 刷新仓库，`search/se` 搜索，`install/in` 安装，`remove/rm` 删除，`update/up` 常规更新，`dist-upgrade/dup` 按发行版仓库做分发升级。Leap 与 Tumbleweed 的更新工作流不同，跨发行版迁移前必须查对应发行说明。[openSUSE 软件管理文档](https://doc.opensuse.org/documentation/leap/reference/html/book-reference/cha-sw-cl.html)、[Tumbleweed 更新说明](https://doc.opensuse.org/documentation/tumbleweed/updating_upgrading_reverting/)

### 13.3 缺命令时查哪个包

下面是 Debian / Ubuntu 的常见映射；其他发行版先搜索包名，不要求一次全部安装。

| 命令 | 常见软件包 |
| --- | --- |
| `man` | `man-db`，手册正文也需要相应软件包 |
| `ip`、`ss` | `iproute2` |
| `dig`、`nslookup` | `dnsutils` 或其对应的 BIND 工具包 |
| `nc` | `netcat-openbsd` 等实现 |
| `iostat` | `sysstat` |
| `lsof`、`tree`、`jq`、`tmux`、`htop` | 通常与命令同名的包 |
| `rg` | `ripgrep` |
| `fd` / `fdfind` | `fd-find`；Debian / Ubuntu 中可执行文件常名为 `fdfind` |
| `bat` / `batcat` | `bat`；Debian / Ubuntu 中可执行文件常名为 `batcat` |
| `zip` / `unzip` | `zip` / `unzip` |

```bash
sudo apt update
sudo apt install tree jq ripgrep tmux lsof sysstat
```

若显示 `command not found`，先查 `command -v 命令`、PATH 和包是否安装；不要默认给命令前加 sudo 就能解决。

## 14 打包压缩与校验

### 14.1 tar：把多个文件归档

**语法**：`tar [操作与选项] -f 归档文件 [路径...]`。tar 本身主要负责归档，gzip/bzip2/xz 等负责压缩。

| 参数 | 含义 |
| --- | --- |
| `-c` / `-x` / `-t` | 创建 / 解包 / 列出归档；一次选择一种主操作 |
| `-f 文件` | 指定归档文件名；文件名必须作为此选项的参数 |
| `-z` / `-j` / `-J` | 使用 gzip / bzip2 / xz；小写 j 与大写 J 不同 |
| `-v` | 列出处理的文件，文件很多时输出也很多 |
| `-C 目录` | 先切到指定目录再处理后续路径，目录需存在 |
| `--exclude='模式'` | GNU tar 排除匹配对象；模式加引号，创建时放在源路径之前 |

```bash
# 创建归档：归档文件放在被打包的目录之外
tar -czf project.tar.gz --exclude='project/.git' project/
# 先看内容，再解到单独目录
tar -tzf project.tar.gz
mkdir -p unpacked
tar -xzf project.tar.gz -C unpacked/
# 将 /var/log 作为相对路径 log/ 打包，读取权限需满足
tar -czf logs.tar.gz -C /var log
```

| 格式 | 创建 | 解包 |
| --- | --- | --- |
| `.tar` | `tar -cf a.tar dir/` | `tar -xf a.tar` |
| `.tar.gz` | `tar -czf a.tar.gz dir/` | `tar -xzf a.tar.gz` |
| `.tar.bz2` | `tar -cjf a.tar.bz2 dir/` | `tar -xjf a.tar.bz2` |
| `.tar.xz` | `tar -cJf a.tar.xz dir/` | `tar -xJf a.tar.xz` |

解包可能覆盖同名文件。对不可信归档先列目录、在新目录中以普通用户解包，留意绝对路径、`..` 和链接；单看文件名并不能保证归档安全。不要在同一待归档目录里生成它自身的归档文件。[GNU tar 手册](https://www.gnu.org/software/tar/manual/tar.html)

### 14.2 gzip、gunzip、zcat：单文件压缩与读取

| 命令 | 参数与结果 |
| --- | --- |
| `gzip app.log` | 压缩为 `app.log.gz`，成功时通常移除原始文件 |
| `gzip -k app.log` | 保留原文件，需实现支持 |
| `gzip -c app.log > app.log.gz` | `-c` 输出到 stdout，原文件保留；重定向仍会覆盖目标 |
| `gunzip app.log.gz` / `gzip -d app.log.gz` | 解压，通常移除压缩文件 |
| `gzip -t app.log.gz` | 检查压缩数据完整性，不解出文件 |
| `zcat app.log.gz` | 解压内容到 stdout，原压缩文件保留 |

```bash
gzip -c app.log > app.log.gz
gzip -t app.log.gz
zcat app.log.gz | less
```

单独 gzip 不会把整个目录树打包成一个归档；多个文件一起保留目录结构，先使用 tar。

### 14.3 zip、unzip：ZIP 归档

| 命令 | 参数与用途 |
| --- | --- |
| `zip -r archive.zip dir/` | `-r` 递归打包目录 |
| `unzip -l archive.zip` | `-l` 列内容 |
| `unzip -t archive.zip` | `-t` 检查归档数据 |
| `unzip archive.zip -d out/` | `-d` 指定输出目录 |
| `unzip -n archive.zip -d out/` | `-n` 不覆盖已有文件 |
| `unzip -o archive.zip -d out/` | `-o` 直接覆盖，不询问；仅在明确需要时使用 |

```bash
zip -r archive.zip project/
unzip -l archive.zip
unzip -n archive.zip -d unpacked/
```

ZIP 的文件权限、链接和文件名编码行为受实现及平台影响，不能直接视为完整的 Linux 系统备份格式。

### 14.4 sha256sum：内容校验

**语法**：`sha256sum [选项] [文件...]`。

```bash
sha256sum archive.tar.gz
sha256sum archive.tar.gz > SHA256SUMS
sha256sum -c SHA256SUMS
```

第一条生成摘要；第二条生成校验清单；`-c` 按清单检查，结果应为 `OK`。自己下载完再计算一个摘要，只是为后续变化留基准；核验下载正确性要与发布方通过可信渠道提供的期望值比较。摘要相同不能单独证明来源可信。

## 15 环境变量与 Shell 配置

### 15.1 变量、export、env、printenv、unset

| 写法 | 作用 |
| --- | --- |
| `name=value` | 设置当前 Shell 变量，等号两侧不能有空格 |
| `printf '%s\n' "$name"` | 展开并打印变量；固定格式串比拼接 echo 参数更可靠 |
| `export APP_ENV=development` | 创建或设置变量，并导出给此后启动的子进程 |
| `APP_ENV=test 命令` | 只给这一条命令及其后代设置该环境变量，不永久改变当前 Shell |
| `env` / `printenv` | 查看进程环境；输出可能包含令牌等信息，分享前应检查 |
| `printenv PATH` | 只查询指定的环境变量 |
| `env APP_ENV=test 命令` | 显式带给子命令的环境设置 |
| `unset APP_ENV` | 在当前 Shell 删除变量，不能修改已运行进程的环境 |

```bash
export APP_ENV=development
printf '%s\n' "$APP_ENV"
printenv PATH
APP_ENV=test python3 app.py
unset APP_ENV
```

当前 Shell 的更改不会反向修改父进程或其他已运行会话。`echo "$SHELL"` 通常显示账户配置的 Shell 或继承的变量，不能单独证明当前正在运行哪个 Shell；交互 Bash 中可结合 `printf '%s\n' "$BASH_VERSION"`、`ps -p $$ -o comm=` 查看。

### 15.2 PATH：为什么会 command not found

PATH 是用冒号分隔的可执行文件搜索目录列表，Shell 通常按顺序寻找外部命令。

```bash
printf '%s\n' "$PATH" | tr ':' '\n'
command -v python3
type -a python3
export PATH="$HOME/.local/bin:$PATH"
```

新增目录时保留原来的 `$PATH`；误写为仅一个目录会导致其他工具无法按名称找到。当前目录默认不一定在 PATH 中，因此本目录程序用 `./app` 执行。PATH 不应随意加入不可信目录；目录顺序会影响实际执行哪个程序。

### 15.3 source 与直接运行脚本

| 写法 | 执行环境与要求 |
| --- | --- |
| `source ./env.sh` / `. ./env.sh` | 在当前 Shell 执行，变量、函数和目录变化可留在当前环境；不要求文件可执行，但必须可读，且语法兼容当前 Shell |
| `bash ./script.sh` | 由新的 Bash 读取并执行脚本，不要求脚本有执行位；脚本变量不能自动回传父 Shell |
| `./script.sh` | 作为程序执行，需要执行权限，解释器通常由文件开头的 shebang 决定 |

`source` 会执行文件中的全部代码，不是“只读取变量”。修改 Bash 交互配置后可用 `source ~/.bashrc`，zsh 则用 `source ~/.zshrc`；不要在 Bash 中直接加载 fish 配置。

```bash
# 下面这些行适合放入 Bash 的 ~/.bashrc
export PATH="$HOME/.local/bin:$PATH"
alias ll='ls -lah'
```

### 15.4 alias、unalias 与配置文件

**语法**：`alias 名称='命令内容'`；`unalias 名称`。alias 主要用于交互便利，脚本不应依赖交互别名是否启用。

```bash
alias ll='ls -lah'
alias
unalias ll
```

| 配置文件 | 何时或由谁读取 |
| --- | --- |
| `/etc/profile` | Bash 登录式 Shell 的系统级初始化入口之一 |
| `~/.bash_profile`、`~/.bash_login`、`~/.profile` | Bash 登录式 Shell 按此顺序读取第一个存在且可读的文件，不会全部依次读取 |
| `~/.bashrc` | Bash 交互、非登录式 Shell 常用配置；登录式是否再读取它，取决于登录配置是否显式 source |
| `~/.zshrc` | zsh 交互配置；登录配置常见 `~/.zprofile` |
| `~/.config/fish/config.fish` | fish 的配置，语法不同于 Bash |
| `/etc/environment` | 常由 PAM 等组件加载的环境设置，不是通用 Shell 脚本；不要默认支持 `export`、命令替换或 `$PATH` 展开 |

`bash -l`、普通终端、SSH、cron 和 systemd 服务的启动环境可能不同。“终端能运行，定时任务不能运行”时，优先核对解释器、PATH、工作目录和启动文件。[Bash 启动文件规则](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html)

## 16 定时任务

### 16.1 crontab：查看与编辑 cron 任务【修改调度】

| 命令 | 含义 |
| --- | --- |
| `crontab -l` | 列出当前用户的任务；不存在任务表时可能返回非零 |
| `crontab -e` | 编辑当前用户的任务，保存后由 cron 接收 |
| `sudo crontab -u alice -l` | 管理权限下查询 alice 的任务表 |
| `crontab -r` | 删除当前用户的整个任务表，不是删除某一条；通常通过 `-e` 精确编辑更合适 |

用户 crontab 每条任务的格式为：`分 时 日 月 星期 命令`，**不包含用户名字段**。`/etc/crontab`、`/etc/cron.d/` 的系统任务通常还需要用户名，不能直接混用。[crontab 格式手册](https://man7.org/linux/man-pages/man5/crontab.5.html)

| 字段 | 常见范围 | 示例 |
| --- | --- | --- |
| 分 | `0-59` | `*/15` 为每小时的 0、15、30、45 分 |
| 时 | `0-23` | `2` 为凌晨 2 点 |
| 日 | `1-31` | `1` 为每月第一天 |
| 月 | `1-12` | `1,7` 为 1 月与 7 月 |
| 星期 | `0-7`，常见 0 和 7 都表示周日 | `1-5` 为周一至周五，支持细节看实现 |

`*` 表示所有值，`,` 枚举，`-` 范围，`/` 步长。日与星期都被限制时，常见 Cronie/Vixie 语义为**任一满足即可**，不是同时满足。

```cron
SHELL=/bin/sh
PATH=/usr/bin:/bin

# 每天 02:00，用 Bash 运行脚本，并将输出追加到日志
0 2 * * * /bin/bash /home/user/scripts/backup.sh >> /home/user/backup.log 2>&1

# 工作日 09:30
30 9 * * 1-5 /bin/bash /home/user/scripts/report.sh >> /home/user/report.log 2>&1
```

脚本和日志的父目录需要存在，执行身份需要相应权限。cron 通常不加载交互配置，使用绝对路径并在脚本中明确工作目录。直接放在任务命令中的 `%` 在常见 cron 实现里有特殊含义，即使被 Shell 引号包住也需按 cron 规则转义；较复杂的命令更适合放进独立脚本。调度通常按主机时区运行，`CRON_TZ` 等扩展支持情况要查本机手册。[crontab 的命令字段与转义规则](https://man7.org/linux/man-pages/man1/crontab.1p.html)

### 16.2 systemd timers：查看系统已有计划

```bash
systemctl list-timers --all
systemctl --user list-timers --all
```

看 `NEXT`、`LAST`、`UNIT` 和 `ACTIVATES`：分别是下次触发、上次触发、timer 单元及其触发的服务。timer 触发不等于服务执行成功，仍需用 `systemctl status 对应服务` 和 `journalctl -u 对应服务` 检查。是否补跑错过的任务、时区和时间精度由 timer 配置决定。

## 17 常见任务与排错配方

下面按“观察 → 缩小范围 → 决定动作”组织。详细参数回到相应章节查询。

### 17.1 磁盘显示已满，但不知道哪里占空间

```bash
# 先看目标路径所在文件系统及 inode
df -hT /var
df -i /var
# 在同一个文件系统内，从一级目录逐层缩小范围
sudo du -xh --max-depth=1 /var | sort -hr
# 如果 df 很大但 du 对不上，检查已删除仍打开的文件
sudo lsof +L1
```

先区分容量不足与 inode 不足。du 的总计行会与子目录一起出现，不要把这些行相加；不要直接扫描并删除整个 `/var`。若是 journal 占用，先看 `journalctl --disk-usage` 再决定保留策略。见 [[#09 磁盘空间与挂载|磁盘章节]]。

### 17.2 某端口被占用，或应用启动后访问不到

```bash
sudo ss -lntp 'sport = :3000'
sudo lsof -nP -iTCP:3000 -sTCP:LISTEN
curl -sS --connect-timeout 3 --max-time 5 -o /dev/null -w 'HTTP %{http_code}\n' http://127.0.0.1:3000/
```

无监听输出时检查应用是否已退出、端口是否写错、是否位于另一网络命名空间；只有回环监听时检查绑定地址。取得 HTTP 404 也说明已有 HTTP 响应，只是路径可能不对；`000` 通常表示没取得有效 HTTP 状态，要结合 curl 的错误信息判断。不要未经确认就结束占用端口的进程。

### 17.3 systemd 服务启动失败

```bash
systemctl status nginx --no-pager --full
journalctl -u nginx.service -b -n 100 --no-pager
# 仅当确实安装 nginx 时，用它自己的配置检查命令
sudo nginx -t
```

`nginx -t` 检查配置语法并尝试打开配置引用的文件。先按日志区分配置错误、权限、文件缺失和端口占用，修复后再决定 `reload` 或 `restart`。修改的是 `.service` 单元文件时先 `sudo systemctl daemon-reload`；修改的是应用配置时则遵循应用自己的检查和重载方式。

### 17.4 Permission denied：路径、身份还是文件权限

```bash
id
ls -ld /path /path/to /path/to/file
# 可选：util-linux 的 namei -l 展示每一层路径及其权限
namei -l /path/to/file
findmnt -T /path/to/file
```

按顺序确认执行身份、每层目录的 `x`、目标所需的 `r/w/x`、所有者与组、挂载是否只读或 noexec。传统权限看起来正确时，可进一步检查 ACL、SELinux/AppArmor 等。运行脚本还需检查 shebang 指定的解释器是否存在；不要先对整棵目录执行 `chmod -R 777`。

### 17.5 网络失败：按层判断

| 检查层次 | 命令 | 这一步能说明什么 |
| --- | --- | --- |
| 地址与路由 | `ip -br addr`、`ip route` | 是否有地址、默认路由和预期出口 |
| 名称解析 | `getent ahosts example.com`、`dig example.com A` | 系统解析与 DNS 查询分别如何返回 |
| TCP | `nc -vz -w 3 example.com 443` | 是否能够建立到目标端口的 TCP 连接 |
| TLS 与 HTTP | `curl -v --connect-timeout 5 --max-time 15 https://example.com/` | 失败在连接、证书、协议还是 HTTP 响应 |
| 业务接口 | 对实际路径发请求并检查响应 | 状态码、认证、返回数据是否符合业务预期 |

同一域名可能同时有 IPv4、IPv6 和代理路径；必要时用 `curl -4`、`curl -6` 分别观察，不要用某一路径的成功替代另一条路径的验证。代理环境也可能让 curl 与直接 nc 的实际路径不同。

### 17.6 找出最近修改的大文件，或预览待清理缓存

```bash
find ./data -type f -size +100M -mtime -7 -print
find ./cache -type f -name '*.tmp' -mmin +1440 -print
```

第一条查最近不足 7 天修改且大于 100 MiB 的普通文件；第二条预览修改已超过约一天的临时文件。只有确认起始目录、匹配名单和时间含义之后，才考虑把相应 `-print` 改成 `-delete`；find 没有通用的交互式撤销。

### 17.7 批量修改配置，先预览并保留备份

```bash
grep -rnF --include='*.conf' -e 'old-host' ./config
find ./config -type f -name '*.conf' -exec sed 's/old-host/new-host/g' {} +
# 确认所有匹配对象和替换规则后才执行以下修改
find ./config -type f -name '*.conf' -exec sed -i.bak 's/old-host/new-host/g' {} +
```

grep 的 `-F` 是固定字符串；sed 的替换左侧仍是正则，本例中的连字符在该位置按字面处理。带句点、反斜杠等的实际模式需要按 sed 规则转义。复杂结构化配置要使用相应解析工具。重复执行 `.bak` 备份可能覆盖上一份备份，应按需求保留历史。

### 17.8 长任务断线后继续，并保留日志

```bash
tmux new -As work
# 在 tmux 内执行；需要准确返回上游状态时考虑 pipefail
set -o pipefail
python3 app.py 2>&1 | tee -a app.log
```

执行期间按 `Ctrl+b`，松开，再按 `d` 离开 tmux；重新登录后 `tmux attach -t work`。`tee -a` 追加日志，日志文件仍会持续增长；如果程序输出有缓冲，需要按程序自身的方式调整，Python 可按需使用 `python3 -u` 取消其标准流缓冲。长期服务仍应交给服务管理器。

### 17.9 常见报错速查

| 现象 | 优先检查 |
| --- | --- |
| `command not found` | 是否安装、可执行文件实际名字、PATH、是否应写 `./程序`；用 `command -v` 和 `type -a` |
| `No such file or directory` | 路径、当前目录、链接目标；文件明明存在时还要检查 shebang、CRLF 和动态加载器 |
| `Permission denied` | 身份、每层目录、目标权限、ACL/安全策略、挂载选项 |
| `No space left on device` | `df -h` 与 `df -i`，必要时还要检查配额、tmpfs 或相应文件系统限制 |
| `Address already in use` | `ss -lntp` 精确端口过滤，确认实际绑定地址和进程 |
| `Connection refused` | 目标地址/端口是否有服务，是否存在主动拒绝；与连接超时不同 |
| 连接超时 | 路由、过滤、代理、服务响应和网络链路，结合分层探测 |
| SSH `Permission denied (publickey)` | 用户名、实际使用的密钥、服务端 authorized_keys 和权限；用 `ssh -v` 看认证过程 |
| 终端能运行，cron 中失败 | PATH、工作目录、解释器、权限、环境变量、脚本依赖与日志 |
| `System has not been booted with systemd` | 当前环境是否真正运行 systemd，例如容器、WSL 或其他 init 系统 |

## 18 附录终端与开发环境

### 18.1 终端、Shell、tmux 分别负责什么

- **终端模拟器**：窗口、字体、显示、输入和复制粘贴，例如 GNOME Terminal、Konsole、Kitty、WezTerm、Alacritty、Ghostty。
- **Shell**：解释命令、展开变量、连接管道与运行脚本，例如 Bash、zsh、fish、Nushell。
- **会话复用器**：在终端中组织窗口/分屏并支持 detach/attach，例如 tmux、Zellij。终端关闭后会话是否存活，仍受主机和系统会话策略影响。

这些是不同层次，可以组合使用；命令用法应先看当前 Shell 与工具实现，而不是只看使用了哪个终端窗口。

| 工具类别 | 可查阅的选择与适用点 |
| --- | --- |
| 桌面集成终端 | GNOME Terminal、Konsole，分别常见于 GNOME、KDE 环境 |
| 配置驱动的终端 | Kitty、WezTerm、Alacritty、Ghostty；功能与系统支持以各项目当前文档为准 |
| 图形分屏 / 下拉终端 | Terminator、Tilix、Guake |
| Shell | Bash 常见于服务器和脚本；zsh 适合交互定制；fish、Nushell 有自己的语法和数据处理方式 |
| 会话管理 | tmux、Zellij；远程长期交互任务可查其会话恢复功能 |

### 18.2 安装可选交互工具与切换 Shell

以下只演示常见发行版的安装方式；先按需挑选包，不要求全部安装。

```bash
# Debian / Ubuntu
sudo apt install zsh fish tmux ripgrep fd-find bat btop
# Fedora，包名以当前仓库为准
sudo dnf install zsh fish tmux ripgrep fd-find bat btop
# Arch：完整升级后同时安装，避免局部升级
sudo pacman -Syu zsh fish tmux ripgrep fd bat btop
```

补充工具：`fdfind . src/` 在 src 中按名称查找，`batcat README.md` 带高亮分页查看文件，`btop` 交互观察资源。其他发行版的可执行文件可能名为 `fd`、`bat`，使用 `命令 --help` 查看该机参数。

**chsh 语法**：`chsh -s Shell绝对路径 [用户名]`。`-s` 设置登录 Shell，通常要求目标路径位于 `/etc/shells`，并受认证或账户管理策略限制。

```bash
command -v zsh
cat /etc/shells
# 确认本机 zsh 的绝对路径后再执行；/usr/bin/zsh 只是常见位置
chsh -s /usr/bin/zsh
```

切换后通常重新登录才生效；某些服务账户或受集中管理的账户不能这样修改。临时尝试可以在当前终端运行 `zsh` 或 `fish`，退出后回到原 Shell。

### 18.3 VS Code 集成

`Ctrl+Shift+P` 打开命令面板，选择 `Terminal: Select Default Profile`；常见键位 ``Ctrl+` `` 打开/关闭集成终端。Remote SSH / WSL 窗口中的终端通常在相应远端或 WSL 环境执行，先用 `hostname`、`pwd` 确认位置。

`settings.json` 示例：仅在对应 Shell 已安装且可从该环境找到时使用。

```json
{
  "terminal.integrated.defaultProfile.linux": "bash",
  "terminal.integrated.profiles.linux": {
    "bash": {
      "path": "bash"
    },
    "zsh": {
      "path": "zsh"
    },
    "fish": {
      "path": "fish"
    }
  }
}
```

确实需要登录式 Bash 时再加 `"args": ["-l"]`，并按前文检查启动文件。长任务可在远程集成终端中使用 tmux，避免把界面断开与任务退出混为一谈。

## 19 参考资料与验证边界

### 19.1 官方文档入口

本地安装版本的手册优先级最高：内建命令查 `help`，外部命令查 `man` 与 `--help`。下列在线资料用于继续核对，页面可能比服务器安装版本新。

| 命令族 | 一手文档入口 |
| --- | --- |
| Bash 语法、内建命令、展开、作业控制 | [GNU Bash 手册](https://www.gnu.org/software/bash/manual/bash.html) |
| 文件、目录、权限、排序、校验等基础工具 | [GNU Coreutils 手册](https://www.gnu.org/software/coreutils/manual/coreutils.html) |
| find、xargs | [GNU Findutils 手册](https://www.gnu.org/software/findutils/manual/html_mono/find.html) |
| grep / sed / awk | [GNU grep](https://www.gnu.org/software/grep/manual/grep.html)、[GNU sed](https://www.gnu.org/software/sed/manual/sed.html)、[GNU awk](https://www.gnu.org/software/gawk/manual/gawk.html) |
| rg / jq | [ripgrep 上游指南](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md)、[jq 官方手册](https://jqlang.org/manual/) |
| ps、free、vmstat、top 等 | [procps-ng 项目](https://gitlab.com/procps-ng/procps)、本机对应手册 |
| 挂载、设备、路径等 util-linux 工具 | [util-linux 上游](https://github.com/util-linux/util-linux)、[挂载手册](https://man7.org/linux/man-pages/man8/mount.8.html) |
| ip / ss / ping | [iproute2 上游](https://git.kernel.org/pub/scm/network/iproute2/iproute2.git/)、[ss 手册](https://man7.org/linux/man-pages/man8/ss.8.html)、[iputils 上游](https://github.com/iputils/iputils) |
| dig / nslookup | [ISC BIND 文档](https://bind9.readthedocs.io/en/latest/manpages.html) |
| iostat | [sysstat 上游](https://github.com/sysstat/sysstat)、本机 `man iostat` |
| lsof | [上游手册的 Debian 发布页](https://manpages.debian.org/stable/lsof/lsof.8.en.html) |
| 服务与日志 | [systemctl](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)、[journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) |
| curl / wget | [curl 官方手册](https://curl.se/docs/manpage.html)、[GNU Wget 手册](https://www.gnu.org/software/wget/manual/wget.html) |
| SSH / scp / rsync | [ssh](https://man.openbsd.org/ssh)、[scp](https://man.openbsd.org/scp)、[rsync](https://download.samba.org/pub/rsync/rsync.1) |
| 软件包管理 | [Debian APT](https://manpages.debian.org/stable/apt/apt.8.en.html)、[DNF5](https://dnf5.readthedocs.io/en/latest/)、[pacman](https://man.archlinux.org/man/pacman.8.en)、[openSUSE](https://doc.opensuse.org/documentation/leap/reference/html/book-reference/cha-sw-cl.html) |
| 归档压缩 | [GNU tar](https://www.gnu.org/software/tar/manual/tar.html)、[GNU gzip](https://www.gnu.org/software/gzip/manual/gzip.html)、本机 `man zip` / `man unzip` |
| tmux / cron | [tmux 上游文档](https://github.com/tmux/tmux/wiki/Getting-Started)、[Cronie crontab 格式手册](https://man7.org/linux/man-pages/man5/crontab.5.html) |
| VS Code 终端 | [官方终端配置说明](https://code.visualstudio.com/docs/terminal/profiles) |

### 19.2 适用条件与本次检查范围

- 参数以 **GNU/Linux 常见用户态工具与 Bash** 为基准，未绑定某一内核版本。BSD/macOS、BusyBox、不同软件版本的选项和默认行为可能不同。
- systemd 示例要求相应服务管理器实际运行；nginx、tmux、jq、rg、iostat、dig 等命令或服务需要另行安装。
- 文中区分了只读查询、文件修改与系统管理操作。示例依赖的路径、账户、包和服务名称都需要按实际环境替换。
- 本次维护日期为 **2026-10-26**：已核对关键参数来源，检查了 75 张 Markdown 表格、28 处内部链接、1 段 JSON 配置和 2 条 cron 示例的字段结构；74 段 Bash 示例均通过 `bash -n` 语法检查。
- 在 **Git for Windows 的 Bash 5.3.15(2)** 中，通过临时文件运行了 12 组代表性验证，覆盖文件名引用、grep、find/xargs、cp、sed、awk、排序计数、重定向、tee、归档压缩、环境变量和管道退出码。这是相应工具与 Shell 行为的验证；安装、服务控制、Linux 权限与挂载、网络请求和跨机传输**未在真实 Linux 主机实测**。
