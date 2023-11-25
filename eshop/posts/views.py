from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404, redirect, reverse
from pytils.translit import slugify
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.forms.models import modelform_factory

from .forms import SzuForm, GroupForm, SzuUsbForm
from .models import Post, Group, User, Follow
from .settings import POSTS_PER_PAGE
from .constants import PRODUCT_SPECS


def page_obj(request, posts):
    return Paginator(posts, POSTS_PER_PAGE).get_page(request.GET.get('page'))


def index(request):
    child_objects = []
    for model in Post.__subclasses__():
        child_objects.extend(model.objects.all())
    return render(request, 'posts/index.html', {
        'page_obj': page_obj(request, child_objects),
    })


def process_subcategories(category, subcategory_list):
    subcategories = category.subcategories.all()
    subcategory_list.append(category)
    for subcategory in subcategories:
        process_subcategories(subcategory, subcategory_list)


def group_posts(request, group_slug):
    group_slug = group_slug.split('/')[-1]
    group = get_object_or_404(Group, slug=group_slug)

    subcategory_list = []
    process_subcategories(group, subcategory_list)

    child_objects = []
    for model in Post.__subclasses__():
        child_objects.extend(model.objects.filter(group__in=subcategory_list))

    return render(request, 'posts/group_list.html', {
        'page_obj': page_obj(request, child_objects),
        'group': group,
    })

def profile(request, username):
    author = get_object_or_404(User, username=username)
    child_objects = []
    for model in Post.__subclasses__():
        child_objects.extend(model.objects.filter(author=author))
    return render(request, 'posts/profile.html', {
        'page_obj': page_obj(request, child_objects),
        'author': author,
        'following':
            request.user != author
            and request.user.is_authenticated
            and Follow.objects.filter(
                user=request.user, author=author
        ).exists(),
    })


def post_detail(request, post_slug):
    for model in Post.__subclasses__():
        try:
            obj = model.objects.get(slug=post_slug)
            return render(request, 'posts/post_detail.html', {'post': obj, 'PRODUCT_SPECS': PRODUCT_SPECS})
        except model.DoesNotExist:
            continue
    raise Http404("Post not found")


@login_required
def post_create(request, product_model):

    PRODUCT_MODELS = {
        'zaryadki-s-kabelem': SzuForm,
        'szu': SzuUsbForm,
    }
    form = PRODUCT_MODELS[product_model](request.POST or None, files=request.FILES or None)
    if not form.is_valid():
        return render(request, 'posts/create_post.html', {
            'form': form,
            'product_model': product_model,
        })
    post = form.save(commit=False)
    post.author = request.user
    post.slug = slugify(post.title)
    post.save()
    return redirect('posts:profile', request.user)


@login_required
def post_edit(request, slug):
    for model in Post.__subclasses__():
        try:
            post = model.objects.get(slug=slug)
        except model.DoesNotExist:
            continue
    if post.author != request.user:
        return redirect('posts:post_detail', post_slug=slug)
    form_class = modelform_factory(post.__class__, exclude=[])
    form = form_class(
        request.POST or None,
        files=request.FILES or None,
        instance=post)
    if not form.is_valid():
        return render(request, 'posts/create_post.html', {
            'form': form,
            'post': post,
        })
    # post.slug = slugify(post.title)
    form.save()
    return redirect(reverse('posts:post_detail', args=[post.group.get_ancestors_slugs, post.slug]))


@login_required
def group_create(request):
    form = GroupForm(request.POST or None, files=request.FILES or None)
    if not form.is_valid():
        return render(request, 'posts/create_group.html', {
            'form': form,
        })
    group = form.save(commit=False)
    group.slug = slugify(group.title)
    group.save()
    return redirect('posts:profile', request.user)


@login_required
def group_edit(request, slug):
    group = get_object_or_404(Group, slug=slug)
    form = GroupForm(
        request.POST or None,
        files=request.FILES or None,
        instance=group)
    if not form.is_valid():
        return render(request, 'posts/create_group.html', {
            'form': form,
            'group': group,
        })
    group.slug = slugify(group.title)
    form.save()
    return redirect('posts:group_list', slug=slug)


@login_required
def follow_index(request):
    posts = Post.objects.filter(author__following__user=request.user)
    return render(request, 'posts/follow.html', {
        'page_obj': page_obj(request, posts),
    })


@login_required
def profile_follow(request, username):
    if request.user.username != username:
        Follow.objects.get_or_create(
            user=request.user,
            author=get_object_or_404(User, username=username)
        )
    return redirect('posts:profile', username=username)


@login_required
def profile_unfollow(request, username):
    get_object_or_404(
        Follow,
        user=request.user,
        author__username=username
    ).delete()
    return redirect('posts:profile', username=username)
