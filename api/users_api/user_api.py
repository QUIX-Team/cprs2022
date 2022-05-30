import fastapi

from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from core.config import settings
from db.models.users import TokenBlackList
from db.db_setup import SessionLocal

router = fastapi.APIRouter()


class Settings(BaseModel):
    authjwt_secret_key: str = settings.SECRET
    authjwt_denylist_enabled = settings.ACCESS_TOKEN_DENYLIST
    authjwt_algorithm = settings.ALGORITHM


# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()


# exception handler for authjwt
# in production, you can tweak performance using orjson response


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    jti = decrypted_token['jti']
    session = SessionLocal()
    blacklisted = session.query(TokenBlackList).filter(TokenBlackList.jti == jti).first()
    return blacklisted is not None
