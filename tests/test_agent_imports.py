import importlib
import sys
import unittest


class AgentImportTests(unittest.TestCase):
    def test_agent_can_import_tool_registry(self):
        sys.modules.pop("agent", None)
        module = importlib.import_module("agent")
        self.assertTrue(hasattr(module, "Agent"))


if __name__ == "__main__":
    unittest.main()
