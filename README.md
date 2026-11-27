# Pi Agent 手写实验室

用 Python 亲手实现一个本地 Agent：模型调用、工具循环、Skill 加载、会话记录、Mock 与回归测试。Pi v1.6.1 用作设计参照。

这是独立练习目录。已有中文学习站仍在 `http://127.0.0.1:4321`，官方源码保留在上一级的 `vendor/pi/`。

## 从哪里开始

先按 [课前准备：VS Code 上传到 GitHub](lessons/00-github-publish.md) 完成远程发布，再进入第一课。

1. 阅读 [学习计划](LEARNING_PLAN.md)，了解每课要完成什么。
2. 运行环境检查和离线演示。
3. 在 VS Code 中按 [第一课 A：命令与逐行代码](lessons/01-vscode-hands-on.md) 开始，再参考 [第一课完整说明](lessons/01-model-interface.md)。
4. 运行第一课验收，把结果和你的理解拿来继续讨论。

```bash
cd '/Users/miurunxuan/Documents/ChatGPT/skill审核插件/pi-agent-lab'
./lab doctor
./lab demo
./lab check 01
```

第一课只用 Python 标准库，无需安装第三方包，也不会请求模型服务。`demo` 显示的是预设的 Mock 返回值，不能用来证明真实模型能力。

本机已经创建 `.venv/` 虚拟环境，固定使用 Python 3.14.2。统一用 `./lab` 运行课程命令，避免终端中的 `python3` 指向另一个版本。也可以使用 `.venv/bin/python` 直接执行 Python。

`check 01` 是给你的练习准备的验收。初始练习中的 `NotImplementedError` 会使验收失败；完成两个函数后，再以验收通过为目标。这是明确保留的学习任务。

## 目录

```text
pi-agent-lab/
├── AGENTS.md                 # 后续辅导与代码修改约定
├── LEARNING_PLAN.md          # 九课计划、产物和验收标准
├── PROGRESS.md               # 当前学习进度
├── SOURCE_MAP.md             # 练习模块与 Pi 源码对照
├── lab                       # 固定解释器的统一运行入口
├── .venv/                    # 独立 Python 环境，已忽略版本管理
├── lessons/
│   └── 01-model-interface.md # 当前课：先讲清楚，再动手
├── exercises/
│   └── lesson01.py           # 你需要亲手补全的代码
├── mini_agent/               # 可运行的学习命令入口
├── training_support/         # 离线 Mock 等辅导设施
├── checks/                   # 每课的行为验收
├── tests_bootstrap/          # 已提供学习设施的验证
├── samples/                  # 虚构日志等学习数据
├── skills/                   # 第五课开始编写业务 Skill
└── notes/                    # 你自己的理解与复盘
```

## 辅导方式

每课按“说明目标 → 阅读少量代码 → 你实现 → 运行验收 → 解释结果 → 复盘”进行。先完成当前课的能力，再根据你的要求进入下一课。

当前没有替你实现完整 Agent，也没有接入 Dify、Pi SDK 或真实模型。后续工具调度和循环会由你自己写出来。

## Git 版本管理

学习代码、讲义、笔记和进度由本目录的独立仓库管理。虚拟环境、本机配置、缓存和运行日志不入库。

参见 [Git 操作与同步约定](GIT_WORKFLOW.md)。本项目已连接 GitHub 仓库 `Maomaomao3/pi-agent-lab`，于 2026-11-27 完成首次推送并核对远程提交；后续学习继续提交和推送。

## 常用命令

```bash
# 环境检查
./lab doctor

# 查看一次离线模型接口演示
./lab demo

# 验收第一课
./lab check 01

# 完成第一课后运行你的实现
./lab lesson01 --input '解释一下 Agent 是什么'

# 验证已提供的学习设施
.venv/bin/python -m unittest discover -s tests_bootstrap -v
```

如果将来需要重建虚拟环境，先确认所选 Python 版本不低于 3.11，再运行 `python3 -m venv .venv`。当前目录的虚拟环境与其他项目相互独立。

## 最终验收场景

你输入“分析样例日志”，程序能够发现并加载日志分析 Skill，调用受控工具获取真实样例内容，运行分析逻辑，保存过程记录，并根据证据输出结论。

这套能力应由本项目完成，移除 Dify 后仍可运行。真实模型与业务平台的依赖会单独声明；当前离线演示不依赖这些服务。
