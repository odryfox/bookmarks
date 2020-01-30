from src.models import Board


def test_repr_board():
    board = Board(id=1, name="Great board")

    assert repr(board) == "Board(id=1, name='Great board')"


def test_eq_boards():
    board = Board(id=1, name="Great board")
    other_board = Board(id=1, name="Great board")

    assert other_board == board


def test_saved_board(session):
    board = Board(name="Great board")
    session.add(board)
    session.commit()

    saved_board = session.query(Board).first()

    assert saved_board == board
