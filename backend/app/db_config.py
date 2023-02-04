from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import model
import os
from .config import config

POSTGRES_URL = config['DB_URL']

class DatabaseSession:

    def __init__(self) -> None:
        self.session = None
        self.engine = None
        self.db = None
    
    def __getattr__(self,name):
        return getattr(self.session, name)

    def init(self):

        self.engine = create_engine(POSTGRES_URL)
        self.session = sessionmaker(autocommit = False, autoflush= False, bind= self.engine)
        self.db = declarative_base()

    def create_all(self):
        self.db.metadata.create_all(bind= self.engine)


db = DatabaseSession()


def commit_rollback():
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

