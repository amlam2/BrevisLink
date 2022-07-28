from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


app_name = 'auth'
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('reset_password/', view=auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html'), name='reset_password'),
    path('registration/', views.registration_page, name="registration"),
    path('logout/', views.logout_page, name='logout'),
    path('profile<int:pk>/', views.profile_page, name='profile'),
]
