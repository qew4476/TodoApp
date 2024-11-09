# Purpose: Define Pydantic models for the FastAPI application
# It will be used to validate the request body in the POST request(client's or server's input).
#And the sql_model: means the model(table) that will be used to interact with the database

from typing_extensions import Annotated
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime
#restday = 1~7, 1 is Monday, 7 is Sunday
class TaskBase(BaseModel):
    user_id: str
    task_name: str
    deadline: Optional[datetime]=None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    task_id: int

class TaskDelete(TaskBase):
    task_id: int

class UserBase(BaseModel):
    user_id: str

class UserCreate(UserBase):
    password: str
    user_name: str


# task={"task_name":"test","deadline":"2021-10-10T10:00:00","rest_day":[1,4],"workload":1,"workload_unit":"h"}
# TaskCreate(**task)
# print(TaskCreate(**task))