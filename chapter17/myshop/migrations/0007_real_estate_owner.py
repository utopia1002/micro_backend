# Generated by Django 2.2.3 on 2019-12-30 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0006_message_recent_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='real_estate',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
