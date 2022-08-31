from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import api

app = FastAPI()

app.include_router(api.router)

@app.get('/')
def root_api():
    return {"message": "Welcome to Thomas Automobile Site"}