from django import forms
from .models import Income
import datetime

class IncomeForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        initial=datetime.date.today
    )

    class Meta:
        model = Income
        fields = ['category', 'amount', 'date', 'note']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Optional note', 'rows': 2}),
        }