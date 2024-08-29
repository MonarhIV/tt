from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from settings.requests import PostRequest, GetResponse
from db import CreatTickets, clientResponse

app = FastAPI(
    title="tt"
)
origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:4000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/api/ticket')
async def f(request: PostRequest):
    if await CreatTickets(request.name, request.status, datetime.now(), request.timeToSolve, 'client'):
        return 200
    return 400


@app.get('/api/ticket')
async def ff():
    tikets = await clientResponse()
    response = {
        "tikets":[]
    }
    for i in tikets:
        i = list(i)
        tiket = GetResponse(*i)
        tiket.dict()
        response.setdefault('tikets', []).append(tiket)
    return response
