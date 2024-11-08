from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.views.generic.edit import FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.views.generic.edit import UpdateView
from users.models import CustomUser


import secrets

from django.shortcuts import get_object_or_404, redirect

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
