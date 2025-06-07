from fastapi.testclient import TestClient
from single_file import app

class TestUsersAPI:
    
    client = TestClient(app)

    def test_success_with_insert_user(_self):
        sample_user = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testemail"
        }
        response = _self.client.post("/users", json=sample_user)
        assert response.status_code == 201
        assert response.json() == {"message": "User inserted successfully"}

    def test_success_with_get_all_users(_self):
        response = _self.client.get("/users")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    def test_error_with_insert_user(_self):
        invalid_user = {
            "username": "testuser",
            "password": "short",  # Invalid password
            "email": "invalid-email"  # Invalid email
        }
        response = _self.client.post("/users", json=invalid_user)
        assert response.status_code == 400
        assert "detail" in response.json()


    def test_404_invalid_endpoint(_self):
        response = _self.client.get("/invalid")
        assert response.status_code == 404
        assert response.json() == {"detail": "Not Found"}