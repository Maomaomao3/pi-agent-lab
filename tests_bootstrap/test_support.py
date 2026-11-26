"""验证已经提供的辅导设施；不把未完成练习算作已通过。"""

import contextlib
import io
import unittest

from mini_agent.cli import main
from training_support.mock_model import MockModel


class SupportTests(unittest.TestCase):
    def test_mock_records_snapshot_of_messages(self):
        model = MockModel(response="固定输出")
        messages = [{"role": "user", "content": "原始内容"}]
        self.assertEqual(model.complete(messages), "固定输出")
        messages[0]["content"] = "调用后修改"
        self.assertEqual(model.calls[0][0]["content"], "原始内容")

    def test_mock_instances_have_independent_history(self):
        first, second = MockModel(), MockModel()
        first.complete([{"role": "user", "content": "请求"}])
        self.assertEqual(second.calls, [])

    def test_mock_can_expose_failure_for_acceptance(self):
        failure = RuntimeError("模拟故障")
        model = MockModel(failure=failure)
        with self.assertRaises(RuntimeError) as caught:
            model.complete([{"role": "user", "content": "请求"}])
        self.assertIs(caught.exception, failure)
        self.assertEqual(len(model.calls), 1)

    def test_doctor_reports_ready_environment(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = main(["doctor"])
        self.assertEqual(code, 0)
        self.assertIn("离线学习", output.getvalue())

    def test_demo_is_explicit_about_simulation(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = main(["demo"])
        self.assertEqual(code, 0)
        self.assertIn("没有调用真实大模型", output.getvalue())
        self.assertIn("调用次数：1", output.getvalue())


if __name__ == "__main__":
    unittest.main()
