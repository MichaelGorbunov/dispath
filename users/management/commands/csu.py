from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            username="SuperUser",
            email="admin@webstore.ru",
        )
        user.set_password("123456789")
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"Создан суперпользователь - {user.email}")
        )
