from db import db
from enum import Enum
from sqlalchemy import Enum as EnumType


class TaskStatus(Enum):
    TODO = 'TO DO'
    IN_PROGRESS = 'IN PROGRESS'
    COMPLETED = 'COMPLETED'


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(EnumType(TaskStatus), default=TaskStatus.TODO, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

