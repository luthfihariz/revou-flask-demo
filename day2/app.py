import os
from flask import Flask, request
from task.apis import task_blueprint
from event.apis import event_blueprint
from db import db, db_init
from user.apis import user_blueprint
from serializer import ma


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db.init_app(app)
ma.init_app(app)


app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(task_blueprint, url_prefix="/tasks")
# app.register_blueprint(event_blueprint, url_prefix="/events")

with app.app_context():
    db_init()