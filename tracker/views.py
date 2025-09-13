from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .models import Income, Expenditure
from .serializers import IncomeSerializer, ExpenditureSerializer




# Income ViewSet
@extend_schema(tags=['Income'])
class IncomeViewSet(ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



# Expenditure ViewSet
@extend_schema(tags=['Expenditure'])
class ExpenditureViewSet(ModelViewSet):
    serializer_class = ExpenditureSerializer
    permission_classes = []

    def get_queryset(self):
        return Expenditure.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
