import contextlib

from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa


class SQLAlchemy:
    def __init__(self):
        self.Model = declarative_base()
        self.url = None
        self.engine = None
        self.session = None

    def init_from_url(self, url: str):
        self.url = url
        self.engine = sa.create_engine(self.url)
        self.Model.metadata.bind = self.engine
        self.session = orm.scoped_session(orm.sessionmaker(bind=self.engine))

    def truncate_all(self):
        with contextlib.closing(self.engine.connect()) as con:
            trans = con.begin()
            for table in reversed(self.Model.metadata.sorted_tables):
                con.execute(table.delete())
            trans.commit()


db = SQLAlchemy()


from src.models import Board


__all__ = [
    Board,
]
