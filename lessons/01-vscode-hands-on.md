# 第一课 A：在 VS Code 中手写消息组装

## 本次目标

只完成 `build_messages`，让三个消息组装验收通过。`run_single_turn` 留到本课下一步再接起来。

后续全程使用 VS Code：在内置终端创建目录、文件和运行命令，在编辑区亲手写代码。已有骨架用于减少环境准备，不代表业务代码已经实现。

## 1. 打开项目与内置终端

VS Code 应打开下面这个练习文件夹，而不是整个官方源码仓库：

```text
/Users/miurunxuan/Documents/ChatGPT/skill审核插件/pi-agent-lab
```

使用菜单“终端 → 新建终端”，执行：

```bash
cd '/Users/miurunxuan/Documents/ChatGPT/skill审核插件/pi-agent-lab'
pwd
./lab doctor
```

`pwd` 用于确认当前目录，`./lab doctor` 用于检查本项目的 Python 环境。

工作区已经配置 `.venv/bin/python`。右下角若显示其他解释器，可通过命令面板运行 `Python: Select Interpreter`，选择本项目的 `.venv/bin/python`。

## 2. 用命令创建学习笔记

在同一个内置终端运行：

```bash
mkdir -p notes
touch notes/01-messages.md
```

- `mkdir -p`：创建目录；目录已存在时继续使用。
- `touch`：文件不存在时创建空文件，已存在时更新文件时间。

本课练习文件 `exercises/lesson01.py` 已有占位骨架，直接在左侧资源管理器打开。

## 3. 认识当前文件

文件顶部的两项先保留：

```python
from mini_agent.contracts import TextModel

SYSTEM_PROMPT = "你是一个严谨的中文助手。根据已有信息回答，信息不足时明确说明。"
```

`SYSTEM_PROMPT` 是本次调用的系统说明。`TextModel` 是后面连接模型时使用的接口，本步骤暂时不用改。

## 4. 逐行补全第一个函数

只替换 `build_messages` 的占位实现，第二个函数保持原状。推荐自己敲一遍下面的代码，留意缩进。

```python
def build_messages(user_input: str) -> list[dict[str, str]]:
    """把用户输入整理成系统消息和用户消息。"""

    # 去掉两端的空格、换行和制表符，保留内容中间的空白。
    cleaned_input = user_input.strip()

    # 清理后为空，说明没有实际问题；直接报错，不继续请求模型。
    if not cleaned_input:
        raise ValueError("用户输入不能为空")

    # 每次调用都创建新的列表与字典，避免不同请求的消息互相污染。
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": cleaned_input},
    ]
```

按 `Command + S` 保存。

## 5. 读懂每一部分

| 代码 | 本次作用 |
| --- | --- |
| `user_input: str` | 参数预期是一段字符串 |
| `-> list[dict[str, str]]` | 返回列表；每个元素是字符串键值的字典 |
| `.strip()` | 清理字符串两端的空白 |
| `if not cleaned_input` | 检查清理后的字符串是否为空 |
| `raise ValueError(...)` | 把输入无效作为明确错误交给调用者 |
| `role` | 区分系统说明和用户输入 |
| `content` | 消息的实际内容 |
| 函数内部的 `return [...]` | 为每次请求创建独立的消息列表 |

例如输入 `"  你好\n"`，第二条消息的内容应该是 `"你好"`。

## 6. 只验收这一步

在 VS Code 内置终端执行：

```bash
.venv/bin/python -m unittest \
  checks.test_lesson01.Lesson01Acceptance.test_rejects_blank_input \
  checks.test_lesson01.Lesson01Acceptance.test_builds_system_and_trimmed_user_messages \
  checks.test_lesson01.Lesson01Acceptance.test_requests_do_not_share_mutable_messages \
  -v
```

正确实现后，末尾会显示：

```text
Ran 3 tests

OK
```

三项分别验证：空输入被拒绝、消息角色与内容正确、不同请求之间不会共享可变消息。

`./lab check 01` 会运行第一课全部六项验收，其中还包含尚未实现的模型调用函数；本步骤先使用上面的三项。

## 7. 留下一段自己的解释

在 `notes/01-messages.md` 里记录：

- 为什么空格组成的输入也要拒绝？
- 为什么 `return [...]` 放在函数内部？
- 两条消息里的 `role` 与 `content` 分别表示什么？

本步骤验收通过后，再连接 `run_single_turn`，观察模型接口如何收到这些消息。
