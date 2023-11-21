from flask import Blueprint, request
from marshmallow import Schema, fields
from db import db
from sqlalchemy.orm import joinedload
from user.apis import UserSchema
from job.models import Job, JobApplicationStatus, JobApplication

job_blueprint = Blueprint('job_blueprint', __name__)

class JobSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    employer = fields.String(required=True)


class JobApplicationSchema(Schema):
    user_id = fields.Integer(required=True)
    job_id = fields.Integer(required=True)
    status = fields.Enum(JobApplicationStatus, dump_only=True)

@job_blueprint.route("/", methods=["POST"])
def create_job():
    job_schema = JobSchema()
    errors = job_schema.validate(request.get_json())
    if errors:
        return {'errors': errors}, 400
    
    data = job_schema.load(request.get_json())

    job = Job(title=data["title"], description=data["description"], 
              employer=data["employer"])
    db.session.add(job)
    db.session.commit()

    return job_schema.dump(job)


@job_blueprint.route("/application", methods=["POST"])
def apply_job():
    job_application_schema = JobApplicationSchema()
    errors = job_application_schema.validate(request.get_json())
    if errors:
        return {'errors': errors}, 400
    
    data = job_application_schema.load(request.get_json())
    job_application = JobApplication(user_id=data["user_id"], job_id=data["job_id"])
    db.session.add(job_application)
    db.session.commit()

    return job_application_schema.dump(job_application)


@job_blueprint.route("/application", methods=["PUT"])
def update_job_application_status():
    data = request.get_json()
    job_application_id = data["job_application_id"]
    status = data["status"]

    job_application_to_update = JobApplication.query.get(job_application_id)
    job_application_to_update.status = status
    db.session.commit()

    job_application_schema = JobApplicationSchema()
    return job_application_schema.dump(job_application_to_update)



class CompleteJobApplicationSchema(Schema):
    id = fields.Integer()
    status = fields.Enum(JobApplicationStatus, dump_only=True)
    user = fields.Nested(UserSchema())
    job = fields.Nested(JobSchema())


@job_blueprint.route("/application/<int:job_application_id>", methods=["GET"])
def get_job_application(job_application_id):
    job_application = JobApplication.query.options(
        joinedload(JobApplication.user), joinedload(JobApplication.job)
    ).filter_by(id=job_application_id).first()
    schema = CompleteJobApplicationSchema()
    return schema.dump(job_application)