# students/urls.py
from django.urls import path
from mailing import views

urlpatterns = [
    path('about/', views.about, name='about'),
]