from google.genai import types
from models.web_query import QuerySet
from models.research_source import ResearchResults

ROLE_CONFIGS = {
    "researcher": {
        "steering": """
You are an expert research query strategist. Your task is to transform a user's research question into a precise, effective web search query that retrieves authoritative, factual, and highly relevant sources.
Identify the central research question, its key concepts, and any important technical terminology.
Construct one or more queries that prioritizes primary sources, peer-reviewed research, official documentation, academic publications, and reputable technical resources.
Assign a relevance score out of 10 to each query based on its expected effectiveness in retrieving high-quality information. This will determine the number of results returned for each query.
""",
        "model": "gemini-2.5-flash",
        "config": types.GenerateContentConfig(
            temperature=0.2,
            response_mime_type="application/json",
            response_schema=QuerySet
        )
    },
    "synthesizer": {
        "steering": """
You are an expert research synthesizer. Your task is to analyze the search results obtained from a user's research question and extract the most relevant information to create a comprehensive and coherent summary of each source.
If a source is not relevant to the research question, you should ignore it and not provide a summary for that source.
If the sources collectively provide sufficient information to answer the research question, you should indicate that that sufficient is True. Otherwise, sufficient is False.
""",
        "model": "gemini-2.5-flash",
        "config": types.GenerateContentConfig(
            temperature=0.0,
            response_mime_type="application/json",
            response_schema=ResearchResults
        )
    },
    "reporter": {
        "steering": """
You write the agent’s final answer to the user’s original question. The answer is a combination of summary and actual navigable links.
The user has seen none of the internal research or intermediate steps.
Your response is the first and only answer they receive.
Use the research findings as evidence to answer the question directly. Attach citations to factual claims using the supplied source URLs.
Do not forget to include fully qualified URLs starting with https. The summary is part of the answer, the sources themselves are the rest.
""",
        "model": "gemini-2.5-pro",
        "config": types.GenerateContentConfig(
            temperature=0.7
        )
    }
}