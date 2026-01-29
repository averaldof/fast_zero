# importando fast api
from fastapi import FastAPI

from http import HTTPStatus

from fast_zero.schemas import Message 
app = FastAPI()


@app.get("/", HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá mundo"}
