from flask import Blueprint, request
from user.models import User
from marshmallow import Schema, fields
from db import db

user_blueprint = Blueprint('user_blueprint', __name__)

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String(required=True)
    username = fields.String(required=True)
    phone_number = fields.String(required=True)

@user_blueprint.route("", methods=['POST'])
def create_user():
    user_schema = UserSchema()
    errors = user_schema.validate(request.get_json())
    if errors:
        return {'errors': errors}, 400
    
    data = user_schema.load(request.get_json())

    user = User(username=data['username'], 
                email=data['email'], 
                phone_number=data['phone_number'])
    db.session.add(user)
    db.session.commit()

    return user_schema.dump(user)

