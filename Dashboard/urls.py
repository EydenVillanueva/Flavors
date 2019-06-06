from django.urls import path, include
from Dashboard import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'Dashboard'

urlpatterns = [
    path('', views.ContactView.as_view(), name='home'),
    # Urls del sistema de autenticación de usuarios
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name="Dashboard/password_change.html",
        success_url=reverse_lazy("Dashboard:password_change_done")),name="password_change"),

    path('change-password-done/', auth_views.PasswordChangeView.as_view(
        template_name="Dashboard/password_change_done.html"),
        name="password_change_done"),

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
]
