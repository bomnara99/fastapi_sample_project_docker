from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class User(UserCreate):
    seq: int
    class Config:
        orm_mode = True