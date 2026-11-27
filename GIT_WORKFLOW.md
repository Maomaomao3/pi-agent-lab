# 学习资料的 Git 管理

## 管理范围

本学习目录使用独立 Git 仓库，与上一级的文档站工程分开。

需要保存的内容：

- `mini_agent/`、`exercises/`：学习代码与当前实现。
- `lessons/`、`notes/`：讲义和个人复盘。
- `checks/`、`tests_bootstrap/`、`training_support/`：验收与辅导设施。
- `skills/`、`samples/`：技能练习和虚构样例数据。
- 学习计划、进度、源码对照、VS Code 项目配置与依赖声明。

不入库的本地内容由 `.gitignore` 排除：虚拟环境、Python 缓存、`.env` 等本机配置、运行日志和系统文件。`.env.example` 只包含空的变量说明，可以提交。

官方 Pi 源码在上一级 `vendor/pi/`，不复制进本仓库。更换电脑时可从 [固定版本官方仓库](https://github.com/earendil-works/pi/tree/v1.6.1) 获取参考材料。

## 当前状态

本地使用 `main` 分支。用户已创建 GitHub 仓库，`origin` 已配置为：

```text
https://github.com/Maomaomao3/pi-agent-lab.git
```

2026-11-27：远程地址已在本地配置；首次推送尚未完成。代理可用，但辅导终端缺少 GitHub 命令行认证，读取远程时返回无法获取用户名。下一步在 VS Code 新建内置终端，按 [已有仓库的首次推送步骤](lessons/00-github-publish.md) 完成认证和上传。不需要再次运行 `Publish to GitHub`，也不需要在聊天中提供密码或 Token。

## 在 VS Code 中完成一次学习提交

在 VS Code 内置终端进入本学习目录：

```bash
cd '/Users/miurunxuan/Documents/ChatGPT/skill审核插件/pi-agent-lab'
git status --short
git diff
```

先运行当前步骤对应的验收。第一课 A 的消息组装通过后，可以提交这一小步，不必把它描述成整课已经完成。

```bash
git add exercises/lesson01.py notes/ PROGRESS.md
git diff --cached
git commit -m "lesson01: implement message construction"
```

配置远程后再同步：

```bash
git push origin main
```

`git add` 选择要保存的修改，`git commit` 在本地创建版本记录，`git push` 才会把提交发送到远程仓库。

## 同步约定

用户要求本项目的学习资料上传到 Git。后续在明确记录阶段状态、完成相应检查后，沿用用户指定的远程仓库同步。

- 保留未完成练习的真实状态，不为提交而补写用户应当亲手完成的答案。
- 每次提交使用明确的文件路径，先看差异，避免混入其他工作。
- 不上传凭证、虚拟环境或运行日志。
- 不强推、不改写已有远程历史；远程已有内容时先检查再合并。
- 推送成功后报告实际提交；仅有本地提交时明确说明还未上传。
- 不把上一级文档站或其他目录加入这个学习仓库。
