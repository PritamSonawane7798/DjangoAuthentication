# Generated by Django 3.0.3 on 2020-05-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange_api', '0006_auto_20200502_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reciver_userid',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sender_userid',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='date',
            field=models.CharField(blank=True, default='02/05/20 15:42:26', max_length=255),
        ),
    ]