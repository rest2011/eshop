# Generated by Django 3.2.15 on 2023-10-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20231019_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='szu',
            name='amper',
            field=models.DecimalField(choices=[(0.5, '0.5'), (1, '1'), (2, '2'), (2.1, '2.1'), (3, '3')], decimal_places=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='szuusb',
            name='amper',
            field=models.DecimalField(choices=[(0.5, '0.5'), (1, '1'), (2, '2'), (2.1, '2.1'), (3, '3')], decimal_places=1, max_digits=10),
        ),
    ]
