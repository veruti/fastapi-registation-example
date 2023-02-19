from tortoise.contrib.pydantic import pydantic_model_creator

from models.users import Users

UserScheme = pydantic_model_creator(
    Users,
    name='User'
)
