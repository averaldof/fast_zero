# importando fast api
from fastapi import FastAPI, HTTPException

from http import HTTPStatus

from fast_zero.schemas import Message
from fast_zero.schemas import UserSchema
from fast_zero.schemas import UserPublic
from fast_zero.schemas import UserDB
from fast_zero.schemas import UserList


app = FastAPI()

database = []  # fake db


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá mundo"}


# post
@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
# criação de user
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(database) + 1,  # registros > 0, automaticamente preenchidos
        **user.model_dump(),
    )
    database.append(user_with_id)  # add user id

    return user_with_id


# get
@app.get("/users/", response_model=UserList)
# UserPublic View
def read_users():
    return {"users": database}


# update
@app.put("/users/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404, detail="User not found")

    user_with_id = UserDB(
        id=user_id,
        **user.model_dump(),
    )
    
    database[user_id - 1] = user_with_id
    return user_with_id


# deletar
@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404, detail="User not found")

    del database[user_id - 1]

    return {"message": "Usuário deletado"}
