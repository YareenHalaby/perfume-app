from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from routs.routsPerfume import router as Perfume_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.get("/")
async def welcome():
    return "welcome to my perfumes app"

app.include_router(Perfume_router,prefix="/perfumes")

origins =[
    "http://localhost:3000",
    "http://example.com",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






