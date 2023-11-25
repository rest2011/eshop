# Generated by Django 3.2.15 on 2023-10-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20231019_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='azu',
            name='fast_charge',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='azuusb',
            name='fast_charge',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='szu',
            name='fast_charge',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='szuusb',
            name='fast_charge',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='datacabel',
            name='amper',
            field=models.FloatField(blank=True, choices=[(0.5, '0.5'), (1.0, '1'), (2.0, '2'), (2.1, '2.1'), (3.0, '3'), (4.0, '4'), (5.0, '5')], null=True),
        ),
        migrations.AlterField(
            model_name='datacabel',
            name='length',
            field=models.FloatField(choices=[(1, 1), (2, 2), (3, 3)], default=1),
        ),
    ]