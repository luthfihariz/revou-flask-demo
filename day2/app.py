from flask import Flask, request
from task.apis import task_blueprint
from event.apis import event_blueprint

app = Flask(__name__)

app.register_blueprint(task_blueprint, url_prefix="/tasks")
app.register_blueprint(event_blueprint, url_prefix="/events")