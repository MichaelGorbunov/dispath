# students/urls.py
from django.urls import path
from mailing.apps import MailingConfig
from mailing import views
from .views import RecipientCreateView,RecipientUpdateView
app_name = MailingConfig.name

urlpatterns = [
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('recipient_create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipient_update/<int:pk>', RecipientUpdateView.as_view(), name='recipient_updatee'),
]