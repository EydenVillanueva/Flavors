from django.urls import path, include
from Dashboard import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import ChangePasswordForm

app_name = 'Dashboard'

urlpatterns = [
    path('', views.ContactView.as_view(), name='home'),
    # Urls del sistema de autenticación de usuarios
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name="Dashboard/password_change.html",
        form_class=ChangePasswordForm,
        success_url=reverse_lazy("Dashboard:password_change_done")),name="password_change"),

    path('change-password-done/', auth_views.PasswordChangeView.as_view(
        template_name="Dashboard/password_change_done.html"),
        name="password_change_done"),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="Dashboard/password_reset_form.html",
        email_template_name="Dashboard/password_reset_email.html",
        subject_template_name="Dashboard/password_reset_subject.txt",
        success_url = reverse_lazy("Dashboard:password_reset_done")),
        name="password_reset"),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name="Dashboard/password_reset_done.html"),
        name="password_reset_done"),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="Dashboard/password_reset_confirm.html",
        success_url = reverse_lazy("Dashboard:password_reset_complete")),
        name="password_reset_confirm"),

    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(
        template_name="Dashboard/password_reset_complete.html"),
        name="password_reset_complete"),

    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.NewUser.as_view(), name="new_user"),
    # Urls del panel de control
    path('panel/', views.Panel.as_view(), name="panel"),
    path('panel/new_restaurant/',views.CreateRestaurant.as_view(), name="new_restaurant"),
    path('panel/update_restaurant/<int:pk>',views.UpdateRestaurant.as_view(), name="update_restaurant"),
    path('panel/delete/<int:pk>/',views.DeleteRestaurant.as_view(), name="delete_restaurant"),
    path('panel/update_profile/<int:pk>', views.UpdateProfile.as_view(), name="update_profile"),
    path('panel/list_restaurant/', views.ListRestaurant.as_view(), name="list_restaurant"),
    path('panel/create_dish/', views.CreateDish.as_view(), name="create_dish"),
    path('panel/list_dish/', views.ListDish.as_view(), name="list_dish"),
    path('panel/update_plan/', views.UpdatePlan.as_view(), name="update_plan"),
]
