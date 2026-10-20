from typing import TypedDict
from google.genai import Client
from models.web_query import WebResult

class ResearchFindings(TypedDict, total=False):
    sources: list[dict]
    sufficient: bool

class GraphState(TypedDict):
    query: str
    search_results: list[WebResult]
    research_findings: ResearchFindings
    final_report: str

class GraphContext(TypedDict):
    Vertex: Client
    model: str
