import json
from models.graph_state import GraphState
from roles import ROLE_CONFIGS
from utils.vertex import query
from utils.web_search import search_web

def search(state: GraphState):
    role = ROLE_CONFIGS["researcher"]
    context = f"User Question: {state['query']}"
    progress_text = "Generating search queries"

    query_set = json.loads(query(role, context, progress_text))
    results = search_web(query_set)

    return {"search_results": results}