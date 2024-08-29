from fastapi import FastAPI
from datetime import datetime
from settings.requests import PostRequest
from db import CreatRequest

app = FastAPI(
    title="tt"
)


@app.post('/api/ticket')
async def f(request: PostRequest):
    if await CreatRequest(request.name, request.status, datetime.now(), request.timeToSolve, 'client'):
        return 200
    return 400


@app.get('/api/ticket')
async def ff():
    return 200
