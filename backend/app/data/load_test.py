import sys


from sqlalchemy import insert
from db_config import db, Base, commit_rollback
import project,task
import os, json


def load_data():
    with open(os.path.join(os.path.dirname(__file__), "./project.json")) as f:
        project_data = json.loads(f.read())

    proj_list = []
    for proj in project_data:
        proj_list.append(project.Project(id = proj['id'],title = proj['title'], description = proj['description']))    
    db.session.add_all(proj_list)
    commit_rollback()



