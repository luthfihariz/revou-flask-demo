from flask import Blueprint, request
from user.model import User
from db import db
from common.bcrypt import bcrypt
from marshmallow import Schema, fields, ValidationError, validate, validates
import jwt
import os
from datetime import datetime, timedelta

auth_blueprint = Blueprint('auth', __name__)


class UserRegistrationSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=5), load_only=True)

    @validates("email")
    def validate_email(self, value):
        if not value.endswith("revou.co"):
            raise ValidationError("You need to use revou.co email.")

@auth_blueprint.route("/registration", methods=["POST"])
def register():
    data = request.get_json()
    schema = UserRegistrationSchema()
    try:
        data = schema.load(data)
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return schema.dump(new_user)


class UserLoginSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3))
    password = fields.String(required=True, validate=validate.Length(min=5), load_only=True)


@auth_blueprint.route("/login", methods=["POST"])
def login():
    schema = UserLoginSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return {"error": err.messages}, 400

    user = User.query.filter_by(username=data['username']).first()
    if not user:
        return {"error": "User or password is not valid"}, 401
    
    valid = bcrypt.check_password_hash(user.password, data['password'])

    if not valid:
        return {"error": "User or password is not valid"}, 401
    
    token = jwt.encode({
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(seconds=10)
    }, os.getenv('SECRET_KEY'), algorithm='HS256')
    
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'token': token
    }

# @auth_blueprint.route("/registration", methods=["POST"])
# def register():
#     data = request.get_json()
#     username = data["username"]
#     password = data["password"]
#     email = data["email"]

#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#     new_user = User(username=username, email=email, password=hashed_password)
#     db.session.add(new_user)
#     db.session.commit()

#     return {
#         'id' : new_user.id
#     }