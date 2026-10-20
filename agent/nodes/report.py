import json
from models.graph_state import GraphState
from roles import ROLE_CONFIGS
from utils.vertex import query

def report(state: GraphState):
    role = ROLE_CONFIGS["reporter"]
    context = f"User Question: {state['query']} \n\nResearch Findings: {state['research_findings']}"
    progress_text = "Generating report"
    
    response = query(role, context, progress_text)

    return {"final_report": response}