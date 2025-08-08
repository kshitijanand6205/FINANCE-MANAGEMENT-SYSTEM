from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")