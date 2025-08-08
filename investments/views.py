'''from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import InvestmentForm
from .models import Investment
from django.contrib.auth.decorators import login_required

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goal_list')
    else:
        form = InvestmentForm()
    return render(request, 'investments/add_goal.html', {'form': form})

@login_required
def goal_list(request):
    goals = Investment.objects.filter(user=request.user)
    return render(request, 'investments/goal_list.html', {'goals': goals})'''
from django.shortcuts import render, redirect
from .models import Investment
from .forms import InvestmentForm
from django.contrib.auth.decorators import login_required

@login_required
def investment_list(request):
    investments = Investment.objects.filter(user=request.user)
    return render(request, 'investments/investment_list.html', {'investments': investments})

@login_required
def add_investment(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.user = request.user
            investment.save()
            return redirect('investment_list')
    else:
        form = InvestmentForm()
    return render(request, 'investments/investment_form.html', {'form': form})

