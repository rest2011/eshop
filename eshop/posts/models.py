from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from .constants import *

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='Категория',
        help_text='Название категории'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Название идентификатора'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Текст описания'
    )
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE
    )

    def get_ancestors(self):
        ancestors = []
        category = self
        while category is not None:
            ancestors.append(category)
            category = category.parent
        return ancestors[::-1]

    def get_ancestors_slugs(self):
        ancestors = self.get_ancestors()
        slugs = [ancestor.slug for ancestor in ancestors]
        return "/".join(slugs)

    def get_ancestors_urls(category):
        ancestors = category.get_ancestors()
        urls = []
        for ancestor in ancestors:
            url = reverse('posts:group_list', args=[ancestor.get_full_path()])
            urls.append(url)
        return urls

    def get_full_path(category):
        path = category.slug
        parent = category.parent
        while parent:
            path = parent.slug + '/' + path
            parent = parent.parent
        return path

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Бренд',
        help_text='Бренд',
        default='Без бренда'
    )
    slug = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Идентификатор',
        help_text='Название идентификатора'
    )

    def __str__(self):
        return self.name[:15]
    
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Post(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Товар',
        help_text='Название товара',
        blank=False, null=False
    )
    slug = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Идентификатор',
        help_text='Название идентификатора'
    )
    text = models.TextField(
        verbose_name='Описание товара',
        help_text='Описание товара',
        blank=False, null=False
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        help_text='Имя автора'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='Категория',
        help_text='Категория, к которой будет относиться товар',
    )

    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True,
        help_text='Поле для загрузки картинки',

    )
    price = models.DecimalField(
        'Цена',
        help_text='Поле для цены',
        max_digits=10,
        decimal_places=2
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        max_length=100,
        verbose_name='Бренд',
        help_text='Бренд',
        default='без бренда',
    )
    color = models.CharField(
        max_length=100,
        verbose_name='Цвет',
        help_text='Цвет',
        choices=COLORS,
        default='нет',
        blank=True, null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Szu(Post):
    fast_charge = models.BooleanField(default='False')
    amper = models.FloatField(choices=AMPERS)
    charger_type = models.CharField(choices=CHARGER_TYPES, max_length=20)
    usb_outputs = models.PositiveIntegerField(choices=USB_OUTPUTS)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'СЗУ'
        verbose_name_plural = 'СЗУ'
    

class SzuUsb(Post):
    fast_charge = models.BooleanField(default='False')
    amper = models.FloatField(choices=AMPERS)
    usb_outputs = models.PositiveIntegerField(choices=USB_OUTPUTS)
    
    def __str__(self):
        return self.title    
    
    class Meta:
        verbose_name = 'СЗУ-USB'
        verbose_name_plural = 'СЗУ-USB'


class Headphones(Post):
    microphone = models.BooleanField()
    
    def __str__(self):
        return self.title    
    
    class Meta:
        verbose_name = 'Наушники'
        verbose_name_plural = 'Наушники'        


class Azu(Post):
    fast_charge = models.BooleanField(default='False')
    amper = models.FloatField(choices=AMPERS)
    charger_type = models.CharField(choices=CHARGER_TYPES, max_length=20)
    
    def __str__(self):
        return self.title    
    
    class Meta:
        verbose_name = 'АЗУ'
        verbose_name_plural = 'АЗУ' 


class AzuUsb(Post):
    amper = models.FloatField(choices=AMPERS)
    usb_outputs = models.PositiveIntegerField(choices=USB_OUTPUTS)
    fast_charge = models.BooleanField(default='False')
    
    def __str__(self):
        return self.title    
    
    class Meta:
        verbose_name = 'АЗУ-USB'
        verbose_name_plural = 'АЗУ-USB' 


class DataCabel(Post):
    amper = models.FloatField(choices=AMPERS, null=True, blank=True)
    length = models.FloatField(choices=CABEL_LENGTH, default=1)
    charger_type = models.CharField(choices=CHARGER_TYPES, max_length=20)

    def __str__(self):
        return self.title    
    
    class Meta:
        verbose_name = 'Дата-кабель'
        verbose_name_plural = 'Дата-кабели'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Имя подписчика',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
        help_text='Имя автора'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'], name="unique_followers")
        ]

    def __str__(self):
        return SUBSCRIPTION.format(
            user=self.user.username, author=self.author.username
        )
