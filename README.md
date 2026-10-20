Create a virtual environment and install the project dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install uv
uv sync --locked
```

Create `.env` in the project root with `VERTEX_API_KEY` and `TAVILY_API_KEY`, then run:

```bash
python agent/orchestrator.py
```
