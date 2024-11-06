from django.shortcuts import render
from .forms import RecipientForm,MailingForm,MessageForm
from django.views.generic.edit import CreateView,UpdateView
from .models import Mailing,Message,Recipient

# Create your views here.


def about(request):
    return render(request, 'mailing/about.html')

def base(request):
    return render(request, 'mailing/base.html')

class RecipientCreateView(CreateView):
    model =Recipient  # Указываем модель, с которой будет работать это представление
    form_class = RecipientForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/recipient_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = '/base/'  # URL, на который будет перенаправлен пользователь после успешной отправки формы

class RecipientUpdateView(UpdateView):
    model =Recipient  # Указываем модель, с которой будет работать это представление
    form_class = RecipientForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'mailing/recipient_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = '/base/'  # URL, на который будет перенаправлен пользователь после успешной отправки формы



