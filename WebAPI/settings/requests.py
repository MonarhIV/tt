from pydantic import BaseModel
from datetime import datetime


class PostRequest(BaseModel):
    source_system: str
    name: str
    status: str
    timeToSolve: int


class GetResponse(BaseModel):
    id: int
    name: str
    status: str
    timeCreate: datetime
    source_system: str
    timeToResolve: int

    def __init__(self, id, name, status, timeCreate, source_system, timeToResolve ):
        super().__init__(id=id, name=name, status=status, timeCreate=timeCreate, source_system=source_system, timeToResolve=timeToResolve)