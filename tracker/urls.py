from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenditureViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r'income', IncomeViewSet, basename='income')

router.register(r'expenditure', ExpenditureViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
]
