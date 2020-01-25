from src.models import Board


def test_repr_board():
    board = Board(id=1)

    assert repr(board) == "Board(id=1)"


def test_eq_boards():
    board = Board(id=1)
    other_board = Board(id=1)

    assert other_board == board


def test_saved_board(session):
    board = Board()
    session.add(board)
    session.commit()

    saved_board = session.query(Board).first()

    assert saved_board == board
