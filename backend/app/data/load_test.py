from app.config.db_config import db, commit_rollback
from app.model import project,task
from datetime import datetime
import uuid
import os, json
date_format = '%Y/%m/%d %H:%M:%S'

async def load_proj():

    #load data from json
    with open(os.path.join(os.path.dirname(__file__), "./project.json")) as f:
        project_data = json.loads(f.read())
        f.close()

    proj_list = []
    #append pydantic objects in list
    for proj_dict in project_data:
        proj_list.append(project.Project(id = uuid.UUID(proj_dict['id']), title = proj_dict['title'], description = proj_dict['description']))    
    
    #add items in list to db metadata and commit on postgres
    db.add_all(proj_list)
    await commit_rollback()

async def load_task():
    #load data from json
    with open(os.path.join(os.path.dirname(__file__), "./task.json")) as f:
        task_data = json.loads(f.read())
        f.close()

    task_list = []
    #append pydantic objects in list
    for task_dict in task_data:
        print(task_dict['id'])

        task_list.append(task.Task(
            id = uuid.UUID(task_dict['id']), title = task_dict['title'],
             description = task_dict['description'], importantLevel = task.TaskLevel(task_dict['importantLevel']),
            createDate=datetime.strptime(task_dict['createDate'],date_format), dueDate = datetime.strptime(task_dict['dueDate'],date_format),
            status = task.TaskStatus(task_dict['status']), projectId = uuid.UUID(task_dict['projectId'])))   
             
    #add items in list to db metadata and commit on postgres
    db.add_all(task_list)
    await commit_rollback()

async def load_data():
    await load_proj()
    await load_task()



