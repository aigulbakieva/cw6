from django.db import models

from users.models import User

PERIOD = [
    ('1', 'раз в день'),
    ('7', 'раз в неделю'),
    ('30', 'раз в месяц'),
]

STATUS = [
    ('created', 'создана'),
    ('run', 'запущена'),
    ('done', 'завершена'),
]

CHECK_STATUS = [
    ('success', 'успешно'),
    ('fail', 'не успешно'),
]


class Client(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Почта клиента')
    comment = models.CharField(max_length=300, verbose_name='Комментарий', null=True, blank=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Владелец')

    def __str__(self):
        return f'{self.full_name} {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема сообщения')
    message = models.CharField(max_length=400, verbose_name='Тело сообщения')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Владелец')

    def __str__(self):
        return f'{self.title} {self.message}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название рассылки')
    time_start = models.DateTimeField(verbose_name='Дата и время первой отправки рассылки')
    period = models.CharField(max_length=20, choices=PERIOD, default='1', verbose_name='Периодичность')
    status = models.CharField(max_length=20, choices=STATUS, default='created', verbose_name='Статус')
    client = models.ManyToManyField(Client, verbose_name='Клиент')

    message = models.ForeignKey(Message, verbose_name='Сообщение', on_delete=models.CASCADE, null=True, blank=True)
    time_end = models.DateTimeField(null=True, blank=True, verbose_name='Дата и время окончания рассылки ')
    is_active = models.BooleanField(default=True, verbose_name='Активная рассылка')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Владелец')

    def __str__(self):
        return f'{self.time_start} {self.period} {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

        permissions = [
            ("can_deactivate_mailing ", "can deactivate mailing")
        ]


class Log(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.CharField(choices=CHECK_STATUS, max_length=50, verbose_name='Статус', default='success')
    response = models.CharField(max_length=300, verbose_name='ответ сервера', null=True, blank=True)
    mailing_name = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', null=True, blank=True)

    def __str__(self):
        return f'{self.date}, {self.status}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
