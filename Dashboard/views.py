




from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm





def userlogin(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not none:
            login(request, user)
            return redirect('')

def home(request):
    return render(request, 'Dashboard/index.html')