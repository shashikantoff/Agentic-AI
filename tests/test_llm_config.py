import importlib
import os
import sys
import unittest
from unittest.mock import patch


class LLMConfigTests(unittest.TestCase):
    def tearDown(self):
        sys.modules.pop("LLM", None)

    def test_uses_environment_values_when_streamlit_secrets_are_unavailable(self):
        with patch.dict(
            os.environ,
            {
                "API_KEY": "env-key",
                "BASE_URL": "https://example.test/v1",
                "MODEL_NAME": "test-model",
            },
            clear=False,
        ):
            llm = importlib.import_module("LLM")

            self.assertEqual(llm.API_KEY, "env-key")
            self.assertEqual(llm.BASE_URL, "https://example.test/v1")
            self.assertEqual(llm.MODEL_NAME, "test-model")


if __name__ == "__main__":
    unittest.main()
