from pydantic import BaseModel
from typing import Optional, Any
from secrets import token_urlsafe


class UserBase(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    email: str
    username: str
    faculty: str
    city: str
    graduated: Optional[bool]

    class Config:
        orm_mode = True


class UserOut(UserBase):
    pass


class SignUp(UserBase):
    def __init__(__pydantic_self__, **data: Any):
        super().__init__(**data)
        __pydantic_self__.graduated = None

    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'first_name': 'abdullah',
                'last_name': 'magdy',
                'email': 'magdyabdullah200@gmail.com',
                'username': 'abdullah',
                'password': '222000',
                'faculty': 'mansourauni',
                'city': 'mansoura',
                'graduted': True,
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = token_urlsafe(32)


class Login(BaseModel):
    username: str
    password: str
