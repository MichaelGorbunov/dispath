# students/urls.py
from django.urls import path
from mailing.apps import MailingConfig
from mailing import views
from .views import RecipientCreateView,RecipientUpdateView,RecipientListView
from .views import MessageUpdateView,MessageCreateView,MessageListView
from .views import MailingCreateView,MailingUpdateView
app_name = MailingConfig.name

urlpatterns = [
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('recipient_create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipient_list/', RecipientListView.as_view(), name='recipient_list'),
    path('recipient_update/<int:pk>', RecipientUpdateView.as_view(), name='recipient_update'),

    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('message_list/',MessageListView.as_view(), name='message_list'),

    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
]