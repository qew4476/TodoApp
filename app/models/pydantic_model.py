# Purpose: Define Pydantic models for the FastAPI application
# It will be used to validate the request body in the POST request(client's or server's input).
#And the sql_model: means the model(table) that will be used to interact with the database

from typing_extensions import Annotated
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
#restday = 1~7, 1 is Monday, 7 is Sunday
class TaskBase(BaseModel):
    task_name: str
    deadline: Optional[datetime]=None

class TaskCreate(TaskBase):
    user_id: str

class Task(TaskBase):
    task_id:int
    user_id:str

    class Config:
        from_attributes = True

class many_tasks(BaseModel):
    tasks:List[Task]

class UserBase(BaseModel):
    user_name: str

class UserCreate(UserBase):
    user_id: str
    password: str

class User(UserBase):
    user_id:str
    tasks:List[Task] = []

    class Config:   #transfer orm(table) to pydantic if they have the same column
        from_attributes=True

# task={"task_name":"test","deadline":"2021-10-10T10:00:00","rest_day":[1,4],"workload":1,"workload_unit":"h"}
# TaskCreate(**task)
# print(TaskCreate(**task))