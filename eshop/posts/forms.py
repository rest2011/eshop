from django import forms

from .models import Group, Szu, SzuUsb


class SzuForm(forms.ModelForm):
    class Meta:
        model = Szu
        fields = ('title', 'text', 'group', 'image', 'price')


class SzuUsbForm(forms.ModelForm):
    fast_charge = forms.BooleanField(required=False)
    class Meta:
        model = SzuUsb
        exclude = ('slug', 'author')
        


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'description', 'parent')
