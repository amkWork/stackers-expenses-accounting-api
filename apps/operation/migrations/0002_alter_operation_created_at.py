# Generated by Django 5.0.3 on 2024-03-24 17:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Perform date & time'),
        ),
    ]