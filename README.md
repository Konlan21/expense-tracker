# Expense Tracker API

A Django REST API for tracking personal income and expenses. Supports JWT authentication, CRUD operations for income and expenditures, and comes with interactive OpenAPI 3.0 documentation.

## Features

- User registration and authentication with JWT.
- Create, read, update, and delete income and expenditure records.
- Role-based access to ensure users only access their own records.
- API documentation via OpenAPI 3.0.
- Unit and integration tests for all endpoints.

## Tech Stack

- **Backend:** Django, Django REST Framework  
- **Authentication:** JWT (Simple JWT)  
- **Database:** SQLite (default) / can be configured for PostgreSQL  
- **Documentation:** OpenAPI 3.0  
- **Testing:** Pytest, Django test client  

## Installation

1. Clone the repo:
```bash
git clone  https://github.com/Konlan21/expense-tracker.git
cd expense-tracker
```

## Create virtual environment:
```bash
python -m venv env
````

## Activate virtual environment
```bash
source env/bin/activate      # Linux/Mac
env/Scripts/activate         # Windows
````

## Install dependencies:

````bash
pip install -r requirements.txt
````

## Apply migrations:
````bash
python manage.py migrate
````
## Run the development server:
```bash
python manage.py runserver
```

## Running Tests

````bash
pytest
````

## API Documentation

- **OpenAPI 3.0:** [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)  
- **Redoc:** [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)  
- **OpenAPI schema:** [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

## Endpoints

- **Authentication:** /auth/  
- **Income:** /tracker/incomes/  
- **Expenditure:** /tracker/expenditures/  

> ChecK OpenAPI 3.0 for full request and response examples.






