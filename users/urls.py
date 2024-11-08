from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import LogoutView
from .views import RegisterView, UserUpdateView, CustomLoginView

app_name = "users"

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/mailing/'), name='logout'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('update/', UserUpdateView.as_view(template_name='users/register.html'), name='update'),
]
