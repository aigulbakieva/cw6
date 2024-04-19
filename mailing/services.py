from datetime import datetime, timedelta
import pytz
from django.conf import settings
from django.core.mail import send_mail

from mailing.models import Mailing, Log


def my_job():
    day = timedelta(days=1, hours=0, minutes=0)
    week = timedelta(days=7, hours=0, minutes=0)
    month = timedelta(days=30, hours=0, minutes=0)

    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    mailings = Mailing.objects.filter(status='created', time_start__lte=current_datetime)
    print(mailings)
    for mailing in mailings:
        result = send_mail(
            subject=mailing.message.title,
            message=mailing.message.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in mailing.client.all()]
        )
        print(result)


        if result == 1:
            status = 'отправлено'
        else:
            status = 'ошибка отправки'

        log = Log(mailing_name=mailing, status=status)
        log.save()

        if mailing.period == "1":
            mailing.time_start = log.date + day
        elif mailing.period == "7":
            mailing.time_start = log.date + week
        elif mailing.period == "30":
            mailing.time_start = log.date + month

        if mailing.time_start < mailing.time_end:
            mailing.status = "Создана"
        else:
            mailing.status = "Завершена"
        mailing.save()
