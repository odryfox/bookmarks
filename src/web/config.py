import os


class Config:
    def __init__(self):
        self.DEBUG = False
        self.TESTING = False
        self.SECRET_KEY = None
        self.FLASK_ADMIN_SWATCH = "paper"

    def init_from_env_name(self, env_name: str):
        if env_name == "dev":
            self.init_from_dev_env()
        elif env_name == "test":
            self.init_from_test_env()
        else:
            self.init_from_prod_env()

    def init_from_dev_env(self):
        self.DEBUG = True
        self.TESTING = False
        self.SECRET_KEY = os.environ.get("SECRET_KEY", "super_secret_key")

    def init_from_test_env(self):
        self.DEBUG = True
        self.TESTING = True
        self.SECRET_KEY = os.environ.get("SECRET_KEY", "super_secret_key")

    def init_from_prod_env(self):
        self.DEBUG = False
        self.TESTING = False
        self.SECRET_KEY = os.environ["SECRET_KEY"]

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            other.DEBUG == self.DEBUG and
            other.TESTING == self.TESTING and
            other.SECRET_KEY == self.SECRET_KEY and
            other.FLASK_ADMIN_SWATCH == self.FLASK_ADMIN_SWATCH
        )


config = Config()
