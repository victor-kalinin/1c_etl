class DBSettings:
    HOST: str = None
    DATABASE: str = None
    PORT: int = None
    USER: str = None
    PASSWORD: str = None
    DB_DRIVER: str = None

    def __str__(self):
        return f'{self.DB_DRIVER}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}'
