from django.urls import path
from .views import create_budget_view, budget_list_view

urlpatterns = [
    path('create-budget/', create_budget_view, name='create_budget'),
    path('list/', budget_list_view, name='budget_list'),
]