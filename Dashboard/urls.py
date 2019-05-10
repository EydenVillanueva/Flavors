from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('log-in/', views.new_user, name="new_user"),
]