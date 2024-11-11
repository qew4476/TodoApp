from fastapi import FastAPI
from app.routes import routes, routes_auth
app = FastAPI()

app.include_router(routes.task_router, prefix="/todolist", tags=["task_management"])
app.include_router(routes_auth.auth_router, prefix="/auth", tags=["auth"])

