# Generated by Django 4.2.6 on 2023-11-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_szu_usb_outputs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='szuusb',
            name='fast_charge',
            field=models.BooleanField(blank=True, default='False'),
        ),
    ]
