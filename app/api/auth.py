from fastapi import APIRouter
from fastapi import HTTPException

from api.dependencies.auth import User
from app.comands.auth import register_person, authentificate_user

auth_router = APIRouter()


@auth_router.post("/register")
async def register(user: User):
    try:
        await register_person(user=user)
    except HTTPException:
        pass


@auth_router.post("/login_in")
async def login_in(user: User):
    try:
        await authentificate_user(user=user)
    except Exception as e:
        print(e)
