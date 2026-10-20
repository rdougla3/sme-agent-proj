import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

client = genai.Client(
    vertexai=True,
    api_key=os.environ["VERTEX_API_KEY"],
)
