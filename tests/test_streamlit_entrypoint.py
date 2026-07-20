import importlib
import sys
import unittest


class StreamlitEntrypointTests(unittest.TestCase):
    def test_streamlitapp_module_imports(self):
        sys.modules.pop("streamlitapp", None)
        module = importlib.import_module("streamlitapp")
        self.assertTrue(module is not None)


if __name__ == "__main__":
    unittest.main()
