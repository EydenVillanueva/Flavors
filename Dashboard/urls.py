from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


app_name = 'Dashboard'

urlpatterns = [
    path('', views.ContactView.as_view(), name='home'),
    #Urls del sistema de autenticación de usuarios
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.NewUser.as_view(),name="new_user"),
    #Urls del panel de control
    path('panel/', views.Panel.as_view(),name="panel"),
    path('new_restaurant/', views.CreateRestaurant.as_view(), name="new_restaurant"),
    path('delete_list/', views.delete_list_restaurant, name="delete_list_restaurant"),
    path('delete/<id_restaurant>/', views.delete_restaurant, name="delete_restaurant"),
]