from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.core.config import settings

# Aerich가 참조할 Tortoise ORM 설정
# 'aerich.models'를 포함하여 마이그레이션 기록을 관리할 수 있도록 합니다.
TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

app = FastAPI(
    title="FastAPI Tortoise ORM",
    description="Tortoise ORM, FastAPI, Pydantic, and PostgreSQL",
)

# register_tortoise를 사용하여 Tortoise ORM을 FastAPI 앱에 연결합니다.
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # Aerich를 사용하므로 False로 설정
    add_exception_handlers=True,
)


@app.get("/")
async def read_root():
    """
    루트 엔드포인트. 서비스가 정상적으로 실행 중인지 확인합니다.
    """
    return {"message": "Welcome to the FastAPI application!"}
