from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from sqlalchemy import or_
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import session
from db.db_setup import getdb
from db.models.users import TokenBlackList
from db.models.users import User
from db.schemas.users import SignUp, UserOut, Login

auth_router = APIRouter(
    prefix='/auth',
    tags=['registration']
)


@auth_router.post('signup', response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def signup(user: SignUp, db: session = Depends(getdb)):
    db_email = db.query(User).filter(or_(User.email == user.email, User.username == user.username)).first()
    if db_email is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="user with this email/username is already exist")

    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        username=user.username,
        password=generate_password_hash(user.password),
        faculty=user.faculty,
        city=user.city,
        graduated=user.graduated,
    )
    db.add(new_user)
    db.commit()
    return new_user


@auth_router.post("login")
async def login(user_info: Login, db: session = Depends(getdb), Authorize: AuthJWT = Depends()):
    user_in_db = db.query(User).filter(User.username == user_info.username).first()
    if user_in_db is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user not found!")
    if not check_password_hash(user_in_db.password, user_info.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password not correct!")
    access_token = Authorize.create_access_token(subject=user_in_db.id)
    refresh_token = Authorize.create_refresh_token(subject=user_in_db.id)
    return {"access_token": access_token, "refresh_token": refresh_token}


@auth_router.post("logout")
async def logout(db: session = Depends(getdb), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    jti = Authorize.get_raw_jwt()["jti"]
    db.add(TokenBlackList(jti=jti))
