# accounts/tests/test_auth.py

import pytest

@pytest.mark.django_db
def test_user_registration(api_client):
    payload = {
        "email": "newuser@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "testpass123",
        "role": "sales_agent"
    }

    response = api_client.post("/api/accounts/register/", payload)
    assert response.status_code == 201
    assert response.data["email"] == payload["email"]


@pytest.mark.django_db
def test_user_login(api_client, admin_user):
    payload = {
        "email": admin_user.email,
        "password": "adminpass"
    }

    response = api_client.post("/api/accounts/login/", payload)
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data
