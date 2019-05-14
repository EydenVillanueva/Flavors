from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserForm, ClientForm
from django.views.generic import CreateView
from .models import Client

# Create your views here.
def new_user(request):
    error = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        client_form = ClientForm(request.POST)

        if user_form.is_valid() and client_form.is_valid():
            #E-mail check
            repeat_email = User.objects.filter(email=user_form.cleaned_data["email"])
            #Username check
            repeat_user = User.objects.filter(username=user_form.cleaned_data["username"])

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

    context = {'user_form':user_form, 'client_form':client_form}
    
    return render(request, 'Dashboard/new-user-form.html', context)

def userlogin(request):
    if request.method == 'POST':
    
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('Dashboard:home')
        else:
            login_form = LoginForm()
            error = True
            return render(request, 'Dashboard/login.html', {'login_form': login_form, 'error': error})
    else:
        login_form = LoginForm()
        error = False
        return render(request, 'Dashboard/login.html', {'login_form': login_form, 'error': error})

def home(request):
    return render(request, 'Dashboard/index.html')
