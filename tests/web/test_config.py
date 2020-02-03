import os

import pytest

from src.web.config import Config


def test_eq():
    config1 = Config()
    config1.init_from_dev_env()

    config2 = Config()
    config2.init_from_dev_env()

    assert config1 == config2


def test_dev_config():
    config = Config()
    config.init_from_dev_env()
    assert (
        config.DEBUG and
        not config.TESTING and
        config.SECRET_KEY == "super_secret_key"
    )


def test_test_config():
    config = Config()
    config.init_from_test_env()
    assert (
        config.DEBUG and
        config.TESTING and
        config.SECRET_KEY == "super_secret_key"
    )


def test_prod_config():
    config = Config()
    os.environ["SECRET_KEY"] = "not_super_secret_key"
    config.init_from_prod_env()
    assert (
        not config.DEBUG and
        not config.TESTING and
        config.SECRET_KEY == "not_super_secret_key"
    )


def test_init_from_env_name():
    config1 = Config()
    config2 = Config()

    config1.init_from_dev_env()
    config2.init_from_env_name("dev")

    assert config1 == config2

    config1.init_from_test_env()
    config2.init_from_env_name("test")

    assert config1 == config2

    config1.init_from_prod_env()
    config2.init_from_env_name("prod")

    assert config1 == config2


def test_prod_config_without_secret_key():
    config = Config()
    del os.environ["SECRET_KEY"]
    with pytest.raises(KeyError):
        config.init_from_prod_env()
