from flask import Blueprint, request
from user.model import User
from task.model import Task, TaskStatus
from db import db
from marshmallow import Schema, fields

task_blueprint = Blueprint('task_blueprint',__name__)

class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    user_id = fields.Integer(required=True, load_only=True)
    status = fields.Enum(TaskStatus, required=False)
    
@task_blueprint.route("", methods=['POST'])
def create_user_tasks():
    task_schema = TaskSchema()
    errors = task_schema.validate(request.get_json())
    if errors:
        return {'errors': errors}, 400

    data = task_schema.load(request.get_json())

    user = User.query.get(data['user_id'])
    if not user:
        return {"error": "User not found!"}, 404
    
    new_task = Task(user=user, title=data['title'])
    
    db.session.add(new_task)
    db.session.commit()

    return task_schema.dump(new_task)


@task_blueprint.route("", methods=['GET'])
def get_tasks():
    user_id = request.args.get('user_id')
    if not user_id:
        all_tasks = Task.query.all()
        task_schema = TaskSchema(many=True)
        return task_schema.dump(all_tasks)
    
    tasks_by_user = Task.query.filter_by(user_id=user_id)
    task_schema = TaskSchema(many=True)
    return task_schema.dump(tasks_by_user)



# tasks = [{'task': 'Coding with Flask', 'status': 'in progress'}]

# @task_blueprint.route("/", methods=["GET"])
# def get_tasks_list():
#     return tasks

# @task_blueprint.route("/", methods=["POST"])
# def create_tasks():
#     # check json or not
#     if not request.is_json:
#         return {"error": "Bukan json!!"}, 400

#     data = request.get_json()
    
#     # task available in data or not
#     if "task" not in data:
#         return {"error": "Task not available"}, 400
    
#     task = data.get("task")
    
#     tasks.append({
#         'task': task,
#         'status': 'to do'
#     })

#     return tasks

# allowed_status = ["in progress", "to do", "done"]

# @task_blueprint.route("/<int:index>", methods=["PUT"])
# def update_tasks(index):
#     if index > len(tasks):
#         return {"error": "task not found!"}, 404
    
#     if status not in allowed_status:
#         return {"error": "status tidak valid!"}, 400
    
#     data = request.get_json()
#     task = data.get("task")
#     status = data.get("status") # None

#     updated_task = tasks[index - 1]

#     if task:
#         updated_task["task"] = task
    
#     if status:
#         updated_task["status"] = status

#     tasks[index - 1] = updated_task

#     return tasks


# @task_blueprint.route("/<int:index>", methods=["DELETE"])
# def delete_task(index):
#     if index > len(tasks):
#         return {"error": "news not found!"}, 404
    
#     del tasks[index - 1]

#     return tasks