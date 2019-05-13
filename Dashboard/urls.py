from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userlogin, name="login"),
    path('register/', views.new_user, name="new_user"),
]
