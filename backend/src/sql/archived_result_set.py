from sqlmodel import SQLModel, Field
from datetime import datetime

class ArchivedResultSet(SQLModel, table=True):
    __tablename__ = 'archived_result_set'

    id: int | None = Field(default=None, primary_key=True)
    job_search_id: int
    download_url: str
    created_at: datetime