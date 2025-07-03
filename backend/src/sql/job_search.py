from sqlmodel import SQLModel, Field
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.types import JSON

class JobSearch(SQLModel, table=True):
    __tablename__ = 'job_search'

    id: int | None = Field(default=None, primary_key=True)
    name: str
    is_active: bool
    location: str
    # Note: uses keys 'title_includes', 'title_excludes', 'description_includes', 'description_excludes'
    search_parameters: dict = Field(default={}, sa_column=Column(JSON))
    setting_send_email_notifications: bool = Field(default=True)
    last_updated_at: datetime | None = Field(default=None)