# 练习与 Pi 源码对照

固定版本：v1.6.1；提交：`ef4a1cfcca62b77ad3558337ff3e1c7f6beeadfe`。

我们用 Python 学机制，官方源码使用 TypeScript。对照重点是数据结构、边界与行为，不要求逐行翻译。

| 练习内容 | 本地官方源码或文档 | 先看什么 |
| --- | --- | --- |
| 总体数据流 | `../vendor/pi/packages/coding-agent/docs/how-pi-works.md` | 请求、工具、上下文与会话的关系 |
| 模型适配 | `../vendor/pi/packages/ai/README.md` | 模型和供应商边界 |
| 消息、工具与事件 | `../vendor/pi/packages/agent/src/types.ts` | 一次调用需要哪些字段 |
| Agent 循环 | `../vendor/pi/packages/agent/src/agent-loop.ts` | 何时继续、何时停止、工具结果如何加入上下文 |
| Agent 状态入口 | `../vendor/pi/packages/agent/src/agent.ts` | 公共方法、状态与取消 |
| Skill 发现 | `../vendor/pi/packages/coding-agent/src/core/skills.ts` | 元数据、路径、加载诊断 |
| Skill 使用 | `../vendor/pi/packages/coding-agent/docs/skills.md` | 名称描述先发现，完整说明按需读取 |
| 会话与分支 | `../vendor/pi/packages/coding-agent/src/core/session-manager.ts` | 记录树与活动分支 |
| Hook 和扩展 | `../vendor/pi/packages/coding-agent/docs/extensions.md` | 工具执行前后、会话层与内核层的区别 |

## 中文阅读入口

- [运行原理](http://127.0.0.1:4321/#/zh/how-pi-works)
- [Agent 内核导读](http://127.0.0.1:4321/#/zh/agent-core)
- [Skill 技能机制](http://127.0.0.1:4321/#/zh/skills)
- [核心执行循环源码](http://127.0.0.1:4321/#/source/agent-loop)

第一课只处理文本消息和一次调用。后续课程再把响应扩展为文本、工具调用、使用量和状态；不要把第一课的字符串返回值误认为完整 Agent 协议。
