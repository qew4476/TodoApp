import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from app.routes import routes, routes_auth


app = FastAPI()


templates = Jinja2Templates(directory="./app/templates")

app.include_router(routes.task_router, prefix="/todolist", tags=["task_management"])
app.include_router(routes_auth.auth_router, prefix="/auth", tags=["auth"])

@app.get("/login",description="Login Page", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/user/{user_id}", description="User Home Page", response_class=HTMLResponse)
async def user_home(user_id: str,request:Request):
    return templates.TemplateResponse("user_home.html", {"request": request, "user_id": user_id})

#register the user
@app.get("/register", description="Register Page", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


