from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from budget.models import Budget

User = get_user_model()

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def _str_(self):
        return f"{self.category} - ₹{self.amount}"