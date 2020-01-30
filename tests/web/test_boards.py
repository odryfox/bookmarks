from src.models import Board


def test_index(client):
    response = client.get("/boards/")
    boards = response.json

    assert response.status_code == 200 and boards == []


def test_index_after_create_board(client, session):
    board = Board(name="Great board")
    session.add(board)
    session.commit()

    response = client.get("/boards/")

    actual_status_code = response.status_code
    actual_json = response.json

    expected_code = 200
    expected_json = [{'id': board.id, 'name': board.name}]

    assert actual_status_code == expected_code and actual_json == expected_json
