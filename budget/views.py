from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import BudgetForm
from .models import Budget
from django.contrib.auth.decorators import login_required

@login_required
def create_budget_view(request):
    form = BudgetForm()
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budget_list')
    return render(request, 'budget/create_budget.html', {'form': form})

@login_required
def budget_list_view(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'budget/budget_list.html', {'budgets': budgets})