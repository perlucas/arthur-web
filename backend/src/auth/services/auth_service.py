from typing import Annotated
from fastapi import Depends

from src.sql.user import User
from src.user.services.user_gateway import UserGateway

class AuthService:

    def __init__(self, user: User):
        self._user = user

    def current_user(self) -> User:
        return self._user
    
    @classmethod
    def service(cls, gw: Annotated[UserGateway, Depends()]):
        return AuthService(user=gw.fetch_testing_user())