# Generated by Django 3.2 on 2021-04-27 08:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_alter_comment_created_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 8, 38, 43, 29801, tzinfo=utc)),
        ),
    ]
