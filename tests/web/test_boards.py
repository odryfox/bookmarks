from src.models import Board


def test_index(client):
    response = client.get("/boards/")
    boards = response.json

    assert response.status_code == 200 and boards == []


def test_index_after_create_board(client, session):
    board = Board()
    session.add(board)
    session.commit()

    response = client.get("/boards/")
    boards = response.json

    assert response.status_code == 200 and boards == [{'id': board.id}]
