#schemas, modelo de base
from pydantic import BaseModel

class Message(BaseModel):
    message: str