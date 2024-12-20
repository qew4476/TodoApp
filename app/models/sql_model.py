from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.orm import declarative_base
BASE = declarative_base()

class User(BASE):
    __tablename__ = 'users'

    user_id = Column(String(64), primary_key=True, index=True)
    password = Column(String(100), nullable=False)
    user_name = Column(String(64), nullable=False)

    tasks = relationship("Task", back_populates="users", cascade="all, delete")


class Task(BASE):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String(50), nullable=False)
    user_id = Column(String(50), ForeignKey('users.user_id'), nullable=False)
    description = Column(String(90), nullable=True)

    users = relationship(argument="User", back_populates="tasks")