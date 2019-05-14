from django.contrib.auth.models import User
from django import forms
from .models import Client
from django.forms import ModelForm, widgets

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('phone', 'plan', 'city')

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input100','placeholder': 'Ingrese usuario'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'placeholder': 'Ingrese contraseña'})

