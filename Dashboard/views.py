from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import LoginForm, UserForm, ClientForm
from django.views.generic import CreateView, FormView, TemplateView
from .models import Client


# Create your views here.
def new_user(request):
    error = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        client_form = ClientForm(request.POST)

        if user_form.is_valid() and client_form.is_valid():
            # E-mail check
            repeat_email = User.objects.filter(
                email=user_form.cleaned_data["email"])
            # Username check
            repeat_user = User.objects.filter(
                username=user_form.cleaned_data["username"])

            if not repeat_email.exists():
                user = user_form.save()

                client = client_form.save(commit=False)
                client.user = user

                client_form.save()

                username = user_form.cleaned_data.get('username')
                password = user_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)

                return redirect('/')
    else:
        user_form = UserForm()
        client_form = ClientForm()

    context = {'user_form': user_form, 'client_form': client_form}

    return render(request, 'Dashboard/new-user-form.html', context)

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'Dashboard/login.html'
    success_url = reverse_lazy("Dashboard:home")

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


class Home(TemplateView):
    template_name = "Dashboard/index.html"
    
def logout_view(request):
    logout(request)
    return render(request, 'Dashboard/index.html')
