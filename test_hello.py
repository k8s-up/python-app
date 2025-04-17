import pytest

from hello import app


@pytest.fixture(name="client")
def fixture_client():
    with app.test_client() as client:
        yield client


def test_add(client):
    response = client.get("/api/hello")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["message"] == "hello ArgoCD"