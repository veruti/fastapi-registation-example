from pydantic import BaseModel, EmailStr, SecretStr


class User(BaseModel):
    email: EmailStr
    password: SecretStr


class RegistrationUser(BaseModel):
    email: EmailStr
    hashed_password: SecretStr
