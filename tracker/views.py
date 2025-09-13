from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .models import Income, Expenditure
from .serializers import IncomeSerializer, ExpenditureSerializer


# tracker/views.py
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Income, Expenditure
from .serializers import IncomeSerializer, ExpenditureSerializer
from drf_spectacular.utils import extend_schema



# Income ViewSet
@extend_schema(tags=['Income'])
class IncomeViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



# Expenditure ViewSet
@extend_schema(tags=['Expenditure'])
class ExpenditureViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = ExpenditureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expenditure.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
