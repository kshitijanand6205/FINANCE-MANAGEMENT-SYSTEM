'''from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_goal, name='add_goal'),
    path('list/', views.goal_list, name='goal_list'),
]'''
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_investment, name='add_investment'),
    path('list/', views.investment_list, name='investment_list'),  
]