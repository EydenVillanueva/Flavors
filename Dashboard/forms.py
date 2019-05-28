from django.contrib.auth.models import User
from django import forms
from .models import Client, Restaurant
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'password': 'Contraseña',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input100'})

        self.fields['password'].widget = forms.widgets.PasswordInput(
            attrs={'placeholder': 'Ingrese contraseña'})
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo'
        
    def clean_email(self):
        email = self.cleaned_data['email']
        query = User.objects.filter(email=email)
        if query.exists():
            raise ValidationError(('Email ya registrado.'))
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        query = User.objects.filter(username=username)
        if query.exists():
            raise ValidationError(('Nombre de usuario existente.'))
        return username

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('phone', 'plan', 'city')

        labels = {
            'phone': 'Número Telefónico',
            'plan': 'Plan',
            'Ciudad': 'City',
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not(phone):
            raise ValidationError("Ingrese un número telefonico")
        return phone

    def clean_plan(self):
        plan = self.cleaned_data['plan']
        if not(plan):
            raise ValidationError("Ingrese el plan")
        return plan
    
    def clean_city(self):
        city = self.cleaned_data['city']
        if not(city):
            raise ValidationError("Ingrese la ciudad")
        return city

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input100'})

        self.fields['phone'].widget.attrs['placeholder'] = 'Número'
        self.fields['plan'].widget.attrs['placeholder'] = 'Plan'
        self.fields['city'].widget.attrs['placeholder'] = 'Ciudad de Residencia'

ClientFormSet = inlineformset_factory(User, Client, form=ClientForm, validate_min=True)


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'input100', 'placeholder': 'Ingrese usuario'})
        self.fields['password'].widget = forms.widgets.PasswordInput(
            attrs={'placeholder': 'Ingrese contraseña'})


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'logo_url',
                  'web_site')
        labels = {
            'name': 'Nombre',
            'address': 'Dirección',
            'logo_url': 'Dirección Logo',
            'web_site': 'Sitio Web',
            'status': 'Abierto'
        }

    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input100'})
