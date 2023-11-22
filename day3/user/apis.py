from flask import Blueprint, request
from user.model import User
from db import db
from common.bcrypt import bcrypt
import jwt
import os
from auth.utils import decode_jwt

user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("", methods=["GET"])
def get_user():
    payload = decode_jwt(request.headers.get('Authorization'))
    if not payload:
        return {'message': 'Token invalid or expired. Please login again'}, 401
    
    user_id = payload.get('user_id')    
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404
    
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
    }
    

