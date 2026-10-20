from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from models.graph_state import GraphState
from nodes.search import search
from nodes.synth import synthesize
from nodes.report import report

builder = StateGraph(GraphState)

builder.add_node("search", search)
builder.add_node("synthesize", synthesize)
builder.add_node("report", report)

builder.add_edge(START, "search")
builder.add_edge("search", "synthesize")
builder.add_edge("synthesize", "report")
builder.add_edge("report", END)

graph = builder.compile()