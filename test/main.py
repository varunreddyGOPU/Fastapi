from fastapi import FastAPI
import uvicorn
from typing import List
#from doqu import document_base
#from doqu import user
from django.db import models

app = FastAPI()

db: List[User] =[
    User(
        id=uuid4(),
        first_name='jamila',
        last_name='Ahmed',
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name='Alex',
        last_name='jones',
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]
@app.get("/")
async def root():
    return {"hello":"Varun"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;
    
