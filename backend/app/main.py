import uvicorn
from fastapi import FastAPI
from .db_config import db
from .model import task,project



def init_app():

    db.init()
    app = FastAPI()

    @app.on_event("startup")
    def startup():
        project.Base.metadata.create_all(bind=db.engine)
        task.Base.metadata.create_all(bind=db.engine)

    @app.on_event("shutdown")
    def shutdown():
        db.close()
    
    return app

app = init_app()


def start():
    uvicorn.run("app.main:app", host="localhost",port=8000,reload = True)