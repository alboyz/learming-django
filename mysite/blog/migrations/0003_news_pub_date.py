# Generated by Django 3.0.5 on 2020-05-03 16:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200503_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 3, 16, 19, 11, 369395, tzinfo=utc)),
        ),
    ]
