from fastapi import FastAPI

from todo_list import todo_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

app.include_router(todo_router)