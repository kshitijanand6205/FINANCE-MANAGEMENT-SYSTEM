# Create your views here.
# reporting/views.py

from django.shortcuts import render
from expense.models import Expense
from income.models import Income
from budget.models import Budget
from investments.models import Investment
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Sum
from  django.contrib import messages

@login_required
def analytics_dashboard(request):
    user = request.user
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Filter user's data
    expenses = Expense.objects.filter(user=user, date__month=current_month, date__year=current_year)
    income = Income.objects.filter(user=user, date__month=current_month, date__year=current_year)
    budget = Budget.objects.filter(user=user)
    goals = Investment.objects.filter(user=user)

    # Aggregates
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_income = income.aggregate(Sum('amount'))['amount__sum'] or 0
    total_budget = budget.aggregate(Sum('amount'))['amount__sum'] or 0

    over_budget = total_expense > total_budget if total_budget > 0 else False
    
    context = {
        'total_expense': total_expense,
        'total_income': total_income,
        'total_budget': total_budget,
        'expenses': expenses,
        'income': income,
        'goals': goals,
        'over_budget': over_budget,
    }

    return render(request, 'reporting/dashboard.html', context)

    