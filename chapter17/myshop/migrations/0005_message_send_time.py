# Generated by Django 2.2.3 on 2019-12-28 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='send_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]