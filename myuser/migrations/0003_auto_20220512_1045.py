# Generated by Django 2.2.5 on 2022-05-12 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_delete_centerout'),
    ]

    operations = [
        migrations.AddField(
            model_name='start',
            name='dateTimeOfPM',
            field=models.DateTimeField(blank=True, null=True, verbose_name='퇴근시간'),
        ),
        migrations.AlterField(
            model_name='start',
            name='dateTimeOfAM',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 12, 10, 45, 28, 638228), verbose_name='출근시간'),
        ),
    ]