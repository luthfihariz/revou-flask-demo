from abc import ABC, abstractmethod
from core.user.models import UserDomain
from typing import Optional

class IUserAccessor(ABC):

    def create_user(self, username: str, password: str, email: str) -> UserDomain:
        raise NotImplementedError
    
    def get_by_username(self, username: str) -> Optional[UserDomain]:
        raise NotImplementedError