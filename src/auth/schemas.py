from fastapi_users.schemas import model_dump
from pydantic import BaseModel, EmailStr


class UserRead(BaseModel):
    email: str
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str | None = None
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None
    password: str

    def create_update_dict(self):
        return model_dump(
            self,
            exclude_unset=True,
            exclude={
                "id",
                "is_superuser",
                "is_active",
                "is_verified",
                "oauth_accounts",
            },
        )

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    pass
