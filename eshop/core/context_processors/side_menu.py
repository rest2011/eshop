from posts.models import Group

def side_menu(request):
    groups = Group.objects.all()
    return {'groups': groups}
