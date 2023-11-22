from core.user.models import UserDomain
from injector import inject
from core.user.ports import IUserAccessor

class UserService():
    @inject
    def __init__(self, user_accessor: IUserAccessor) -> None:
        self.user_accessor = user_accessor

    def get_user_profile(self, username: str) -> UserDomain:
        user = self.user_accessor.get_by_username(username=username)
        return user