from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse




# Create your views here.
def new_user(request):
    return render(request,'Dashboard/new-user-form.html',{})
