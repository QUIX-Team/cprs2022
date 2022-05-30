from fastapi import FastAPI
from api import careers_api
from api.users_api import user_api, auth, users
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException

app = FastAPI(
    title="RecSystem App",
    description=" End points for CPRS",
    version="0.0.1",
    terms_of_service="",
    contact={
        "name": "Quix",
    },
    license_info={
        "name": "MIT",
    }, )


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


app.include_router(careers_api.router)
app.include_router(user_api.router)
app.include_router(auth.auth_router)
app.include_router(users.users_router)
