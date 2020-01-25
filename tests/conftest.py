import pytest
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database

database_url = "postgresql://localhost/bookmarks_testing"
engine = create_engine(database_url)
Session = sessionmaker()


@pytest.fixture(scope="session", autouse=True)
def db():
    if not database_exists(database_url):
        create_database(database_url)

    alembic_config = AlembicConfig("alembic.ini")
    alembic_config.set_main_option("sqlalchemy.url", database_url)
    alembic_upgrade(alembic_config, "head")
    yield
    drop_database(database_url)


@pytest.fixture(scope="module")
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture
def session(connection):
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()
