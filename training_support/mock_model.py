"""用于学习消息流的离线模型替身，不进行网络调用或 AI 推理。"""

from dataclasses import dataclass, field


@dataclass
class MockModel:
    """记录每次输入，并返回预设文本或抛出指定异常。"""

    response: str = "[离线模拟] 我收到了消息；这不是实际模型推理。"
    failure: Exception | None = None
    calls: list[list[dict[str, str]]] = field(default_factory=list)

    def complete(self, messages: list[dict[str, str]]) -> str:
        self.calls.append([dict(message) for message in messages])
        if self.failure is not None:
            raise self.failure
        return self.response
