import os
from flask import Flask
from db import db, db_init
from job.apis import job_blueprint
from user.apis import user_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)


app.register_blueprint(job_blueprint, url_prefix="/job")
app.register_blueprint(user_blueprint, url_prefix="/user")

# Job Board API
# API Design
# POST /user -> user registration
# POST /job -> create job
# POST /job/application -> apply to a job
# PUT /job/application/<job_application_id> -> update job application status
# GET /job/application/<job_application_id> -> get job application status


# Database Design
# User (id, email, username)
# Job (id, title, description, employer)
# Job Application (id, user_id, job_id, status)

# with app.app_context():
#     db_init()