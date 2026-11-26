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

本地使用 `main` 分支。远程仓库地址尚未提供，因此当前不能宣称资料已经上传到远程。

用户已选择 GitHub，先按 [VS Code 发布步骤](lessons/00-github-publish.md) 登录并创建私有仓库。也可在已有远程仓库时配置对应的 HTTPS 或 SSH 克隆地址。不需要在聊天中提供密码或 Token；认证在本机完成。

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
