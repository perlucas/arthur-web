from sqlmodel import SQLModel, Field
from datetime import datetime

class JobSearchResult(SQLModel, table=True):
    __tablename__ = 'job_search_result'

    id: int | None = Field(default=None, primary_key=True)
    job_search_id: int
    url: str
    title: str
    platform: str
    published_at: datetime
    processed_at: datetime