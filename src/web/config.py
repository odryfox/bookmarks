import os


class ProductionConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ["SECRET_KEY"]
    FLASK_ADMIN_SWATCH = "paper"


class DevelopmentConfig(ProductionConfig):
    DEBUG = True
    TESTING = False


class TestingConfig:
    DEBUG = True
    TESTING = True


config_by_env_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig,
)
