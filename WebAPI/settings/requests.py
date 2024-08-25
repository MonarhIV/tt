from pydantic import BaseModel
from datetime import datetime


class PostRequest(BaseModel):
    source_system: str
    name: str
    status: str
    timeToSolve: datetime
