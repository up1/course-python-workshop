from pydantic import BaseModel

class DBModel(BaseModel):
    username: str
    password: str
    email: str