from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenditureViewSet


router = DefaultRouter()

router.register('incomes', IncomeViewSet, basename='income')
router.register('expenditures', ExpenditureViewSet, basename='expense')


urlpatterns = router.urls