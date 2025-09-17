# accounts/tests/test_accounts.py
import pytest
from django.urls import reverse
from rest_framework import status



# Signup Tests
@pytest.mark.django_db
def test_signup_success(api_client):

    url = reverse("signup")
    data = {
        "email": "newuser@example.com",
        "username": "newuser",
        "first_name": "New",
        "last_name": "User",
        "password": "StrongPass@123",
        "confirm_password": "StrongPass@123"
    }

    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
    assert response.data["email"] == "newuser@example.com"


@pytest.mark.django_db
def test_signup_invalid_password(api_client):
    url = reverse("signup")
    data = {
        "email": "weakuser@example.com",
        "username": "weakuser",
        "first_name": "Weak",
        "last_name": "User",
        "password": "weakpass",
        "confirm_password": "weakpass"
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "password" in response.data


# Login Tests

@pytest.mark.django_db
def test_login_success(api_client, test_user):

    url = reverse("login")
    response = api_client.post(
        url,
        {"email": test_user.email, "password": "StrongPass@123"},
        format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_login_invalid_credentials(api_client):

    url = reverse("login")
    response = api_client.post(
        url,
        {"email": "wrong@example.com", "password": "nopass"},
        format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


# Logout Tests
@pytest.mark.django_db
def test_logout_success(api_client, auth_token):
    access_token, refresh_token = auth_token
    url = reverse("logout")

    # Set authorization header
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    response = api_client.post(url, {"refresh": refresh_token}, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "User logged out successfully"


@pytest.mark.django_db
def test_logout_invalid_token(api_client, auth_token):
    access_token, _ = auth_token
    url = reverse("logout")

    # Setting authorization header
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    # Send an invalid refresh token
    response = api_client.post(url, {"refresh": "invalidtoken"}, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "detail" in response.data


# User Profile Tests
@pytest.mark.django_db
def test_get_user_profile_success(api_client, test_user, auth_token):
    access_token, _ = auth_token
    url = reverse("user-profile", kwargs={"userID": test_user.id})
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == test_user.email


@pytest.mark.django_db
def test_get_user_profile_invalid_id(api_client, auth_token):
    access_token, _ = auth_token
    url = reverse("user-profile", kwargs={"userID": "00000000-0000-0000-0000-000000000000"})
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = api_client.get(url)
    assert response.status_code in [
        status.HTTP_400_BAD_REQUEST, 
        status.HTTP_403_FORBIDDEN, 
        status.HTTP_404_NOT_FOUND
        ]



@pytest.mark.django_db
def test_update_user_profile_success(api_client, test_user, auth_token):
    access_token, _ = auth_token
    url = reverse("user-profile", kwargs={"userID": test_user.id})
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    data = {
        "first_name": "Updated",
        "last_name": "User",
        "username": "updateduser",
        "email": test_user.email 
    }
    response = api_client.put(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["first_name"] == "Updated"


@pytest.mark.django_db
def test_update_user_profile_missing_field(api_client, test_user, auth_token):
    access_token, _ = auth_token
    url = reverse("user-profile", kwargs={"userID": test_user.id})
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    data = {"first_name": "Updated"} 
    response = api_client.put(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST