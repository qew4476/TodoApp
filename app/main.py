from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from app.routes import routes, routes_auth

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(routes.task_router, prefix="/todolist", tags=["task_management"])
app.include_router(routes_auth.auth_router, prefix="/auth", tags=["auth"])

@app.get("/login",description="Login Page")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

#homw page
@app.get("/",description="Home Page(To do list)")
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})