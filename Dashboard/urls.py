from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.new_user, name="new_user"),
    path('new_restaurant/', views.CreateRestaurant.as_view(), name="new_restaurant"),
    #path('register/', views.CreateView.as_view(),name="new_user"),
]
