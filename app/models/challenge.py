from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Challenge(BaseModel):
    title: str
    description: str
    target_value: int
    duration_days: int
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True