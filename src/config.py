import os


class Config:
    def __init__(self):
        self.DATABASE_URL = None

    def init_from_env_name(self, env_name: str):
        if env_name == "dev":
            self.init_from_dev_env()
        elif env_name == "test":
            self.init_from_test_env()
        else:
            self.init_from_prod_env()

    def init_from_dev_env(self):
        default_database_url = "postgresql://localhost/bookmarks_development"
        database_url = os.environ.get("DATABASE_URL", default_database_url)
        self.DATABASE_URL = database_url

    def init_from_test_env(self):
        default_database_url = "postgresql://localhost/bookmarks_testing"
        database_url = os.environ.get("TEST_DATABASE_URL", default_database_url)
        self.DATABASE_URL = database_url

    def init_from_prod_env(self):
        database_url = os.environ["TEST_DATABASE_URL"]
        self.DATABASE_URL = database_url


config = Config()
