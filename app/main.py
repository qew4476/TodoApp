from fastapi import FastAPI, HTTPException

from app.db.crud import create_user, get_all_users
from app.routes import routes
from app.models.pydantic_model import UserCreate, UserLogin
from app.auth.jwt_handler import signJWT
app = FastAPI()

app.include_router(routes.todo_route, prefix="/todolist", tags=["task"])

#user registration
@app.post('/register', tags=["user"])
def user_register(user:UserCreate):
    new_user = create_user(user)    #type(user) = SQL Table:User
    # Check if the user was created successfully
    if new_user.get('status') == 'error':
        raise HTTPException(status_code=400, detail=new_user.get('msg'))
    return signJWT(new_user.get('data').user_id)

#user login
@app.post('/login', tags=["user"])
def user_login(login_user: UserLogin):
    # It will stop the search when the first item is found.
    existing_user = next((user for user in get_all_users() if user.user_id == login_user.user_id), None)

    if existing_user is None or existing_user.password != login_user.password:
        raise HTTPException(status_code=401, detail="Invalid login credentials")

    return signJWT(login_user.user_id)

#user logout(destroy the token, and the user will be transferred to the login page)