from typing import Union
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI


app = FastAPI()
db_info = [
    1, 2, 3, 4, 5, 6
]


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/items/last")
async def last_item():
    return {"item1": db_info[-1]}


@app.get("/items/{item_id}")
async def get_itemid(item_id: Union[int, str]):
    return {"item_id": item_id}


@app.get("/hello/")
async def get_hello_name(name: str = "Ghoste"):
    return {"message": f"Hello {name}"}


@app.post("/users/")
async def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }


@app.post("/calc/")
async def calc(a: Union[int, float], b: Union[int, float], mod: str):
    if mod == '/':
        result = a/b
    if mod == '*':
        result = a*b
    if mod == '-':
        result = a-b
    if mod == '+':
        result = a+b
    return {
        "a": a,
        "b": b,
        "mod": mod,
        "result": result
    }
