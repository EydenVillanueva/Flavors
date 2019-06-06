from django.urls import path
from Dashboard import views
from django.contrib.auth import views as auth_views


app_name = 'Dashboard'

urlpatterns = [
    path('', views.ContactView.as_view(), name='home'),
    # Urls del sistema de autenticación de usuarios
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.NewUser.as_view(), name="new_user"),
    # Urls del panel de control
    path('panel/', views.Panel.as_view(), name="panel"),
    path('panel/new_restaurant/',views.CreateRestaurant.as_view(), name="new_restaurant"),
    path('panel/update_restaurant/<int:pk>',views.UpdateRestaurant.as_view(), name="update_restaurant"),
    path('panel/delete_list/', views.delete_list_restaurant,name="delete_list_restaurant"),
    path('panel/delete/<id_restaurant>/',views.delete_restaurant, name="delete_restaurant"),
    path('panel/update_profile/<int:pk>', views.UpdateProfile.as_view(), name="update_profile"),
    path('panel/list_restaurant/<int:pk>', views.ListRestaurant.as_view(), name="list_restaurant"),
]
