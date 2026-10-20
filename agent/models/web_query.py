from pydantic import BaseModel

class WebQuery(BaseModel):
    query: str
    results_count: int

class QuerySet(BaseModel):
    queries: list[WebQuery]

class WebResult():
    name: str
    url: str
    date: str
    content: str