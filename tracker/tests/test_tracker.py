import pytest
from django.urls import reverse
from rest_framework import status
from tracker.models import Income, Expenditure
from accounts.models import User


# Income
@pytest.mark.django_db
def test_create_income(api_client, test_user, auth_token):
    # api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")

    url = reverse("income-list")
    data = {
        "name_of_revenue": "Salary",
        "amount": "2500.00"
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name_of_revenue"] == "Salary"
    assert response.data["amount"] == "2500.00"


@pytest.mark.django_db
def test_list_incomes(api_client, test_user, auth_token):
    Income.objects.create(user=test_user, name_of_revenue="Salary", amount=2500)
    # api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")
    url = reverse("income-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) >= 1


@pytest.mark.django_db
@pytest.mark.django_db
def test_update_income(api_client, test_user, auth_token):
    income = Income.objects.create(user=test_user, name_of_revenue="Salary", amount=2500)
    # api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")

    url = reverse("income-detail", kwargs={"pk": income.id})
    data = {"name_of_revenue": "Updated Salary", "amount": "3000.00"}

    response = api_client.put(url, data, format="json")
    
    assert response.status_code == status.HTTP_200_OK
    income.refresh_from_db()
    assert income.name_of_revenue == "Updated Salary"
    assert float(income.amount) == 3000.00



@pytest.mark.django_db
def test_delete_income(api_client, test_user, auth_token):
    income = Income.objects.create(user=test_user, name_of_revenue="Salary", amount=2500)
    # api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")

    url = reverse("income-detail", kwargs={"pk": income.id})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Income.objects.filter(id=income.id).count() == 0


# Expenditure 
@pytest.mark.django_db
def test_create_expenditure(api_client, test_user, auth_token):
    # api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")

    url = reverse("expense-list")
    data = {
        "category": "FOOD",
        "name_of_item": "Groceries",
        "estimated_amount": "150.00"
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name_of_item"] == "Groceries"
    assert response.data["estimated_amount"] == "150.00"


@pytest.mark.django_db
def test_list_expenditures(api_client, test_user, auth_token):
    Expenditure.objects.create(user=test_user, category="FOOD", name_of_item="Groceries", estimated_amount=150)
    # api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")

    url = reverse("expense-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_update_expenditure(api_client, test_user, auth_token):
    exp = Expenditure.objects.create(user=test_user, category="FOOD", name_of_item="Groceries", estimated_amount=150)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")
    url = reverse("expense-detail", kwargs={"pk": exp.id})
    data = {"category": "FOOD", "name_of_item": "Supermarket", "estimated_amount": "200.00"}
    response = api_client.patch(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    exp.refresh_from_db()
    assert exp.name_of_item == "Supermarket"
    assert str(exp.estimated_amount) == "200.00"


@pytest.mark.django_db
def test_delete_expenditure(api_client, test_user, auth_token):
    exp = Expenditure.objects.create(user=test_user, category="FOOD", name_of_item="Groceries", estimated_amount=150)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")

    url = reverse("expense-detail", kwargs={"pk": exp.id})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Expenditure.objects.filter(id=exp.id).count() == 0


# Extra Cases
@pytest.mark.django_db
def test_unauthorized_access_income(api_client):
    url = reverse("income-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_invalid_income_creation(api_client, test_user, auth_token):
    # api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")
    url = reverse("income-list")
    data = {"amount": "500.00"}  
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_invalid_expenditure_category(api_client, test_user, auth_token):
    # api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")
    url = reverse("expense-list")
    data = {
        "category": "INVALID",
        "name_of_item": "Test Item",
        "estimated_amount": "100.00"
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_cross_user_access_blocked(api_client, test_user, auth_token):
    # Another user creates an income
    other_user = User.objects.create_user(
        email="other@example.com",
        username="otheruser",
        password="StrongPass@123",
        first_name="abc",
        last_name="abc"
    )
    income = Income.objects.create(user=other_user, name_of_revenue="Other Salary", amount=1000)

    # api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")

    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token['access']}")

    url = reverse("income-detail", kwargs={"pk": income.id})

    # Test 
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
