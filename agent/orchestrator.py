from graph import graph

query = input("Type a detailed & specific query for the research agent to analyize, such as: \nWhat are the pros and cons of using PFA release flim compared to ACF and traditional FEP in SLA/DLP 3d printing?\n\n")

result = graph.invoke({
    "query": query,
    "search_results": [],
    "research_findings": {},
    "final_report": ""
})

print("\n", result["final_report"])