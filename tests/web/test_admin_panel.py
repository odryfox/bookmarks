def test_index(client):
    response = client.get("/admin/")

    assert response.status_code == 200


def test_boards(client):
    response = client.get("/admin/board/")

    assert response.status_code == 200
