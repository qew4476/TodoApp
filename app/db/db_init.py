#create the tables according to sql_model's Pydantic Format
from app.db.connection import engine
from app.models.sql_model import BASE

def init_db():
    BASE.metadata.create_all(bind=engine)

init_db()