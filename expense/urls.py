from django.urls import path
from .views import add_expense, expense_list

urlpatterns = [
    path('add/', add_expense, name='add_expense'),
    path('list/', expense_list, name='expense_list'),
]