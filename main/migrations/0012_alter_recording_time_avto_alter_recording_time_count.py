# Generated by Django 5.0.4 on 2024-07-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_page_options_alter_time_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording_time',
            name='avto',
            field=models.CharField(blank=True, max_length=100, verbose_name='Автомобиль'),
        ),
        migrations.AlterField(
            model_name='recording_time',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='число записей'),
        ),
    ]
