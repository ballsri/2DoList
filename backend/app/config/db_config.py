from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config.config import config

if config['MODE'] == 'development':
    POSTGRES_URL = config['DB_DEV_URL']
elif config['MODE'] == 'production':
    POSTGRES_URL = config['DB_PROD_URL']

class AsyncDatabaseSession:

    def __init__(self) -> None:
        self.session = None
        self.engine = None
  
    def __getattr__(self,name):
        return getattr(self.session, name)

    def init(self):
        self.engine = create_async_engine(POSTGRES_URL,future=True,echo=True)
        self.session = sessionmaker(autocommit = False, autoflush= False, bind= self.engine, class_=AsyncSession)()


db = AsyncDatabaseSession()
Base = declarative_base()

async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise

async def init_model():
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def reinit_model():
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)



