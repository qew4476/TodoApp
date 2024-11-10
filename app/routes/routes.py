from fastapi import APIRouter
import app.db.crud as db
from app.models import sql_model, pydantic_model
from datetime import datetime

todo_route = APIRouter()

@todo_route.post('/task')
def new_task(doc:pydantic_model.TaskCreate):
    doc = dict(doc)
    return db.create_task(doc)