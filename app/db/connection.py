# Database configuration and connection setup

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_user: str = 'postgres'
db_port: int = 5432
db_host: str = 'localhost'
db_password: str = 'zx985632'

DATABASE_URL: str = F'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/todo_db'

engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = session()
# try:
#     connection = engine.connect()
#     connection.close()
#     print('ping, Connected')
# except Exception as e:
#     print(f'Error:{str(e)}')