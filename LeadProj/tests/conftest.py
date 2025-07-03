# conftest.py
import pytest
from rest_framework.test import APIClient
from django.conf import settings

from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()

@pytest.fixture
def manager_user(db):
    return User.objects.create_user(
        email="manager@test.com", 
        password="manager", 
        role="manager")

@pytest.fixture
def agent_user(db):
    return User.objects.create_user(
        email="agent@test.com", 
        password="agent", 
        role="sales_agent")

@pytest.fixture
def lead_factory(db):
    def create_lead(**kwargs):
        defaults = {
            "name": "Default Lead",
            "email": "default@example.com",
            "status": "new",
            "created_at": now(),
        }
        defaults.update(kwargs)
        return Lead.objects.create(**defaults)
    return create_lead


@pytest.fixture
def admin_user(db):
    return User.objects.create_user(
        email='admin@example.com',
        password='adminpass',
        role='admin',
        is_staff=True,
        is_superuser=True
    )

@pytest.fixture
def api_client():    
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def authenticated_client(api_client, admin_user):
    # Log in to get the token
    response = api_client.post('/api/accounts/login/', {
        'email': 'admin@example.com',
        'password': 'adminpass'
    })
    access_token = response.data['access']
    
    # Set the token in the header
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    return api_client

# Make sure to run pytest with Django settings configured.
# Example:
# pytest --ds=LeadProj.settings
# Or set the environment variable:
# set DJANGO_SETTINGS_MODULE=LeadProj.settings


