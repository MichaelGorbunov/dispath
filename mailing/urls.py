# students/urls.py
from django.urls import path
from mailing.apps import MailingConfig
from mailing import views
from .views import RecipientCreateView,RecipientUpdateView,RecipientListView,RecipientDeleteView
from .views import MessageUpdateView,MessageCreateView,MessageListView,MessageDeleteView
from .views import MailingCreateView,MailingUpdateView,MailingListView,MailingDeleteView,MailingSendView
from .views import HomePageView
app_name = MailingConfig.name

urlpatterns = [
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),

    path('', HomePageView.as_view(), name='home'),
    path('recipient_create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipient_list/', RecipientListView.as_view(), name='recipient_list'),
    path('recipient_update/<int:pk>', RecipientUpdateView.as_view(), name='recipient_update'),
    path("recipient_delete/<int:pk>", RecipientDeleteView.as_view(), name="recipient_delete"),


    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('message_list/',MessageListView.as_view(), name='message_list'),
    path("message_delete/<int:pk>", MessageDeleteView.as_view(), name="message_delete"),


    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_list/',MailingListView.as_view(), name='mailing_list'),
    path("mailing_delete/<int:pk>", MailingDeleteView.as_view(), name="mailing_delete"),
    path('mailing_send/<int:pk>/', MailingSendView.as_view(), name='mailing_send'),

]