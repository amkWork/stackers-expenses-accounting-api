# Generated by Django 5.0.3 on 2024-03-22 13:28

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('holder_type', models.CharField(choices=[('saving_account', 'Saving Account'), ('deposit', 'Deposit')], default='saving_account', max_length=32, verbose_name='Holder type')),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='Start date')),
                ('finish_date', models.DateField(null=True, verbose_name='Finish date')),
                ('value', models.FloatField(verbose_name='Amount of money')),
            ],
            options={
                'verbose_name': 'Goal',
                'verbose_name_plural': 'Goals',
            },
        ),
    ]
