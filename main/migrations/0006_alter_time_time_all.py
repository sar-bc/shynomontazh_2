# Generated by Django 5.0.4 on 2024-04-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_user_id_recording_time_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='time_all',
            field=models.TimeField(verbose_name='Время'),
        ),
    ]
