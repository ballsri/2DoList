import uvicorn
from fastapi import FastAPI
from app.config import db_config 
from app.config import config
from .data.load_test import load_data

db,Base, init_model, reinit_model = db_config.db, db_config.Base, db_config.init_model, db_config.reinit_model
config = config.config

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