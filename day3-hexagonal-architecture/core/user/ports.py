from abc import ABC, abstractmethod
from core.user.models import UserDomain
from typing import Optional

class IUserAccessor(ABC):

    @abstractmethod
    def create_user(self, username: str, password: str, email: str) -> UserDomain:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_username(self, username: str) -> Optional[UserDomain]:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, user_id:int) -> Optional[UserDomain]:
        raise NotImplementedError