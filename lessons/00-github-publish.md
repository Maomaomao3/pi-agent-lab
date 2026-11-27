# 课前准备：在 VS Code 中上传到 GitHub

## 先理解当前进度

- Git：保存在电脑上的版本记录。
- GitHub：托管远程 Git 仓库的网站。
- 本地提交只保存在电脑上；连接远程仓库并成功推送后，才能确认已上传。

尚未创建远程仓库时，可使用下面的 VS Code 内置发布流程。账号登录与授权由你在本机完成，不需要在聊天中提供密码或 Token。已经在 GitHub 网页建好仓库时，直接使用后面的“已有仓库：首次推送”，不要重复创建同名仓库。

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

## 已有仓库：首次推送

本项目已经连接用户创建的仓库：`https://github.com/Maomaomao3/pi-agent-lab.git`，远程名称为 `origin`。无需重复执行 `git remote add origin`。

本项目于 2026-11-27 完成首次推送，并核对了远程 `main` 与本地提交一致。下面保留首次操作供复习；继续学习时使用后面的日常同步流程。

在 VS Code 点击“终端 → 新建终端”，执行：

```bash
cd '/Users/miurunxuan/Documents/ChatGPT/skill审核插件/pi-agent-lab'
git remote -v
git -c http.proxy=http://127.0.0.1:7897 push -u origin main
```

- `origin`：本项目给 GitHub 远程地址起的简称。
- `main`：准备上传的本地分支。
- `-u`：首次推送成功后，建立本地分支与远程分支的跟踪关系。
- `-c http.proxy=...`：仅为这一次命令指定本机已验证可用的代理，不永久修改 Git 配置。代理端口将来变化时，要改成当时的实际端口。

VS Code 内置终端可以通过编辑器的 Git 身份验证通道处理登录；若出现 GitHub 登录或授权提示，在本机完成。若终端直接要求输入用户名或密码，先停止并核对身份验证方式，不把 GitHub 账号密码当作 HTTPS 推送密码。

成功输出通常包含 `main -> main` 和分支跟踪提示。接着执行：

```bash
git status -sb
git ls-remote --heads origin main
```

再刷新 GitHub 仓库，检查 `README.md`、`lessons/` 和 `exercises/`。如果提示远程已有更新导致拒绝推送，保留报错并先检查远程内容，不使用强推覆盖。

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
- [VS Code：内置终端与 Git 身份验证](https://code.visualstudio.com/docs/terminal/advanced)
- [GitHub：上传本地代码](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

上传完成后，继续 [第一课 A：VS Code 手写消息组装](01-vscode-hands-on.md)。
