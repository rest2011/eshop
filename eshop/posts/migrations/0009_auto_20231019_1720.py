# Generated by Django 3.2.15 on 2023-10-19 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0008_auto_20231019_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='szu',
            name='amper',
            field=models.FloatField(choices=[(0.5, '0.5'), (1.0, '1'), (2.0, '2'), (2.1, '2.1'), (3.0, '3'), (4.0, '4'), (5.0, '5')]),
        ),
        migrations.AlterField(
            model_name='szuusb',
            name='amper',
            field=models.FloatField(choices=[(0.5, '0.5'), (1.0, '1'), (2.0, '2'), (2.1, '2.1'), (3.0, '3'), (4.0, '4'), (5.0, '5')]),
        ),
        migrations.CreateModel(
            name='Headphones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название товара', max_length=255, verbose_name='Товар')),
                ('slug', models.CharField(help_text='Название идентификатора', max_length=255, unique=True, verbose_name='Идентификатор')),
                ('text', models.TextField(help_text='Описание товара', verbose_name='Описание товара')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True, help_text='Поле для загрузки картинки', upload_to='posts/', verbose_name='Картинка')),
                ('price', models.DecimalField(decimal_places=2, help_text='Поле для цены', max_digits=10, verbose_name='Цена')),
                ('color', models.CharField(blank=True, choices=[('red', 'красный'), ('blue', 'синий'), ('green', 'зеленый'), ('white', 'белый'), ('black', 'черный')], default='нет', help_text='Цвет', max_length=100, null=True, verbose_name='Цвет')),
                ('microphone', models.BooleanField()),
                ('author', models.ForeignKey(help_text='Имя автора', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('brand', models.ForeignKey(default='без бренда', help_text='Бренд', max_length=100, on_delete=django.db.models.deletion.PROTECT, to='posts.brand', verbose_name='Бренд')),
                ('group', models.ForeignKey(blank=True, help_text='Категория, к которой будет относиться товар', null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.group', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Наушники',
                'verbose_name_plural': 'Наушники',
            },
        ),
    ]
