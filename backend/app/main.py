import uvicorn
from fastapi import FastAPI
from .db_config import db

def init_app():
    
    db.init()
    app = FastAPI()

    @app.on_event("startup")
    def startup():
        db.create_all()

    @app.on_event("shutdown")
    def shutdown():
        db.close()
    
    return app

app = init_app()


def start():
    uvicorn.run("app.main:app", host="localhost",port=8000,reload = True)