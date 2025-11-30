from fastapi import APIRouter
from typing import List
from app.apis.users.models import Users
from app.apis.users.schemas import User_Pydantic, UserIn_Pydantic

router = APIRouter()

@router.post("/users", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)

@router.get("/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(Users.all())
