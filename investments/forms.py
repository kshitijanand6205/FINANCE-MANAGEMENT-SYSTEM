'''from django import forms
from .models import Investment
import datetime

class InvestmentForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        initial=datetime.date.today
    )

    class Meta:
        model = Investment
        fields = ['title', 'target_amount', 'saved_amount', 'deadline', 'note']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Buy a laptop'}),
            'target_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Target amount'}),
            'saved_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Current savings'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Optional note', 'rows': 2}),
        }'''

from django import forms
from .models import Investment

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['title', 'amount_invested', 'target_amount', 'start_date', 'end_date', 'note']