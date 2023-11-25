from django.urls import path, re_path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^(.*)/(?P<post_slug>[-\w]+).html',
            views.post_detail, name='post_detail'),
    path("create/category", views.group_create, name="group_create"),
    path("create/product/<str:product_model>/", views.post_create, name="post_create"),
    path("posts/<slug:slug>/edit/", views.post_edit, name="post_edit"),
    path("group/<slug:slug>/edit/", views.group_edit, name="group_edit"),
    path('follow/', views.follow_index, name='follow_index'),
    path(
        'profile/<str:username>/follow/',
        views.profile_follow,
        name='profile_follow'
    ),
    path(
        'profile/<str:username>/unfollow/',
        views.profile_unfollow,
        name='profile_unfollow'
    ),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("profile/<str:username>/", views.profile, name="profile"),

    re_path(r'^(?P<group_slug>.+)/$', views.group_posts, name="group_list"),    
]
