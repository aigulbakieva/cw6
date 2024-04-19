from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', null=True, blank=True)
    phone = models.CharField(max_length=35, verbose_name='Телефон', null=True, blank=True)
    token = models.CharField(max_length=50, blank=True, null=True, verbose_name='Токен')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
