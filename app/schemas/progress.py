from pydantic import BaseModel

class ProgressUpdate(BaseModel):
    challenge_id: str
    progress_value: int