import pytest

from src.config import Config


def test_eq():
    config1 = Config()
    config1.init_from_dev_env()

    config2 = Config()
    config2.init_from_dev_env()

    assert config1 == config2


def test_dev_config(monkeypatch):
    config = Config()
    database_url = "postgresql://localhost/bookmarks_development_other"
    monkeypatch.setenv("DATABASE_URL", database_url)
    config.init_from_dev_env()
    assert config.DATABASE_URL == database_url


def test_test_config(monkeypatch):
    config = Config()
    database_url = "postgresql://localhost/bookmarks_testing_other"
    monkeypatch.setenv("TEST_DATABASE_URL", database_url)
    config.init_from_test_env()
    assert config.DATABASE_URL == database_url


def test_prod_config(monkeypatch):
    config = Config()
    database_url = "postgresql://localhost/bookmarks"
    monkeypatch.setenv("DATABASE_URL", database_url)
    config.init_from_prod_env()
    assert config.DATABASE_URL == database_url


def test_init_from_env_name(monkeypatch):
    config1 = Config()
    config2 = Config()

    config1.init_from_dev_env()
    config2.init_from_env_name("dev")

    assert config1 == config2

    config1.init_from_test_env()
    config2.init_from_env_name("test")

    assert config1 == config2

    database_url = "postgresql://localhost/bookmarks"
    monkeypatch.setenv("DATABASE_URL", database_url)

    config1.init_from_prod_env()
    config2.init_from_env_name("prod")

    assert config1 == config2


def test_dev_config_without_database_url(monkeypatch):
    config = Config()
    monkeypatch.delenv("DATABASE_URL", raising=False)
    config.init_from_dev_env()
    assert config.DATABASE_URL == "postgresql://localhost/bookmarks_development"


def test_test_config_without_database_url(monkeypatch):
    config = Config()
    monkeypatch.delenv("TEST_DATABASE_URL", raising=False)
    config.init_from_test_env()
    assert config.DATABASE_URL == "postgresql://localhost/bookmarks_testing"


def test_prod_config_without_database_url(monkeypatch):
    config = Config()
    monkeypatch.delenv("DATABASE_URL", raising=False)
    with pytest.raises(KeyError):
        config.init_from_prod_env()
