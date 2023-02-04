from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import config

POSTGRES_URL = config['DB_URL']

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

