"""第一课的最小文本模型接口，后续真实实现可以遵守同一契约。"""

from typing import Protocol


class TextModel(Protocol):
    """只约定调用入口，不指定供应商或实现方式。"""

    def complete(self, messages: list[dict[str, str]]) -> str:
        """接收消息列表，返回一次调用的文本。"""
        ...
