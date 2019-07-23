from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .models import Client, Restaurant, Dish, Shedule, Media, Social
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory
from django.core.mail import send_mail
#from django.bootstrap_datepicker_plus import DatePickerInput


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


ClientFormSet = inlineformset_factory(
    User, Client, form=ClientForm, validate_min=True)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
        }

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('phone', 'city')
        labels = {
            'phone': 'Número Telefónico',
            'Ciudad': 'City',
        }

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        # self.fields['plan'].widget.attrs.update({'disabled': 'true'})


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
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'rows': 3})


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('name', 'description', 'price', 'restaurant', 'categories', 'flavors')
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'restaurant': 'Restaurante',
            'categories': 'Categoria',
            'flavors': 'Sabor'
        }

    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs['placeholder'] = 'Ingresa el nombre del platillo.'
        self.fields['description'].widget.attrs['placeholder'] = 'Ingresa una descripción del platillo.'
        self.fields['price'].widget.attrs['placeholder'] = 'Ingresa el precio.'
        self.fields['restaurant'].empty_label = '---Seleccione uno de sus restaurantes---'


class SheduleForm(forms.ModelForm):

    class Meta:
        model = Shedule
        fields = ('days', 'time_open', 'time_close', 'restaurant')
        labels = {
            'days': 'Dia(s)',
            'time_open': 'Hora de Apertura',
            'time_close': 'Hora de Cierre',
            'restaurant': 'Restaurante'
        }
        """widgets = {
            #'days': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Ingrese los dias del horario'}),
            'time_open': DatePickerInput(),
            #'time_close': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la hora de cierre'}),
        }"""

    def __init__(self, *args, **kwargs):
        super(SheduleForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['days'].widget.attrs['placeholder'] = 'Ingrese los dias del horario.'
        self.fields['time_open'].widget.attrs['placeholder'] = 'Ingrese la hora de apertura'
        self.fields['time_close'].widget.attrs['placeholder'] = 'Ingrese la hora de cierre'
        self.fields['restaurant'].empty_label = '---Seleccione uno de sus restaurantes---'


"""class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ('name', 'red')
        labels = {
            'name': 'Nombre',
            #'red': 'Red Social'
        }

    def __init__(self, *args, **kwargs):
        super(SocialForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs['placeholder'] = 'Ingrese el nombre de la red '
        #self.fields['red'].widget.attrs['placeholder'] = 'Ingrese el url de red social'"""


class MediaForm(forms.ModelForm):

    class Meta:
        model = Media
        fields = ('restaurant', 'social','red')
        labels = {
            'restaurant': 'Restaurante',
            'social': 'Redes Sociales',
            'red': 'URL'
        }

    def __init__(self, *args, **kwargs):
        super(MediaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['restaurant'].empty_label = '---Seleccione uno de sus restaurantes---'
        self.fields['social'].widget.attrs['placeholder'] = 'Ingrese la red social'
        self.fields['red'].widget.attrs['placeholder'] = 'Ingrese el url de red social'


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs['placeholder'] = 'What is your name?'
        self.fields['email'].widget.attrs['placeholder'] = 'What is your email?'
        self.fields['subject'].widget.attrs['placeholder'] = 'What is your subject?'
        self.fields['message'].widget.attrs['placeholder'] = 'What is your message?'

    def send_email(self):
        try:
            self.name = self.cleaned_data.get('name')
            self.email = self.cleaned_data.get('email')
            self.subject = self.cleaned_data.get('subject')
            self.message = self.cleaned_data.get('message')
            email_to = ['pedroesparzaaa@gmail.com']
            email_mensaje = '%s: %s enviado por %s' % (
                self.name, self.message, self.email)

            send_mail(
                self.subject,
                email_mensaje,
                self.email,
                email_to,
                fail_silently=False
            )

        except ValueError:
            print('Hubo un error al enviar el email')

        return True


class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].label = "Contraseña Antigua"
        self.fields['new_password1'].label = "Nueva Contraseña"
        self.fields['new_password2'].label = "Repetir Nueva Contraseña"

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
