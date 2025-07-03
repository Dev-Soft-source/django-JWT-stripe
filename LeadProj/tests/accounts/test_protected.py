import pytest

@pytest.mark.django_db
def test_protected_view_requires_auth(api_client):
    response = api_client.get('/api/accounts/protected/')
    assert response.status_code == 401

@pytest.mark.django_db
def test_protected_view_success(authenticated_client):
    response = authenticated_client.get('/api/accounts/protected/')
    assert response.status_code == 200
    assert 'message' in response.data