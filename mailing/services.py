# services.py
from .models import Recipient,Message,Mailing
from django.conf import settings
from django.core.cache import cache

class MailingService:
    @staticmethod
    def get_all_recipient():
        """получатели"""
        if settings.CACHES_ENABLED:
            key = "recipients"
            recipients = cache.get(key)
            if recipients is None:
                recipients = Recipient.objects.all()
                cache.set(key, recipients, 120)
        else:
            recipients = Recipient.objects.get.all()
        return recipients

    @staticmethod
    def get_all_mesages():
        """сообщения"""
        if settings.CACHES_ENABLED:
            key = "messages"
            messages = cache.get(key)
            if messages is None:
                messages = Message.objects.all()
                cache.set(key, messages, 120)
        else:
            messages = Message.objects.get.all()
        return messages

    @staticmethod
    def get_all_mailing():
        if settings.CACHES_ENABLED:
            key = "mailings"
            mailings = cache.get(key)
            if mailings is None:
                mailings = Mailing.objects.all()
                cache.set(key, mailings, 120)
        else:
            mailings = Mailing.objects.get.all()
        return mailings

