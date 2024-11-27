from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("mailing_permission", "Can mailing operation"),  # блокировка пользователей
            ("can_disabling_users", "Can disable users"),  # блокировка пользователей
            ("can_disabling_mailing ", "Can disable mailing"),  # блокировка рассылок
        ]

    def __str__(self):
        return self.email
