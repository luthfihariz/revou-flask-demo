from flask import Blueprint, request
from app.auth.utils import decode_jwt
from core.user.services import UserService
from app.di import injector

user_service = injector.get(UserService)

user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("", methods=["GET"])
def get_user():
    payload = decode_jwt(request.headers.get('Authorization'))
    if not payload:
        return {'message': 'Token invalid or expired. Please login again'}, 401
    
    username = payload.get('username')    
    user = user_service.get_user_profile(username)
    if not user:
        return {"error": "User not found"}, 404
    
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
    }
    

