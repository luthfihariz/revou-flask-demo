from core.auth.specs import AuthRegistrationSpec, AuthRegistrationResult
from core.common.bcrypt import bcrypt
from core.user.ports import IUserAccessor
from core.user.models import UserDomain
from injector import inject
import jwt, os
from datetime import datetime, timedelta

class AuthService():

    @inject
    def __init__(self, user_accessor: IUserAccessor) -> None:
        self.user_accessor = user_accessor

    def register(self, username: str, password: str, email:str) -> UserDomain:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')     
        user = self.user_accessor.create_user(
            username,
            hashed_password,
            email
        )   
        return user

    def login(self, username: str, password: str):
        user = self.user_accessor.get_by_username(
            username
        )

        if not user:
            return None
        
        valid = bcrypt.check_password_hash(user.password, password)

        if not valid:
            return None
        
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