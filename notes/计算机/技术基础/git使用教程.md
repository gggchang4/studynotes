# 1、版本控制方式
## 集中式版本控制工具
版本库集中存放在中央服务器，联网才能工作，eg.SVG，CVS
## 分布式版本控制工具
每个终端都有一个完整的版本库 eg.git

---
# 2、git基本概念
## 2.1 git工作流
![[Editor _ Mermaid Chart-2025-06-24-020820.png]]
![[Pasted image 20250827104159.png]]
## 2.2 git基本命令
1.clone：从远程仓库中克隆代码到本地仓库
2.checkout：从本地仓库中检出一个仓库分支然后进行修订
3.add：再提交前先将代码提交到暂存区
4.commit：提交到本地仓库。本地仓库存放修改的各个版本
5.fetch：从远程库，抓取到本地仓库，不进行任何的合并动作
6.pull：从远程仓库拉取到本地仓库，自动进行合并（merge），然后放到工作区，相当于fetch+merge
7.push：修改完成后，将代码推送到远程仓库

## 2.3 git的安装
- Windows
	https://git-scm.com/download/win
- Mac
	方法1：``` brew install git ```
	方法2： https://git-scm.com/download/mac
- Linux
	```sudo apt update```
	```sudo apt install git -y```

安装完成后验证安装：```git --version```
首次配置（必须）：设置用户名和邮箱
```
git config --global user.name yourname
git config --global user.email youremail@example.com
```

---
# 3、git基本操作
Git 的基本操作主要包括仓库初始化、修改追踪、版本记录、分支管理和远程协作等。以下是常见操作流程及对应命令说明：

## 3.1 初始化仓库
在本地创建一个新的 Git 仓库：
`git init`
执行后，会在当前目录生成一个 `.git` 隐藏文件夹，用于存放版本信息。
文件夹中除了.git文件外都叫工作文件

## 3.2 查看仓库状态
用于查看当前工作区与暂存区的状态差异：
`git status`
可以帮助我们确认哪些文件已修改、哪些已添加到暂存区等。

新修改但是未添加到暂存区的文件分为
	未暂存unstaged
	未跟踪untracked
都可以通过`git add`指令添加到stage里

## 3.3 添加修改到暂存区
将修改后的文件添加到暂存区：
`git add <文件名> # 添加所有修改 git add .`

注意：`add` 并不会直接提交，只是将修改纳入版本控制的准备阶段。

## 3.4 提交到本地仓库
将暂存区中的文件提交到本地仓库，生成一个快照版本：
`git commit -m "提交说明"`
每次提交都会生成一个唯一的提交 ID（哈希值），用于版本追踪。

## 3.5 查看提交历史
查看提交记录及变更日志：
`git log`

命令形式`git log [options]`
options
- --all 显示所有分支
- --pretty=oneline 将所有信息显示为一行
- --abbrev-commit 使得输出的commit更加简短
- --graph 以图的形式输出
以上options可以随意在前后叠加使用

还可以用起别名的方法简化git log命令

## 3.6 版本控制
作用：版本切换
命令形式：`git reset --hard commitID`
	commitID可以通过`git log`查看
	--hard选项的作用是
		HEAD指针指向指定的commit
		工作区和暂存区同时被重置为该commit状态
		**注意**：未提交的修改会丢失

查看已删除的文件
`git reflog`
该指令可以查看已删除的提交记录
原理：git reflog记录了HEAD的移动轨迹，包括reset，merge，checkout
恢复误删的文件可通过以下命令恢复
`git reset --hard commitID`

git reset三种模式
- --soft
- --mixed
- --hard

| 模式            | HEAD 移动        | 暂存区（index） | 工作区（working directory） | 使用场景                                |
| ------------- | -------------- | ---------- | ---------------------- | ----------------------------------- |
| `--soft`      | ✅ 移动到指定 commit | ❌ 不变       | ❌ 不变                   | 回退 commit，但保留修改到暂存区（常用于“撤销提交但继续编辑”） |
| `--mixed`（默认） | ✅ 移动到指定 commit | ✅ 重置暂存区    | ❌ 不变                   | 撤销提交和暂存，但保留文件改动在工作区                 |
| `--hard`      | ✅ 移动到指定 commit | ✅ 重置暂存区    | ✅ 重置工作区                | 完全回退，彻底回到指定 commit 状态（未保存的修改会丢失）    |

## 3.7 分支管理
### 创建分支
`git branch <分支名>`
### 切换分支
`git checkout <分支名>`

也可以用 `git switch`（新版本推荐）：
`git switch <分支名>`
### 创建并切换
`git checkout -b <分支名>`

等价于：
`git branch <分支名> git checkout <分支名>`
### 删除分支
`git branch -d <分支名>`

## 3.8 合并分支

先切换到目标分支，再执行合并命令：
`git checkout main git merge feature-branch`

合并后可能产生冲突，需手动解决并重新提交。

## 3.9 远程仓库操作

### 添加远程仓库地址
`git remote add origin <远程仓库地址>`

例如 GitHub：
`git remote add origin https://github.com/username/repo.git`

### 推送到远程仓库
首次推送：
`git push -u origin main`
常规推送：
`git push`
### 拉取远程仓库最新内容
`git pull`
等价于 `git fetch` + `git merge`，更新本地代码并合并到当前分支。

## 3.10克隆远程仓库

克隆整个远程仓库到本地：
`git clone <远程仓库地址>`
例如：
`git clone https://github.com/username/repo.git`

## 3.11 添加文件至忽略列表
对于某些自动生成的文件如日志文件，临时文件等，不需要纳入git的管理，可以将其添加至.gitignore
1. .gitignore的作用
	- 用于指定哪些文件或目录不需要被Git跟踪
	- 只对于未被跟踪的新文件有效，已被跟踪的文件不会因为被写进.gitignore而被移除
2. 基本语法规则
	- `#`：表示注释行
	- `*.log`：忽略所有 `.log` 结尾的文件
	- `temp/`：忽略整个 `temp` 文件夹
	- `/config.json`：忽略仓库根目录下的 `config.json`，但不忽略子目录中的同名文件
	- `!important.log`：`!` 表示例外规则，不忽略 `important.log` 文件
3. 使用步骤
	1. 在项目根目录创建或编辑.gitignore文件
	2. 写入要忽略的文件/目录规则
	3. 若某文件已被跟踪但是想忽略，先执行
		`git rm --cached filename`
		然后在提交
	4. 全局忽略文件
		如果你希望在所有项目中忽略某些文件（如系统文件 `.DS_Store`、编辑器配置等），可以设置全局 `.gitignore`：
		`git config --global core.excludesfile ~/.gitignore_global`
		然后在 `~/.gitignore_global` 中写入全局忽略规则

> [!example] 示例
> ```gitignore
> # 编译输出
>/build/
>dist/
># 系统文件
>.DS_Store
>Thumbs.db
># 日志与临时文件
*.log
*.tmp
># Python 虚拟环境
>venv/
>__pycache__/
># Node.js 依赖
>node_modules/
># 环境配置文件（含敏感信息）
>.env
> ```