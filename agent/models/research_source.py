from pydantic import BaseModel

class ResearchSource(BaseModel):
    url: str
    date: str
    summary: str

class ResearchResults(BaseModel):
    sources: list[ResearchSource]
    sufficient: bool