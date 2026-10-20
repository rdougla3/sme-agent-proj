import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from utils.tui import progress_text

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

client = genai.Client(
    vertexai=True,
    api_key=os.environ["VERTEX_API_KEY"],
)

def query(role, context, terminal_message):
    stop_text = progress_text(terminal_message)
    try:
        response = client.models.generate_content(
            model=role["model"],
            contents=f"{role['steering']} \n\n{context}",
            config=role["config"]
        )
        return response.text
    finally:
        stop_text()
