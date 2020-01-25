class Board:
    def __init__(self, *, id: int):
        self.id = id

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.id == self.id

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"
