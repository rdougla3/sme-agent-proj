import json
from models.graph_state import GraphState
from roles import ROLE_CONFIGS
from utils.vertex import client
from utils.web_search import search_web
from utils.tui import show_text, hide_text

def search(state: GraphState):
    role = ROLE_CONFIGS["researcher"]

    show_text("Generating search queries")

    response = client.models.generate_content(
        model=role["model"],
        contents=f"{role['steering']} \n\nUser Question: {state['query']}",
        config=role["config"]
    )

    hide_text()
    show_text("Searching the web")

    query_json = json.loads(response.text)
    for query in query_json['queries']:
        results = search_web(query['query'], num_results=query['results_count'])
        state["search_results"].append(results)
    hide_text()
    return {"search_results": state["search_results"]}
