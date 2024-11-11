from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from mailing.models import Mailing, MailingAttempt


class Command(BaseCommand):
    def handle(self, *args, **options):

        def send_mailing():
            all_objects = Mailing.objects.filter(status__in=("Создана", "Запущена"))
            for mailing in all_objects:

                if mailing.enabled is True:

                    recipients = mailing.recipients.all()

                    # Проходим по каждому получателю
                    for recipient in recipients:
                        try:
                            # Попытка отправки письма
                            send_mail(
                                subject=mailing.message.subject,
                                message=mailing.message.body,
                                from_email=settings.EMAIL_HOST_USER,
                                recipient_list=[recipient.email],
                            )
                            # Если письмо отправлено успешно, создаем запись в попытках
                            MailingAttempt.objects.create(
                                mailing=mailing,
                                status="Успешно",
                                server_response="Сообщение отправлено успешно",
                            )
                        except Exception as e:
                            MailingAttempt.objects.create(
                                mailing=mailing,
                                status="Не успешно",
                                server_response=str(e),
                            )
                    # Обновляем статус рассылки после завершения попыток отправки
                    mailing.status = "Запущена"
                    mailing.save()
                    # messages.success(request, 'Рассылка отправлена!')
                    # else:
                    #     messages.error(request, 'Эта рассылка уже была отправлена.')

        send_mailing()
