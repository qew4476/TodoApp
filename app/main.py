from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates


from app.routes import routes, routes_auth

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(routes.task_router, prefix="/todolist", tags=["task_management"])
app.include_router(routes_auth.auth_router, prefix="/auth", tags=["auth"])

@app.get("/login",description="Login Page")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/user/{user_id}")
async def user_home(user_id: str,request:Request):
    # 這裡的 token 已經是經過驗證的 Bearer Token
    return templates.TemplateResponse("user_home.html", {"request": request, "user_id": user_id})