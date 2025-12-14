from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    애플리케이션 설정을 관리하는 클래스.
    Pydantic의 BaseSettings를 상속받아 환경 변수를 자동으로 읽어옵니다.
    """
    # .env 파일을 읽어오도록 설정합니다. (로컬 환경용)
    # Docker 환경에서는 이 파일을 사용하지 않고 docker-compose.yml에 정의된 환경 변수를 직접 읽습니다.
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    DATABASE_URL: str


# settings 객체를 생성하여 다른 모듈에서 import하여 사용할 수 있도록 합니다.
settings = Settings()
