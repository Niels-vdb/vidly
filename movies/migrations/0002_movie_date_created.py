# Generated by Django 5.0 on 2023-12-17 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 17, 18, 5, 20, 884577, tzinfo=datetime.timezone.utc)),
        ),
    ]
