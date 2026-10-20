import json
from models.graph_state import GraphState
from roles import ROLE_CONFIGS
from utils.vertex import client
from utils.tui import show_text, hide_text

def synthesize(state: GraphState):
    role = ROLE_CONFIGS["synthesizer"]

    show_text("Synthesizing research findings")

    response = client.models.generate_content(
        model=role["model"],
        contents=f"{role['steering']} \n\nUser Question: {state['query']} \n\nSearch Results: {state['search_results']}",
        config=role["config"]
    )

    hide_text()
    findings = json.loads(response.text)
    state['research_findings']['sources'] = findings['sources']
    state['research_findings']['sufficient'] = findings['sufficient']

    return {"research_findings": state['research_findings']}
