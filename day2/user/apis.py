from flask import Blueprint, request
from user.model import User
from db import db

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
    

@user_blueprint.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data["username"]
    email = data["email"]

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return {
        'id' : new_user.id
    }