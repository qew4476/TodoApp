# Database configuration and connection setup

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import get_settings

CONFIG=get_settings()



DATABASE_URL: str = F'postgresql://{CONFIG.DB_USER}:{CONFIG.DB_PASSWORD}@{CONFIG.DB_HOST}:{CONFIG.DB_PORT}/{CONFIG.DB_NAME}'

engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = session()
# try:
#     connection = engine.connect()
#     connection.close()
#     print('ping, Connected')
# except Exception as e:
#     print(f'Error:{str(e)}')