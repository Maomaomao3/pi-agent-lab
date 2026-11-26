"""提供环境检查、离线演示和逐课验收，不代替学习者的练习实现。"""

import argparse
import json
from pathlib import Path
import sys
import unittest

from training_support.mock_model import MockModel

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def doctor() -> int:
    """检查第一课依赖的本地条件，不读取或显示模型凭证。"""
    checks = [
        ("Python 版本不低于 3.11", sys.version_info >= (3, 11)),
        ("第一课练习文件存在", (PROJECT_ROOT / "exercises/lesson01.py").is_file()),
        ("样例日志存在", (PROJECT_ROOT / "samples/app.log").is_file()),
        ("学习计划存在", (PROJECT_ROOT / "LEARNING_PLAN.md").is_file()),
    ]
    print(f"项目：{PROJECT_ROOT}")
    print(f"Python：{sys.version.split()[0]}")
    for label, passed in checks:
        print(f"[{'通过' if passed else '失败'}] {label}")
    print("当前模式：离线学习；无需第三方依赖，不请求真实模型。")
    return 0 if all(passed for _, passed in checks) else 1


def demo() -> int:
    """展示一次预设输入和预设回复，所有模拟行为均明确标注。"""
    messages = [
        {"role": "system", "content": "这是离线演示的系统说明。"},
        {"role": "user", "content": "演示一次消息收发。"},
    ]
    model = MockModel()
    print("[离线模拟] 以下数据流用于演示接口，没有调用真实大模型。")
    print("发送给模型接口的消息：")
    print(json.dumps(messages, ensure_ascii=False, indent=2))
    print("返回：", model.complete(messages))
    print(f"记录到的调用次数：{len(model.calls)}")
    print("下一步：阅读 lessons/01-model-interface.md，完成 exercises/lesson01.py。")
    return 0


def run_lesson01(user_input: str) -> int:
    """运行学习者提供的第一课实现。"""
    from exercises.lesson01 import run_single_turn

    print("[离线模拟] 当前使用 MockModel，不进行真实模型推理。")
    try:
        response = run_single_turn(user_input, MockModel())
    except NotImplementedError as error:
        print(f"尚待实现：{error}", file=sys.stderr)
        return 2
    except ValueError as error:
        print(f"输入错误：{error}", file=sys.stderr)
        return 2
    print(response)
    return 0


def check_lesson(lesson: str) -> int:
    """执行当前课的行为验收，未实现练习必须保持未通过状态。"""
    print("第一课验收：练习未实现时出现 NotImplementedError 是预期起点。", flush=True)
    suite = unittest.defaultTestLoader.loadTestsFromName(f"checks.test_lesson{lesson}")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


def main(argv: list[str] | None = None) -> int:
    """解析学习命令并返回明确退出码。"""
    parser = argparse.ArgumentParser(description="Pi Agent 手写实验室：先理解，再逐课实现。")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("doctor", help="检查本地学习环境")
    commands.add_parser("demo", help="运行明确标记的离线 Mock 演示")
    lesson = commands.add_parser("lesson01", help="运行你实现的第一课代码（离线）")
    lesson.add_argument("--input", required=True, help="传给练习的用户输入")
    check = commands.add_parser("check", help="运行逐课行为验收")
    check.add_argument("lesson", choices=["01"], help="当前已准备的课次")
    args = parser.parse_args(argv)
    if args.command == "doctor":
        return doctor()
    if args.command == "demo":
        return demo()
    if args.command == "lesson01":
        return run_lesson01(args.input)
    return check_lesson(args.lesson)
