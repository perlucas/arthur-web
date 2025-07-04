from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.types import JSON
from datetime import datetime
import enum

class PaymentType(str, enum.Enum):
    subscription_renewed = "subscription_renewed"

class Payment(SQLModel, table=True):
    __tablename__ = 'payment'

    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    type: PaymentType
    metadata: dict = Field(default={}, sa_column=Column(JSON))
    created_at: datetime
    approved_at: datetime