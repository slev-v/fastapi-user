class HasherPasswordMock:
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return hashed_password == plain_password[::-1]

    def get_password_hash(self, password: str) -> str:
        return password[::-1]
