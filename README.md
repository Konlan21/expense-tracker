# Expense Tracker API

A Django REST API for tracking personal income and expenses. Supports JWT authentication, CRUD operations for income and expenditures, and comes with interactive Swagger documentation.

## Features

- User registration and authentication with JWT.
- Create, read, update, and delete income and expenditure records.
- Role-based access to ensure users only access their own records.
- API documentation via Swagger UI.
- Unit and integration tests for all endpoints.

## Tech Stack

- **Backend:** Django, Django REST Framework  
- **Authentication:** JWT (Simple JWT)  
- **Database:** SQLite (default) / can be configured for PostgreSQL  
- **Documentation:** drf-spectacular (OpenAPI / Swagger)  
- **Testing:** Pytest, Django test client  

## Installation

1. Clone the repo:

```bash
git clone  https://github.com/Konlan21/expense-tracker.git
cd expense-tracker

## Create virtual environment:
python -m venv env

## Activate virtual environment
source env/bin/activate      # Linux/Mac
env\Scripts\activate         # Windows

##Install dependencies
pip install -r requirements.txt

## Apply migrations:
python manage.py migrate

## Run the development server:
python manage.py runserver

## Running Tests
pytest


