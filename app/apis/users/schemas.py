from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User_Pydantic(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserIn_Pydantic(BaseModel):
    username: str
    password: str
