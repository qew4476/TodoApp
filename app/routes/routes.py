from typing import List
from fastapi import APIRouter,Depends
import app.db.crud as db
from app.models import sql_model, pydantic_model
from datetime import datetime
from app.auth.jwt_bearer import JWTBearer

task_router = APIRouter()

@task_router.post('/task', response_model=pydantic_model.Task)
def create_task(doc:pydantic_model.TaskCreate):
    return db.create_task(doc)
#dependencies=[Depends(JWTBearer())]
@task_router.get('/task/{task_id}',dependencies=[Depends(JWTBearer())], response_model=pydantic_model.Task)
def get_task(task_id:int):
    return db.get_one_task(task_id)

@task_router.get('/tasks/{user_id}', response_model=List[pydantic_model.Task])
def get_one_user_all_tasks(user_id:str):
    return db.get_a_user_all_tasks(user_id)

#delete a task
@task_router.delete('/task/{task_id}', response_model=pydantic_model.Task)
def delete_task(task_id:int):
    return db.delete_task(task_id)

#update a task
@task_router.put('/task/{task_id}', response_model=pydantic_model.Task)
def update_task(task_id:int,doc:pydantic_model.Task):
    return db.update_task(task_id,doc)

