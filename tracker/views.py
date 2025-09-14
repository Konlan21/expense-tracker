from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiExample
from .models import Income, Expenditure
from .serializers import IncomeSerializer, ExpenditureSerializer

# -----------------------------
# Income ViewSet
# -----------------------------
@extend_schema(
    tags=["Income"],
    description="CRUD operations for user income. Users can list, retrieve, create, update, and delete their income records.",
    examples=[
        OpenApiExample(
            "Create Income Example",
            value={"name_of_revenue": "Salary", "amount": 500},
            request_only=True,
        ),
        OpenApiExample(
            "Income Response Example",
            value={
                "id": "c9f2c7c0-1c8f-4c8f-9c3a-b63a5b62cafa",
                "name_of_revenue": "Salary",
                "amount": 500,
            },
            response_only=True,
        ),
    ],
)
class IncomeViewSet(ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# -----------------------------
# Expenditure ViewSet
# -----------------------------
@extend_schema(
    tags=["Expenditure"],
    description="CRUD operations for user expenditures. Users can list, retrieve, create, update, and delete their expenditure records.",
    examples=[
        OpenApiExample(
            "Create Expenditure Example",
            value={"category": "TRANSPORT", "name_of_item": "Bus fare", "amount": 100},
            request_only=True,
        ),
        OpenApiExample(
            "Expenditure Response Example",
            value={
                "id": "c9f2c7c0-1c8f-4c8f-9c3a-b63a5b62cafa",
                "category": "TRANSPORT",
                "name_of_item": "Bus fare",
                "amount": 100,
            },
            response_only=True,
        ),
    ],
)
class ExpenditureViewSet(ModelViewSet):
    serializer_class = ExpenditureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expenditure.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
