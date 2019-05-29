from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.ContactView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('new_restaurant/', views.CreateRestaurant.as_view(), name="new_restaurant"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.NewUser.as_view(),name="new_user"),
]
