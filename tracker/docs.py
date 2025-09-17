from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample
from .serializers import IncomeSerializer, ExpenditureSerializer

# ---------------- Income Schemas ----------------
income_schemas = extend_schema_view(
    list=extend_schema(
        tags=["income"],
        summary="List incomes",
        description="Retrieve a list of all income records for the authenticated user.",
        responses={200: IncomeSerializer(many=True)},
    ),
    create=extend_schema(
        tags=["income"],
        summary="Add a new income",
        description="Create a new income record for the authenticated user.",
        request=IncomeSerializer,
        responses={201: IncomeSerializer},
        examples=[
            OpenApiExample(
                "Create Income Request Example",
                value={"amount": 2000, "source": "Salary", "date": "2025-09-01"},
                request_only=True,
            ),
            OpenApiExample(
                "Create Income Success Response",
                value={"id": 1, "amount": 2000, "source": "Salary", "date": "2025-09-01"},
                response_only=True,
            ),
        ],
    ),
    retrieve=extend_schema(
        tags=["income"],
        summary="Retrieve an income",
        description="Retrieve a specific income record by ID.",
        responses={200: IncomeSerializer},
    ),
    update=extend_schema(
        tags=["income"],
        summary="Update an existing income",
        description="Fully update an existing income record by ID. Requires authentication.",
        request=IncomeSerializer,
        responses={200: IncomeSerializer},
        examples=[
            OpenApiExample(
                "Update Income Request Example",
                value={"amount": 2500, "source": "Salary", "date": "2025-09-01"},
                request_only=True,
            ),
            OpenApiExample(
                "Update Income Success Response",
                value={"id": 1, "amount": 2500, "source": "Salary", "date": "2025-09-01"},
                response_only=True,
            ),
        ],
    ),
    partial_update=extend_schema(
        tags=["income"],
        summary="Partially update an income",
        description="Update selected fields of an existing income record.",
        request=IncomeSerializer,
        responses={200: IncomeSerializer},
        examples=[
            OpenApiExample(
                "Partial Update Income Request Example",
                value={"amount": 1800},
                request_only=True,
            ),
            OpenApiExample(
                "Partial Update Income Success Response",
                value={"id": 1, "amount": 1800, "source": "Salary", "date": "2025-09-01"},
                response_only=True,
            ),
        ],
    ),
    destroy=extend_schema(
        tags=["income"],
        summary="Delete an income",
        description="Delete an existing income record by ID.",
        responses={204: None},
    ),
)

# ---------------- Expenditure Schemas ----------------
expenditure_schemas = extend_schema_view(
    list=extend_schema(
        tags=["expenditure"],
        summary="List expenditures",
        description="Retrieve a list of all expenditure records for the authenticated user.",
        responses={200: ExpenditureSerializer(many=True)},
    ),
    create=extend_schema(
        tags=["expenditure"],
        summary="Add a new expenditure",
        description="Create a new expenditure record for the authenticated user.",
        request=ExpenditureSerializer,
        responses={201: ExpenditureSerializer},
        examples=[
            OpenApiExample(
                "Create Expenditure Request Example",
                value={"amount": 500, "category": "Food", "date": "2025-09-01"},
                request_only=True,
            ),
            OpenApiExample(
                "Create Expenditure Success Response",
                value={"id": 1, "amount": 500, "category": "Food", "date": "2025-09-01"},
                response_only=True,
            ),
        ],
    ),
    retrieve=extend_schema(
        tags=["expenditure"],
        summary="Retrieve an expenditure",
        description="Retrieve a specific expenditure record by ID.",
        responses={200: ExpenditureSerializer},
    ),
    update=extend_schema(
        tags=["expenditure"],
        summary="Update an existing expenditure",
        description="Fully update an existing expenditure record by ID. Requires authentication.",
        request=ExpenditureSerializer,
        responses={200: ExpenditureSerializer},
        examples=[
            OpenApiExample(
                "Update Expenditure Request Example",
                value={"amount": 600, "category": "Food", "date": "2025-09-01"},
                request_only=True,
            ),
            OpenApiExample(
                "Update Expenditure Success Response",
                value={"id": 1, "amount": 600, "category": "Food", "date": "2025-09-01"},
                response_only=True,
            ),
        ],
    ),
    partial_update=extend_schema(
        tags=["expenditure"],
        summary="Partially update an expenditure",
        description="Update selected fields of an existing expenditure record.",
        request=ExpenditureSerializer,
        responses={200: ExpenditureSerializer},
        examples=[
            OpenApiExample(
                "Partial Update Expenditure Request Example",
                value={"amount": 550},
                request_only=True,
            ),
            OpenApiExample(
                "Partial Update Expenditure Success Response",
                value={"id": 1, "amount": 550, "category": "Food", "date": "2025-09-01"},
                response_only=True,
            ),
        ],
    ),
    destroy=extend_schema(
        tags=["expenditure"],
        summary="Delete an expenditure",
        description="Delete an existing expenditure record by ID.",
        responses={204: None},
    ),
)
