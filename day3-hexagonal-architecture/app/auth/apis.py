from flask import Blueprint, request
from marshmallow import Schema, fields, ValidationError, validate, validates
from datetime import datetime, timedelta
from core.auth.services import AuthService
from app.di import injector

auth_blueprint = Blueprint('auth', __name__)
auth_service = injector.get(AuthService)

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
    
    return schema.dump(auth_service.register(
        data['username'], data['password'], data['email']
    ))


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
    
    result = auth_service.login(
        username=data['username'],
        password=data['password']
    )

    if not result:
        return {"error": "User or password is not valid"}, 401
    
    return result

    # user = User.query.filter_by(username=data['username']).first()
    # if not user:
    #     return {"error": "User or password is not valid"}, 401
    
    # valid = bcrypt.check_password_hash(user.password, data['password'])

    # if not valid:
    #     return {"error": "User or password is not valid"}, 401
    
    # token = jwt.encode({
    #     'user_id': user.id,
    #     'username': user.username,
    #     'exp': datetime.utcnow() + timedelta(seconds=10)
    # }, os.getenv('SECRET_KEY'), algorithm='HS256')
    
    # return {
    #     'id': user.id,
    #     'username': user.username,
    #     'email': user.email,
    #     'token': token
    # }