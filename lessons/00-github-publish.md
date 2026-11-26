# 课前准备：在 VS Code 中上传到 GitHub

## 先理解当前进度

- Git：保存在电脑上的版本记录。
- GitHub：托管远程 Git 仓库的网站。
- 本地已经创建独立仓库和初始提交，但还没有配置远程仓库，因此尚未上传。

下面使用 VS Code 内置的发布流程。账号登录与授权由你在本机完成，不需要在聊天中提供密码或 Token。

## 第一步：只打开学习目录

在 VS Code 使用“文件 → 打开文件夹”，选择：

```text
/Users/miurunxuan/Documents/ChatGPT/skill审核插件/pi-agent-lab
```

在“终端 → 新建终端”中执行：

```bash
cd '/Users/miurunxuan/Documents/ChatGPT/skill审核插件/pi-agent-lab'
git rev-parse --show-toplevel
git status -sb
git log -1 --oneline
```

第一条 Git 命令输出的目录应以 `pi-agent-lab` 结尾。这样发布的是学习项目，不会把上一级中文文档站混进来。

## 第二步：打开发布命令

在 macOS 上按 `Command + Shift + P` 打开 VS Code 命令面板，搜索：

```text
Publish to GitHub
```

选择对应的“发布到 GitHub”命令。它会引导创建远程仓库并上传本地提交。

## 第三步：完成 GitHub 登录

如果 VS Code 提示登录，按界面引导进入浏览器，在 `github.com` 完成账号登录和 VS Code 授权，然后返回 VS Code。

如果尚未拥有 GitHub 账号，先在 GitHub 官网注册。密码、验证码和授权操作都在你的本机完成。

基础 GitHub 身份验证和 Git 操作由 VS Code 内置支持，本步骤不要求安装 Pull Requests 扩展。

## 第四步：创建私有仓库并发布

在发布流程中填写仓库名称：

```text
pi-agent-lab
```

选择 **Publish to GitHub private repository**，即“发布到 GitHub 私有仓库”。如果你账号下已有同名仓库，可换一个名称。

当前上传内容包括学习代码、讲义、笔记、进度和验收。虚拟环境、缓存、运行日志和本机环境变量文件已经被忽略。

等待 VS Code 显示发布完成，再使用提示中的“在 GitHub 上打开”。

## 第五步：核对是否真的上传

在 GitHub 仓库中检查：

- 存在 `README.md`、`LEARNING_PLAN.md`、`PROGRESS.md`。
- 存在 `exercises/`、`lessons/`、`mini_agent/` 等目录。
- 能看到本地已创建的提交记录。
- 不应出现 `.venv/`、`.env`、`.runs/` 等本机文件。

在 VS Code 内置终端执行：

```bash
git remote -v
git status -sb
```

正常情况下会看到 GitHub 远程地址，以及 `main` 跟踪远程分支。可把仓库网页地址发回对话，后续继续核对。

## 以后每次学习如何同步

```text
修改代码和笔记
  → 运行当前步骤验收
  → 查看 git diff
  → git add 指定文件
  → git commit 保存本地版本
  → git push 上传
```

完成一次提交不等于已经上传；发布后，后续新增的提交仍需要推送。VS Code 的“同步更改”还会先拉取远程内容，再推送本地提交；初学时先区分提交、推送与同步。

## 官方资料

- [VS Code：源代码管理快速开始](https://code.visualstudio.com/docs/sourcecontrol/quickstart)
- [VS Code：使用 GitHub](https://code.visualstudio.com/docs/sourcecontrol/github)

上传完成后，继续 [第一课 A：VS Code 手写消息组装](01-vscode-hands-on.md)。
