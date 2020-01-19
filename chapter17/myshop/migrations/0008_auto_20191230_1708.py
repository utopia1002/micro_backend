# Generated by Django 2.2.3 on 2019-12-30 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0007_real_estate_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='real_estate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]