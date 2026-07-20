import os
import streamlit as st

# The OpenAI client may not be available in all environments (for example
# on a fresh deploy where dependencies haven't been installed yet). Import
# defensively so the app can surface a clear error instead of crashing at
# import time.
try:
    from openai import OpenAI, APITimeoutError
    _OPENAI_IMPORTED = True
except Exception:
    OpenAI = None
    APITimeoutError = Exception
    _OPENAI_IMPORTED = False


def _get_setting(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name)
    if value:
        return value

    try:
        if name in st.secrets:
            return st.secrets[name]
    except Exception:
        pass

    try:
        import config
        if hasattr(config, name):
            return getattr(config, name)
    except ImportError:
        pass

    return default


API_KEY = _get_setting("API_KEY")
BASE_URL = _get_setting("BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = _get_setting("MODEL_NAME", "gpt-4o-mini")

client = None
CONFIG_ERROR = None

# If the `openai` package isn't installed, expose a clear configuration
# error instead of letting the import fail during app import.
if not _OPENAI_IMPORTED:
    CONFIG_ERROR = (
        "LLM configuration error: missing 'openai' Python package. "
        "Add 'openai' to your requirements.txt and redeploy."
    )
else:
    if API_KEY:
        try:
            client = OpenAI(
                api_key=API_KEY,
                base_url=BASE_URL,
            )
        except Exception as exc:
            CONFIG_ERROR = f"LLM configuration error: {exc}"
    else:
        CONFIG_ERROR = (
            "LLM is not configured. Set API_KEY in environment variables or add it to Streamlit secrets."
        )


def chat(messages: list) -> str:
    """
    Send messages to the LLM and return the response.
    """
    if client is None:
        return CONFIG_ERROR or "LLM Error: client is not configured."

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0,
            timeout=60,
        )

        return response.choices[0].message.content.strip()

    except APITimeoutError:
        return "LLM Error: Request timed out. Please try again."

    except Exception as exc:
        return f"LLM Error: {exc}"


if __name__ == "__main__":
    print("=" * 50)
    print("LLM Test")
    print("=" * 50)

    messages = [
        {
            "role": "user",
            "content": "Tell me the current date and time.",
        }
    ]

    response = chat(messages)

    print("\nResponse:\n")
    print(response)