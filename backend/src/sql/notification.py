from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.types import JSON
from datetime import datetime
import enum

class NotificationType(str, enum.Enum):
    welcome_user = "welcome_user"
    new_results_available = "new_results_available"
    payment_approved = "payment_approved"


class Notification(SQLModel, table=True):
    __tablename__ = 'notification'

    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    is_read: bool
    type: NotificationType
    metadata: dict = Field(default={}, sa_column=Column(JSON))
    created_at: datetime