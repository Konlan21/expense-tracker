import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user(db):
    user = User.objects.create_user(
        email="financeuser@example.com",
        username="financeuser",
        first_name="Finance",
        last_name="User",
        password="StrongPass@123"
    )
    return user

@pytest.fixture
def auth_token(api_client, test_user):
    login_url = reverse("login")
    response = api_client.post(
        login_url,
        {"email": test_user.email, "password": "StrongPass@123"},
        format="json"
    )
    assert response.status_code == 200
    return response.data["access"], response.data["refresh"]
