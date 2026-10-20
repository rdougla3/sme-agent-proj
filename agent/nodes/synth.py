import json
from models.graph_state import GraphState
from roles import ROLE_CONFIGS
from utils.vertex import query

def synthesize(state: GraphState):
    role = ROLE_CONFIGS["synthesizer"]
    context = f"User Question: {state['query']} \n\nSearch Results: {state['search_results']}"
    progress_text = "Synthesizing research findings"

    findings = json.loads(query(role, context, progress_text))

    return {"research_findings": findings}
