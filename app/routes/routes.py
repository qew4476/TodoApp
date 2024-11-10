from typing import List

from fastapi import APIRouter
import app.db.crud as db
from app.models import sql_model, pydantic_model
from datetime import datetime

todo_route = APIRouter()

@todo_route.post('/task',response_model=pydantic_model.Task)
def create_task(doc:pydantic_model.TaskCreate):
    return db.create_task(doc)

@todo_route.get('/task/{task_id}',response_model=pydantic_model.Task)
def get_task(task_id:int):
    return db.get_one_task(task_id)

@todo_route.get('/tasks/{user_id}',response_model=List[pydantic_model.Task])
def get_a_user_all_tasks(user_id:str):
    return db.get_a_user_all_tasks(user_id)

#delete a task
@todo_route.delete('/task/{task_id}',response_model=pydantic_model.Task)
def delete_task(task_id:int):
    return db.delete_task(task_id)

@todo_route.post('/user',response_model=pydantic_model.User)
def create_user(doc:pydantic_model.UserCreate):
    return db.create_user(doc)

