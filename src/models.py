from sqlalchemy import Column, Integer, String

from src.db import db


class Board(db.Model):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            other.id == self.id and
            other.name == self.name
        )

    def __repr__(self):
        class_name = self.__class__.__name__
        name = repr(self.name)
        id_ = repr(self.id)
        return f"{class_name}(id={id_}, name={name})"
