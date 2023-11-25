from django.contrib import admin

from .models import *


class SzuAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'group',
        'amper',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('title',)}


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    prepopulated_fields = {'slug': ('name',)}


class SzuUsbAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'group',
        'amper',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'    
    prepopulated_fields = {'slug': ('title',)}


class HeadphonesAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'group',
        'microphone',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'    
    prepopulated_fields = {'slug': ('title',)}


class AzuAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'    
    prepopulated_fields = {'slug': ('title',)}


class AzuUsbAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'    
    prepopulated_fields = {'slug': ('title',)}


class DataCabelAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'    
    prepopulated_fields = {'slug': ('title',)}  


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
    )
    list_editable = ('title',)
    search_fields = ('description',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('title',)}



class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'post',
    )
    search_fields = ('text',)
    list_filter = ('text',)
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'author',
    )
    empty_value_display = '-пусто-'


admin.site.register(Szu, SzuAdmin)
admin.site.register(SzuUsb, SzuUsbAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Headphones, HeadphonesAdmin)
admin.site.register(Azu, AzuAdmin)
admin.site.register(AzuUsb, AzuUsbAdmin)
admin.site.register(DataCabel, DataCabelAdmin)
