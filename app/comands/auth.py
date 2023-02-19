from api.dependencies.auth import User, RegistrationUser
from app.db.repository import user_repository
from schemas.auth import UserScheme
from services.auth_service import auth_service


async def register_person(user: User):
    hashed_password = auth_service.get_password_hash(password=user.password.get_secret_value())
    user_schema = RegistrationUser(email=user.email, hashed_password=hashed_password)

    await user_repository.create(user=user_schema)


async def authentificate_user(user: User):
    original_user: UserScheme = await user_repository.read_by_email(user=user)

    password_verification = auth_service.verify_password(
        password=user.password.get_secret_value(),
        hashed_password=original_user.hashed_password
    )

    if password_verification:
        new_hashed_password = auth_service.get_password_hash(
            password=user.password.get_secret_value()
        )

        original_user.hashed_password = new_hashed_password
        await user_repository.update(user=original_user)
