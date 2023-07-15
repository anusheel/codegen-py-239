from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

users = []

@app.post("/user/")
async def create_user(user: User):
    users.append(user)
    return user

@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return users[user_id]

@app.put("/user/{user_id}")
async def update_user(user_id: int, user: User):
    users[user_id] = user
    return users[user_id]

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    deleted_user = users[user_id]
    users.pop(user_id)
    return deleted_user