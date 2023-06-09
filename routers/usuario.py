from fastapi import APIRouter
from fastapi.responses import JSONResponse
from jwt_manager import create_token
from schemas.user import User


user_router = APIRouter()


@user_router.post('/login',tags=['auth'])
def login(user: User):
    if user.email == 'la calaca recochera' and user.pasword == 'lacalaca':
            token: str = create_token(user.dict())
            return JSONResponse(content=token)