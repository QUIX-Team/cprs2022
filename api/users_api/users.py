from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

users_router = APIRouter(
    prefix='/users',
    tags=['admin', 'users']
)


@users_router.get('all')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return {"users": current_user}
