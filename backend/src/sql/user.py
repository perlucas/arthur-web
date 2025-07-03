import enum
from datetime import datetime
from sqlmodel import SQLModel, Field

class Language(str, enum.Enum):
    es = "es"
    en = "en"

class PlanType(str, enum.Enum):
    demo = "demo"
    premium = "premium"
    custom = "custom"


class User(SQLModel, table=True):
    __tablename__ = 'user'

    id: int | None = Field(default=None, primary_key=True)
    full_name: str
    email: str = Field(unique=True)
    password_hash: str
    setting_send_email_notifications: bool = Field(default=True)
    setting_language: Language = Field(default=Language.en)
    plan_type: PlanType
    plan_expires_on: datetime

