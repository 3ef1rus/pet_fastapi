from typing import Union
from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.models import Base, db_helper

from items_views import router as items_router
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(items_router)
app.include_router(users_router)


@app.get("/hello/")
async def get_hello_name(name: str = "Ghoste"):
    return {"message": f"Hello {name}"}


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
