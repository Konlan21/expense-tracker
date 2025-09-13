import pytest
from rest_framework.test import APIClient
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken



# API client fixture
@pytest.fixture
def api_client():
    return APIClient()


# Test user fixture
@pytest.fixture
def test_user(db):
    """
    Creates and returns a default test user.
    """
    user = User.objects.create_user(
        email="financeuser@example.com",
        username="financeuser",
        password="StrongPass@123",
        first_name="Finance",
        last_name="User"
    )
    return user


# Auth token fixture
@pytest.fixture
def auth_token(test_user):
    """
    Returns a dict with access and refresh tokens for the test_user.
    """
    refresh = RefreshToken.for_user(test_user)
    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }


# Another user fixture
@pytest.fixture
def other_user(db):
    """
    Creates and returns another user for cross-user access tests.
    """
    user = User.objects.create_user(
        email="other@example.com",
        username="otheruser",
        password="StrongPass@123",
        first_name="Other",
        last_name="User"
    )
    return user
