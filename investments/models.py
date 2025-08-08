from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2, )
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.email}"
   
