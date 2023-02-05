from app.config.db_config import db, commit_rollback
from app.model import project,task
from sqlalchemy import select
import os, json
from datetime import datetime

async def load_proj():
    with open(os.path.join(os.path.dirname(__file__), "./project.json")) as f:
        project_data = json.loads(f.read())
        f.close()

    proj_list = []

    for proj_dict in project_data:
        proj_list.append(project.Project(id = proj_dict['id'], title = proj_dict['title'], description = proj_dict['description']))    

    db.add_all(proj_list)
    await commit_rollback()

async def load_task():
    with open(os.path.join(os.path.dirname(__file__), "./task.json")) as f:
        task_data = json.loads(f.read())
        f.close()

    task_list = []

    date_format = '%Y/%m/%d %H:%M:%S'
    for task_dict in task_data:
        task_list.append(task.Task(
            id = task_dict['id'], title = task_dict['title'], description = task_dict['description'], importantLevel = task.ILevel(task_dict['importantLevel']),
             createDate=datetime.strptime(task_dict['createDate'],date_format), dueDate = datetime.strptime(task_dict['dueDate'],date_format), projectId = task_dict['projectId']))    

    db.add_all(task_list)
    await commit_rollback()

async def load_data():
    await load_proj()
    await load_task()



