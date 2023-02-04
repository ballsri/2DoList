from app.config import db_config 
from app.model import project,task
import os, json

db,Base, init_model, reinit_model, commit_rollback = db_config.db, db_config.Base, db_config.init_model, db_config.reinit_model, db_config.commit_rollback

def load_proj():
    with open(os.path.join(os.path.dirname(__file__), "./project.json")) as f:
        project_data = json.loads(f.read())
        f.close()

    proj_list = []

    for proj_dict in project_data:
        proj_list.append(project.Project(id = proj_dict['id'], title = proj_dict['title'], description = proj_dict['description']))    

    db.session.add_all(proj_list)
    commit_rollback()

def load_task():
    with open(os.path.join(os.path.dirname(__file__), "./task.json")) as f:
        task_data = json.loads(f.read())
        f.close()

    task_list = []

    for task_dict in task_data:
        task_list.append(task.Task(
            id = task_dict['id'], title = task_dict['title'], description = task_dict['description'], importantLevel = task.ILevel(task_dict['importantLevel']),
             createDate=task_dict['createDate'], dueDate = task_dict['dueDate'], projectId = task_dict['projectId']))    

    db.session.add_all(task_list)
    commit_rollback()



def load_data():
    load_proj()
    load_task()
    



