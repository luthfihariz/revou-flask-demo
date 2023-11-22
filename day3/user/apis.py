from flask import Blueprint, request
from user.model import User
from db import db
from common.bcrypt import bcrypt

user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404
    
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
    }
    

