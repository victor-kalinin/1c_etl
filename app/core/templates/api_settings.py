class APISettings:
    HOST: str = None
    PORT: str = None
    BASE_PATH: str = None
    USER: str = None
    PASSWORD: str = None

    @property
    def API_PATH(self):
        return f'{self.HOST}:{self.PORT}/{self.BASE_PATH.strip("/")}'
