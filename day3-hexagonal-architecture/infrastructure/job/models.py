from core.job.constants import JobApplicationStatus
from infrastructure.db import db
from enum import Enum
from sqlalchemy import Enum as EnumType


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    employer = db.Column(db.String(50), nullable=False)


class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('job_applications', lazy=True))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    job = db.relationship('Job', backref=db.backref('jobs', lazy=True))
    status = db.Column(EnumType(JobApplicationStatus), default=JobApplicationStatus.APPLIED, nullable=False)
