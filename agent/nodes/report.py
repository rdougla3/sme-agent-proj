import json
from models.graph_state import GraphState
from roles import ROLE_CONFIGS
from utils.vertex import client
from utils.tui import show_text, hide_text

def report(state: GraphState):
    role = ROLE_CONFIGS["reporter"]

    show_text("Generating report")

    response = client.models.generate_content(
        model=role["model"],
        contents=f"{role['steering']} \n\nUser Question: {state['query']} \n\nResearch Findings: {state['research_findings']}",
        config=role["config"]
    )

    hide_text()
    print(response.text)
    state['final_report'] = response.text
