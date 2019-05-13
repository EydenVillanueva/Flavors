from django.contrib.auth.models import User
from django import forms
from .models import Client
from django.forms import ModelForm, widgets

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('phone', 'plan', 'city')

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

