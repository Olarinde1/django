# Generated by Django 3.2 on 2021-04-27 08:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20210427_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 8, 59, 52, 350853, tzinfo=utc)),
        ),
    ]
