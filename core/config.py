from pydantic import BaseModel
from secrets import token_urlsafe


class Settings(BaseModel):
    ALGORITHM: str = "HS256"
    SECRET: str = token_urlsafe(32)
    ACCESS_TOKEN_DENYLIST: bool = True


settings = Settings()
