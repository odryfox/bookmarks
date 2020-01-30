import os

import pytest
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from dotenv import load_dotenv
from sqlalchemy_utils import database_exists, create_database, drop_database

from src.db import db as database
from src.web import create_app

load_dotenv()


def migrate_db(database_url: str):
    alembic_config = AlembicConfig("alembic.ini")
    alembic_config.set_main_option("sqlalchemy.url", database_url)
    alembic_upgrade(alembic_config, "head")


@pytest.fixture(scope="session", autouse=True)
def init_db():
    default_database_url = "postgresql://localhost/bookmarks_testing"
    database_url = os.environ.get("TEST_DATABASE_URL", default_database_url)

    if database_exists(database_url):
        drop_database(database_url)

    create_database(database_url)
    migrate_db(database_url)
    database.init_from_url(database_url)

    yield

    drop_database(database_url)


@pytest.fixture
def db():
    database.truncate_all()
    yield database
    database.truncate_all()


@pytest.fixture
def session(db):
    yield db.session


@pytest.fixture(scope="session")
def web_app():
    return create_app("test")


@pytest.fixture(scope="session")
def client(web_app):
    return web_app.test_client()
