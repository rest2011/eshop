from .models import Group

def side_menu(request):
    groups = Group.objects.exclude(id=3)
    return {'groups': groups}