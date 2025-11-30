from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.core.config import DATABASE_URL
from app.apis.users.router import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/api")

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.apis.users.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)
