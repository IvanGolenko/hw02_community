from django.shortcuts import render, get_object_or_404

from .models import Post, Group


NUM_OF_OBJ = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:NUM_OF_OBJ]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUM_OF_OBJ]
    title = (f'Записи сообщества {group.title}')
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
