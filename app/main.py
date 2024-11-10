import uvicorn
from fastapi import FastAPI
from app.routes import routes
app = FastAPI()

app.include_router(routes.todo_route, prefix="/todolist")

