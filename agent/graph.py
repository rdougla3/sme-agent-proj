from langgraph.graph import StateGraph, START, END
from models.graph_state import GraphState
from nodes.search import search
from nodes.synth import synthesize
from nodes.report import report

def evidence_gate(state: GraphState):
    if(state["research_findings"]["sufficient"]):
        return "report"
    else:
        print("Insufficient evidence was found to answer the query")
        return END # TODO, obviously

builder = StateGraph(GraphState)

builder.add_node("search", search)
builder.add_node("synthesize", synthesize)
builder.add_node("report", report)

builder.add_edge(START, "search")
builder.add_edge("search", "synthesize")
builder.add_conditional_edges("synthesize", evidence_gate)
builder.add_edge("report", END)

graph = builder.compile()
