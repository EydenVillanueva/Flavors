from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import CreateView, FormView, UpdateView, TemplateView, ListView
from .models import Client, Restaurant


# Create your views here.

''' 
------------------------------------------
Views sistema de autenticación de usuarios
------------------------------------------
'''
class NewUser(CreateView):
    model = User
    template_name = 'Dashboard/new-user-form.html'
    form_class = UserForm
    success_url = '/'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_cliente = ClientFormSet()
        return self.render_to_response(self.get_context_data(form=form, detalle_client_form_set=detalle_cliente))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        client_form_set = ClientFormSet(request.POST)
        if form.is_valid() and client_form_set.is_valid():

            return self.form_valid(form, client_form_set)
        else:
            return self.form_invalid(form, client_form_set)

    def form_valid(self, form, client_form_set):
        self.object = form.save()
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        self.object= authenticate(username=self.object.username, password=form.cleaned_data['password'])
        client_form_set.instance = self.object
        client_form_set.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, client_form_set):
        return self.render_to_response(self.get_context_data(form=form, detalle_client_form_set=client_form_set))


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'Dashboard/login.html'
    success_url = reverse_lazy("Dashboard:panel")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            login(self.request, form.get_user())
            return super(LoginView, self).form_valid(form)
        else:
            return super(LoginView, self).form_invalid(form)


def logout_view(request):
    logout(request)
    return render(request, 'Dashboard/index.html')


''' 
------------------------------------------
Views landing page
------------------------------------------
'''


class Home(TemplateView):
    template_name = "Dashboard/index.html"


class ContactView(FormView):
    template_name = 'Dashboard/index.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


''' 
------------------------------------------
Views panel de control
------------------------------------------
'''


class Panel(LoginRequiredMixin,TemplateView):
    template_name = "Panel/index.html"
    login_url = 'Dashboard:login'


class CreateRestaurant(LoginRequiredMixin, CreateView):
    form_class = RestaurantForm
    template_name = "Restaurants/new_restaurant.html"
    success_url = reverse_lazy("Dashboard:panel")

    login_url = 'Dashboard:login'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.owner = self.get_object()
            restaurant.save()
            return super(CreateRestaurant, self).form_valid(form)
        else:
            return super(CreateRestaurant, self).form_invalid(form)

    def get_object(self):
        client = Client.objects.get(user=self.request.user)
        return client


class UpdateRestaurant(LoginRequiredMixin, UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = "Restaurants/update_restaurant.html"
    success_url = reverse_lazy("Dashboard:panel")

    login_url = 'Dashboard:login'


class ListRestaurant(LoginRequiredMixin, ListView):
    Error = False
    model = Restaurant
    template_name = "Panel/list_restaurant.html"

    def get_queryset(self):
        queryset = Restaurant.objects.filter(owner=self.request.user.client, active=True)
        return queryset



class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'Panel/update_profile.html'
    form_class = UserUpdateForm
    second_form_class = UpdateProfileForm
    success_url = reverse_lazy("Dashboard:panel")

    login_url = 'Dashboard:login'

    def get(self, request, *args, **kwargs):
        super(UpdateProfile, self).get(request, *args, **kwargs)

        if kwargs['pk']:
            form = UserUpdateForm(instance = self.request.user)
            form2 = UpdateProfileForm(instance = self.request.user.client)

        return self.render_to_response(self.get_context_data(object=self.object, form=form, form2=form2))
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        user = self.request.user
        client = self.request.user.client

        form = self.form_class(request.POST, instance=user)
        form2 = self.second_form_class(request.POST, instance=client)

        if form.is_valid() and form2.is_valid():

            userdata = form.save(commit=False)
            userdata.save()

            clientdata = form2.save(commit=False)
            clientdata.user = userdata
            clientdata.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


def delete_list_restaurant(request):
    restaurants = Restaurant.objects.all().order_by('id')
    contexto = {'restaurants':restaurants}
    return render(request,'Restaurants/delete_list_restaurant.html', contexto)

def delete_restaurant(request, id_restaurant):
    restaurant = Restaurant.objects.get(id=id_restaurant)
    if request.method == 'POST':
        restaurant.active = False
        restaurant.save()
        return redirect('Dashboard:delete_list_restaurant')
    return render(request, 'Restaurants/delete_restaurant.html',{'restaurant':restaurant})


