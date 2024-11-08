from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import LogoutView
from .views import RegisterView, UserUpdateView, CustomLoginView, email_verification, password_reset_confirm, \
    password_reset_request,password_reset_done,password_reset_complete,password_reset_invalid,UsersListView

app_name = "users"

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/mailing/'), name='logout'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('update/', UserUpdateView.as_view(template_name='users/register.html'), name='update'),

    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),


    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset_done/', password_reset_done, name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_complete/', password_reset_complete, name='password_reset_complete'),
    path('password_reset_invalid/', password_reset_invalid, name='password_reset_invalid'),


    path('users_list/', UsersListView.as_view(template_name='users/user_list.html'), name='user_list'),

]
