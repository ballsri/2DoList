import uvicorn
from fastapi import FastAPI
from app.config.db_config import db,Base, init_model, reinit_model
from app.config.config import config
from app.data.load_test import load_data

def init_app():

    db.init()
    app = FastAPI()

    @app.on_event("startup")
    def startup():
        if config['MODE'] == 'development':
            try:
                init_model()
                load_data()
            except Exception:
                reinit_model()
                load_data()
        elif config['MODE'] == 'production':
            init_model()
            
    @app.on_event("shutdown")
    def shutdown():
        db.close()
    
    return app

app = init_app()

def start():
    uvicorn.run("app.main:app", host=config['HOST'],port= int(config['PORT']),reload = True)