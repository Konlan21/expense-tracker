# tracker/views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Income, Expenditure
from .serializers import IncomeSerializer, ExpenditureSerializer
from .docs import income_schemas, expenditure_schemas
from .utils import apply_schemas



# Income ViewSet
@apply_schemas(income_schemas)
class IncomeViewSet(ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Expenditure ViewSet
@apply_schemas(expenditure_schemas)
class ExpenditureViewSet(ModelViewSet):
    serializer_class = ExpenditureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expenditure.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
