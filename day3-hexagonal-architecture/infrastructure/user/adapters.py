from core.user.models import UserDomain
from core.user.ports import IUserAccessor
from infrastructure.db import db
from infrastructure.user.models import User
from core.common.utils import ObjectMapperUtil
from typing import Optional

class UserAccessor(IUserAccessor):
    
    def create_user(self, username: str, hashed_password: str, email: str) -> UserDomain:
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return ObjectMapperUtil.map(new_user, UserDomain)
    
    def get_by_username(self, username) -> Optional[UserDomain]:
        user = User.query.filter_by(username=username).first()
        return ObjectMapperUtil.map(user, UserDomain)
    
    def get_by_id(self, user_id: int) -> UserDomain | None:
        user = User.query.get(user_id)
        return ObjectMapperUtil.map(user, UserDomain)