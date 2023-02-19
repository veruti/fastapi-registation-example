from fastapi import HTTPException
from starlette import status

from api.dependencies.auth import RegistrationUser, User
from app.models.users import Users
from schemas.auth import UserScheme


class UserRepository:
    def __init__(self, db: type(Users)):
        self.db: Users = db

    async def _check_user_existence(self, email: str):
        return await self.db.get_or_none(email=email) is not None

    async def create(self, user: RegistrationUser):
        is_user_exist = await self._check_user_existence(email=user.email)

        if is_user_exist:
            await self.db.get_or_none(email=user.email)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists"
            )
        else:
            await self.db.create(**user.dict())

    async def read_by_email(self, user: User) -> UserScheme:
        is_user_exist = await self._check_user_existence(email=user.email)

        if is_user_exist:
            user_db = await self.db.get(email=user.email)
            user_scheme = UserScheme.from_tortoise_orm(user_db)
            return await user_scheme
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User doesn't exists"
            )

    async def update(self, user: UserScheme):
        is_user_exist = await self._check_user_existence(email=user.email)

        if is_user_exist:
            new_data = user.dict()
            del new_data["id"]
            await self.db.filter(id=user.id).update(**new_data)

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User doesn't exists"
            )

    async def delete(self, user_id: id):
        await self.db.filter(id=user_id).delete()


user_repository = UserRepository(db=Users)
