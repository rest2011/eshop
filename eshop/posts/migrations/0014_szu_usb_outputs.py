# Generated by Django 4.2.6 on 2023-10-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_alter_azu_charger_type_alter_azu_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='szu',
            name='usb_outputs',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1),
            preserve_default=False,
        ),
    ]
