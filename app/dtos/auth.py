from datetime import date
from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.user import UserModel


# ==================================================================================================
# Pydantic Schemas for API Output
# ==================================================================================================

# 'pydantic_model_creator' creates a Pydantic model from a Tortoise ORM model.
# This schema is for data that the API will send back to the client.
UserOutSchema = pydantic_model_creator(
    UserModel,
    # The name for the generated Pydantic model
    name="UserOut",
    # Exclude sensitive fields like the password hash from the output.
    exclude=("hashed_password",),
)


# ==================================================================================================
# Pydantic Schemas for API Input
# ==================================================================================================

class UserCreateSchema(BaseModel):
    """
    Schema for creating a new user. This defines the data the client must send.
    """
    login_id: str = Field(..., description="User's login ID", max_length=255)
    email: str = Field(..., description="User's email address", max_length=255)
    nickname: str = Field(..., description="User's nickname", max_length=255)
    password: str = Field(..., description="User's password (will be hashed)", min_length=8)
    birthday: date | None = Field(None, description="User's birthday")


class LoginRequest(BaseModel):
    """
    Schema for user login requests.
    """
    login_id: str
    password: str
