import os
from pathlib import Path
from dotenv import load_dotenv
import httpx
import trafilatura

from models.web_query import QuerySet
from utils.tui import progress_text

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

def search_web(querySet: QuerySet):
    results = []
    stop_text = progress_text("Searching the web")
    try:
        for query in querySet['queries']:
            results.extend(run_query(query['query'], num_results=query['results_count']))
        return results
    finally:
        stop_text()

def run_query(query: str, num_results: int = 10, timeout: float = 20):
    key = os.environ["TAVILY_API_KEY"]
    with httpx.Client(timeout=timeout) as client:
        response = client.post(
            "https://api.tavily.com/search",
            headers={"Authorization": f"Bearer {key}"},
            json={
                "query": query.strip(),
                "max_results": num_results,
                "search_depth": "basic",
                "auto_parameters": False,
                "include_answer": False,
                "include_raw_content": False,
            },
        )
        response.raise_for_status()

    results = []
    for result in response.json()["results"]:
        try:
            content = fetch_article(result["url"])
        except Exception:
            continue # Some websites do not like to be scraped. not a big deal. we move on
        results.append({
            "name": result["title"],
            "url": result["url"],
            "date": result.get("date"),
            "content": content,
        })

    return results[:num_results]


def fetch_article(url: str) -> tuple[str, str | None]:
    with httpx.Client(follow_redirects=True, timeout=20) as client:
        response = client.get(url)
        response.raise_for_status()

    resolved_url = str(response.url)
    content = trafilatura.extract(
        response.text,
        include_tables=True,
        favor_recall=True,
    )
    return resolved_url, content
