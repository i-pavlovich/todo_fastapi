import uvicorn
from fastapi import FastAPI

from src.todo.router import router as todo_router

app = FastAPI()


@app.get("/")
def health_check() -> str:
    return "OK"


app.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
