from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecipientForm, MailingForm, MessageForm
from .forms import ModeratorMailingForm
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic import DetailView, ListView, TemplateView
from .models import Mailing, Message, Recipient,MailingAttempt
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def about(request):
    return render(request, 'mailing/about.html')


def base(request):
    return render(request, 'mailing/base.html')


class RecipientListView(ListView):
    model = Recipient
    template_name = "mailing/recipient_list.html"
    context_object_name = "recipients"
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        # Разрешить менеджерам просматривать всех получателей
        if user.has_perm('users.can_disabling_users'):
            return queryset
        else:
            queryset = queryset.filter(ownership=user)
            return queryset

class RecipientDeleteView(DeleteView):
    """удаление получателя"""

    model = Recipient
    template_name = "mailing/recipient_confirm_delete.html"
    success_url = reverse_lazy('mailing:recipient_list')

class RecipientCreateView(LoginRequiredMixin,CreateView):
    """view для создания получателя рассылки"""
    model = Recipient  # Указываем модель, с которой будет работать это представление
    form_class = RecipientForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/recipient_form.html'  # Шаблон, который будет использоваться для отображения формы
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('mailing:recipient_list')

    def form_valid(self, form):
        recipient = form.save()
        user = self.request.user
        recipient.ownership = user
        recipient.save()
        return super().form_valid(form)



class RecipientUpdateView(UpdateView):
    """view для обновления получателя рассылки"""
    model = Recipient  # Указываем модель, с которой будет работать это представление
    form_class = RecipientForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/recipient_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy('mailing:recipient_list')  # URL, на который будет перенаправлен пользователь после успешной отправки формы


class MessageListView(ListView):
    model = Message
    template_name = "mailing/message_list.html"
    context_object_name = "messages"



class MessageUpdateView(UpdateView):
    """view для обновления сообщения"""
    model = Message  # Указываем модель, с которой будет работать это представление
    form_class = MessageForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/message_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy('mailing:message_list')  # URL, на который будет перенаправлен пользователь после успешной отправки формы


class MessageCreateView(CreateView):
    """view для создания сообщения"""
    model = Message  # Указываем модель, с которой будет работать это представление
    form_class = MessageForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/message_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy('mailing:message_list')  # URL, на который будет перенаправлен пользователь после успешной отправки формы

class MessageDeleteView(DeleteView):
    """удаление сообщения"""

    model = Message
    template_name = "mailing/message_confirm_delete.html"
    success_url = reverse_lazy('mailing:message_list')


class MailingCreateView(LoginRequiredMixin,CreateView):
    """view для создания рассылки"""
    model = Mailing  # Указываем модель, с которой будет работать это представление
    form_class = MailingForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/mailing_form.html'  # Шаблон, который будет использоваться для отображения формы
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('mailing:mailing_list')  # URL, на который будет перенаправлен пользователь после успешной отправки формы

    def get_form_class(self):
        # Пример: выбор формы в зависимости от пользователя
        if self.request.user.has_perm('mailing.can_disabling_mailing'):
            return ModeratorMailingForm # Форма для суперпользователей
        else:
            return MailingForm # Форма для обычных пользователей
    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.ownership = user
        mailing.save()
        return super().form_valid(form)




class MailingUpdateView(LoginRequiredMixin,UpdateView):
    """view для создания рассылки"""
    model = Mailing  # Указываем модель, с которой будет работать это представление
    form_class = MailingForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/mailing_form.html'  # Шаблон, который будет использоваться для отображения формы
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('mailing:mailing_list')  # URL, на который будет перенаправлен пользователь после успешной отправки формы

    def get_form_class(self):

        # Пример: выбор формы в зависимости от пользователя
        if self.request.user.has_perm('users.can_disabling_users'):
            return ModeratorMailingForm # Форма для суперпользователей
        else:
            return MailingForm # Форма для обычных пользователей

class MailingDeleteView(LoginRequiredMixin,DeleteView):
    """удаление сообщения"""
    login_url = reverse_lazy('users:login')
    model = Mailing
    template_name = "mailing/mailing_confirm_delete.html"
    success_url = reverse_lazy('mailing:mailing_list')

class MailingListView(LoginRequiredMixin,ListView):
    model = Mailing
    template_name = "mailing/mailing_list.html"
    login_url = reverse_lazy('users:login')
    context_object_name = "mailings"

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        # Разрешить менеджерам просматривать всех получателей
        if user.has_perm('users.can_disabling_users'):
            return queryset
        else:
            queryset = queryset.filter(ownership=user)
            return queryset



# Отправка рассылки вручную
class MailingSendView(View):
    def get(self, request, pk, *args, **kwargs):
        mailing = get_object_or_404(Mailing, pk=pk)
        return render(request, 'mailing/mailing_send.html', {'mailing': mailing})

    def post(self, request, pk, *args, **kwargs):
        mailing = get_object_or_404(Mailing, pk=pk)

        # Проверяем, что статус рассылки "Создана"
        if mailing.status == 'Создана':
            recipients = mailing.recipients.all()

            # Проходим по каждому получателю
            for recipient in recipients:
                try:
                    # Попытка отправки письма
                    send_mail(
                        subject=mailing.message.subject,
                        message=mailing.message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[recipient.email],
                    )
                    # Если письмо отправлено успешно, создаем запись в попытках
                    MailingAttempt.objects.create(
                        mailing=mailing,
                        status='Успешно',
                        server_response='Сообщение отправлено успешно',
                    )
                except Exception as e:
                   MailingAttempt.objects.create(
                        mailing=mailing,
                        status='Не успешно',
                        server_response=str(e),
                    )
            # Обновляем статус рассылки после завершения попыток отправки
            mailing.status = 'Запущена'
            mailing.save()
            messages.success(request, 'Рассылка отправлена!')
        else:
            messages.error(request, 'Эта рассылка уже была отправлена.')


        return redirect("mailing:mailing_list")


class HomePageView(TemplateView):
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Количество всех рассылок
        context['total_mailings'] = Mailing.objects.count()

        # Количество активных рассылок (со статусом 'Запущена')
        context['active_mailings'] = Mailing.objects.filter(status='Запущена').count()

        # Количество уникальных получателей
        context['unique_recipients'] = Recipient.objects.distinct().count()

        return context


