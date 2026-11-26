"""第一课验收：约束消息与调用行为，不依赖真实模型。"""

import unittest

from exercises.lesson01 import SYSTEM_PROMPT, build_messages, run_single_turn
from training_support.mock_model import MockModel


class Lesson01Acceptance(unittest.TestCase):
    def test_rejects_blank_input(self):
        with self.assertRaises(ValueError):
            build_messages(" \n\t ")

    def test_builds_system_and_trimmed_user_messages(self):
        messages = build_messages("  请分析日志\n")
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0], {"role": "system", "content": SYSTEM_PROMPT})
        self.assertTrue(SYSTEM_PROMPT.strip())
        self.assertEqual(messages[1], {"role": "user", "content": "请分析日志"})

    def test_requests_do_not_share_mutable_messages(self):
        first = build_messages("第一个请求")
        first[0]["content"] = "只修改本次消息"
        first.append({"role": "assistant", "content": "只属于第一个请求"})
        second = build_messages("第二个请求")
        self.assertEqual(len(second), 2)
        self.assertEqual(second[0]["content"], SYSTEM_PROMPT)
        self.assertEqual(second[1]["content"], "第二个请求")

    def test_calls_model_once_and_preserves_reply(self):
        model = MockModel(response="  原始回复\n保留换行与空白  ")
        response = run_single_turn("  检查消息流  ", model)
        self.assertEqual(len(model.calls), 1)
        self.assertEqual(model.calls[0], build_messages("检查消息流"))
        self.assertEqual(response, model.response)

    def test_blank_input_never_reaches_model(self):
        model = MockModel()
        with self.assertRaises(ValueError):
            run_single_turn(" \n ", model)
        self.assertEqual(model.calls, [])

    def test_model_failure_is_not_reported_as_success(self):
        error = RuntimeError("预设的模型故障")
        model = MockModel(failure=error)
        with self.assertRaises(RuntimeError) as caught:
            run_single_turn("有效输入", model)
        self.assertIs(caught.exception, error)
        self.assertEqual(len(model.calls), 1)


if __name__ == "__main__":
    unittest.main()
