import uvicorn
from fastapi import FastAPI
from app.config.db_config import db, init_model, reinit_model
from app.config.config import config
from app.data.load_test import load_data


def init_app():

    db.init()
    app = FastAPI()

    @app.on_event("startup")
    async def startup():
        if config['MODE'] == 'development':
            try:
                await init_model()
                await load_data()
            except Exception:
                await reinit_model()
                await load_data()
        elif config['MODE'] == 'production':
            await init_model()


            
    @app.on_event("shutdown")
    async def shutdown():
        await db.close()
    
    return app

app = init_app()
def start():
    uvicorn.run("app.main:app", host=config['HOST'],port= int(config['PORT']),reload = True)