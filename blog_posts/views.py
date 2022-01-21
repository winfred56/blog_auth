from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog_posts/index.html',context)


def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'blog_posts/detail.html', context)
