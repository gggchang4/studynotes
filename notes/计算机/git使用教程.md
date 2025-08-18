# 1、版本控制方式
## 集中式版本控制工具
版本库集中存放在中央服务器，联网才能工作，eg.SVG，CVS
## 分布式版本控制工具
每个终端都有一个完整的版本库 eg.git

---
# 2、git基本概念
## 2.1 git工作流
![[Editor _ Mermaid Chart-2025-06-24-020820.png]]
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
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

---
# 3、git基本操作
Git 的基本操作主要包括仓库初始化、修改追踪、版本记录、分支管理和远程协作等。以下是常见操作流程及对应命令说明：

## 3.1 初始化仓库
在本地创建一个新的 Git 仓库：
`git init`
执行后，会在当前目录生成一个 `.git` 隐藏文件夹，用于存放版本信息。

## 3.2 查看仓库状态
用于查看当前工作区与暂存区的状态差异：
`git status`
可以帮助我们确认哪些文件已修改、哪些已添加到暂存区等。

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

常用参数：
- `--oneline`：简洁模式，一行显示一条记录；
    
- `--graph`：图形化展示分支结构。
    

## 3.6 分支管理
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

## 3.7 合并分支

先切换到目标分支，再执行合并命令：
`git checkout main git merge feature-branch`

合并后可能产生冲突，需手动解决并重新提交。

## 3.8 远程仓库操作

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

## 3.9 克隆远程仓库

克隆整个远程仓库到本地：
`git clone <远程仓库地址>`
例如：
`git clone https://github.com/username/repo.git`