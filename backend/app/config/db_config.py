from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import config

if config['MODE'] == 'development':
    POSTGRES_URL = config['DB_DEV_URL']
elif config['MODE'] == 'production':
    POSTGRES_URL = config['DB_PROD_URL']

class DatabaseSession:

    def __init__(self) -> None:
        self.session = None
        self.engine = None
  
    def __getattr__(self,name):
        return getattr(self.session, name)

    def init(self):
        self.engine = create_engine(POSTGRES_URL)
        self.session = sessionmaker(autocommit = False, autoflush= False, bind= self.engine)()


db = DatabaseSession()
Base = declarative_base()

def commit_rollback():
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise


import task,project

def init_model():
    Base.metadata.create_all(db.engine)

def reinit_model():
    Base.metadata.drop_all(bind=db.engine)
    init_model()


