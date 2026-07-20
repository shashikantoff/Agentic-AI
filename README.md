# Agentic-AI

Simple Streamlit AI agent app.

Deploy instructions (Streamlit Cloud):

- Set **Main file path** to `streamlitapp.py`.
- Add a secret named `API_KEY` (your OpenAI API key) under Advanced → Secrets.
- Ensure `requirements.txt` is present (this repo includes `streamlit` and `openai`).
- Click Deploy and monitor logs; errors about missing packages mean `requirements.txt` needs adjustment.

Local run:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell
pip install -r requirements.txt
python -m streamlit run streamlitapp.py
```

If you want me to pin exact versions for faster, more deterministic builds, say `pin versions` and I'll set exact versions for you.
