from sqlalchemy import Column, Integer

from src.db import db


class Board(db.Model):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.id == self.id

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"
