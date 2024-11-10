from typing import List

import app.models.sql_model as sql_model
import app.models.pydantic_model as pydantic_model


import datetime #to get the current time

from app.db.connection import db_session


def get_timestamp():
    return datetime.datetime.now()


def create_user(user:pydantic_model.UserCreate):    #It means the input data must match the format of UserCreate
    try:
        #Format the input data (user) to meet the requirements for entering user data into the database.
        db_user_data = sql_model.User(user_id=user.user_id,password=user.password,user_name=user.user_name)

        db_session.add(db_user_data)
        db_session.commit()
        db_session.refresh(db_user_data)
        return db_user_data
    except Exception as e:
        return {
            'status': 'error',
            'msg': str(e)
        }

def create_task(task:pydantic_model.TaskCreate):
    try:
        db_task_data = sql_model.Task(task_name=task.task_name, deadline=task.deadline,  user_id=task.user_id)
        db_session.add(db_task_data)
        db_session.commit()
        db_session.refresh(db_task_data)
        return db_task_data

    except Exception as e:
        return {
            'status':'error',
            'msg':str(e)
        }

def get_one_task(task_id:int):
    task_db = db_session.query(sql_model.Task).filter(sql_model.Task.task_id==task_id).first()
    if not task_db:
        return None
    return pydantic_model.Task.model_validate(task_db)

def get_a_user_all_tasks(user_id:str):
    tasks_db = db_session.query(sql_model.Task).filter(sql_model.Task.user_id==user_id).all()
    return [pydantic_model.Task.model_validate(task) for task in tasks_db]

def delete_task(task_id:int):
    task_db = db_session.query(sql_model.Task).filter(sql_model.Task.task_id==task_id).first()
    if not task_db:
        return None
    db_session.delete(task_db)
    db_session.commit()
    return task_db

def update_task(task_id:int, new_task:pydantic_model.Task):
    db_task = db_session.query(sql_model.Task).filter(sql_model.Task.task_id==task_id).first()
    if not db_task:
        return None
    for key, value in new_task.model_dump().items():
        setattr(db_task, key, value)
    db_session.commit()
    return pydantic_model.Task.model_validate(db_task)



# # test
# user = {'user_id':'abc','password':'123','user_name':'Me'}
# print(create_user(pydantic_model.UserCreate(**user)))
#
# task={"task_name":"test","deadline":"2021-10-10T10:00:00","user_id":"abc"}
# print(create_task(pydantic_model.TaskCreate(**task)))

