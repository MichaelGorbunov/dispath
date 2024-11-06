from django.db import models


# Create your models here.
class Recipient(models.Model):
    """Получатель рассылки"""
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)


class Message(models.Model):
    """Сообщение"""
    subject = models.CharField(max_length=255)
    body = models.TextField()


class Mailing(models.Model):
    """Рассылка"""
    STATUS_CHOICES = [
        ('Создана', 'Создана'),
        ('Завершена', 'Завершена'),
        ('Запущена', 'Запущена'),
    ]
    # Статус(строка: 'Завершена' , 'Создана','Запущена' )

    start_time = models.DateTimeField(verbose_name='Начало отправки рассылки')
    end_time = models.DateTimeField(verbose_name='Последняя дата отправки рассылки', null=True, blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='Создана')
    message = models.ForeignKey(
        Message, on_delete=models.SET_NULL,
        related_name="message",
        null=True, blank=True,

    )
    recipients = models.ManyToManyField(Recipient, verbose_name='Клиент', related_name='client')

class MailingAttempt(models.Model):
    """попытка рассылки"""
    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10)  # 'Успешно' или 'Не успешно'
    server_response = models.TextField(null=True, blank=True)  # Ответ сервера
    mailing = models.ForeignKey(
        Mailing, on_delete=models.SET_NULL,
        related_name="attempts",
        null=True, blank=True,

    )

