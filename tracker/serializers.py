from rest_framework.serializers import ModelSerializer
from tracker.models import Income, Expenditure


# Income
class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ["id", "name_of_revenue", "amount", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

# Expenditure
class ExpenditureSerializer(ModelSerializer):
    class Meta:
        model = Expenditure
        fields = ["id", "category", "name_of_item", "estimated_amount", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
