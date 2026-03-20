from pydantic import BaseModel, Field
from datetime import datetime

class UserChallenge(BaseModel):
    user_id: str
    challenge_id: str
    joined_at: datetime = Field(default_factory=datetime.utcnow)
    progress: int = 0

    class Config:
        orm_mode = True