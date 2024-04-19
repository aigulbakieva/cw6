from django.contrib import admin
from mailing.models import Mailing, Message, Client, Log

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_start', 'period', 'status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'message',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'response', 'mailing_name')