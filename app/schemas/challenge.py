from pydantic import BaseModel

class ChallengeCreate(BaseModel):
    title: str
    description: str
    target_value: int
    duration_days: int