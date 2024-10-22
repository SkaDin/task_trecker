from fastapi import Depends
from fastapi_users import BaseUserManager, FastAPIUsers, IntegerIDMixin

from src.auth.auth import auth_backend
from src.core.config import config
from src.core.db import get_user_db
from src.models import User


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = config.SECRET
    verification_token_secret = config.SECRET

    pass


async def get_user_manager(user_db=Depends(get_user_db)) -> UserManager:
    yield UserManager(user_db)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
