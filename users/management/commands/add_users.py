from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Создаем новую группу «Пользователи»
        users_group = Group.objects.create(name='Mailing_users')



        # Создаем новую группу «Модератор продуктов»
        manager_group = Group.objects.create(name='Mailing_managers')



        User = get_user_model()
        user = User.objects.create(
            username="Petrov_Petr",
            email='petrov@webstore.ru',
            first_name='Petr',
            last_name='Petrov'
        )
        user.set_password('123456789')
        user.is_staff = True
        user.save()

        User = get_user_model()
        user = User.objects.create(
            username="Ivanov_Ivan",
            email='ivanov@webstore.ru',
            first_name='Ivan',
            last_name='Ivanov'
        )
        user.set_password('123456789')
        user.is_staff = True
        user.save()

        User = get_user_model()
        user = User.objects.create(
            username="Vasiljev_Vasilij",
            email='vasiljev@webstore.ru',
            first_name='Vasilij',
            last_name='Vasiljev'
        )
        user.set_password('123456789')
        user.is_staff = True
        user.save()

        User = get_user_model()
        user = User.objects.create(
            username="Sergjev_Sergey",
            email='sergejev@webstore.ru',
            first_name='Sergey',
            last_name='Sergjev'
        )
        user.set_password('123456789')
        user.is_staff = True
        user.save()

        # Пользователи

        user = CustomUser.objects.get(email='ivanov@webstore.ru')
        users_group = Group.objects.get(name='Mailing_users')
        user.groups.add(users_group)

        user = CustomUser.objects.get(email='vasiljev@webstore.ru')
        users_group = Group.objects.get(name='Mailing_users')
        user.groups.add(users_group)

        user = CustomUser.objects.get(email='sergejev@webstore.ru')
        users_group = Group.objects.get(name='Mailing_users')
        user.groups.add(users_group)

        # Managers
        user = CustomUser.objects.get(email='petrov@webstore.ru')
        manager_group = Group.objects.get(name='Mailing_managers')
        user.groups.add(manager_group)

        user = CustomUser.objects.get(email='ivanov@webstore.ru')
        manager_group = Group.objects.get(name='Mailing_managers')
        user.groups.add(manager_group)




        # Получаем разрешения на добавление и изменение рассылок
        users_group = Group.objects.get(name='Mailing_users')
        mailing_permission = Permission.objects.get(codename='mailing_permission')

        # Назначаем разрешения группе
        users_group.permissions.add(mailing_permission)



        # Получаем разрешения на отключение пользователей и рассылок
        can_disabling_users = Permission.objects.get(codename='can_disabling_users')
        can_disabling_mailing = Permission.objects.get(codename='can_disabling_mailing ')

        # Назначаем разрешения группе
        manager_group = Group.objects.get(name='Mailing_managers')
        manager_group.permissions.add(can_disabling_users, can_disabling_mailing)
