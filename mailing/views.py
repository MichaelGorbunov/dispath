from django.shortcuts import render
from .forms import RecipientForm, MailingForm, MessageForm
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic import DetailView, ListView, TemplateView
from .models import Mailing, Message, Recipient
from django.urls import reverse, reverse_lazy


# Create your views here.


def about(request):
    return render(request, 'mailing/about.html')


def base(request):
    return render(request, 'mailing/base.html')


class RecipientListView(ListView):
    model = Recipient
    template_name = "mailing/recipient_list.html"
    context_object_name = "recipients"

class RecipientDeleteView(DeleteView):
    """удаление получателя"""

    model = Recipient
    template_name = "mailing/recipient_confirm_delete.html"
    success_url = reverse_lazy('mailing:recipient_list')

class RecipientCreateView(CreateView):
    """view для создания получателя рассылки"""
    model = Recipient  # Указываем модель, с которой будет работать это представление
    form_class = RecipientForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/recipient_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy('mailing:recipient_list')  # URL, на который будет перенаправлен пользователь после успешной отправки формы


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


class MailingCreateView(CreateView):
    """view для создания рассылки"""
    model = Mailing  # Указываем модель, с которой будет работать это представление
    form_class = MailingForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/mailing_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy('mailing:mailing_list')  # URL, на который будет перенаправлен пользователь после успешной отправки формы


class MailingUpdateView(UpdateView):
    """view для создания рассылки"""
    model = Mailing  # Указываем модель, с которой будет работать это представление
    form_class = MailingForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/mailing_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy('mailing:mailing_list')  # URL, на который будет перенаправлен пользователь после успешной отправки формы

class MailingDeleteView(DeleteView):
    """удаление сообщения"""

    model = Mailing
    template_name = "mailing/mailing_confirm_delete.html"
    success_url = reverse_lazy('mailing:mailing_list')

class MailingListView(ListView):
    model = Mailing
    template_name = "mailing/mailing_list.html"
    context_object_name = "mailings"