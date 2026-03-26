# schemas, modelo de base
from pydantic import BaseModel
from pydantic import EmailStr  # formatação de email


class Message(BaseModel):
    message: str


# Classe de users
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDB(UserSchema):
    id: int


# Classe pública de exposição do user
class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserPublic]
