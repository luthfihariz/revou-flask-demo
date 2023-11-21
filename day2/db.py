from flask_sqlalchemy import SQLAlchemy
from common.base_model import Base

db = SQLAlchemy(model_class=Base)

def db_init():
    db.create_all()
