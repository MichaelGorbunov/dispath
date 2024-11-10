from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserUpdateForm, CustomUserBlockUpdateForm
from django.views.generic.edit import FormView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.views.generic.edit import UpdateView
from users.models import CustomUser

from users.forms import (PasswordResetRequestForm, SetNewPasswordForm)

import secrets
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.views import LoginView


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mailing:home')

    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейдите по ссылке для подтверждения почты {url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'register.html'  # замените на вашу HTML-шаблон
    success_url = reverse_lazy('mailing:home')  # замените 'profile' на имя вашего URL

    def get_object(self):
        # Ensure that the form updates the current logged-in user
        return self.request.user


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('mailing:home')


def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = get_object_or_404(CustomUser, email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode())
            reset_url = request.build_absolute_uri(
                reverse("users:password_reset_confirm", kwargs={"uidb64": uid, "token": token})
            )
            send_mail(
                "Восстановление пароля",
                f"Перейдите по ссылке, чтобы сбросить пароль: {reset_url}",
                settings.EMAIL_HOST_USER,
                [email],
            )
            return redirect("users:password_reset_done")
    else:
        form = PasswordResetRequestForm()
    return render(request, "users/password_reset_form.html", {"form": form})


def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            form = SetNewPasswordForm(request.POST)
            if form.is_valid():
                user.set_password(form.cleaned_data["new_password"])
                user.save()
                return redirect("users:password_reset_complete")
        else:
            form = SetNewPasswordForm()
        return render(request, "users/password_reset_confirm.html", {"form": form})
    else:
        return redirect("users:password_reset_invalid")


def password_reset_done(request):
    return render(request, "users/password_reset_done.html")


def password_reset_complete(request):
    return render(request, "users/password_reset_complete.html")


def password_reset_invalid(request):
    return render(request, "users/password_reset_invalid.html")


class UsersListView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    """Просмотр списка пользователей"""
    model = CustomUser
    login_url = reverse_lazy('users:login')
    template_name = 'users/user_list.html'
    context_object_name = 'object_list_users'
    permission_required = "users.can_disabling_users"


class UserBlockUpdateView(LoginRequiredMixin,UpdateView):
    """view для блокировки разблокировки пользователя"""
    model = CustomUser  # Указываем модель, с которой будет работать это представление
    form_class = CustomUserBlockUpdateForm
    login_url = reverse_lazy('users:login')
    template_name = 'users/user_block.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy(
        'users:user_list')  # URL, на который будет перенаправлен пользователь после успешной отправки формы


