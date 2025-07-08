from pydantic import BaseModel, Field
from datetime import datetime

class JobSearchParameters(BaseModel):
    title_includes: list[str] = Field(max_length=3)
    title_excludes: list[str] = Field(max_length=3)
    description_includes: list[str] = Field(max_length=3)
    description_excludes: list[str] = Field(max_length=3)

class JobSearchOutput(BaseModel):
    id: int
    name: str
    is_active: bool
    location: str
    search_parameters: dict
    setting_send_email_notifications: bool
    updated_at: datetime