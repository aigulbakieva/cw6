# Generated by Django 5.0.3 on 2024-04-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_mailing_time_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активная рассылка'),
        ),
    ]
