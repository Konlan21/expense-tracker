from django.db import models
import uuid
from accounts.models import User
from django.core.validators import MinValueValidator




# Income
class Income(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    nameOfRevenue = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['created_at']),
            models.Index(fields=['user', 'created_at'])
        ]


    def __str__(self):
        return f"{self.name_of_revenue} - {self.amount}"


# Expenditure
class Expenditure(models.Model):

    CATEGORY_CHOICES = [
        ('FOOD', 'Food & Groceries'),
        ('TRANSPORT', 'Transport'),
        ('RENT', 'Rent'),
        ('UTILITIES', 'Utilities'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('HEALTHCARE', 'Healthcare'),
        ('EDUCATION', 'Education'),
        ('OTHER', 'Other'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenditures")
    category = models.CharField(choices=CATEGORY_CHOICES, default='OTHER', max_length=20)
    name_of_item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # indexing 
    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['category']),
            models.Index(fields=['created_at']),
            models.Index(fields=['user', 'category']),
            models.Index(fields=['user', 'created_at'])
        ]
        
    def __str__(self):
        return f"{self.name_of_item} - {self.amount}"