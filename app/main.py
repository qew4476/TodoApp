from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from app.routes import routes, routes_auth

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(routes.task_router, prefix="/todolist", tags=["task_management"])
app.include_router(routes_auth.auth_router, prefix="/auth", tags=["auth"])

@app.get("/login",description="Login Page")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

#homw page
@app.get("/user/{user_id}", description="Home Page",response_class=HTMLResponse)
async def user_home(request: Request, user_id: str):
    return templates.TemplateResponse("user_home.html", {"request": request, "user_id": user_id})