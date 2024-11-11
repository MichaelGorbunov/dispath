from django.contrib import admin

# Register your models here.
from .models import Mailing, MailingAttempt, Message, Recipient

admin.site.register(Mailing)
admin.site.register(MailingAttempt)
admin.site.register(Message)
admin.site.register(Recipient)
