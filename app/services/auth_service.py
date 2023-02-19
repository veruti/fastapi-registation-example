from passlib.context import CryptContext


class AuthService:
    def __init__(self):
        self._crypt_context = CryptContext(schemes="sha256_crypt")

    def get_password_hash(self, password: str):
        return self._crypt_context.hash(secret=password)

    def verify_password(self, password: str, hashed_password: str):
        return self._crypt_context.verify(secret=password, hash=hashed_password)


auth_service = AuthService()
