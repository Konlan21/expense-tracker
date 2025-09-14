# tracker/docs.py
from drf_spectacular.utils import extend_schema, OpenApiExample

# -------------------------
# Income Schemas
# -------------------------
income_schemas = {
    "list": extend_schema(
        description="List all incomes of the authenticated user",
        tags=["Income"],
        examples=[
            OpenApiExample(
                "Income List Example",
                value=[
                    {"id": "uuid1", "name_of_revenue": "Salary", "amount": 500},
                    {"id": "uuid2", "name_of_revenue": "Freelance", "amount": 200},
                ],
                response_only=True,
            ),
        ],
    ),
    "retrieve": extend_schema(
        description="Retrieve a single income by ID",
        tags=["Income"],
        examples=[
            OpenApiExample(
                "Income Retrieve Example",
                value={"id": "uuid1", "name_of_revenue": "Salary", "amount": 500},
                response_only=True,
            )
        ]
    ),
    "create": extend_schema(
        description="Create a new income record for the authenticated user",
        tags=["Income"],
        examples=[
            OpenApiExample(
                "Create Income Example",
                value={"name_of_revenue": "Salary", "amount": 500},
                request_only=True,
            ),
            OpenApiExample(
                "Income Response Example",
                value={"id": "uuid1", "name_of_revenue": "Salary", "amount": 500},
                response_only=True,
            ),
        ],
    ),
    "update": extend_schema(
        description="Update an existing income record completely",
        tags=["Income"],
    ),
    "partial_update": extend_schema(
        description="Partially update an existing income record",
        tags=["Income"],
    ),
    "destroy": extend_schema(
        description="Delete an income record",
        tags=["Income"],
    ),
}

# -------------------------
# Expenditure Schemas
# -------------------------
expenditure_schemas = {
    "list": extend_schema(
        description="List all expenditures of the authenticated user",
        tags=["Expenditure"],
        examples=[
            OpenApiExample(
                "Expenditure List Example",
                value=[
                    {"id": "uuid1", "category": "FOOD", "name_of_item": "Groceries", "amount": 150.00},
                    {"id": "uuid2", "category": "TRANSPORT", "name_of_item": "Bus fare", "amount": 100.00},
                ],
                response_only=True,
            )
        ]
    ),
    "retrieve": extend_schema(
        description="Retrieve a single expenditure record by its ID",
        tags=["Expenditure"],
        examples=[
            OpenApiExample(
                "Expenditure Retrieve Example",
                value={"id": "uuid1", "category": "FOOD", "name_of_item": "Groceries", "amount": 150.00},
                response_only=True,
            )
        ]
    ),
    "create": extend_schema(
        description="Create a new expenditure record for the authenticated user",
        tags=["Expenditure"],
        examples=[
            OpenApiExample(
                "Create Expenditure Example",
                value={"category": "TRANSPORT", "name_of_item": "Bus fare", "amount": 100.00},
                request_only=True,
            ),
            OpenApiExample(
                "Expenditure Response Example",
                value={"id": "uuid1", "category": "TRANSPORT", "name_of_item": "Bus fare", "amount": 100.00},
                response_only=True,
            ),
        ],
    ),
    "update": extend_schema(
        description="Update an existing expenditure record completely",
        tags=["Expenditure"],
    ),
    "partial_update": extend_schema(
        description="Partially update an existing expenditure record",
        tags=["Expenditure"],
    ),
    "destroy": extend_schema(
        description="Delete an expenditure record",
        tags=["Expenditure"],
    ),
}
