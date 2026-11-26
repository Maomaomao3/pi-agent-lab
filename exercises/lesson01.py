"""第一课练习：请根据讲义亲手完成两个函数。"""

from mini_agent.contracts import TextModel

SYSTEM_PROMPT = "你是一个严谨的中文助手。根据已有信息回答，信息不足时明确说明。"


def build_messages(user_input: str) -> list[dict[str, str]]:
    """清理输入，拒绝空内容，返回新的 system 与 user 消息列表。"""
    raise NotImplementedError("练习 01-A：请先完成 build_messages。")


def run_single_turn(user_input: str, model: TextModel) -> str:
    """通过传入的模型接口完成一次调用，原样返回回复。"""
    raise NotImplementedError("练习 01-B：请完成 run_single_turn。")
