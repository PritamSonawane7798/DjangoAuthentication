# Generated by Django 3.0.3 on 2020-05-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange_api', '0005_auto_20200502_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='loss',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='profit',
        ),
        migrations.AlterField(
            model_name='wallet',
            name='date',
            field=models.CharField(blank=True, default='02/05/20 15:32:20', max_length=255),
        ),
    ]
