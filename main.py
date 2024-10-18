from fastapi import FastAPI

app = FastAPI()


@app.get("/name/me")
async def read_name_me():
    return {"name": "Ivan"}


@app.get("/name/{name}")
async def read_name(name: str):
    return {"name": name}
