from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.views.generic.edit import FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.views.generic.edit import UpdateView
from users.models import CustomUser


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mailing:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # self.send_welcome_email(user.email, user.username)
        return super().form_valid(form)

    # def send_welcome_email(self, user_email, user_name):
    #     subject = 'Добро пожаловать в наш сервис'
    #     message = f'{user_name},cпасибо, что зарегистрировались в нашем сервисе!'
    #     from_email = settings.EMAIL_HOST_USER
    #     recipient_list = [user_email]
    #     send_mail(subject, message, from_email, recipient_list)


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
