import os

from pydantic import BaseSettings

"postgres://fast_api_registration_user:password@localhost:5432/fast_api_registration"


class CommonConfig(BaseSettings):

    # TODO: remove default values
    POSTGRES_DB = os.getenv("POSTGRES_DB", "fast_api_registration")
    POSTGRES_USER = os.getenv("POSTGRES_USER", "fast_api_registration_user")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))

    POSTGRES_URL = F"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"



config = CommonConfig()
